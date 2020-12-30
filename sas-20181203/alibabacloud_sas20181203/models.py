# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class AddVpcHoneyPotRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        vpc_id: str = None,
        vpc_switch_id: str = None,
    ):
        self.source_ip = source_ip
        self.vpc_id = vpc_id
        self.vpc_switch_id = vpc_switch_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.vpc_switch_id is not None:
            result['VpcSwitchId'] = self.vpc_switch_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VpcSwitchId') is not None:
            self.vpc_switch_id = m.get('VpcSwitchId')
        return self


class AddVpcHoneyPotResponseBody(TeaModel):
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


class AddVpcHoneyPotResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AddVpcHoneyPotResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = AddVpcHoneyPotResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAntiBruteForceRuleRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        resource_owner_id: int = None,
        name: str = None,
        span: int = None,
        fail_count: int = None,
        forbidden_time: int = None,
        enable_smart_rule: bool = None,
        default_rule: bool = None,
        uuid_list: List[str] = None,
    ):
        self.source_ip = source_ip
        self.resource_owner_id = resource_owner_id
        self.name = name
        self.span = span
        self.fail_count = fail_count
        self.forbidden_time = forbidden_time
        self.enable_smart_rule = enable_smart_rule
        self.default_rule = default_rule
        self.uuid_list = uuid_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.name is not None:
            result['Name'] = self.name
        if self.span is not None:
            result['Span'] = self.span
        if self.fail_count is not None:
            result['FailCount'] = self.fail_count
        if self.forbidden_time is not None:
            result['ForbiddenTime'] = self.forbidden_time
        if self.enable_smart_rule is not None:
            result['EnableSmartRule'] = self.enable_smart_rule
        if self.default_rule is not None:
            result['DefaultRule'] = self.default_rule
        if self.uuid_list is not None:
            result['UuidList'] = self.uuid_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Span') is not None:
            self.span = m.get('Span')
        if m.get('FailCount') is not None:
            self.fail_count = m.get('FailCount')
        if m.get('ForbiddenTime') is not None:
            self.forbidden_time = m.get('ForbiddenTime')
        if m.get('EnableSmartRule') is not None:
            self.enable_smart_rule = m.get('EnableSmartRule')
        if m.get('DefaultRule') is not None:
            self.default_rule = m.get('DefaultRule')
        if m.get('UuidList') is not None:
            self.uuid_list = m.get('UuidList')
        return self


class CreateAntiBruteForceRuleResponseBodyCreateAntiBruteForceRule(TeaModel):
    def __init__(
        self,
        rule_id: int = None,
    ):
        self.rule_id = rule_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        return self


class CreateAntiBruteForceRuleResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        create_anti_brute_force_rule: CreateAntiBruteForceRuleResponseBodyCreateAntiBruteForceRule = None,
    ):
        self.request_id = request_id
        self.create_anti_brute_force_rule = create_anti_brute_force_rule

    def validate(self):
        if self.create_anti_brute_force_rule:
            self.create_anti_brute_force_rule.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.create_anti_brute_force_rule is not None:
            result['CreateAntiBruteForceRule'] = self.create_anti_brute_force_rule.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('CreateAntiBruteForceRule') is not None:
            temp_model = CreateAntiBruteForceRuleResponseBodyCreateAntiBruteForceRule()
            self.create_anti_brute_force_rule = temp_model.from_map(m['CreateAntiBruteForceRule'])
        return self


class CreateAntiBruteForceRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateAntiBruteForceRuleResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateAntiBruteForceRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateOrUpdateAssetGroupRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        uuids: str = None,
        group_name: str = None,
        group_id: int = None,
    ):
        self.source_ip = source_ip
        self.uuids = uuids
        self.group_name = group_name
        self.group_id = group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.uuids is not None:
            result['Uuids'] = self.uuids
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Uuids') is not None:
            self.uuids = m.get('Uuids')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        return self


class CreateOrUpdateAssetGroupResponseBody(TeaModel):
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


class CreateOrUpdateAssetGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateOrUpdateAssetGroupResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateOrUpdateAssetGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSasOrderRequest(TeaModel):
    def __init__(
        self,
        period: int = None,
        period_unit: str = None,
        auto_renew_period: int = None,
        auto_pay: bool = None,
        auto_use_coupon: bool = None,
        spec: str = None,
        instance_count: str = None,
        sas_sls_storage: str = None,
        sas_anti_ransomware: str = None,
        sas_webguard_boolean: str = None,
        sas_sc: str = None,
        sas_product_service: str = None,
        sas_webguard_order_num: str = None,
    ):
        self.period = period
        self.period_unit = period_unit
        self.auto_renew_period = auto_renew_period
        self.auto_pay = auto_pay
        self.auto_use_coupon = auto_use_coupon
        self.spec = spec
        self.instance_count = instance_count
        self.sas_sls_storage = sas_sls_storage
        self.sas_anti_ransomware = sas_anti_ransomware
        self.sas_webguard_boolean = sas_webguard_boolean
        self.sas_sc = sas_sc
        self.sas_product_service = sas_product_service
        self.sas_webguard_order_num = sas_webguard_order_num

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.period is not None:
            result['Period'] = self.period
        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit
        if self.auto_renew_period is not None:
            result['AutoRenewPeriod'] = self.auto_renew_period
        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay
        if self.auto_use_coupon is not None:
            result['AutoUseCoupon'] = self.auto_use_coupon
        if self.spec is not None:
            result['Spec'] = self.spec
        if self.instance_count is not None:
            result['InstanceCount'] = self.instance_count
        if self.sas_sls_storage is not None:
            result['SasSlsStorage'] = self.sas_sls_storage
        if self.sas_anti_ransomware is not None:
            result['SasAntiRansomware'] = self.sas_anti_ransomware
        if self.sas_webguard_boolean is not None:
            result['SasWebguardBoolean'] = self.sas_webguard_boolean
        if self.sas_sc is not None:
            result['SasSc'] = self.sas_sc
        if self.sas_product_service is not None:
            result['SasProductService'] = self.sas_product_service
        if self.sas_webguard_order_num is not None:
            result['SasWebguardOrderNum'] = self.sas_webguard_order_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')
        if m.get('AutoRenewPeriod') is not None:
            self.auto_renew_period = m.get('AutoRenewPeriod')
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')
        if m.get('AutoUseCoupon') is not None:
            self.auto_use_coupon = m.get('AutoUseCoupon')
        if m.get('Spec') is not None:
            self.spec = m.get('Spec')
        if m.get('InstanceCount') is not None:
            self.instance_count = m.get('InstanceCount')
        if m.get('SasSlsStorage') is not None:
            self.sas_sls_storage = m.get('SasSlsStorage')
        if m.get('SasAntiRansomware') is not None:
            self.sas_anti_ransomware = m.get('SasAntiRansomware')
        if m.get('SasWebguardBoolean') is not None:
            self.sas_webguard_boolean = m.get('SasWebguardBoolean')
        if m.get('SasSc') is not None:
            self.sas_sc = m.get('SasSc')
        if m.get('SasProductService') is not None:
            self.sas_product_service = m.get('SasProductService')
        if m.get('SasWebguardOrderNum') is not None:
            self.sas_webguard_order_num = m.get('SasWebguardOrderNum')
        return self


class CreateSasOrderResponseBody(TeaModel):
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


class CreateSasOrderResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateSasOrderResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateSasOrderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSimilarSecurityEventsQueryTaskRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        resource_owner_id: int = None,
        security_event_id: int = None,
        similar_event_scenario_code: str = None,
    ):
        self.source_ip = source_ip
        self.resource_owner_id = resource_owner_id
        self.security_event_id = security_event_id
        self.similar_event_scenario_code = similar_event_scenario_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.security_event_id is not None:
            result['SecurityEventId'] = self.security_event_id
        if self.similar_event_scenario_code is not None:
            result['SimilarEventScenarioCode'] = self.similar_event_scenario_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SecurityEventId') is not None:
            self.security_event_id = m.get('SecurityEventId')
        if m.get('SimilarEventScenarioCode') is not None:
            self.similar_event_scenario_code = m.get('SimilarEventScenarioCode')
        return self


class CreateSimilarSecurityEventsQueryTaskResponseBodyCreateSimilarSecurityEventsQueryTaskResponse(TeaModel):
    def __init__(
        self,
        status: str = None,
        task_id: int = None,
    ):
        self.status = status
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class CreateSimilarSecurityEventsQueryTaskResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        create_similar_security_events_query_task_response: CreateSimilarSecurityEventsQueryTaskResponseBodyCreateSimilarSecurityEventsQueryTaskResponse = None,
    ):
        self.request_id = request_id
        self.create_similar_security_events_query_task_response = create_similar_security_events_query_task_response

    def validate(self):
        if self.create_similar_security_events_query_task_response:
            self.create_similar_security_events_query_task_response.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.create_similar_security_events_query_task_response is not None:
            result['CreateSimilarSecurityEventsQueryTaskResponse'] = self.create_similar_security_events_query_task_response.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('CreateSimilarSecurityEventsQueryTaskResponse') is not None:
            temp_model = CreateSimilarSecurityEventsQueryTaskResponseBodyCreateSimilarSecurityEventsQueryTaskResponse()
            self.create_similar_security_events_query_task_response = temp_model.from_map(m['CreateSimilarSecurityEventsQueryTaskResponse'])
        return self


class CreateSimilarSecurityEventsQueryTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateSimilarSecurityEventsQueryTaskResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateSimilarSecurityEventsQueryTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteGroupRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        group_id: int = None,
    ):
        self.source_ip = source_ip
        self.group_id = group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        return self


class DeleteGroupResponseBody(TeaModel):
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


class DeleteLoginBaseConfigRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        type: str = None,
        config: str = None,
        target: str = None,
    ):
        self.source_ip = source_ip
        self.type = type
        self.config = config
        self.target = target

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.type is not None:
            result['Type'] = self.type
        if self.config is not None:
            result['Config'] = self.config
        if self.target is not None:
            result['Target'] = self.target
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Config') is not None:
            self.config = m.get('Config')
        if m.get('Target') is not None:
            self.target = m.get('Target')
        return self


class DeleteLoginBaseConfigResponseBody(TeaModel):
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


class DeleteLoginBaseConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteLoginBaseConfigResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteLoginBaseConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteTagWithUuidRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        tag_name: str = None,
        uuid_list: str = None,
    ):
        self.source_ip = source_ip
        self.tag_name = tag_name
        self.uuid_list = uuid_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.tag_name is not None:
            result['TagName'] = self.tag_name
        if self.uuid_list is not None:
            result['UuidList'] = self.uuid_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('TagName') is not None:
            self.tag_name = m.get('TagName')
        if m.get('UuidList') is not None:
            self.uuid_list = m.get('UuidList')
        return self


class DeleteTagWithUuidResponseBody(TeaModel):
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


class DeleteTagWithUuidResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteTagWithUuidResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteTagWithUuidResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteVpcHoneyPotRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        vpc_id: str = None,
    ):
        self.source_ip = source_ip
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class DeleteVpcHoneyPotResponseBody(TeaModel):
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


class DeleteVpcHoneyPotResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteVpcHoneyPotResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteVpcHoneyPotResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAccesskeyLeakListRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        status: str = None,
        query: str = None,
        start_ts: int = None,
        page_size: int = None,
        current_page: int = None,
    ):
        self.source_ip = source_ip
        self.status = status
        self.query = query
        self.start_ts = start_ts
        self.page_size = page_size
        self.current_page = current_page

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.status is not None:
            result['Status'] = self.status
        if self.query is not None:
            result['Query'] = self.query
        if self.start_ts is not None:
            result['StartTs'] = self.start_ts
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Query') is not None:
            self.query = m.get('Query')
        if m.get('StartTs') is not None:
            self.start_ts = m.get('StartTs')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        return self


class DescribeAccesskeyLeakListResponseBodyAccessKeyLeakList(TeaModel):
    def __init__(
        self,
        deal_time: str = None,
        status: str = None,
        type: str = None,
        user_type: str = None,
        accesskey_id: str = None,
        ali_user_name: str = None,
        deal_type: str = None,
        url: str = None,
        gmt_modified: int = None,
        asset: str = None,
        id: int = None,
    ):
        self.deal_time = deal_time
        self.status = status
        self.type = type
        self.user_type = user_type
        self.accesskey_id = accesskey_id
        self.ali_user_name = ali_user_name
        self.deal_type = deal_type
        self.url = url
        self.gmt_modified = gmt_modified
        self.asset = asset
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.deal_time is not None:
            result['DealTime'] = self.deal_time
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        if self.user_type is not None:
            result['UserType'] = self.user_type
        if self.accesskey_id is not None:
            result['AccesskeyId'] = self.accesskey_id
        if self.ali_user_name is not None:
            result['AliUserName'] = self.ali_user_name
        if self.deal_type is not None:
            result['DealType'] = self.deal_type
        if self.url is not None:
            result['Url'] = self.url
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.asset is not None:
            result['Asset'] = self.asset
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DealTime') is not None:
            self.deal_time = m.get('DealTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UserType') is not None:
            self.user_type = m.get('UserType')
        if m.get('AccesskeyId') is not None:
            self.accesskey_id = m.get('AccesskeyId')
        if m.get('AliUserName') is not None:
            self.ali_user_name = m.get('AliUserName')
        if m.get('DealType') is not None:
            self.deal_type = m.get('DealType')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Asset') is not None:
            self.asset = m.get('Asset')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class DescribeAccesskeyLeakListResponseBody(TeaModel):
    def __init__(
        self,
        ak_leak_count: int = None,
        access_key_leak_list: List[DescribeAccesskeyLeakListResponseBodyAccessKeyLeakList] = None,
        total_count: int = None,
        request_id: str = None,
        page_size: int = None,
        current_page: int = None,
        gmt_last: int = None,
    ):
        self.ak_leak_count = ak_leak_count
        self.access_key_leak_list = access_key_leak_list
        self.total_count = total_count
        self.request_id = request_id
        self.page_size = page_size
        self.current_page = current_page
        self.gmt_last = gmt_last

    def validate(self):
        if self.access_key_leak_list:
            for k in self.access_key_leak_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.ak_leak_count is not None:
            result['AkLeakCount'] = self.ak_leak_count
        result['AccessKeyLeakList'] = []
        if self.access_key_leak_list is not None:
            for k in self.access_key_leak_list:
                result['AccessKeyLeakList'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.gmt_last is not None:
            result['GmtLast'] = self.gmt_last
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AkLeakCount') is not None:
            self.ak_leak_count = m.get('AkLeakCount')
        self.access_key_leak_list = []
        if m.get('AccessKeyLeakList') is not None:
            for k in m.get('AccessKeyLeakList'):
                temp_model = DescribeAccesskeyLeakListResponseBodyAccessKeyLeakList()
                self.access_key_leak_list.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('GmtLast') is not None:
            self.gmt_last = m.get('GmtLast')
        return self


class DescribeAccesskeyLeakListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeAccesskeyLeakListResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeAccesskeyLeakListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAffectedMaliciousFileImagesRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        malicious_md_5: str = None,
        current_page: int = None,
        page_size: str = None,
        lang: str = None,
        repo_region_id: str = None,
        repo_instance_id: str = None,
        repo_id: str = None,
        repo_name: str = None,
        repo_namespace: str = None,
        image_tag: str = None,
        image_digest: str = None,
        image_layer: str = None,
        uuids: List[str] = None,
    ):
        self.source_ip = source_ip
        self.malicious_md_5 = malicious_md_5
        self.current_page = current_page
        self.page_size = page_size
        self.lang = lang
        self.repo_region_id = repo_region_id
        self.repo_instance_id = repo_instance_id
        self.repo_id = repo_id
        self.repo_name = repo_name
        self.repo_namespace = repo_namespace
        self.image_tag = image_tag
        self.image_digest = image_digest
        self.image_layer = image_layer
        self.uuids = uuids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.malicious_md_5 is not None:
            result['MaliciousMd5'] = self.malicious_md_5
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.repo_region_id is not None:
            result['RepoRegionId'] = self.repo_region_id
        if self.repo_instance_id is not None:
            result['RepoInstanceId'] = self.repo_instance_id
        if self.repo_id is not None:
            result['RepoId'] = self.repo_id
        if self.repo_name is not None:
            result['RepoName'] = self.repo_name
        if self.repo_namespace is not None:
            result['RepoNamespace'] = self.repo_namespace
        if self.image_tag is not None:
            result['ImageTag'] = self.image_tag
        if self.image_digest is not None:
            result['ImageDigest'] = self.image_digest
        if self.image_layer is not None:
            result['ImageLayer'] = self.image_layer
        if self.uuids is not None:
            result['Uuids'] = self.uuids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('MaliciousMd5') is not None:
            self.malicious_md_5 = m.get('MaliciousMd5')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('RepoRegionId') is not None:
            self.repo_region_id = m.get('RepoRegionId')
        if m.get('RepoInstanceId') is not None:
            self.repo_instance_id = m.get('RepoInstanceId')
        if m.get('RepoId') is not None:
            self.repo_id = m.get('RepoId')
        if m.get('RepoName') is not None:
            self.repo_name = m.get('RepoName')
        if m.get('RepoNamespace') is not None:
            self.repo_namespace = m.get('RepoNamespace')
        if m.get('ImageTag') is not None:
            self.image_tag = m.get('ImageTag')
        if m.get('ImageDigest') is not None:
            self.image_digest = m.get('ImageDigest')
        if m.get('ImageLayer') is not None:
            self.image_layer = m.get('ImageLayer')
        if m.get('Uuids') is not None:
            self.uuids = m.get('Uuids')
        return self


class DescribeAffectedMaliciousFileImagesResponseBodyAffectedMaliciousFileImagesResponse(TeaModel):
    def __init__(
        self,
        status: int = None,
        digest: str = None,
        latest_verify_timestamp: int = None,
        repo_instance_id: str = None,
        namespace: str = None,
        repo_region_id: str = None,
        tag: str = None,
        image_uuid: str = None,
        malicious_md_5: str = None,
        first_scan_timestamp: int = None,
        file_path: str = None,
        repo_id: str = None,
        layer: str = None,
        latest_scan_timestamp: int = None,
        repo_name: str = None,
        level: str = None,
    ):
        self.status = status
        self.digest = digest
        self.latest_verify_timestamp = latest_verify_timestamp
        self.repo_instance_id = repo_instance_id
        self.namespace = namespace
        self.repo_region_id = repo_region_id
        self.tag = tag
        self.image_uuid = image_uuid
        self.malicious_md_5 = malicious_md_5
        self.first_scan_timestamp = first_scan_timestamp
        self.file_path = file_path
        self.repo_id = repo_id
        self.layer = layer
        self.latest_scan_timestamp = latest_scan_timestamp
        self.repo_name = repo_name
        self.level = level

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.digest is not None:
            result['Digest'] = self.digest
        if self.latest_verify_timestamp is not None:
            result['LatestVerifyTimestamp'] = self.latest_verify_timestamp
        if self.repo_instance_id is not None:
            result['RepoInstanceId'] = self.repo_instance_id
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.repo_region_id is not None:
            result['RepoRegionId'] = self.repo_region_id
        if self.tag is not None:
            result['Tag'] = self.tag
        if self.image_uuid is not None:
            result['ImageUuid'] = self.image_uuid
        if self.malicious_md_5 is not None:
            result['MaliciousMd5'] = self.malicious_md_5
        if self.first_scan_timestamp is not None:
            result['FirstScanTimestamp'] = self.first_scan_timestamp
        if self.file_path is not None:
            result['FilePath'] = self.file_path
        if self.repo_id is not None:
            result['RepoId'] = self.repo_id
        if self.layer is not None:
            result['Layer'] = self.layer
        if self.latest_scan_timestamp is not None:
            result['LatestScanTimestamp'] = self.latest_scan_timestamp
        if self.repo_name is not None:
            result['RepoName'] = self.repo_name
        if self.level is not None:
            result['Level'] = self.level
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Digest') is not None:
            self.digest = m.get('Digest')
        if m.get('LatestVerifyTimestamp') is not None:
            self.latest_verify_timestamp = m.get('LatestVerifyTimestamp')
        if m.get('RepoInstanceId') is not None:
            self.repo_instance_id = m.get('RepoInstanceId')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('RepoRegionId') is not None:
            self.repo_region_id = m.get('RepoRegionId')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        if m.get('ImageUuid') is not None:
            self.image_uuid = m.get('ImageUuid')
        if m.get('MaliciousMd5') is not None:
            self.malicious_md_5 = m.get('MaliciousMd5')
        if m.get('FirstScanTimestamp') is not None:
            self.first_scan_timestamp = m.get('FirstScanTimestamp')
        if m.get('FilePath') is not None:
            self.file_path = m.get('FilePath')
        if m.get('RepoId') is not None:
            self.repo_id = m.get('RepoId')
        if m.get('Layer') is not None:
            self.layer = m.get('Layer')
        if m.get('LatestScanTimestamp') is not None:
            self.latest_scan_timestamp = m.get('LatestScanTimestamp')
        if m.get('RepoName') is not None:
            self.repo_name = m.get('RepoName')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        return self


class DescribeAffectedMaliciousFileImagesResponseBodyPageInfo(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        page_size: int = None,
        total_count: int = None,
        count: int = None,
    ):
        self.current_page = current_page
        self.page_size = page_size
        self.total_count = total_count
        self.count = count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.count is not None:
            result['Count'] = self.count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        return self


class DescribeAffectedMaliciousFileImagesResponseBody(TeaModel):
    def __init__(
        self,
        affected_malicious_file_images_response: List[DescribeAffectedMaliciousFileImagesResponseBodyAffectedMaliciousFileImagesResponse] = None,
        page_info: DescribeAffectedMaliciousFileImagesResponseBodyPageInfo = None,
        request_id: str = None,
    ):
        self.affected_malicious_file_images_response = affected_malicious_file_images_response
        self.page_info = page_info
        self.request_id = request_id

    def validate(self):
        if self.affected_malicious_file_images_response:
            for k in self.affected_malicious_file_images_response:
                if k:
                    k.validate()
        if self.page_info:
            self.page_info.validate()

    def to_map(self):
        result = dict()
        result['AffectedMaliciousFileImagesResponse'] = []
        if self.affected_malicious_file_images_response is not None:
            for k in self.affected_malicious_file_images_response:
                result['AffectedMaliciousFileImagesResponse'].append(k.to_map() if k else None)
        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.affected_malicious_file_images_response = []
        if m.get('AffectedMaliciousFileImagesResponse') is not None:
            for k in m.get('AffectedMaliciousFileImagesResponse'):
                temp_model = DescribeAffectedMaliciousFileImagesResponseBodyAffectedMaliciousFileImagesResponse()
                self.affected_malicious_file_images_response.append(temp_model.from_map(k))
        if m.get('PageInfo') is not None:
            temp_model = DescribeAffectedMaliciousFileImagesResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m['PageInfo'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeAffectedMaliciousFileImagesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeAffectedMaliciousFileImagesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeAffectedMaliciousFileImagesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAlarmEventDetailRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        alarm_unique_info: str = None,
        from_: str = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.alarm_unique_info = alarm_unique_info
        self.from_ = from_

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.alarm_unique_info is not None:
            result['AlarmUniqueInfo'] = self.alarm_unique_info
        if self.from_ is not None:
            result['From'] = self.from_
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('AlarmUniqueInfo') is not None:
            self.alarm_unique_info = m.get('AlarmUniqueInfo')
        if m.get('From') is not None:
            self.from_ = m.get('From')
        return self


class DescribeAlarmEventDetailResponseBodyDataCauseDetailsValue(TeaModel):
    def __init__(
        self,
        type: str = None,
        value: str = None,
        name: str = None,
    ):
        self.type = type
        self.value = value
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.value is not None:
            result['Value'] = self.value
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class DescribeAlarmEventDetailResponseBodyDataCauseDetails(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: List[DescribeAlarmEventDetailResponseBodyDataCauseDetailsValue] = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        if self.value:
            for k in self.value:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        result['Value'] = []
        if self.value is not None:
            for k in self.value:
                result['Value'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        self.value = []
        if m.get('Value') is not None:
            for k in m.get('Value'):
                temp_model = DescribeAlarmEventDetailResponseBodyDataCauseDetailsValue()
                self.value.append(temp_model.from_map(k))
        return self


class DescribeAlarmEventDetailResponseBodyData(TeaModel):
    def __init__(
        self,
        type: str = None,
        internet_ip: str = None,
        k_8s_cluster_name: str = None,
        container_image_id: str = None,
        alarm_event_desc: str = None,
        alarm_unique_info: str = None,
        cause_details: List[DescribeAlarmEventDetailResponseBodyDataCauseDetails] = None,
        can_cancel_fault: bool = None,
        app_name: str = None,
        can_be_deal_on_line: bool = None,
        container_image_name: str = None,
        k_8s_cluster_id: str = None,
        contain_hw_mode: bool = None,
        k_8s_node_id: str = None,
        instance_name: str = None,
        solution: str = None,
        data_source: str = None,
        intranet_ip: str = None,
        end_time: int = None,
        alarm_event_alias_name: str = None,
        start_time: int = None,
        uuid: str = None,
        k_8s_pod_name: str = None,
        container_id: str = None,
        k_8s_namespace: str = None,
        k_8s_node_name: str = None,
        level: str = None,
    ):
        self.type = type
        self.internet_ip = internet_ip
        self.k_8s_cluster_name = k_8s_cluster_name
        self.container_image_id = container_image_id
        self.alarm_event_desc = alarm_event_desc
        self.alarm_unique_info = alarm_unique_info
        self.cause_details = cause_details
        self.can_cancel_fault = can_cancel_fault
        self.app_name = app_name
        self.can_be_deal_on_line = can_be_deal_on_line
        self.container_image_name = container_image_name
        self.k_8s_cluster_id = k_8s_cluster_id
        self.contain_hw_mode = contain_hw_mode
        self.k_8s_node_id = k_8s_node_id
        self.instance_name = instance_name
        self.solution = solution
        self.data_source = data_source
        self.intranet_ip = intranet_ip
        self.end_time = end_time
        self.alarm_event_alias_name = alarm_event_alias_name
        self.start_time = start_time
        self.uuid = uuid
        self.k_8s_pod_name = k_8s_pod_name
        self.container_id = container_id
        self.k_8s_namespace = k_8s_namespace
        self.k_8s_node_name = k_8s_node_name
        self.level = level

    def validate(self):
        if self.cause_details:
            for k in self.cause_details:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.internet_ip is not None:
            result['InternetIp'] = self.internet_ip
        if self.k_8s_cluster_name is not None:
            result['K8sClusterName'] = self.k_8s_cluster_name
        if self.container_image_id is not None:
            result['ContainerImageId'] = self.container_image_id
        if self.alarm_event_desc is not None:
            result['AlarmEventDesc'] = self.alarm_event_desc
        if self.alarm_unique_info is not None:
            result['AlarmUniqueInfo'] = self.alarm_unique_info
        result['CauseDetails'] = []
        if self.cause_details is not None:
            for k in self.cause_details:
                result['CauseDetails'].append(k.to_map() if k else None)
        if self.can_cancel_fault is not None:
            result['CanCancelFault'] = self.can_cancel_fault
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.can_be_deal_on_line is not None:
            result['CanBeDealOnLine'] = self.can_be_deal_on_line
        if self.container_image_name is not None:
            result['ContainerImageName'] = self.container_image_name
        if self.k_8s_cluster_id is not None:
            result['K8sClusterId'] = self.k_8s_cluster_id
        if self.contain_hw_mode is not None:
            result['ContainHwMode'] = self.contain_hw_mode
        if self.k_8s_node_id is not None:
            result['K8sNodeId'] = self.k_8s_node_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.solution is not None:
            result['Solution'] = self.solution
        if self.data_source is not None:
            result['DataSource'] = self.data_source
        if self.intranet_ip is not None:
            result['IntranetIp'] = self.intranet_ip
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.alarm_event_alias_name is not None:
            result['AlarmEventAliasName'] = self.alarm_event_alias_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        if self.k_8s_pod_name is not None:
            result['K8sPodName'] = self.k_8s_pod_name
        if self.container_id is not None:
            result['ContainerId'] = self.container_id
        if self.k_8s_namespace is not None:
            result['K8sNamespace'] = self.k_8s_namespace
        if self.k_8s_node_name is not None:
            result['K8sNodeName'] = self.k_8s_node_name
        if self.level is not None:
            result['Level'] = self.level
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('InternetIp') is not None:
            self.internet_ip = m.get('InternetIp')
        if m.get('K8sClusterName') is not None:
            self.k_8s_cluster_name = m.get('K8sClusterName')
        if m.get('ContainerImageId') is not None:
            self.container_image_id = m.get('ContainerImageId')
        if m.get('AlarmEventDesc') is not None:
            self.alarm_event_desc = m.get('AlarmEventDesc')
        if m.get('AlarmUniqueInfo') is not None:
            self.alarm_unique_info = m.get('AlarmUniqueInfo')
        self.cause_details = []
        if m.get('CauseDetails') is not None:
            for k in m.get('CauseDetails'):
                temp_model = DescribeAlarmEventDetailResponseBodyDataCauseDetails()
                self.cause_details.append(temp_model.from_map(k))
        if m.get('CanCancelFault') is not None:
            self.can_cancel_fault = m.get('CanCancelFault')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('CanBeDealOnLine') is not None:
            self.can_be_deal_on_line = m.get('CanBeDealOnLine')
        if m.get('ContainerImageName') is not None:
            self.container_image_name = m.get('ContainerImageName')
        if m.get('K8sClusterId') is not None:
            self.k_8s_cluster_id = m.get('K8sClusterId')
        if m.get('ContainHwMode') is not None:
            self.contain_hw_mode = m.get('ContainHwMode')
        if m.get('K8sNodeId') is not None:
            self.k_8s_node_id = m.get('K8sNodeId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('Solution') is not None:
            self.solution = m.get('Solution')
        if m.get('DataSource') is not None:
            self.data_source = m.get('DataSource')
        if m.get('IntranetIp') is not None:
            self.intranet_ip = m.get('IntranetIp')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('AlarmEventAliasName') is not None:
            self.alarm_event_alias_name = m.get('AlarmEventAliasName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        if m.get('K8sPodName') is not None:
            self.k_8s_pod_name = m.get('K8sPodName')
        if m.get('ContainerId') is not None:
            self.container_id = m.get('ContainerId')
        if m.get('K8sNamespace') is not None:
            self.k_8s_namespace = m.get('K8sNamespace')
        if m.get('K8sNodeName') is not None:
            self.k_8s_node_name = m.get('K8sNodeName')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        return self


class DescribeAlarmEventDetailResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: DescribeAlarmEventDetailResponseBodyData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = DescribeAlarmEventDetailResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class DescribeAlarmEventDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeAlarmEventDetailResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeAlarmEventDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAlarmEventListRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        dealed: str = None,
        from_: str = None,
        levels: str = None,
        remark: str = None,
        group_id: str = None,
        alarm_event_name: str = None,
        alarm_event_type: str = None,
        current_page: int = None,
        page_size: str = None,
        cluster_id: str = None,
        container_field_name: str = None,
        container_field_value: str = None,
        target_type: str = None,
        operate_error_code_list: List[str] = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.dealed = dealed
        self.from_ = from_
        self.levels = levels
        self.remark = remark
        self.group_id = group_id
        self.alarm_event_name = alarm_event_name
        self.alarm_event_type = alarm_event_type
        self.current_page = current_page
        self.page_size = page_size
        self.cluster_id = cluster_id
        self.container_field_name = container_field_name
        self.container_field_value = container_field_value
        self.target_type = target_type
        self.operate_error_code_list = operate_error_code_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.dealed is not None:
            result['Dealed'] = self.dealed
        if self.from_ is not None:
            result['From'] = self.from_
        if self.levels is not None:
            result['Levels'] = self.levels
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.alarm_event_name is not None:
            result['AlarmEventName'] = self.alarm_event_name
        if self.alarm_event_type is not None:
            result['AlarmEventType'] = self.alarm_event_type
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.container_field_name is not None:
            result['ContainerFieldName'] = self.container_field_name
        if self.container_field_value is not None:
            result['ContainerFieldValue'] = self.container_field_value
        if self.target_type is not None:
            result['TargetType'] = self.target_type
        if self.operate_error_code_list is not None:
            result['OperateErrorCodeList'] = self.operate_error_code_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('Dealed') is not None:
            self.dealed = m.get('Dealed')
        if m.get('From') is not None:
            self.from_ = m.get('From')
        if m.get('Levels') is not None:
            self.levels = m.get('Levels')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('AlarmEventName') is not None:
            self.alarm_event_name = m.get('AlarmEventName')
        if m.get('AlarmEventType') is not None:
            self.alarm_event_type = m.get('AlarmEventType')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ContainerFieldName') is not None:
            self.container_field_name = m.get('ContainerFieldName')
        if m.get('ContainerFieldValue') is not None:
            self.container_field_value = m.get('ContainerFieldValue')
        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')
        if m.get('OperateErrorCodeList') is not None:
            self.operate_error_code_list = m.get('OperateErrorCodeList')
        return self


class DescribeAlarmEventListResponseBodyPageInfo(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        page_size: int = None,
        total_count: int = None,
        count: int = None,
    ):
        self.current_page = current_page
        self.page_size = page_size
        self.total_count = total_count
        self.count = count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.count is not None:
            result['Count'] = self.count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        return self


class DescribeAlarmEventListResponseBodySuspEvents(TeaModel):
    def __init__(
        self,
        dealed: bool = None,
        stages: str = None,
        internet_ip: str = None,
        suspicious_event_count: int = None,
        k_8s_cluster_name: str = None,
        container_image_id: str = None,
        gmt_modified: int = None,
        alarm_event_name_original: str = None,
        alarm_unique_info: str = None,
        can_cancel_fault: bool = None,
        app_name: str = None,
        security_event_ids: str = None,
        can_be_deal_on_line: bool = None,
        container_image_name: str = None,
        k_8s_cluster_id: str = None,
        description: str = None,
        contain_hw_mode: bool = None,
        instance_name: str = None,
        k_8s_node_id: str = None,
        sale_version: str = None,
        operate_error_code: str = None,
        solution: str = None,
        has_trace_info: bool = None,
        operate_time: int = None,
        data_source: str = None,
        instance_id: str = None,
        intranet_ip: str = None,
        end_time: int = None,
        uuid: str = None,
        start_time: int = None,
        k_8s_pod_name: str = None,
        container_id: str = None,
        alarm_event_type: str = None,
        k_8s_namespace: str = None,
        k_8s_node_name: str = None,
        alarm_event_name: str = None,
        level: str = None,
    ):
        self.dealed = dealed
        self.stages = stages
        self.internet_ip = internet_ip
        self.suspicious_event_count = suspicious_event_count
        self.k_8s_cluster_name = k_8s_cluster_name
        self.container_image_id = container_image_id
        self.gmt_modified = gmt_modified
        self.alarm_event_name_original = alarm_event_name_original
        self.alarm_unique_info = alarm_unique_info
        self.can_cancel_fault = can_cancel_fault
        self.app_name = app_name
        self.security_event_ids = security_event_ids
        self.can_be_deal_on_line = can_be_deal_on_line
        self.container_image_name = container_image_name
        self.k_8s_cluster_id = k_8s_cluster_id
        self.description = description
        self.contain_hw_mode = contain_hw_mode
        self.instance_name = instance_name
        self.k_8s_node_id = k_8s_node_id
        self.sale_version = sale_version
        self.operate_error_code = operate_error_code
        self.solution = solution
        self.has_trace_info = has_trace_info
        self.operate_time = operate_time
        self.data_source = data_source
        self.instance_id = instance_id
        self.intranet_ip = intranet_ip
        self.end_time = end_time
        self.uuid = uuid
        self.start_time = start_time
        self.k_8s_pod_name = k_8s_pod_name
        self.container_id = container_id
        self.alarm_event_type = alarm_event_type
        self.k_8s_namespace = k_8s_namespace
        self.k_8s_node_name = k_8s_node_name
        self.alarm_event_name = alarm_event_name
        self.level = level

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.dealed is not None:
            result['Dealed'] = self.dealed
        if self.stages is not None:
            result['Stages'] = self.stages
        if self.internet_ip is not None:
            result['InternetIp'] = self.internet_ip
        if self.suspicious_event_count is not None:
            result['SuspiciousEventCount'] = self.suspicious_event_count
        if self.k_8s_cluster_name is not None:
            result['K8sClusterName'] = self.k_8s_cluster_name
        if self.container_image_id is not None:
            result['ContainerImageId'] = self.container_image_id
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.alarm_event_name_original is not None:
            result['AlarmEventNameOriginal'] = self.alarm_event_name_original
        if self.alarm_unique_info is not None:
            result['AlarmUniqueInfo'] = self.alarm_unique_info
        if self.can_cancel_fault is not None:
            result['CanCancelFault'] = self.can_cancel_fault
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.security_event_ids is not None:
            result['SecurityEventIds'] = self.security_event_ids
        if self.can_be_deal_on_line is not None:
            result['CanBeDealOnLine'] = self.can_be_deal_on_line
        if self.container_image_name is not None:
            result['ContainerImageName'] = self.container_image_name
        if self.k_8s_cluster_id is not None:
            result['K8sClusterId'] = self.k_8s_cluster_id
        if self.description is not None:
            result['Description'] = self.description
        if self.contain_hw_mode is not None:
            result['ContainHwMode'] = self.contain_hw_mode
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.k_8s_node_id is not None:
            result['K8sNodeId'] = self.k_8s_node_id
        if self.sale_version is not None:
            result['SaleVersion'] = self.sale_version
        if self.operate_error_code is not None:
            result['OperateErrorCode'] = self.operate_error_code
        if self.solution is not None:
            result['Solution'] = self.solution
        if self.has_trace_info is not None:
            result['HasTraceInfo'] = self.has_trace_info
        if self.operate_time is not None:
            result['OperateTime'] = self.operate_time
        if self.data_source is not None:
            result['DataSource'] = self.data_source
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.intranet_ip is not None:
            result['IntranetIp'] = self.intranet_ip
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.k_8s_pod_name is not None:
            result['K8sPodName'] = self.k_8s_pod_name
        if self.container_id is not None:
            result['ContainerId'] = self.container_id
        if self.alarm_event_type is not None:
            result['AlarmEventType'] = self.alarm_event_type
        if self.k_8s_namespace is not None:
            result['K8sNamespace'] = self.k_8s_namespace
        if self.k_8s_node_name is not None:
            result['K8sNodeName'] = self.k_8s_node_name
        if self.alarm_event_name is not None:
            result['AlarmEventName'] = self.alarm_event_name
        if self.level is not None:
            result['Level'] = self.level
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Dealed') is not None:
            self.dealed = m.get('Dealed')
        if m.get('Stages') is not None:
            self.stages = m.get('Stages')
        if m.get('InternetIp') is not None:
            self.internet_ip = m.get('InternetIp')
        if m.get('SuspiciousEventCount') is not None:
            self.suspicious_event_count = m.get('SuspiciousEventCount')
        if m.get('K8sClusterName') is not None:
            self.k_8s_cluster_name = m.get('K8sClusterName')
        if m.get('ContainerImageId') is not None:
            self.container_image_id = m.get('ContainerImageId')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('AlarmEventNameOriginal') is not None:
            self.alarm_event_name_original = m.get('AlarmEventNameOriginal')
        if m.get('AlarmUniqueInfo') is not None:
            self.alarm_unique_info = m.get('AlarmUniqueInfo')
        if m.get('CanCancelFault') is not None:
            self.can_cancel_fault = m.get('CanCancelFault')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('SecurityEventIds') is not None:
            self.security_event_ids = m.get('SecurityEventIds')
        if m.get('CanBeDealOnLine') is not None:
            self.can_be_deal_on_line = m.get('CanBeDealOnLine')
        if m.get('ContainerImageName') is not None:
            self.container_image_name = m.get('ContainerImageName')
        if m.get('K8sClusterId') is not None:
            self.k_8s_cluster_id = m.get('K8sClusterId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ContainHwMode') is not None:
            self.contain_hw_mode = m.get('ContainHwMode')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('K8sNodeId') is not None:
            self.k_8s_node_id = m.get('K8sNodeId')
        if m.get('SaleVersion') is not None:
            self.sale_version = m.get('SaleVersion')
        if m.get('OperateErrorCode') is not None:
            self.operate_error_code = m.get('OperateErrorCode')
        if m.get('Solution') is not None:
            self.solution = m.get('Solution')
        if m.get('HasTraceInfo') is not None:
            self.has_trace_info = m.get('HasTraceInfo')
        if m.get('OperateTime') is not None:
            self.operate_time = m.get('OperateTime')
        if m.get('DataSource') is not None:
            self.data_source = m.get('DataSource')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('IntranetIp') is not None:
            self.intranet_ip = m.get('IntranetIp')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('K8sPodName') is not None:
            self.k_8s_pod_name = m.get('K8sPodName')
        if m.get('ContainerId') is not None:
            self.container_id = m.get('ContainerId')
        if m.get('AlarmEventType') is not None:
            self.alarm_event_type = m.get('AlarmEventType')
        if m.get('K8sNamespace') is not None:
            self.k_8s_namespace = m.get('K8sNamespace')
        if m.get('K8sNodeName') is not None:
            self.k_8s_node_name = m.get('K8sNodeName')
        if m.get('AlarmEventName') is not None:
            self.alarm_event_name = m.get('AlarmEventName')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        return self


class DescribeAlarmEventListResponseBody(TeaModel):
    def __init__(
        self,
        page_info: DescribeAlarmEventListResponseBodyPageInfo = None,
        request_id: str = None,
        susp_events: List[DescribeAlarmEventListResponseBodySuspEvents] = None,
    ):
        self.page_info = page_info
        self.request_id = request_id
        self.susp_events = susp_events

    def validate(self):
        if self.page_info:
            self.page_info.validate()
        if self.susp_events:
            for k in self.susp_events:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['SuspEvents'] = []
        if self.susp_events is not None:
            for k in self.susp_events:
                result['SuspEvents'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageInfo') is not None:
            temp_model = DescribeAlarmEventListResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m['PageInfo'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.susp_events = []
        if m.get('SuspEvents') is not None:
            for k in m.get('SuspEvents'):
                temp_model = DescribeAlarmEventListResponseBodySuspEvents()
                self.susp_events.append(temp_model.from_map(k))
        return self


class DescribeAlarmEventListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeAlarmEventListResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeAlarmEventListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAllEntityRequest(TeaModel):
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


class DescribeAllEntityResponseBodyEntityList(TeaModel):
    def __init__(
        self,
        uuid: str = None,
        group_id: int = None,
        internet_ip: str = None,
        instance_name: str = None,
        ip: str = None,
        os: str = None,
        intranet_ip: str = None,
    ):
        self.uuid = uuid
        self.group_id = group_id
        self.internet_ip = internet_ip
        self.instance_name = instance_name
        self.ip = ip
        self.os = os
        self.intranet_ip = intranet_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.internet_ip is not None:
            result['InternetIp'] = self.internet_ip
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.os is not None:
            result['Os'] = self.os
        if self.intranet_ip is not None:
            result['IntranetIp'] = self.intranet_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('InternetIp') is not None:
            self.internet_ip = m.get('InternetIp')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('Os') is not None:
            self.os = m.get('Os')
        if m.get('IntranetIp') is not None:
            self.intranet_ip = m.get('IntranetIp')
        return self


class DescribeAllEntityResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        entity_list: List[DescribeAllEntityResponseBodyEntityList] = None,
    ):
        self.request_id = request_id
        self.entity_list = entity_list

    def validate(self):
        if self.entity_list:
            for k in self.entity_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['EntityList'] = []
        if self.entity_list is not None:
            for k in self.entity_list:
                result['EntityList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.entity_list = []
        if m.get('EntityList') is not None:
            for k in m.get('EntityList'):
                temp_model = DescribeAllEntityResponseBodyEntityList()
                self.entity_list.append(temp_model.from_map(k))
        return self


class DescribeAllEntityResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeAllEntityResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeAllEntityResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAllGroupsRequest(TeaModel):
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


class DescribeAllGroupsResponseBodyGroups(TeaModel):
    def __init__(
        self,
        group_name: str = None,
        group_id: int = None,
        group_flag: int = None,
    ):
        self.group_name = group_name
        self.group_id = group_id
        self.group_flag = group_flag

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.group_flag is not None:
            result['GroupFlag'] = self.group_flag
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('GroupFlag') is not None:
            self.group_flag = m.get('GroupFlag')
        return self


class DescribeAllGroupsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        groups: List[DescribeAllGroupsResponseBodyGroups] = None,
        count: int = None,
    ):
        self.request_id = request_id
        self.groups = groups
        self.count = count

    def validate(self):
        if self.groups:
            for k in self.groups:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Groups'] = []
        if self.groups is not None:
            for k in self.groups:
                result['Groups'].append(k.to_map() if k else None)
        if self.count is not None:
            result['Count'] = self.count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.groups = []
        if m.get('Groups') is not None:
            for k in m.get('Groups'):
                temp_model = DescribeAllGroupsResponseBodyGroups()
                self.groups.append(temp_model.from_map(k))
        if m.get('Count') is not None:
            self.count = m.get('Count')
        return self


class DescribeAllGroupsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeAllGroupsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeAllGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAllRegionsStatisticsRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        from_: str = None,
        group_id: int = None,
        remark: str = None,
        type: str = None,
        uuid: str = None,
        status: int = None,
        status_list: str = None,
        start_time: str = None,
        end_time: str = None,
        web_group_id: int = None,
        rule_type: int = None,
        action_1: int = None,
        flow: int = None,
        sale_id: str = None,
        dealed: str = None,
        tag: str = None,
        current_page: int = None,
        page_size: int = None,
        secure_token: str = None,
        all_region: bool = None,
    ):
        self.source_ip = source_ip
        self.from_ = from_
        self.group_id = group_id
        self.remark = remark
        self.type = type
        self.uuid = uuid
        self.status = status
        self.status_list = status_list
        self.start_time = start_time
        self.end_time = end_time
        self.web_group_id = web_group_id
        self.rule_type = rule_type
        self.action_1 = action_1
        self.flow = flow
        self.sale_id = sale_id
        self.dealed = dealed
        self.tag = tag
        self.current_page = current_page
        self.page_size = page_size
        self.secure_token = secure_token
        self.all_region = all_region

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.from_ is not None:
            result['From'] = self.from_
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.type is not None:
            result['Type'] = self.type
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        if self.status is not None:
            result['Status'] = self.status
        if self.status_list is not None:
            result['StatusList'] = self.status_list
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.web_group_id is not None:
            result['WebGroupId'] = self.web_group_id
        if self.rule_type is not None:
            result['RuleType'] = self.rule_type
        if self.action_1 is not None:
            result['Action1'] = self.action_1
        if self.flow is not None:
            result['Flow'] = self.flow
        if self.sale_id is not None:
            result['SaleId'] = self.sale_id
        if self.dealed is not None:
            result['Dealed'] = self.dealed
        if self.tag is not None:
            result['Tag'] = self.tag
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.secure_token is not None:
            result['SecureToken'] = self.secure_token
        if self.all_region is not None:
            result['AllRegion'] = self.all_region
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('From') is not None:
            self.from_ = m.get('From')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StatusList') is not None:
            self.status_list = m.get('StatusList')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('WebGroupId') is not None:
            self.web_group_id = m.get('WebGroupId')
        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')
        if m.get('Action1') is not None:
            self.action_1 = m.get('Action1')
        if m.get('Flow') is not None:
            self.flow = m.get('Flow')
        if m.get('SaleId') is not None:
            self.sale_id = m.get('SaleId')
        if m.get('Dealed') is not None:
            self.dealed = m.get('Dealed')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SecureToken') is not None:
            self.secure_token = m.get('SecureToken')
        if m.get('AllRegion') is not None:
            self.all_region = m.get('AllRegion')
        return self


class DescribeAllRegionsStatisticsResponseBodyData(TeaModel):
    def __init__(
        self,
        account: int = None,
        vul: int = None,
        health: int = None,
        trojan: int = None,
        new_suspicious: int = None,
        suspicious: int = None,
    ):
        self.account = account
        self.vul = vul
        self.health = health
        self.trojan = trojan
        self.new_suspicious = new_suspicious
        self.suspicious = suspicious

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.account is not None:
            result['Account'] = self.account
        if self.vul is not None:
            result['Vul'] = self.vul
        if self.health is not None:
            result['Health'] = self.health
        if self.trojan is not None:
            result['Trojan'] = self.trojan
        if self.new_suspicious is not None:
            result['NewSuspicious'] = self.new_suspicious
        if self.suspicious is not None:
            result['Suspicious'] = self.suspicious
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Account') is not None:
            self.account = m.get('Account')
        if m.get('Vul') is not None:
            self.vul = m.get('Vul')
        if m.get('Health') is not None:
            self.health = m.get('Health')
        if m.get('Trojan') is not None:
            self.trojan = m.get('Trojan')
        if m.get('NewSuspicious') is not None:
            self.new_suspicious = m.get('NewSuspicious')
        if m.get('Suspicious') is not None:
            self.suspicious = m.get('Suspicious')
        return self


class DescribeAllRegionsStatisticsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: DescribeAllRegionsStatisticsResponseBodyData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = DescribeAllRegionsStatisticsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class DescribeAllRegionsStatisticsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeAllRegionsStatisticsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeAllRegionsStatisticsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAntiBruteForceRulesRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        resource_owner_id: int = None,
    ):
        self.source_ip = source_ip
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DescribeAntiBruteForceRulesResponseBodyPageInfo(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        page_size: int = None,
        total_count: int = None,
        count: int = None,
    ):
        self.current_page = current_page
        self.page_size = page_size
        self.total_count = total_count
        self.count = count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.count is not None:
            result['Count'] = self.count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        return self


class DescribeAntiBruteForceRulesResponseBodyRules(TeaModel):
    def __init__(
        self,
        uuid_list: List[str] = None,
        machine_count: int = None,
        enable_smart_rule: bool = None,
        fail_count: int = None,
        forbidden_time: int = None,
        span: int = None,
        default_rule: bool = None,
        name: str = None,
        id: int = None,
    ):
        self.uuid_list = uuid_list
        self.machine_count = machine_count
        self.enable_smart_rule = enable_smart_rule
        self.fail_count = fail_count
        self.forbidden_time = forbidden_time
        self.span = span
        self.default_rule = default_rule
        self.name = name
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.uuid_list is not None:
            result['UuidList'] = self.uuid_list
        if self.machine_count is not None:
            result['MachineCount'] = self.machine_count
        if self.enable_smart_rule is not None:
            result['EnableSmartRule'] = self.enable_smart_rule
        if self.fail_count is not None:
            result['FailCount'] = self.fail_count
        if self.forbidden_time is not None:
            result['ForbiddenTime'] = self.forbidden_time
        if self.span is not None:
            result['Span'] = self.span
        if self.default_rule is not None:
            result['DefaultRule'] = self.default_rule
        if self.name is not None:
            result['Name'] = self.name
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UuidList') is not None:
            self.uuid_list = m.get('UuidList')
        if m.get('MachineCount') is not None:
            self.machine_count = m.get('MachineCount')
        if m.get('EnableSmartRule') is not None:
            self.enable_smart_rule = m.get('EnableSmartRule')
        if m.get('FailCount') is not None:
            self.fail_count = m.get('FailCount')
        if m.get('ForbiddenTime') is not None:
            self.forbidden_time = m.get('ForbiddenTime')
        if m.get('Span') is not None:
            self.span = m.get('Span')
        if m.get('DefaultRule') is not None:
            self.default_rule = m.get('DefaultRule')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class DescribeAntiBruteForceRulesResponseBody(TeaModel):
    def __init__(
        self,
        page_info: DescribeAntiBruteForceRulesResponseBodyPageInfo = None,
        request_id: str = None,
        rules: List[DescribeAntiBruteForceRulesResponseBodyRules] = None,
    ):
        self.page_info = page_info
        self.request_id = request_id
        self.rules = rules

    def validate(self):
        if self.page_info:
            self.page_info.validate()
        if self.rules:
            for k in self.rules:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Rules'] = []
        if self.rules is not None:
            for k in self.rules:
                result['Rules'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageInfo') is not None:
            temp_model = DescribeAntiBruteForceRulesResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m['PageInfo'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.rules = []
        if m.get('Rules') is not None:
            for k in m.get('Rules'):
                temp_model = DescribeAntiBruteForceRulesResponseBodyRules()
                self.rules.append(temp_model.from_map(k))
        return self


class DescribeAntiBruteForceRulesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeAntiBruteForceRulesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeAntiBruteForceRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAssetDetailByUuidRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        uuid: str = None,
        lang: str = None,
    ):
        self.source_ip = source_ip
        self.uuid = uuid
        self.lang = lang

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        if self.lang is not None:
            result['Lang'] = self.lang
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        return self


class DescribeAssetDetailByUuidResponseBodyAssetDetail(TeaModel):
    def __init__(
        self,
        cpu_info: str = None,
        internet_ip: str = None,
        os_detail: str = None,
        kernel: str = None,
        create_time: int = None,
        os_name: str = None,
        tag: str = None,
        client_status: str = None,
        mem: int = None,
        vpc_instance_id: str = None,
        instance_name: str = None,
        region: str = None,
        ip_list: List[str] = None,
        group_trace: str = None,
        disk_info_list: List[str] = None,
        host_name: str = None,
        ip: str = None,
        mac_list: List[str] = None,
        os: str = None,
        instance_id: str = None,
        asset_type: str = None,
        intranet_ip: str = None,
        sys_info: str = None,
        uuid: str = None,
        cpu: int = None,
        region_name: str = None,
        instance_status: str = None,
    ):
        self.cpu_info = cpu_info
        self.internet_ip = internet_ip
        self.os_detail = os_detail
        self.kernel = kernel
        self.create_time = create_time
        self.os_name = os_name
        self.tag = tag
        self.client_status = client_status
        self.mem = mem
        self.vpc_instance_id = vpc_instance_id
        self.instance_name = instance_name
        self.region = region
        self.ip_list = ip_list
        self.group_trace = group_trace
        self.disk_info_list = disk_info_list
        self.host_name = host_name
        self.ip = ip
        self.mac_list = mac_list
        self.os = os
        self.instance_id = instance_id
        self.asset_type = asset_type
        self.intranet_ip = intranet_ip
        self.sys_info = sys_info
        self.uuid = uuid
        self.cpu = cpu
        self.region_name = region_name
        self.instance_status = instance_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.cpu_info is not None:
            result['CpuInfo'] = self.cpu_info
        if self.internet_ip is not None:
            result['InternetIp'] = self.internet_ip
        if self.os_detail is not None:
            result['OsDetail'] = self.os_detail
        if self.kernel is not None:
            result['Kernel'] = self.kernel
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.os_name is not None:
            result['OsName'] = self.os_name
        if self.tag is not None:
            result['Tag'] = self.tag
        if self.client_status is not None:
            result['ClientStatus'] = self.client_status
        if self.mem is not None:
            result['Mem'] = self.mem
        if self.vpc_instance_id is not None:
            result['VpcInstanceId'] = self.vpc_instance_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.region is not None:
            result['Region'] = self.region
        if self.ip_list is not None:
            result['IpList'] = self.ip_list
        if self.group_trace is not None:
            result['GroupTrace'] = self.group_trace
        if self.disk_info_list is not None:
            result['DiskInfoList'] = self.disk_info_list
        if self.host_name is not None:
            result['HostName'] = self.host_name
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.mac_list is not None:
            result['MacList'] = self.mac_list
        if self.os is not None:
            result['Os'] = self.os
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.asset_type is not None:
            result['AssetType'] = self.asset_type
        if self.intranet_ip is not None:
            result['IntranetIp'] = self.intranet_ip
        if self.sys_info is not None:
            result['SysInfo'] = self.sys_info
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        if self.region_name is not None:
            result['RegionName'] = self.region_name
        if self.instance_status is not None:
            result['InstanceStatus'] = self.instance_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CpuInfo') is not None:
            self.cpu_info = m.get('CpuInfo')
        if m.get('InternetIp') is not None:
            self.internet_ip = m.get('InternetIp')
        if m.get('OsDetail') is not None:
            self.os_detail = m.get('OsDetail')
        if m.get('Kernel') is not None:
            self.kernel = m.get('Kernel')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('OsName') is not None:
            self.os_name = m.get('OsName')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        if m.get('ClientStatus') is not None:
            self.client_status = m.get('ClientStatus')
        if m.get('Mem') is not None:
            self.mem = m.get('Mem')
        if m.get('VpcInstanceId') is not None:
            self.vpc_instance_id = m.get('VpcInstanceId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('IpList') is not None:
            self.ip_list = m.get('IpList')
        if m.get('GroupTrace') is not None:
            self.group_trace = m.get('GroupTrace')
        if m.get('DiskInfoList') is not None:
            self.disk_info_list = m.get('DiskInfoList')
        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('MacList') is not None:
            self.mac_list = m.get('MacList')
        if m.get('Os') is not None:
            self.os = m.get('Os')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('AssetType') is not None:
            self.asset_type = m.get('AssetType')
        if m.get('IntranetIp') is not None:
            self.intranet_ip = m.get('IntranetIp')
        if m.get('SysInfo') is not None:
            self.sys_info = m.get('SysInfo')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        if m.get('RegionName') is not None:
            self.region_name = m.get('RegionName')
        if m.get('InstanceStatus') is not None:
            self.instance_status = m.get('InstanceStatus')
        return self


class DescribeAssetDetailByUuidResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        asset_detail: DescribeAssetDetailByUuidResponseBodyAssetDetail = None,
    ):
        self.request_id = request_id
        self.asset_detail = asset_detail

    def validate(self):
        if self.asset_detail:
            self.asset_detail.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.asset_detail is not None:
            result['AssetDetail'] = self.asset_detail.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('AssetDetail') is not None:
            temp_model = DescribeAssetDetailByUuidResponseBodyAssetDetail()
            self.asset_detail = temp_model.from_map(m['AssetDetail'])
        return self


class DescribeAssetDetailByUuidResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeAssetDetailByUuidResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeAssetDetailByUuidResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAssetDetailByUuidsRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        uuids: str = None,
    ):
        self.source_ip = source_ip
        self.uuids = uuids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.uuids is not None:
            result['Uuids'] = self.uuids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Uuids') is not None:
            self.uuids = m.get('Uuids')
        return self


class DescribeAssetDetailByUuidsResponseBodyAssetList(TeaModel):
    def __init__(
        self,
        internet_ip: str = None,
        os_name: str = None,
        ip: str = None,
        os: str = None,
        instance_id: str = None,
        client_status: str = None,
        vpc_instance_id: str = None,
        asset_type: str = None,
        intranet_ip: str = None,
        region_id: str = None,
        uuid: str = None,
        region_name: str = None,
        instance_name: str = None,
        region: str = None,
    ):
        self.internet_ip = internet_ip
        self.os_name = os_name
        self.ip = ip
        self.os = os
        self.instance_id = instance_id
        self.client_status = client_status
        self.vpc_instance_id = vpc_instance_id
        self.asset_type = asset_type
        self.intranet_ip = intranet_ip
        self.region_id = region_id
        self.uuid = uuid
        self.region_name = region_name
        self.instance_name = instance_name
        self.region = region

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.internet_ip is not None:
            result['InternetIp'] = self.internet_ip
        if self.os_name is not None:
            result['OsName'] = self.os_name
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.os is not None:
            result['Os'] = self.os
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.client_status is not None:
            result['ClientStatus'] = self.client_status
        if self.vpc_instance_id is not None:
            result['VpcInstanceId'] = self.vpc_instance_id
        if self.asset_type is not None:
            result['AssetType'] = self.asset_type
        if self.intranet_ip is not None:
            result['IntranetIp'] = self.intranet_ip
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        if self.region_name is not None:
            result['RegionName'] = self.region_name
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.region is not None:
            result['Region'] = self.region
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InternetIp') is not None:
            self.internet_ip = m.get('InternetIp')
        if m.get('OsName') is not None:
            self.os_name = m.get('OsName')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('Os') is not None:
            self.os = m.get('Os')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ClientStatus') is not None:
            self.client_status = m.get('ClientStatus')
        if m.get('VpcInstanceId') is not None:
            self.vpc_instance_id = m.get('VpcInstanceId')
        if m.get('AssetType') is not None:
            self.asset_type = m.get('AssetType')
        if m.get('IntranetIp') is not None:
            self.intranet_ip = m.get('IntranetIp')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        if m.get('RegionName') is not None:
            self.region_name = m.get('RegionName')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        return self


class DescribeAssetDetailByUuidsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        asset_list: List[DescribeAssetDetailByUuidsResponseBodyAssetList] = None,
    ):
        self.request_id = request_id
        self.asset_list = asset_list

    def validate(self):
        if self.asset_list:
            for k in self.asset_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['AssetList'] = []
        if self.asset_list is not None:
            for k in self.asset_list:
                result['AssetList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.asset_list = []
        if m.get('AssetList') is not None:
            for k in m.get('AssetList'):
                temp_model = DescribeAssetDetailByUuidsResponseBodyAssetList()
                self.asset_list.append(temp_model.from_map(k))
        return self


class DescribeAssetDetailByUuidsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeAssetDetailByUuidsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeAssetDetailByUuidsResponseBody()
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


class DescribeBruteForceSummaryRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        resource_owner_id: int = None,
    ):
        self.source_ip = source_ip
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DescribeBruteForceSummaryResponseBodyBruteForceSummary(TeaModel):
    def __init__(
        self,
        all_strategy_count: int = None,
        effective_count: int = None,
    ):
        self.all_strategy_count = all_strategy_count
        self.effective_count = effective_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.all_strategy_count is not None:
            result['AllStrategyCount'] = self.all_strategy_count
        if self.effective_count is not None:
            result['EffectiveCount'] = self.effective_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllStrategyCount') is not None:
            self.all_strategy_count = m.get('AllStrategyCount')
        if m.get('EffectiveCount') is not None:
            self.effective_count = m.get('EffectiveCount')
        return self


class DescribeBruteForceSummaryResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        brute_force_summary: DescribeBruteForceSummaryResponseBodyBruteForceSummary = None,
    ):
        self.request_id = request_id
        self.brute_force_summary = brute_force_summary

    def validate(self):
        if self.brute_force_summary:
            self.brute_force_summary.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.brute_force_summary is not None:
            result['BruteForceSummary'] = self.brute_force_summary.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('BruteForceSummary') is not None:
            temp_model = DescribeBruteForceSummaryResponseBodyBruteForceSummary()
            self.brute_force_summary = temp_model.from_map(m['BruteForceSummary'])
        return self


class DescribeBruteForceSummaryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeBruteForceSummaryResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeBruteForceSummaryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCheckEcsWarningsRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        uuid_list: str = None,
    ):
        self.source_ip = source_ip
        self.uuid_list = uuid_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.uuid_list is not None:
            result['UuidList'] = self.uuid_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('UuidList') is not None:
            self.uuid_list = m.get('UuidList')
        return self


class DescribeCheckEcsWarningsResponseBody(TeaModel):
    def __init__(
        self,
        sas_version: str = None,
        request_id: str = None,
        can_try: str = None,
        weak_password_count: str = None,
    ):
        self.sas_version = sas_version
        self.request_id = request_id
        self.can_try = can_try
        self.weak_password_count = weak_password_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.sas_version is not None:
            result['SasVersion'] = self.sas_version
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.can_try is not None:
            result['CanTry'] = self.can_try
        if self.weak_password_count is not None:
            result['WeakPasswordCount'] = self.weak_password_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SasVersion') is not None:
            self.sas_version = m.get('SasVersion')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('CanTry') is not None:
            self.can_try = m.get('CanTry')
        if m.get('WeakPasswordCount') is not None:
            self.weak_password_count = m.get('WeakPasswordCount')
        return self


class DescribeCheckEcsWarningsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeCheckEcsWarningsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeCheckEcsWarningsResponseBody()
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


class DescribeCheckWarningsRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        uuid: str = None,
        risk_id: int = None,
        page_size: int = None,
        current_page: int = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.uuid = uuid
        self.risk_id = risk_id
        self.page_size = page_size
        self.current_page = current_page

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
        if self.risk_id is not None:
            result['RiskId'] = self.risk_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        if m.get('RiskId') is not None:
            self.risk_id = m.get('RiskId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        return self


class DescribeCheckWarningsResponseBodyCheckWarnings(TeaModel):
    def __init__(
        self,
        status: int = None,
        check_warning_id: int = None,
        type: str = None,
        uuid: str = None,
        item: str = None,
        check_id: int = None,
        level: str = None,
    ):
        self.status = status
        self.check_warning_id = check_warning_id
        self.type = type
        self.uuid = uuid
        self.item = item
        self.check_id = check_id
        self.level = level

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.check_warning_id is not None:
            result['CheckWarningId'] = self.check_warning_id
        if self.type is not None:
            result['Type'] = self.type
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        if self.item is not None:
            result['Item'] = self.item
        if self.check_id is not None:
            result['CheckId'] = self.check_id
        if self.level is not None:
            result['Level'] = self.level
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('CheckWarningId') is not None:
            self.check_warning_id = m.get('CheckWarningId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        if m.get('Item') is not None:
            self.item = m.get('Item')
        if m.get('CheckId') is not None:
            self.check_id = m.get('CheckId')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        return self


class DescribeCheckWarningsResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        check_warnings: List[DescribeCheckWarningsResponseBodyCheckWarnings] = None,
        page_size: int = None,
        request_id: str = None,
        current_page: int = None,
        count: int = None,
    ):
        self.total_count = total_count
        self.check_warnings = check_warnings
        self.page_size = page_size
        self.request_id = request_id
        self.current_page = current_page
        self.count = count

    def validate(self):
        if self.check_warnings:
            for k in self.check_warnings:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['CheckWarnings'] = []
        if self.check_warnings is not None:
            for k in self.check_warnings:
                result['CheckWarnings'].append(k.to_map() if k else None)
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.count is not None:
            result['Count'] = self.count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.check_warnings = []
        if m.get('CheckWarnings') is not None:
            for k in m.get('CheckWarnings'):
                temp_model = DescribeCheckWarningsResponseBodyCheckWarnings()
                self.check_warnings.append(temp_model.from_map(k))
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        return self


class DescribeCheckWarningsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeCheckWarningsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeCheckWarningsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCheckWarningSummaryRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        type_name: str = None,
        status: str = None,
        risk_status: int = None,
        risk_name: str = None,
        strategy_id: int = None,
        uuids: str = None,
        page_size: int = None,
        current_page: int = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.type_name = type_name
        self.status = status
        self.risk_status = risk_status
        self.risk_name = risk_name
        self.strategy_id = strategy_id
        self.uuids = uuids
        self.page_size = page_size
        self.current_page = current_page

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.type_name is not None:
            result['TypeName'] = self.type_name
        if self.status is not None:
            result['Status'] = self.status
        if self.risk_status is not None:
            result['RiskStatus'] = self.risk_status
        if self.risk_name is not None:
            result['RiskName'] = self.risk_name
        if self.strategy_id is not None:
            result['StrategyId'] = self.strategy_id
        if self.uuids is not None:
            result['Uuids'] = self.uuids
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('TypeName') is not None:
            self.type_name = m.get('TypeName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('RiskStatus') is not None:
            self.risk_status = m.get('RiskStatus')
        if m.get('RiskName') is not None:
            self.risk_name = m.get('RiskName')
        if m.get('StrategyId') is not None:
            self.strategy_id = m.get('StrategyId')
        if m.get('Uuids') is not None:
            self.uuids = m.get('Uuids')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        return self


class DescribeCheckWarningSummaryResponseBodyWarningSummarys(TeaModel):
    def __init__(
        self,
        low_warning_count: int = None,
        check_count: int = None,
        medium_warning_count: int = None,
        last_found_time: str = None,
        risk_id: int = None,
        sub_type_alias: str = None,
        warning_machine_count: int = None,
        high_warning_count: int = None,
        type_alias: str = None,
        risk_name: str = None,
        level: str = None,
    ):
        self.low_warning_count = low_warning_count
        self.check_count = check_count
        self.medium_warning_count = medium_warning_count
        self.last_found_time = last_found_time
        self.risk_id = risk_id
        self.sub_type_alias = sub_type_alias
        self.warning_machine_count = warning_machine_count
        self.high_warning_count = high_warning_count
        self.type_alias = type_alias
        self.risk_name = risk_name
        self.level = level

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.low_warning_count is not None:
            result['LowWarningCount'] = self.low_warning_count
        if self.check_count is not None:
            result['CheckCount'] = self.check_count
        if self.medium_warning_count is not None:
            result['MediumWarningCount'] = self.medium_warning_count
        if self.last_found_time is not None:
            result['LastFoundTime'] = self.last_found_time
        if self.risk_id is not None:
            result['RiskId'] = self.risk_id
        if self.sub_type_alias is not None:
            result['SubTypeAlias'] = self.sub_type_alias
        if self.warning_machine_count is not None:
            result['WarningMachineCount'] = self.warning_machine_count
        if self.high_warning_count is not None:
            result['HighWarningCount'] = self.high_warning_count
        if self.type_alias is not None:
            result['TypeAlias'] = self.type_alias
        if self.risk_name is not None:
            result['RiskName'] = self.risk_name
        if self.level is not None:
            result['Level'] = self.level
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LowWarningCount') is not None:
            self.low_warning_count = m.get('LowWarningCount')
        if m.get('CheckCount') is not None:
            self.check_count = m.get('CheckCount')
        if m.get('MediumWarningCount') is not None:
            self.medium_warning_count = m.get('MediumWarningCount')
        if m.get('LastFoundTime') is not None:
            self.last_found_time = m.get('LastFoundTime')
        if m.get('RiskId') is not None:
            self.risk_id = m.get('RiskId')
        if m.get('SubTypeAlias') is not None:
            self.sub_type_alias = m.get('SubTypeAlias')
        if m.get('WarningMachineCount') is not None:
            self.warning_machine_count = m.get('WarningMachineCount')
        if m.get('HighWarningCount') is not None:
            self.high_warning_count = m.get('HighWarningCount')
        if m.get('TypeAlias') is not None:
            self.type_alias = m.get('TypeAlias')
        if m.get('RiskName') is not None:
            self.risk_name = m.get('RiskName')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        return self


class DescribeCheckWarningSummaryResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        page_size: int = None,
        request_id: str = None,
        current_page: int = None,
        count: int = None,
        warning_summarys: List[DescribeCheckWarningSummaryResponseBodyWarningSummarys] = None,
    ):
        self.total_count = total_count
        self.page_size = page_size
        self.request_id = request_id
        self.current_page = current_page
        self.count = count
        self.warning_summarys = warning_summarys

    def validate(self):
        if self.warning_summarys:
            for k in self.warning_summarys:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.count is not None:
            result['Count'] = self.count
        result['WarningSummarys'] = []
        if self.warning_summarys is not None:
            for k in self.warning_summarys:
                result['WarningSummarys'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        self.warning_summarys = []
        if m.get('WarningSummarys') is not None:
            for k in m.get('WarningSummarys'):
                temp_model = DescribeCheckWarningSummaryResponseBodyWarningSummarys()
                self.warning_summarys.append(temp_model.from_map(k))
        return self


class DescribeCheckWarningSummaryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeCheckWarningSummaryResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeCheckWarningSummaryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCloudCenterInstancesRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        region_id: str = None,
        criteria: str = None,
        machine_types: str = None,
        logical_exp: str = None,
        no_page: bool = None,
        page_size: int = None,
        current_page: int = None,
        importance: int = None,
    ):
        self.source_ip = source_ip
        self.region_id = region_id
        self.criteria = criteria
        self.machine_types = machine_types
        self.logical_exp = logical_exp
        self.no_page = no_page
        self.page_size = page_size
        self.current_page = current_page
        self.importance = importance

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.criteria is not None:
            result['Criteria'] = self.criteria
        if self.machine_types is not None:
            result['MachineTypes'] = self.machine_types
        if self.logical_exp is not None:
            result['LogicalExp'] = self.logical_exp
        if self.no_page is not None:
            result['NoPage'] = self.no_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.importance is not None:
            result['Importance'] = self.importance
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Criteria') is not None:
            self.criteria = m.get('Criteria')
        if m.get('MachineTypes') is not None:
            self.machine_types = m.get('MachineTypes')
        if m.get('LogicalExp') is not None:
            self.logical_exp = m.get('LogicalExp')
        if m.get('NoPage') is not None:
            self.no_page = m.get('NoPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('Importance') is not None:
            self.importance = m.get('Importance')
        return self


class DescribeCloudCenterInstancesResponseBodyInstances(TeaModel):
    def __init__(
        self,
        status: str = None,
        internet_ip: str = None,
        os_name: str = None,
        tag: str = None,
        client_status: str = None,
        vpc_instance_id: str = None,
        flag: int = None,
        region: str = None,
        instance_name: str = None,
        pod_count: int = None,
        vul_count: int = None,
        hc_status: str = None,
        created_time: int = None,
        cluster_id: str = None,
        risk_status: str = None,
        vul_status: str = None,
        alarm_status: str = None,
        health_check_count: int = None,
        importance: int = None,
        ip: str = None,
        os: str = None,
        instance_id: str = None,
        safe_event_count: int = None,
        asset_type: str = None,
        intranet_ip: str = None,
        region_id: str = None,
        uuid: str = None,
        group_id: str = None,
        region_name: str = None,
        cluster_name: str = None,
        exposed_status: int = None,
        risk_count: str = None,
        client_version: str = None,
    ):
        self.status = status
        self.internet_ip = internet_ip
        self.os_name = os_name
        self.tag = tag
        self.client_status = client_status
        self.vpc_instance_id = vpc_instance_id
        self.flag = flag
        self.region = region
        self.instance_name = instance_name
        self.pod_count = pod_count
        self.vul_count = vul_count
        self.hc_status = hc_status
        self.created_time = created_time
        self.cluster_id = cluster_id
        self.risk_status = risk_status
        self.vul_status = vul_status
        self.alarm_status = alarm_status
        self.health_check_count = health_check_count
        self.importance = importance
        self.ip = ip
        self.os = os
        self.instance_id = instance_id
        self.safe_event_count = safe_event_count
        self.asset_type = asset_type
        self.intranet_ip = intranet_ip
        self.region_id = region_id
        self.uuid = uuid
        self.group_id = group_id
        self.region_name = region_name
        self.cluster_name = cluster_name
        self.exposed_status = exposed_status
        self.risk_count = risk_count
        self.client_version = client_version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.internet_ip is not None:
            result['InternetIp'] = self.internet_ip
        if self.os_name is not None:
            result['OsName'] = self.os_name
        if self.tag is not None:
            result['Tag'] = self.tag
        if self.client_status is not None:
            result['ClientStatus'] = self.client_status
        if self.vpc_instance_id is not None:
            result['VpcInstanceId'] = self.vpc_instance_id
        if self.flag is not None:
            result['Flag'] = self.flag
        if self.region is not None:
            result['Region'] = self.region
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.pod_count is not None:
            result['PodCount'] = self.pod_count
        if self.vul_count is not None:
            result['VulCount'] = self.vul_count
        if self.hc_status is not None:
            result['HcStatus'] = self.hc_status
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.risk_status is not None:
            result['RiskStatus'] = self.risk_status
        if self.vul_status is not None:
            result['VulStatus'] = self.vul_status
        if self.alarm_status is not None:
            result['AlarmStatus'] = self.alarm_status
        if self.health_check_count is not None:
            result['HealthCheckCount'] = self.health_check_count
        if self.importance is not None:
            result['Importance'] = self.importance
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.os is not None:
            result['Os'] = self.os
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.safe_event_count is not None:
            result['SafeEventCount'] = self.safe_event_count
        if self.asset_type is not None:
            result['AssetType'] = self.asset_type
        if self.intranet_ip is not None:
            result['IntranetIp'] = self.intranet_ip
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.region_name is not None:
            result['RegionName'] = self.region_name
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name
        if self.exposed_status is not None:
            result['ExposedStatus'] = self.exposed_status
        if self.risk_count is not None:
            result['RiskCount'] = self.risk_count
        if self.client_version is not None:
            result['ClientVersion'] = self.client_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('InternetIp') is not None:
            self.internet_ip = m.get('InternetIp')
        if m.get('OsName') is not None:
            self.os_name = m.get('OsName')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        if m.get('ClientStatus') is not None:
            self.client_status = m.get('ClientStatus')
        if m.get('VpcInstanceId') is not None:
            self.vpc_instance_id = m.get('VpcInstanceId')
        if m.get('Flag') is not None:
            self.flag = m.get('Flag')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('PodCount') is not None:
            self.pod_count = m.get('PodCount')
        if m.get('VulCount') is not None:
            self.vul_count = m.get('VulCount')
        if m.get('HcStatus') is not None:
            self.hc_status = m.get('HcStatus')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('RiskStatus') is not None:
            self.risk_status = m.get('RiskStatus')
        if m.get('VulStatus') is not None:
            self.vul_status = m.get('VulStatus')
        if m.get('AlarmStatus') is not None:
            self.alarm_status = m.get('AlarmStatus')
        if m.get('HealthCheckCount') is not None:
            self.health_check_count = m.get('HealthCheckCount')
        if m.get('Importance') is not None:
            self.importance = m.get('Importance')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('Os') is not None:
            self.os = m.get('Os')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('SafeEventCount') is not None:
            self.safe_event_count = m.get('SafeEventCount')
        if m.get('AssetType') is not None:
            self.asset_type = m.get('AssetType')
        if m.get('IntranetIp') is not None:
            self.intranet_ip = m.get('IntranetIp')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('RegionName') is not None:
            self.region_name = m.get('RegionName')
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')
        if m.get('ExposedStatus') is not None:
            self.exposed_status = m.get('ExposedStatus')
        if m.get('RiskCount') is not None:
            self.risk_count = m.get('RiskCount')
        if m.get('ClientVersion') is not None:
            self.client_version = m.get('ClientVersion')
        return self


class DescribeCloudCenterInstancesResponseBodyPageInfo(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        page_size: int = None,
        total_count: int = None,
        count: int = None,
    ):
        self.current_page = current_page
        self.page_size = page_size
        self.total_count = total_count
        self.count = count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.count is not None:
            result['Count'] = self.count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        return self


class DescribeCloudCenterInstancesResponseBody(TeaModel):
    def __init__(
        self,
        instances: List[DescribeCloudCenterInstancesResponseBodyInstances] = None,
        page_info: DescribeCloudCenterInstancesResponseBodyPageInfo = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.instances = instances
        self.page_info = page_info
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.instances:
            for k in self.instances:
                if k:
                    k.validate()
        if self.page_info:
            self.page_info.validate()

    def to_map(self):
        result = dict()
        result['Instances'] = []
        if self.instances is not None:
            for k in self.instances:
                result['Instances'].append(k.to_map() if k else None)
        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instances = []
        if m.get('Instances') is not None:
            for k in m.get('Instances'):
                temp_model = DescribeCloudCenterInstancesResponseBodyInstances()
                self.instances.append(temp_model.from_map(k))
        if m.get('PageInfo') is not None:
            temp_model = DescribeCloudCenterInstancesResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m['PageInfo'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeCloudCenterInstancesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeCloudCenterInstancesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeCloudCenterInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCloudProductFieldStatisticsRequest(TeaModel):
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


class DescribeCloudProductFieldStatisticsResponseBodyGroupedFields(TeaModel):
    def __init__(
        self,
        category_count: str = None,
        instance_count: int = None,
        risk_instance_count: int = None,
    ):
        self.category_count = category_count
        self.instance_count = instance_count
        self.risk_instance_count = risk_instance_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.category_count is not None:
            result['CategoryCount'] = self.category_count
        if self.instance_count is not None:
            result['InstanceCount'] = self.instance_count
        if self.risk_instance_count is not None:
            result['RiskInstanceCount'] = self.risk_instance_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryCount') is not None:
            self.category_count = m.get('CategoryCount')
        if m.get('InstanceCount') is not None:
            self.instance_count = m.get('InstanceCount')
        if m.get('RiskInstanceCount') is not None:
            self.risk_instance_count = m.get('RiskInstanceCount')
        return self


class DescribeCloudProductFieldStatisticsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        grouped_fields: DescribeCloudProductFieldStatisticsResponseBodyGroupedFields = None,
    ):
        self.request_id = request_id
        self.grouped_fields = grouped_fields

    def validate(self):
        if self.grouped_fields:
            self.grouped_fields.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.grouped_fields is not None:
            result['GroupedFields'] = self.grouped_fields.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('GroupedFields') is not None:
            temp_model = DescribeCloudProductFieldStatisticsResponseBodyGroupedFields()
            self.grouped_fields = temp_model.from_map(m['GroupedFields'])
        return self


class DescribeCloudProductFieldStatisticsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeCloudProductFieldStatisticsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeCloudProductFieldStatisticsResponseBody()
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


class DescribeContainerStatisticsRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        cluster_id: str = None,
    ):
        self.source_ip = source_ip
        self.cluster_id = cluster_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        return self


class DescribeContainerStatisticsResponseBodyData(TeaModel):
    def __init__(
        self,
        total_node: int = None,
        remind_alarm_count: int = None,
        total_alarm_count: int = None,
        suspicious_alarm_count: int = None,
        serious_alarm_count: int = None,
        has_risk_node: int = None,
    ):
        self.total_node = total_node
        self.remind_alarm_count = remind_alarm_count
        self.total_alarm_count = total_alarm_count
        self.suspicious_alarm_count = suspicious_alarm_count
        self.serious_alarm_count = serious_alarm_count
        self.has_risk_node = has_risk_node

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.total_node is not None:
            result['TotalNode'] = self.total_node
        if self.remind_alarm_count is not None:
            result['RemindAlarmCount'] = self.remind_alarm_count
        if self.total_alarm_count is not None:
            result['TotalAlarmCount'] = self.total_alarm_count
        if self.suspicious_alarm_count is not None:
            result['SuspiciousAlarmCount'] = self.suspicious_alarm_count
        if self.serious_alarm_count is not None:
            result['SeriousAlarmCount'] = self.serious_alarm_count
        if self.has_risk_node is not None:
            result['hasRiskNode'] = self.has_risk_node
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalNode') is not None:
            self.total_node = m.get('TotalNode')
        if m.get('RemindAlarmCount') is not None:
            self.remind_alarm_count = m.get('RemindAlarmCount')
        if m.get('TotalAlarmCount') is not None:
            self.total_alarm_count = m.get('TotalAlarmCount')
        if m.get('SuspiciousAlarmCount') is not None:
            self.suspicious_alarm_count = m.get('SuspiciousAlarmCount')
        if m.get('SeriousAlarmCount') is not None:
            self.serious_alarm_count = m.get('SeriousAlarmCount')
        if m.get('hasRiskNode') is not None:
            self.has_risk_node = m.get('hasRiskNode')
        return self


class DescribeContainerStatisticsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: DescribeContainerStatisticsResponseBodyData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = DescribeContainerStatisticsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class DescribeContainerStatisticsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeContainerStatisticsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeContainerStatisticsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCriteriaRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        machine_types: str = None,
        value: str = None,
    ):
        self.source_ip = source_ip
        self.machine_types = machine_types
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.machine_types is not None:
            result['MachineTypes'] = self.machine_types
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('MachineTypes') is not None:
            self.machine_types = m.get('MachineTypes')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeCriteriaResponseBodyCriteriaList(TeaModel):
    def __init__(
        self,
        type: str = None,
        values: str = None,
        name: str = None,
    ):
        self.type = type
        self.values = values
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.values is not None:
            result['Values'] = self.values
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Values') is not None:
            self.values = m.get('Values')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class DescribeCriteriaResponseBody(TeaModel):
    def __init__(
        self,
        criteria_list: List[DescribeCriteriaResponseBodyCriteriaList] = None,
        request_id: str = None,
    ):
        self.criteria_list = criteria_list
        self.request_id = request_id

    def validate(self):
        if self.criteria_list:
            for k in self.criteria_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['CriteriaList'] = []
        if self.criteria_list is not None:
            for k in self.criteria_list:
                result['CriteriaList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.criteria_list = []
        if m.get('CriteriaList') is not None:
            for k in m.get('CriteriaList'):
                temp_model = DescribeCriteriaResponseBodyCriteriaList()
                self.criteria_list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeCriteriaResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeCriteriaResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeCriteriaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDialogMessagesRequest(TeaModel):
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


class DescribeDialogMessagesResponseBodyDialogList(TeaModel):
    def __init__(
        self,
        dialog_key: str = None,
        params: str = None,
        id: int = None,
    ):
        self.dialog_key = dialog_key
        self.params = params
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.dialog_key is not None:
            result['DialogKey'] = self.dialog_key
        if self.params is not None:
            result['Params'] = self.params
        if self.id is not None:
            result['ID'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DialogKey') is not None:
            self.dialog_key = m.get('DialogKey')
        if m.get('Params') is not None:
            self.params = m.get('Params')
        if m.get('ID') is not None:
            self.id = m.get('ID')
        return self


class DescribeDialogMessagesResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        request_id: str = None,
        dialog_list: List[DescribeDialogMessagesResponseBodyDialogList] = None,
    ):
        self.total_count = total_count
        self.request_id = request_id
        self.dialog_list = dialog_list

    def validate(self):
        if self.dialog_list:
            for k in self.dialog_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['DialogList'] = []
        if self.dialog_list is not None:
            for k in self.dialog_list:
                result['DialogList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.dialog_list = []
        if m.get('DialogList') is not None:
            for k in m.get('DialogList'):
                temp_model = DescribeDialogMessagesResponseBodyDialogList()
                self.dialog_list.append(temp_model.from_map(k))
        return self


class DescribeDialogMessagesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDialogMessagesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeDialogMessagesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDingTalkRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        rule_action_name: str = None,
        page_size: int = None,
        current_page: int = None,
    ):
        self.source_ip = source_ip
        self.rule_action_name = rule_action_name
        self.page_size = page_size
        self.current_page = current_page

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.rule_action_name is not None:
            result['RuleActionName'] = self.rule_action_name
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('RuleActionName') is not None:
            self.rule_action_name = m.get('RuleActionName')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        return self


class DescribeDingTalkResponseBodyPageInfo(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.current_page = current_page
        self.page_size = page_size
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeDingTalkResponseBodyActionList(TeaModel):
    def __init__(
        self,
        status: int = None,
        config_list: str = None,
        gmt_create: int = None,
        action_name: str = None,
        url: str = None,
        ali_uid: int = None,
        ding_talk_lang: str = None,
        interval_time: int = None,
        gmt_modified: int = None,
        group_id_list: str = None,
        id: int = None,
    ):
        self.status = status
        self.config_list = config_list
        self.gmt_create = gmt_create
        self.action_name = action_name
        self.url = url
        self.ali_uid = ali_uid
        self.ding_talk_lang = ding_talk_lang
        self.interval_time = interval_time
        self.gmt_modified = gmt_modified
        self.group_id_list = group_id_list
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.config_list is not None:
            result['ConfigList'] = self.config_list
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.action_name is not None:
            result['ActionName'] = self.action_name
        if self.url is not None:
            result['Url'] = self.url
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.ding_talk_lang is not None:
            result['DingTalkLang'] = self.ding_talk_lang
        if self.interval_time is not None:
            result['IntervalTime'] = self.interval_time
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.group_id_list is not None:
            result['GroupIdList'] = self.group_id_list
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ConfigList') is not None:
            self.config_list = m.get('ConfigList')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('ActionName') is not None:
            self.action_name = m.get('ActionName')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('DingTalkLang') is not None:
            self.ding_talk_lang = m.get('DingTalkLang')
        if m.get('IntervalTime') is not None:
            self.interval_time = m.get('IntervalTime')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('GroupIdList') is not None:
            self.group_id_list = m.get('GroupIdList')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class DescribeDingTalkResponseBody(TeaModel):
    def __init__(
        self,
        page_info: DescribeDingTalkResponseBodyPageInfo = None,
        request_id: str = None,
        action_list: List[DescribeDingTalkResponseBodyActionList] = None,
    ):
        self.page_info = page_info
        self.request_id = request_id
        self.action_list = action_list

    def validate(self):
        if self.page_info:
            self.page_info.validate()
        if self.action_list:
            for k in self.action_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['ActionList'] = []
        if self.action_list is not None:
            for k in self.action_list:
                result['ActionList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageInfo') is not None:
            temp_model = DescribeDingTalkResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m['PageInfo'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.action_list = []
        if m.get('ActionList') is not None:
            for k in m.get('ActionList'):
                temp_model = DescribeDingTalkResponseBodyActionList()
                self.action_list.append(temp_model.from_map(k))
        return self


class DescribeDingTalkResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDingTalkResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeDingTalkResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainCountRequest(TeaModel):
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


class DescribeDomainCountResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        total_domains_count: int = None,
        root_domains_count: int = None,
    ):
        self.request_id = request_id
        self.total_domains_count = total_domains_count
        self.root_domains_count = root_domains_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_domains_count is not None:
            result['TotalDomainsCount'] = self.total_domains_count
        if self.root_domains_count is not None:
            result['RootDomainsCount'] = self.root_domains_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalDomainsCount') is not None:
            self.total_domains_count = m.get('TotalDomainsCount')
        if m.get('RootDomainsCount') is not None:
            self.root_domains_count = m.get('RootDomainsCount')
        return self


class DescribeDomainCountResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDomainCountResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeDomainCountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainDetailRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        domain_name: str = None,
    ):
        self.source_ip = source_ip
        self.domain_name = domain_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        return self


class DescribeDomainDetailResponseBodyDomainDetailItems(TeaModel):
    def __init__(
        self,
        uuid: str = None,
        internet_ip: str = None,
        instance_name: str = None,
        instance_id: str = None,
        intranet_ip: str = None,
        asset_type: str = None,
    ):
        self.uuid = uuid
        self.internet_ip = internet_ip
        self.instance_name = instance_name
        self.instance_id = instance_id
        self.intranet_ip = intranet_ip
        self.asset_type = asset_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        if self.internet_ip is not None:
            result['InternetIp'] = self.internet_ip
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.intranet_ip is not None:
            result['IntranetIp'] = self.intranet_ip
        if self.asset_type is not None:
            result['AssetType'] = self.asset_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        if m.get('InternetIp') is not None:
            self.internet_ip = m.get('InternetIp')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('IntranetIp') is not None:
            self.intranet_ip = m.get('IntranetIp')
        if m.get('AssetType') is not None:
            self.asset_type = m.get('AssetType')
        return self


class DescribeDomainDetailResponseBody(TeaModel):
    def __init__(
        self,
        domain_detail_items: List[DescribeDomainDetailResponseBodyDomainDetailItems] = None,
        request_id: str = None,
        root_domain: str = None,
        domain: str = None,
        vul_count: int = None,
        alarm_count: int = None,
    ):
        self.domain_detail_items = domain_detail_items
        self.request_id = request_id
        self.root_domain = root_domain
        self.domain = domain
        self.vul_count = vul_count
        self.alarm_count = alarm_count

    def validate(self):
        if self.domain_detail_items:
            for k in self.domain_detail_items:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['DomainDetailItems'] = []
        if self.domain_detail_items is not None:
            for k in self.domain_detail_items:
                result['DomainDetailItems'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.root_domain is not None:
            result['RootDomain'] = self.root_domain
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.vul_count is not None:
            result['VulCount'] = self.vul_count
        if self.alarm_count is not None:
            result['AlarmCount'] = self.alarm_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.domain_detail_items = []
        if m.get('DomainDetailItems') is not None:
            for k in m.get('DomainDetailItems'):
                temp_model = DescribeDomainDetailResponseBodyDomainDetailItems()
                self.domain_detail_items.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RootDomain') is not None:
            self.root_domain = m.get('RootDomain')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('VulCount') is not None:
            self.vul_count = m.get('VulCount')
        if m.get('AlarmCount') is not None:
            self.alarm_count = m.get('AlarmCount')
        return self


class DescribeDomainDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDomainDetailResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeDomainDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainListRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        fuzzy_domain: str = None,
        domain_type: str = None,
        page_size: int = None,
        current_page: int = None,
    ):
        self.source_ip = source_ip
        self.fuzzy_domain = fuzzy_domain
        self.domain_type = domain_type
        self.page_size = page_size
        self.current_page = current_page

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.fuzzy_domain is not None:
            result['FuzzyDomain'] = self.fuzzy_domain
        if self.domain_type is not None:
            result['DomainType'] = self.domain_type
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('FuzzyDomain') is not None:
            self.fuzzy_domain = m.get('FuzzyDomain')
        if m.get('DomainType') is not None:
            self.domain_type = m.get('DomainType')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        return self


class DescribeDomainListResponseBodyPageInfo(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        page_size: int = None,
        total_count: int = None,
        count: int = None,
    ):
        self.current_page = current_page
        self.page_size = page_size
        self.total_count = total_count
        self.count = count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.count is not None:
            result['Count'] = self.count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        return self


class DescribeDomainListResponseBodyDomainListResponseList(TeaModel):
    def __init__(
        self,
        domain: str = None,
        ip_list: str = None,
    ):
        self.domain = domain
        self.ip_list = ip_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.ip_list is not None:
            result['IpList'] = self.ip_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('IpList') is not None:
            self.ip_list = m.get('IpList')
        return self


class DescribeDomainListResponseBody(TeaModel):
    def __init__(
        self,
        page_info: DescribeDomainListResponseBodyPageInfo = None,
        request_id: str = None,
        domain_list_response_list: List[DescribeDomainListResponseBodyDomainListResponseList] = None,
    ):
        self.page_info = page_info
        self.request_id = request_id
        self.domain_list_response_list = domain_list_response_list

    def validate(self):
        if self.page_info:
            self.page_info.validate()
        if self.domain_list_response_list:
            for k in self.domain_list_response_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['DomainListResponseList'] = []
        if self.domain_list_response_list is not None:
            for k in self.domain_list_response_list:
                result['DomainListResponseList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageInfo') is not None:
            temp_model = DescribeDomainListResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m['PageInfo'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.domain_list_response_list = []
        if m.get('DomainListResponseList') is not None:
            for k in m.get('DomainListResponseList'):
                temp_model = DescribeDomainListResponseBodyDomainListResponseList()
                self.domain_list_response_list.append(temp_model.from_map(k))
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
        result = dict()
        if self.headers is not None:
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


class DescribeEmgVulGroupRequest(TeaModel):
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


class DescribeEmgVulGroupResponseBodyEmgVulGroupList(TeaModel):
    def __init__(
        self,
        type: str = None,
        description: str = None,
        gmt_publish: int = None,
        pending_count: int = None,
        alias_name: str = None,
        name: str = None,
    ):
        self.type = type
        self.description = description
        self.gmt_publish = gmt_publish
        self.pending_count = pending_count
        self.alias_name = alias_name
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.description is not None:
            result['Description'] = self.description
        if self.gmt_publish is not None:
            result['GmtPublish'] = self.gmt_publish
        if self.pending_count is not None:
            result['PendingCount'] = self.pending_count
        if self.alias_name is not None:
            result['AliasName'] = self.alias_name
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GmtPublish') is not None:
            self.gmt_publish = m.get('GmtPublish')
        if m.get('PendingCount') is not None:
            self.pending_count = m.get('PendingCount')
        if m.get('AliasName') is not None:
            self.alias_name = m.get('AliasName')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class DescribeEmgVulGroupResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        request_id: str = None,
        emg_vul_group_list: List[DescribeEmgVulGroupResponseBodyEmgVulGroupList] = None,
    ):
        self.total_count = total_count
        self.request_id = request_id
        self.emg_vul_group_list = emg_vul_group_list

    def validate(self):
        if self.emg_vul_group_list:
            for k in self.emg_vul_group_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['EmgVulGroupList'] = []
        if self.emg_vul_group_list is not None:
            for k in self.emg_vul_group_list:
                result['EmgVulGroupList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.emg_vul_group_list = []
        if m.get('EmgVulGroupList') is not None:
            for k in m.get('EmgVulGroupList'):
                temp_model = DescribeEmgVulGroupResponseBodyEmgVulGroupList()
                self.emg_vul_group_list.append(temp_model.from_map(k))
        return self


class DescribeEmgVulGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeEmgVulGroupResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeEmgVulGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeExportInfoRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        export_id: int = None,
    ):
        self.source_ip = source_ip
        self.export_id = export_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.export_id is not None:
            result['ExportId'] = self.export_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ExportId') is not None:
            self.export_id = m.get('ExportId')
        return self


class DescribeExportInfoResponseBody(TeaModel):
    def __init__(
        self,
        progress: int = None,
        total_count: int = None,
        request_id: str = None,
        message: str = None,
        file_name: str = None,
        export_status: str = None,
        current_count: int = None,
        id: int = None,
        link: str = None,
    ):
        self.progress = progress
        self.total_count = total_count
        self.request_id = request_id
        self.message = message
        self.file_name = file_name
        self.export_status = export_status
        self.current_count = current_count
        self.id = id
        self.link = link

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.export_status is not None:
            result['ExportStatus'] = self.export_status
        if self.current_count is not None:
            result['CurrentCount'] = self.current_count
        if self.id is not None:
            result['Id'] = self.id
        if self.link is not None:
            result['Link'] = self.link
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('ExportStatus') is not None:
            self.export_status = m.get('ExportStatus')
        if m.get('CurrentCount') is not None:
            self.current_count = m.get('CurrentCount')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Link') is not None:
            self.link = m.get('Link')
        return self


class DescribeExportInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeExportInfoResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeExportInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeExposedInstanceCriteriaRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        value: str = None,
    ):
        self.source_ip = source_ip
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeExposedInstanceCriteriaResponseBodyCriteriaList(TeaModel):
    def __init__(
        self,
        type: str = None,
        values: str = None,
        name: str = None,
    ):
        self.type = type
        self.values = values
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.values is not None:
            result['Values'] = self.values
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Values') is not None:
            self.values = m.get('Values')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class DescribeExposedInstanceCriteriaResponseBody(TeaModel):
    def __init__(
        self,
        criteria_list: List[DescribeExposedInstanceCriteriaResponseBodyCriteriaList] = None,
        request_id: str = None,
    ):
        self.criteria_list = criteria_list
        self.request_id = request_id

    def validate(self):
        if self.criteria_list:
            for k in self.criteria_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['CriteriaList'] = []
        if self.criteria_list is not None:
            for k in self.criteria_list:
                result['CriteriaList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.criteria_list = []
        if m.get('CriteriaList') is not None:
            for k in m.get('CriteriaList'):
                temp_model = DescribeExposedInstanceCriteriaResponseBodyCriteriaList()
                self.criteria_list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeExposedInstanceCriteriaResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeExposedInstanceCriteriaResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeExposedInstanceCriteriaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeExposedInstanceDetailRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        uuid: str = None,
    ):
        self.source_ip = source_ip
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        return self


class DescribeExposedInstanceDetailResponseBodyExposedChainsAllVulList(TeaModel):
    def __init__(
        self,
        type: int = None,
        necessity: str = None,
        uuid: int = None,
        alias_name: str = None,
        name: str = None,
    ):
        self.type = type
        self.necessity = necessity
        self.uuid = uuid
        self.alias_name = alias_name
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.necessity is not None:
            result['Necessity'] = self.necessity
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        if self.alias_name is not None:
            result['AliasName'] = self.alias_name
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Necessity') is not None:
            self.necessity = m.get('Necessity')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        if m.get('AliasName') is not None:
            self.alias_name = m.get('AliasName')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class DescribeExposedInstanceDetailResponseBodyExposedChainsRealVulList(TeaModel):
    def __init__(
        self,
        type: int = None,
        necessity: str = None,
        uuid: int = None,
        alias_name: str = None,
        name: str = None,
    ):
        self.type = type
        self.necessity = necessity
        self.uuid = uuid
        self.alias_name = alias_name
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.necessity is not None:
            result['Necessity'] = self.necessity
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        if self.alias_name is not None:
            result['AliasName'] = self.alias_name
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Necessity') is not None:
            self.necessity = m.get('Necessity')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        if m.get('AliasName') is not None:
            self.alias_name = m.get('AliasName')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class DescribeExposedInstanceDetailResponseBodyExposedChains(TeaModel):
    def __init__(
        self,
        exposure_ip: str = None,
        internet_ip: str = None,
        nntf_vul_count: int = None,
        all_vul_list: List[DescribeExposedInstanceDetailResponseBodyExposedChainsAllVulList] = None,
        instance_id: str = None,
        exposure_type: str = None,
        intranet_ip: str = None,
        exposure_type_id: str = None,
        region_id: str = None,
        asap_vul_count: int = None,
        uuid: str = None,
        real_vul_list: List[DescribeExposedInstanceDetailResponseBodyExposedChainsRealVulList] = None,
        exposure_port: str = None,
        instance_name: str = None,
        later_vul_count: int = None,
        exposure_component: str = None,
    ):
        self.exposure_ip = exposure_ip
        self.internet_ip = internet_ip
        self.nntf_vul_count = nntf_vul_count
        self.all_vul_list = all_vul_list
        self.instance_id = instance_id
        self.exposure_type = exposure_type
        self.intranet_ip = intranet_ip
        self.exposure_type_id = exposure_type_id
        self.region_id = region_id
        self.asap_vul_count = asap_vul_count
        self.uuid = uuid
        self.real_vul_list = real_vul_list
        self.exposure_port = exposure_port
        self.instance_name = instance_name
        self.later_vul_count = later_vul_count
        self.exposure_component = exposure_component

    def validate(self):
        if self.all_vul_list:
            for k in self.all_vul_list:
                if k:
                    k.validate()
        if self.real_vul_list:
            for k in self.real_vul_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.exposure_ip is not None:
            result['ExposureIp'] = self.exposure_ip
        if self.internet_ip is not None:
            result['InternetIp'] = self.internet_ip
        if self.nntf_vul_count is not None:
            result['NntfVulCount'] = self.nntf_vul_count
        result['AllVulList'] = []
        if self.all_vul_list is not None:
            for k in self.all_vul_list:
                result['AllVulList'].append(k.to_map() if k else None)
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.exposure_type is not None:
            result['ExposureType'] = self.exposure_type
        if self.intranet_ip is not None:
            result['IntranetIp'] = self.intranet_ip
        if self.exposure_type_id is not None:
            result['ExposureTypeId'] = self.exposure_type_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.asap_vul_count is not None:
            result['AsapVulCount'] = self.asap_vul_count
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        result['RealVulList'] = []
        if self.real_vul_list is not None:
            for k in self.real_vul_list:
                result['RealVulList'].append(k.to_map() if k else None)
        if self.exposure_port is not None:
            result['ExposurePort'] = self.exposure_port
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.later_vul_count is not None:
            result['LaterVulCount'] = self.later_vul_count
        if self.exposure_component is not None:
            result['ExposureComponent'] = self.exposure_component
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExposureIp') is not None:
            self.exposure_ip = m.get('ExposureIp')
        if m.get('InternetIp') is not None:
            self.internet_ip = m.get('InternetIp')
        if m.get('NntfVulCount') is not None:
            self.nntf_vul_count = m.get('NntfVulCount')
        self.all_vul_list = []
        if m.get('AllVulList') is not None:
            for k in m.get('AllVulList'):
                temp_model = DescribeExposedInstanceDetailResponseBodyExposedChainsAllVulList()
                self.all_vul_list.append(temp_model.from_map(k))
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ExposureType') is not None:
            self.exposure_type = m.get('ExposureType')
        if m.get('IntranetIp') is not None:
            self.intranet_ip = m.get('IntranetIp')
        if m.get('ExposureTypeId') is not None:
            self.exposure_type_id = m.get('ExposureTypeId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('AsapVulCount') is not None:
            self.asap_vul_count = m.get('AsapVulCount')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        self.real_vul_list = []
        if m.get('RealVulList') is not None:
            for k in m.get('RealVulList'):
                temp_model = DescribeExposedInstanceDetailResponseBodyExposedChainsRealVulList()
                self.real_vul_list.append(temp_model.from_map(k))
        if m.get('ExposurePort') is not None:
            self.exposure_port = m.get('ExposurePort')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('LaterVulCount') is not None:
            self.later_vul_count = m.get('LaterVulCount')
        if m.get('ExposureComponent') is not None:
            self.exposure_component = m.get('ExposureComponent')
        return self


class DescribeExposedInstanceDetailResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        exposed_chains: List[DescribeExposedInstanceDetailResponseBodyExposedChains] = None,
    ):
        self.request_id = request_id
        self.exposed_chains = exposed_chains

    def validate(self):
        if self.exposed_chains:
            for k in self.exposed_chains:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['ExposedChains'] = []
        if self.exposed_chains is not None:
            for k in self.exposed_chains:
                result['ExposedChains'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.exposed_chains = []
        if m.get('ExposedChains') is not None:
            for k in m.get('ExposedChains'):
                temp_model = DescribeExposedInstanceDetailResponseBodyExposedChains()
                self.exposed_chains.append(temp_model.from_map(k))
        return self


class DescribeExposedInstanceDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeExposedInstanceDetailResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeExposedInstanceDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeExposedInstanceListRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        from_: str = None,
        page_size: int = None,
        current_page: int = None,
        uuid: str = None,
        group_id: int = None,
        vul_status: bool = None,
        exposure_component: str = None,
        exposure_type: str = None,
        exposure_port: str = None,
        exposure_ip: str = None,
        instance_id: str = None,
        instance_name: str = None,
    ):
        self.source_ip = source_ip
        self.from_ = from_
        self.page_size = page_size
        self.current_page = current_page
        self.uuid = uuid
        self.group_id = group_id
        self.vul_status = vul_status
        self.exposure_component = exposure_component
        self.exposure_type = exposure_type
        self.exposure_port = exposure_port
        self.exposure_ip = exposure_ip
        self.instance_id = instance_id
        self.instance_name = instance_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.from_ is not None:
            result['From'] = self.from_
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.vul_status is not None:
            result['VulStatus'] = self.vul_status
        if self.exposure_component is not None:
            result['ExposureComponent'] = self.exposure_component
        if self.exposure_type is not None:
            result['ExposureType'] = self.exposure_type
        if self.exposure_port is not None:
            result['ExposurePort'] = self.exposure_port
        if self.exposure_ip is not None:
            result['ExposureIp'] = self.exposure_ip
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('From') is not None:
            self.from_ = m.get('From')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('VulStatus') is not None:
            self.vul_status = m.get('VulStatus')
        if m.get('ExposureComponent') is not None:
            self.exposure_component = m.get('ExposureComponent')
        if m.get('ExposureType') is not None:
            self.exposure_type = m.get('ExposureType')
        if m.get('ExposurePort') is not None:
            self.exposure_port = m.get('ExposurePort')
        if m.get('ExposureIp') is not None:
            self.exposure_ip = m.get('ExposureIp')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        return self


class DescribeExposedInstanceListResponseBodyPageInfo(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        page_size: int = None,
        total_count: int = None,
        count: int = None,
    ):
        self.current_page = current_page
        self.page_size = page_size
        self.total_count = total_count
        self.count = count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.count is not None:
            result['Count'] = self.count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        return self


class DescribeExposedInstanceListResponseBodyExposedInstances(TeaModel):
    def __init__(
        self,
        total_vul_count: int = None,
        exposure_ip: str = None,
        internet_ip: str = None,
        nntf_vul_count: int = None,
        instance_id: str = None,
        exposure_type: str = None,
        intranet_ip: str = None,
        exposure_type_id: str = None,
        region_id: str = None,
        asap_vul_count: int = None,
        uuid: str = None,
        exposure_port: str = None,
        group_name: str = None,
        group_id: int = None,
        instance_name: str = None,
        exposure_component: str = None,
        later_vul_count: int = None,
    ):
        self.total_vul_count = total_vul_count
        self.exposure_ip = exposure_ip
        self.internet_ip = internet_ip
        self.nntf_vul_count = nntf_vul_count
        self.instance_id = instance_id
        self.exposure_type = exposure_type
        self.intranet_ip = intranet_ip
        self.exposure_type_id = exposure_type_id
        self.region_id = region_id
        self.asap_vul_count = asap_vul_count
        self.uuid = uuid
        self.exposure_port = exposure_port
        self.group_name = group_name
        self.group_id = group_id
        self.instance_name = instance_name
        self.exposure_component = exposure_component
        self.later_vul_count = later_vul_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.total_vul_count is not None:
            result['TotalVulCount'] = self.total_vul_count
        if self.exposure_ip is not None:
            result['ExposureIp'] = self.exposure_ip
        if self.internet_ip is not None:
            result['InternetIp'] = self.internet_ip
        if self.nntf_vul_count is not None:
            result['NntfVulCount'] = self.nntf_vul_count
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.exposure_type is not None:
            result['ExposureType'] = self.exposure_type
        if self.intranet_ip is not None:
            result['IntranetIp'] = self.intranet_ip
        if self.exposure_type_id is not None:
            result['ExposureTypeId'] = self.exposure_type_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.asap_vul_count is not None:
            result['AsapVulCount'] = self.asap_vul_count
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        if self.exposure_port is not None:
            result['ExposurePort'] = self.exposure_port
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.exposure_component is not None:
            result['ExposureComponent'] = self.exposure_component
        if self.later_vul_count is not None:
            result['LaterVulCount'] = self.later_vul_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalVulCount') is not None:
            self.total_vul_count = m.get('TotalVulCount')
        if m.get('ExposureIp') is not None:
            self.exposure_ip = m.get('ExposureIp')
        if m.get('InternetIp') is not None:
            self.internet_ip = m.get('InternetIp')
        if m.get('NntfVulCount') is not None:
            self.nntf_vul_count = m.get('NntfVulCount')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ExposureType') is not None:
            self.exposure_type = m.get('ExposureType')
        if m.get('IntranetIp') is not None:
            self.intranet_ip = m.get('IntranetIp')
        if m.get('ExposureTypeId') is not None:
            self.exposure_type_id = m.get('ExposureTypeId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('AsapVulCount') is not None:
            self.asap_vul_count = m.get('AsapVulCount')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        if m.get('ExposurePort') is not None:
            self.exposure_port = m.get('ExposurePort')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('ExposureComponent') is not None:
            self.exposure_component = m.get('ExposureComponent')
        if m.get('LaterVulCount') is not None:
            self.later_vul_count = m.get('LaterVulCount')
        return self


class DescribeExposedInstanceListResponseBody(TeaModel):
    def __init__(
        self,
        page_info: DescribeExposedInstanceListResponseBodyPageInfo = None,
        request_id: str = None,
        exposed_instances: List[DescribeExposedInstanceListResponseBodyExposedInstances] = None,
        success: bool = None,
    ):
        self.page_info = page_info
        self.request_id = request_id
        self.exposed_instances = exposed_instances
        self.success = success

    def validate(self):
        if self.page_info:
            self.page_info.validate()
        if self.exposed_instances:
            for k in self.exposed_instances:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['ExposedInstances'] = []
        if self.exposed_instances is not None:
            for k in self.exposed_instances:
                result['ExposedInstances'].append(k.to_map() if k else None)
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageInfo') is not None:
            temp_model = DescribeExposedInstanceListResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m['PageInfo'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.exposed_instances = []
        if m.get('ExposedInstances') is not None:
            for k in m.get('ExposedInstances'):
                temp_model = DescribeExposedInstanceListResponseBodyExposedInstances()
                self.exposed_instances.append(temp_model.from_map(k))
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeExposedInstanceListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeExposedInstanceListResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeExposedInstanceListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeExposedStatisticsRequest(TeaModel):
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


class DescribeExposedStatisticsResponseBody(TeaModel):
    def __init__(
        self,
        exposed_port_count: int = None,
        request_id: str = None,
        exposed_later_vul_count: int = None,
        exposed_instance_count: int = None,
        gateway_asset_count: int = None,
        exposed_component_count: int = None,
        exposed_nntf_vul_count: int = None,
        exposed_ip_count: int = None,
        exposed_asap_vul_count: int = None,
    ):
        self.exposed_port_count = exposed_port_count
        self.request_id = request_id
        self.exposed_later_vul_count = exposed_later_vul_count
        self.exposed_instance_count = exposed_instance_count
        self.gateway_asset_count = gateway_asset_count
        self.exposed_component_count = exposed_component_count
        self.exposed_nntf_vul_count = exposed_nntf_vul_count
        self.exposed_ip_count = exposed_ip_count
        self.exposed_asap_vul_count = exposed_asap_vul_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.exposed_port_count is not None:
            result['ExposedPortCount'] = self.exposed_port_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.exposed_later_vul_count is not None:
            result['ExposedLaterVulCount'] = self.exposed_later_vul_count
        if self.exposed_instance_count is not None:
            result['ExposedInstanceCount'] = self.exposed_instance_count
        if self.gateway_asset_count is not None:
            result['GatewayAssetCount'] = self.gateway_asset_count
        if self.exposed_component_count is not None:
            result['ExposedComponentCount'] = self.exposed_component_count
        if self.exposed_nntf_vul_count is not None:
            result['ExposedNntfVulCount'] = self.exposed_nntf_vul_count
        if self.exposed_ip_count is not None:
            result['ExposedIpCount'] = self.exposed_ip_count
        if self.exposed_asap_vul_count is not None:
            result['ExposedAsapVulCount'] = self.exposed_asap_vul_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExposedPortCount') is not None:
            self.exposed_port_count = m.get('ExposedPortCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ExposedLaterVulCount') is not None:
            self.exposed_later_vul_count = m.get('ExposedLaterVulCount')
        if m.get('ExposedInstanceCount') is not None:
            self.exposed_instance_count = m.get('ExposedInstanceCount')
        if m.get('GatewayAssetCount') is not None:
            self.gateway_asset_count = m.get('GatewayAssetCount')
        if m.get('ExposedComponentCount') is not None:
            self.exposed_component_count = m.get('ExposedComponentCount')
        if m.get('ExposedNntfVulCount') is not None:
            self.exposed_nntf_vul_count = m.get('ExposedNntfVulCount')
        if m.get('ExposedIpCount') is not None:
            self.exposed_ip_count = m.get('ExposedIpCount')
        if m.get('ExposedAsapVulCount') is not None:
            self.exposed_asap_vul_count = m.get('ExposedAsapVulCount')
        return self


class DescribeExposedStatisticsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeExposedStatisticsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeExposedStatisticsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeFieldStatisticsRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        region_id: str = None,
        machine_types: str = None,
    ):
        self.source_ip = source_ip
        self.region_id = region_id
        self.machine_types = machine_types

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.machine_types is not None:
            result['MachineTypes'] = self.machine_types
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('MachineTypes') is not None:
            self.machine_types = m.get('MachineTypes')
        return self


class DescribeFieldStatisticsResponseBodyGroupedFields(TeaModel):
    def __init__(
        self,
        offline_instance_count: int = None,
        region_count: int = None,
        new_instance_count: int = None,
        group_count: int = None,
        exposed_instance_count: int = None,
        general_asset_count: int = None,
        unprotected_instance_count: int = None,
        important_asset_count: int = None,
        test_asset_count: int = None,
        vpc_count: int = None,
        instance_count: int = None,
        not_running_status_count: int = None,
        risk_instance_count: int = None,
    ):
        self.offline_instance_count = offline_instance_count
        self.region_count = region_count
        self.new_instance_count = new_instance_count
        self.group_count = group_count
        self.exposed_instance_count = exposed_instance_count
        self.general_asset_count = general_asset_count
        self.unprotected_instance_count = unprotected_instance_count
        self.important_asset_count = important_asset_count
        self.test_asset_count = test_asset_count
        self.vpc_count = vpc_count
        self.instance_count = instance_count
        self.not_running_status_count = not_running_status_count
        self.risk_instance_count = risk_instance_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.offline_instance_count is not None:
            result['OfflineInstanceCount'] = self.offline_instance_count
        if self.region_count is not None:
            result['RegionCount'] = self.region_count
        if self.new_instance_count is not None:
            result['NewInstanceCount'] = self.new_instance_count
        if self.group_count is not None:
            result['GroupCount'] = self.group_count
        if self.exposed_instance_count is not None:
            result['ExposedInstanceCount'] = self.exposed_instance_count
        if self.general_asset_count is not None:
            result['GeneralAssetCount'] = self.general_asset_count
        if self.unprotected_instance_count is not None:
            result['UnprotectedInstanceCount'] = self.unprotected_instance_count
        if self.important_asset_count is not None:
            result['ImportantAssetCount'] = self.important_asset_count
        if self.test_asset_count is not None:
            result['TestAssetCount'] = self.test_asset_count
        if self.vpc_count is not None:
            result['VpcCount'] = self.vpc_count
        if self.instance_count is not None:
            result['InstanceCount'] = self.instance_count
        if self.not_running_status_count is not None:
            result['NotRunningStatusCount'] = self.not_running_status_count
        if self.risk_instance_count is not None:
            result['RiskInstanceCount'] = self.risk_instance_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OfflineInstanceCount') is not None:
            self.offline_instance_count = m.get('OfflineInstanceCount')
        if m.get('RegionCount') is not None:
            self.region_count = m.get('RegionCount')
        if m.get('NewInstanceCount') is not None:
            self.new_instance_count = m.get('NewInstanceCount')
        if m.get('GroupCount') is not None:
            self.group_count = m.get('GroupCount')
        if m.get('ExposedInstanceCount') is not None:
            self.exposed_instance_count = m.get('ExposedInstanceCount')
        if m.get('GeneralAssetCount') is not None:
            self.general_asset_count = m.get('GeneralAssetCount')
        if m.get('UnprotectedInstanceCount') is not None:
            self.unprotected_instance_count = m.get('UnprotectedInstanceCount')
        if m.get('ImportantAssetCount') is not None:
            self.important_asset_count = m.get('ImportantAssetCount')
        if m.get('TestAssetCount') is not None:
            self.test_asset_count = m.get('TestAssetCount')
        if m.get('VpcCount') is not None:
            self.vpc_count = m.get('VpcCount')
        if m.get('InstanceCount') is not None:
            self.instance_count = m.get('InstanceCount')
        if m.get('NotRunningStatusCount') is not None:
            self.not_running_status_count = m.get('NotRunningStatusCount')
        if m.get('RiskInstanceCount') is not None:
            self.risk_instance_count = m.get('RiskInstanceCount')
        return self


class DescribeFieldStatisticsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        grouped_fields: DescribeFieldStatisticsResponseBodyGroupedFields = None,
    ):
        self.request_id = request_id
        self.grouped_fields = grouped_fields

    def validate(self):
        if self.grouped_fields:
            self.grouped_fields.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.grouped_fields is not None:
            result['GroupedFields'] = self.grouped_fields.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('GroupedFields') is not None:
            temp_model = DescribeFieldStatisticsResponseBodyGroupedFields()
            self.grouped_fields = temp_model.from_map(m['GroupedFields'])
        return self


class DescribeFieldStatisticsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeFieldStatisticsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeFieldStatisticsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeGraph4InvestigationOnlineRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        namespace: str = None,
        vertex_id: str = None,
        anomaly_uuid: str = None,
        anomaly_id: str = None,
        path_length: int = None,
        direction: str = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.namespace = namespace
        self.vertex_id = vertex_id
        self.anomaly_uuid = anomaly_uuid
        self.anomaly_id = anomaly_id
        self.path_length = path_length
        self.direction = direction

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.vertex_id is not None:
            result['VertexId'] = self.vertex_id
        if self.anomaly_uuid is not None:
            result['AnomalyUuid'] = self.anomaly_uuid
        if self.anomaly_id is not None:
            result['AnomalyId'] = self.anomaly_id
        if self.path_length is not None:
            result['PathLength'] = self.path_length
        if self.direction is not None:
            result['Direction'] = self.direction
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('VertexId') is not None:
            self.vertex_id = m.get('VertexId')
        if m.get('AnomalyUuid') is not None:
            self.anomaly_uuid = m.get('AnomalyUuid')
        if m.get('AnomalyId') is not None:
            self.anomaly_id = m.get('AnomalyId')
        if m.get('PathLength') is not None:
            self.path_length = m.get('PathLength')
        if m.get('Direction') is not None:
            self.direction = m.get('Direction')
        return self


class DescribeGraph4InvestigationOnlineResponseBodyDataVertexListNeighborList(TeaModel):
    def __init__(
        self,
        type: str = None,
        has_more: bool = None,
        count: int = None,
    ):
        self.type = type
        self.has_more = has_more
        self.count = count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.has_more is not None:
            result['HasMore'] = self.has_more
        if self.count is not None:
            result['Count'] = self.count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('HasMore') is not None:
            self.has_more = m.get('HasMore')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        return self


class DescribeGraph4InvestigationOnlineResponseBodyDataVertexList(TeaModel):
    def __init__(
        self,
        type: str = None,
        uuid: str = None,
        time: str = None,
        aliuid: str = None,
        neighbor_list: List[DescribeGraph4InvestigationOnlineResponseBodyDataVertexListNeighborList] = None,
        position: str = None,
        position_id: str = None,
        name: str = None,
        id: str = None,
        properties: str = None,
    ):
        self.type = type
        self.uuid = uuid
        self.time = time
        self.aliuid = aliuid
        self.neighbor_list = neighbor_list
        self.position = position
        self.position_id = position_id
        self.name = name
        self.id = id
        self.properties = properties

    def validate(self):
        if self.neighbor_list:
            for k in self.neighbor_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        if self.time is not None:
            result['Time'] = self.time
        if self.aliuid is not None:
            result['Aliuid'] = self.aliuid
        result['NeighborList'] = []
        if self.neighbor_list is not None:
            for k in self.neighbor_list:
                result['NeighborList'].append(k.to_map() if k else None)
        if self.position is not None:
            result['Position'] = self.position
        if self.position_id is not None:
            result['PositionId'] = self.position_id
        if self.name is not None:
            result['Name'] = self.name
        if self.id is not None:
            result['Id'] = self.id
        if self.properties is not None:
            result['Properties'] = self.properties
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        if m.get('Time') is not None:
            self.time = m.get('Time')
        if m.get('Aliuid') is not None:
            self.aliuid = m.get('Aliuid')
        self.neighbor_list = []
        if m.get('NeighborList') is not None:
            for k in m.get('NeighborList'):
                temp_model = DescribeGraph4InvestigationOnlineResponseBodyDataVertexListNeighborList()
                self.neighbor_list.append(temp_model.from_map(k))
        if m.get('Position') is not None:
            self.position = m.get('Position')
        if m.get('PositionId') is not None:
            self.position_id = m.get('PositionId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Properties') is not None:
            self.properties = m.get('Properties')
        return self


class DescribeGraph4InvestigationOnlineResponseBodyDataEntityTypeList(TeaModel):
    def __init__(
        self,
        display_color: str = None,
        display_icon: str = None,
        display_order: str = None,
        name: str = None,
        id: str = None,
    ):
        self.display_color = display_color
        self.display_icon = display_icon
        self.display_order = display_order
        self.name = name
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.display_color is not None:
            result['DisplayColor'] = self.display_color
        if self.display_icon is not None:
            result['DisplayIcon'] = self.display_icon
        if self.display_order is not None:
            result['DisplayOrder'] = self.display_order
        if self.name is not None:
            result['Name'] = self.name
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisplayColor') is not None:
            self.display_color = m.get('DisplayColor')
        if m.get('DisplayIcon') is not None:
            self.display_icon = m.get('DisplayIcon')
        if m.get('DisplayOrder') is not None:
            self.display_order = m.get('DisplayOrder')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class DescribeGraph4InvestigationOnlineResponseBodyDataRelationTypeList(TeaModel):
    def __init__(
        self,
        show_type: str = None,
        name: str = None,
        id: str = None,
        directed: int = None,
    ):
        self.show_type = show_type
        self.name = name
        self.id = id
        self.directed = directed

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.show_type is not None:
            result['ShowType'] = self.show_type
        if self.name is not None:
            result['Name'] = self.name
        if self.id is not None:
            result['Id'] = self.id
        if self.directed is not None:
            result['Directed'] = self.directed
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ShowType') is not None:
            self.show_type = m.get('ShowType')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Directed') is not None:
            self.directed = m.get('Directed')
        return self


class DescribeGraph4InvestigationOnlineResponseBodyDataEdgeList(TeaModel):
    def __init__(
        self,
        type: str = None,
        time: str = None,
        end_id: str = None,
        start_type: str = None,
        end_type: str = None,
        name: str = None,
        start_id: str = None,
        id: int = None,
    ):
        self.type = type
        self.time = time
        self.end_id = end_id
        self.start_type = start_type
        self.end_type = end_type
        self.name = name
        self.start_id = start_id
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.time is not None:
            result['Time'] = self.time
        if self.end_id is not None:
            result['EndId'] = self.end_id
        if self.start_type is not None:
            result['StartType'] = self.start_type
        if self.end_type is not None:
            result['EndType'] = self.end_type
        if self.name is not None:
            result['Name'] = self.name
        if self.start_id is not None:
            result['StartId'] = self.start_id
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Time') is not None:
            self.time = m.get('Time')
        if m.get('EndId') is not None:
            self.end_id = m.get('EndId')
        if m.get('StartType') is not None:
            self.start_type = m.get('StartType')
        if m.get('EndType') is not None:
            self.end_type = m.get('EndType')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('StartId') is not None:
            self.start_id = m.get('StartId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class DescribeGraph4InvestigationOnlineResponseBodyData(TeaModel):
    def __init__(
        self,
        vertex_list: List[DescribeGraph4InvestigationOnlineResponseBodyDataVertexList] = None,
        entity_type_list: List[DescribeGraph4InvestigationOnlineResponseBodyDataEntityTypeList] = None,
        relation_type_list: List[DescribeGraph4InvestigationOnlineResponseBodyDataRelationTypeList] = None,
        edge_list: List[DescribeGraph4InvestigationOnlineResponseBodyDataEdgeList] = None,
    ):
        self.vertex_list = vertex_list
        self.entity_type_list = entity_type_list
        self.relation_type_list = relation_type_list
        self.edge_list = edge_list

    def validate(self):
        if self.vertex_list:
            for k in self.vertex_list:
                if k:
                    k.validate()
        if self.entity_type_list:
            for k in self.entity_type_list:
                if k:
                    k.validate()
        if self.relation_type_list:
            for k in self.relation_type_list:
                if k:
                    k.validate()
        if self.edge_list:
            for k in self.edge_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['VertexList'] = []
        if self.vertex_list is not None:
            for k in self.vertex_list:
                result['VertexList'].append(k.to_map() if k else None)
        result['EntityTypeList'] = []
        if self.entity_type_list is not None:
            for k in self.entity_type_list:
                result['EntityTypeList'].append(k.to_map() if k else None)
        result['RelationTypeList'] = []
        if self.relation_type_list is not None:
            for k in self.relation_type_list:
                result['RelationTypeList'].append(k.to_map() if k else None)
        result['EdgeList'] = []
        if self.edge_list is not None:
            for k in self.edge_list:
                result['EdgeList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.vertex_list = []
        if m.get('VertexList') is not None:
            for k in m.get('VertexList'):
                temp_model = DescribeGraph4InvestigationOnlineResponseBodyDataVertexList()
                self.vertex_list.append(temp_model.from_map(k))
        self.entity_type_list = []
        if m.get('EntityTypeList') is not None:
            for k in m.get('EntityTypeList'):
                temp_model = DescribeGraph4InvestigationOnlineResponseBodyDataEntityTypeList()
                self.entity_type_list.append(temp_model.from_map(k))
        self.relation_type_list = []
        if m.get('RelationTypeList') is not None:
            for k in m.get('RelationTypeList'):
                temp_model = DescribeGraph4InvestigationOnlineResponseBodyDataRelationTypeList()
                self.relation_type_list.append(temp_model.from_map(k))
        self.edge_list = []
        if m.get('EdgeList') is not None:
            for k in m.get('EdgeList'):
                temp_model = DescribeGraph4InvestigationOnlineResponseBodyDataEdgeList()
                self.edge_list.append(temp_model.from_map(k))
        return self


class DescribeGraph4InvestigationOnlineResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: DescribeGraph4InvestigationOnlineResponseBodyData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = DescribeGraph4InvestigationOnlineResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class DescribeGraph4InvestigationOnlineResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeGraph4InvestigationOnlineResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeGraph4InvestigationOnlineResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeGroupedContainerInstancesRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        criteria: str = None,
        logical_exp: str = None,
        group_field: str = None,
        field_value: str = None,
        page_size: int = None,
        current_page: int = None,
    ):
        self.source_ip = source_ip
        self.criteria = criteria
        self.logical_exp = logical_exp
        self.group_field = group_field
        self.field_value = field_value
        self.page_size = page_size
        self.current_page = current_page

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.criteria is not None:
            result['Criteria'] = self.criteria
        if self.logical_exp is not None:
            result['LogicalExp'] = self.logical_exp
        if self.group_field is not None:
            result['GroupField'] = self.group_field
        if self.field_value is not None:
            result['FieldValue'] = self.field_value
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Criteria') is not None:
            self.criteria = m.get('Criteria')
        if m.get('LogicalExp') is not None:
            self.logical_exp = m.get('LogicalExp')
        if m.get('GroupField') is not None:
            self.group_field = m.get('GroupField')
        if m.get('FieldValue') is not None:
            self.field_value = m.get('FieldValue')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        return self


class DescribeGroupedContainerInstancesResponseBodyPageInfo(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        page_size: int = None,
        total_count: int = None,
        count: int = None,
    ):
        self.current_page = current_page
        self.page_size = page_size
        self.total_count = total_count
        self.count = count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.count is not None:
            result['Count'] = self.count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        return self


class DescribeGroupedContainerInstancesResponseBodyGroupedContainerInstanceList(TeaModel):
    def __init__(
        self,
        host_ip: str = None,
        risk_level: str = None,
        risk_status: str = None,
        pod: str = None,
        create_time: int = None,
        custer_state: str = None,
        namespace: str = None,
        instance_id: str = None,
        region_id: str = None,
        app_name: str = None,
        instance_count: int = None,
        cluster_type: str = None,
        cluster_name: str = None,
        pod_ip: str = None,
        vul_count: int = None,
        alarm_count: int = None,
        risk_instance_count: int = None,
        cluster_id: str = None,
    ):
        self.host_ip = host_ip
        self.risk_level = risk_level
        self.risk_status = risk_status
        self.pod = pod
        self.create_time = create_time
        self.custer_state = custer_state
        self.namespace = namespace
        self.instance_id = instance_id
        self.region_id = region_id
        self.app_name = app_name
        self.instance_count = instance_count
        self.cluster_type = cluster_type
        self.cluster_name = cluster_name
        self.pod_ip = pod_ip
        self.vul_count = vul_count
        self.alarm_count = alarm_count
        self.risk_instance_count = risk_instance_count
        self.cluster_id = cluster_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.host_ip is not None:
            result['HostIp'] = self.host_ip
        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level
        if self.risk_status is not None:
            result['RiskStatus'] = self.risk_status
        if self.pod is not None:
            result['Pod'] = self.pod
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.custer_state is not None:
            result['CusterState'] = self.custer_state
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.instance_count is not None:
            result['InstanceCount'] = self.instance_count
        if self.cluster_type is not None:
            result['ClusterType'] = self.cluster_type
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name
        if self.pod_ip is not None:
            result['PodIp'] = self.pod_ip
        if self.vul_count is not None:
            result['VulCount'] = self.vul_count
        if self.alarm_count is not None:
            result['AlarmCount'] = self.alarm_count
        if self.risk_instance_count is not None:
            result['RiskInstanceCount'] = self.risk_instance_count
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HostIp') is not None:
            self.host_ip = m.get('HostIp')
        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')
        if m.get('RiskStatus') is not None:
            self.risk_status = m.get('RiskStatus')
        if m.get('Pod') is not None:
            self.pod = m.get('Pod')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CusterState') is not None:
            self.custer_state = m.get('CusterState')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('InstanceCount') is not None:
            self.instance_count = m.get('InstanceCount')
        if m.get('ClusterType') is not None:
            self.cluster_type = m.get('ClusterType')
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')
        if m.get('PodIp') is not None:
            self.pod_ip = m.get('PodIp')
        if m.get('VulCount') is not None:
            self.vul_count = m.get('VulCount')
        if m.get('AlarmCount') is not None:
            self.alarm_count = m.get('AlarmCount')
        if m.get('RiskInstanceCount') is not None:
            self.risk_instance_count = m.get('RiskInstanceCount')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        return self


class DescribeGroupedContainerInstancesResponseBody(TeaModel):
    def __init__(
        self,
        page_info: DescribeGroupedContainerInstancesResponseBodyPageInfo = None,
        grouped_container_instance_list: List[DescribeGroupedContainerInstancesResponseBodyGroupedContainerInstanceList] = None,
        request_id: str = None,
    ):
        self.page_info = page_info
        self.grouped_container_instance_list = grouped_container_instance_list
        self.request_id = request_id

    def validate(self):
        if self.page_info:
            self.page_info.validate()
        if self.grouped_container_instance_list:
            for k in self.grouped_container_instance_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()
        result['GroupedContainerInstanceList'] = []
        if self.grouped_container_instance_list is not None:
            for k in self.grouped_container_instance_list:
                result['GroupedContainerInstanceList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageInfo') is not None:
            temp_model = DescribeGroupedContainerInstancesResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m['PageInfo'])
        self.grouped_container_instance_list = []
        if m.get('GroupedContainerInstanceList') is not None:
            for k in m.get('GroupedContainerInstanceList'):
                temp_model = DescribeGroupedContainerInstancesResponseBodyGroupedContainerInstanceList()
                self.grouped_container_instance_list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeGroupedContainerInstancesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeGroupedContainerInstancesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeGroupedContainerInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeGroupedMaliciousFilesRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        levels: str = None,
        fuzzy_malicious_name: str = None,
        current_page: int = None,
        page_size: str = None,
        repo_region_id: str = None,
        repo_instance_id: str = None,
        repo_id: str = None,
        repo_name: str = None,
        repo_namespace: str = None,
        image_tag: str = None,
        image_digest: str = None,
        image_layer: str = None,
        uuids: List[str] = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.levels = levels
        self.fuzzy_malicious_name = fuzzy_malicious_name
        self.current_page = current_page
        self.page_size = page_size
        self.repo_region_id = repo_region_id
        self.repo_instance_id = repo_instance_id
        self.repo_id = repo_id
        self.repo_name = repo_name
        self.repo_namespace = repo_namespace
        self.image_tag = image_tag
        self.image_digest = image_digest
        self.image_layer = image_layer
        self.uuids = uuids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.levels is not None:
            result['Levels'] = self.levels
        if self.fuzzy_malicious_name is not None:
            result['FuzzyMaliciousName'] = self.fuzzy_malicious_name
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.repo_region_id is not None:
            result['RepoRegionId'] = self.repo_region_id
        if self.repo_instance_id is not None:
            result['RepoInstanceId'] = self.repo_instance_id
        if self.repo_id is not None:
            result['RepoId'] = self.repo_id
        if self.repo_name is not None:
            result['RepoName'] = self.repo_name
        if self.repo_namespace is not None:
            result['RepoNamespace'] = self.repo_namespace
        if self.image_tag is not None:
            result['ImageTag'] = self.image_tag
        if self.image_digest is not None:
            result['ImageDigest'] = self.image_digest
        if self.image_layer is not None:
            result['ImageLayer'] = self.image_layer
        if self.uuids is not None:
            result['Uuids'] = self.uuids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('Levels') is not None:
            self.levels = m.get('Levels')
        if m.get('FuzzyMaliciousName') is not None:
            self.fuzzy_malicious_name = m.get('FuzzyMaliciousName')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RepoRegionId') is not None:
            self.repo_region_id = m.get('RepoRegionId')
        if m.get('RepoInstanceId') is not None:
            self.repo_instance_id = m.get('RepoInstanceId')
        if m.get('RepoId') is not None:
            self.repo_id = m.get('RepoId')
        if m.get('RepoName') is not None:
            self.repo_name = m.get('RepoName')
        if m.get('RepoNamespace') is not None:
            self.repo_namespace = m.get('RepoNamespace')
        if m.get('ImageTag') is not None:
            self.image_tag = m.get('ImageTag')
        if m.get('ImageDigest') is not None:
            self.image_digest = m.get('ImageDigest')
        if m.get('ImageLayer') is not None:
            self.image_layer = m.get('ImageLayer')
        if m.get('Uuids') is not None:
            self.uuids = m.get('Uuids')
        return self


class DescribeGroupedMaliciousFilesResponseBodyPageInfo(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        page_size: int = None,
        total_count: int = None,
        count: int = None,
    ):
        self.current_page = current_page
        self.page_size = page_size
        self.total_count = total_count
        self.count = count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.count is not None:
            result['Count'] = self.count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        return self


class DescribeGroupedMaliciousFilesResponseBodyGroupedMaliciousFileResponse(TeaModel):
    def __init__(
        self,
        status: int = None,
        image_count: int = None,
        latest_scan_timestamp: int = None,
        malicious_name: str = None,
        malicious_md_5: str = None,
        first_scan_timestamp: int = None,
        level: str = None,
    ):
        self.status = status
        self.image_count = image_count
        self.latest_scan_timestamp = latest_scan_timestamp
        self.malicious_name = malicious_name
        self.malicious_md_5 = malicious_md_5
        self.first_scan_timestamp = first_scan_timestamp
        self.level = level

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.image_count is not None:
            result['ImageCount'] = self.image_count
        if self.latest_scan_timestamp is not None:
            result['LatestScanTimestamp'] = self.latest_scan_timestamp
        if self.malicious_name is not None:
            result['MaliciousName'] = self.malicious_name
        if self.malicious_md_5 is not None:
            result['MaliciousMd5'] = self.malicious_md_5
        if self.first_scan_timestamp is not None:
            result['FirstScanTimestamp'] = self.first_scan_timestamp
        if self.level is not None:
            result['Level'] = self.level
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ImageCount') is not None:
            self.image_count = m.get('ImageCount')
        if m.get('LatestScanTimestamp') is not None:
            self.latest_scan_timestamp = m.get('LatestScanTimestamp')
        if m.get('MaliciousName') is not None:
            self.malicious_name = m.get('MaliciousName')
        if m.get('MaliciousMd5') is not None:
            self.malicious_md_5 = m.get('MaliciousMd5')
        if m.get('FirstScanTimestamp') is not None:
            self.first_scan_timestamp = m.get('FirstScanTimestamp')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        return self


class DescribeGroupedMaliciousFilesResponseBody(TeaModel):
    def __init__(
        self,
        page_info: DescribeGroupedMaliciousFilesResponseBodyPageInfo = None,
        grouped_malicious_file_response: List[DescribeGroupedMaliciousFilesResponseBodyGroupedMaliciousFileResponse] = None,
        request_id: str = None,
    ):
        self.page_info = page_info
        self.grouped_malicious_file_response = grouped_malicious_file_response
        self.request_id = request_id

    def validate(self):
        if self.page_info:
            self.page_info.validate()
        if self.grouped_malicious_file_response:
            for k in self.grouped_malicious_file_response:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()
        result['GroupedMaliciousFileResponse'] = []
        if self.grouped_malicious_file_response is not None:
            for k in self.grouped_malicious_file_response:
                result['GroupedMaliciousFileResponse'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageInfo') is not None:
            temp_model = DescribeGroupedMaliciousFilesResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m['PageInfo'])
        self.grouped_malicious_file_response = []
        if m.get('GroupedMaliciousFileResponse') is not None:
            for k in m.get('GroupedMaliciousFileResponse'):
                temp_model = DescribeGroupedMaliciousFilesResponseBodyGroupedMaliciousFileResponse()
                self.grouped_malicious_file_response.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeGroupedMaliciousFilesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeGroupedMaliciousFilesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeGroupedMaliciousFilesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeGroupedTagsRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        machine_types: str = None,
    ):
        self.source_ip = source_ip
        self.machine_types = machine_types

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.machine_types is not None:
            result['MachineTypes'] = self.machine_types
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('MachineTypes') is not None:
            self.machine_types = m.get('MachineTypes')
        return self


class DescribeGroupedTagsResponseBodyGroupedFileds(TeaModel):
    def __init__(
        self,
        name: str = None,
        count: str = None,
        tag_id: int = None,
    ):
        self.name = name
        self.count = count
        self.tag_id = tag_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.count is not None:
            result['Count'] = self.count
        if self.tag_id is not None:
            result['TagId'] = self.tag_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('TagId') is not None:
            self.tag_id = m.get('TagId')
        return self


class DescribeGroupedTagsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        http_status_code: int = None,
        grouped_fileds: List[DescribeGroupedTagsResponseBodyGroupedFileds] = None,
        count: int = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.http_status_code = http_status_code
        self.grouped_fileds = grouped_fileds
        self.count = count
        self.success = success

    def validate(self):
        if self.grouped_fileds:
            for k in self.grouped_fileds:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        result['GroupedFileds'] = []
        if self.grouped_fileds is not None:
            for k in self.grouped_fileds:
                result['GroupedFileds'].append(k.to_map() if k else None)
        if self.count is not None:
            result['Count'] = self.count
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        self.grouped_fileds = []
        if m.get('GroupedFileds') is not None:
            for k in m.get('GroupedFileds'):
                temp_model = DescribeGroupedTagsResponseBodyGroupedFileds()
                self.grouped_fileds.append(temp_model.from_map(k))
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeGroupedTagsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeGroupedTagsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeGroupedTagsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeGroupedVulRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        type: str = None,
        uuids: str = None,
        alias_name: str = None,
        necessity: str = None,
        dealed: str = None,
        current_page: int = None,
        page_size: int = None,
        status_list: str = None,
        group_id: str = None,
        container_field_name: str = None,
        container_field_value: str = None,
        target_type: str = None,
        cluster_id: str = None,
        min_score: int = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.type = type
        self.uuids = uuids
        self.alias_name = alias_name
        self.necessity = necessity
        self.dealed = dealed
        self.current_page = current_page
        self.page_size = page_size
        self.status_list = status_list
        self.group_id = group_id
        self.container_field_name = container_field_name
        self.container_field_value = container_field_value
        self.target_type = target_type
        self.cluster_id = cluster_id
        self.min_score = min_score

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.type is not None:
            result['Type'] = self.type
        if self.uuids is not None:
            result['Uuids'] = self.uuids
        if self.alias_name is not None:
            result['AliasName'] = self.alias_name
        if self.necessity is not None:
            result['Necessity'] = self.necessity
        if self.dealed is not None:
            result['Dealed'] = self.dealed
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.status_list is not None:
            result['StatusList'] = self.status_list
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.container_field_name is not None:
            result['ContainerFieldName'] = self.container_field_name
        if self.container_field_value is not None:
            result['ContainerFieldValue'] = self.container_field_value
        if self.target_type is not None:
            result['TargetType'] = self.target_type
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.min_score is not None:
            result['MinScore'] = self.min_score
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Uuids') is not None:
            self.uuids = m.get('Uuids')
        if m.get('AliasName') is not None:
            self.alias_name = m.get('AliasName')
        if m.get('Necessity') is not None:
            self.necessity = m.get('Necessity')
        if m.get('Dealed') is not None:
            self.dealed = m.get('Dealed')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('StatusList') is not None:
            self.status_list = m.get('StatusList')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('ContainerFieldName') is not None:
            self.container_field_name = m.get('ContainerFieldName')
        if m.get('ContainerFieldValue') is not None:
            self.container_field_value = m.get('ContainerFieldValue')
        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('MinScore') is not None:
            self.min_score = m.get('MinScore')
        return self


class DescribeGroupedVulResponseBodyGroupedVulItems(TeaModel):
    def __init__(
        self,
        type: str = None,
        nntf_count: int = None,
        handled_count: int = None,
        gmt_last: int = None,
        tags: str = None,
        later_count: int = None,
        alias_name: str = None,
        name: str = None,
        asap_count: int = None,
    ):
        self.type = type
        self.nntf_count = nntf_count
        self.handled_count = handled_count
        self.gmt_last = gmt_last
        self.tags = tags
        self.later_count = later_count
        self.alias_name = alias_name
        self.name = name
        self.asap_count = asap_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.nntf_count is not None:
            result['NntfCount'] = self.nntf_count
        if self.handled_count is not None:
            result['HandledCount'] = self.handled_count
        if self.gmt_last is not None:
            result['GmtLast'] = self.gmt_last
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.later_count is not None:
            result['LaterCount'] = self.later_count
        if self.alias_name is not None:
            result['AliasName'] = self.alias_name
        if self.name is not None:
            result['Name'] = self.name
        if self.asap_count is not None:
            result['AsapCount'] = self.asap_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('NntfCount') is not None:
            self.nntf_count = m.get('NntfCount')
        if m.get('HandledCount') is not None:
            self.handled_count = m.get('HandledCount')
        if m.get('GmtLast') is not None:
            self.gmt_last = m.get('GmtLast')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('LaterCount') is not None:
            self.later_count = m.get('LaterCount')
        if m.get('AliasName') is not None:
            self.alias_name = m.get('AliasName')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('AsapCount') is not None:
            self.asap_count = m.get('AsapCount')
        return self


class DescribeGroupedVulResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        request_id: str = None,
        page_size: int = None,
        current_page: int = None,
        grouped_vul_items: List[DescribeGroupedVulResponseBodyGroupedVulItems] = None,
    ):
        self.total_count = total_count
        self.request_id = request_id
        self.page_size = page_size
        self.current_page = current_page
        self.grouped_vul_items = grouped_vul_items

    def validate(self):
        if self.grouped_vul_items:
            for k in self.grouped_vul_items:
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
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        result['GroupedVulItems'] = []
        if self.grouped_vul_items is not None:
            for k in self.grouped_vul_items:
                result['GroupedVulItems'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        self.grouped_vul_items = []
        if m.get('GroupedVulItems') is not None:
            for k in m.get('GroupedVulItems'):
                temp_model = DescribeGroupedVulResponseBodyGroupedVulItems()
                self.grouped_vul_items.append(temp_model.from_map(k))
        return self


class DescribeGroupedVulResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeGroupedVulResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeGroupedVulResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeHoneyPotAuthRequest(TeaModel):
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


class DescribeHoneyPotAuthResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        honey_pot_auth_count: int = None,
        honey_pot_count: int = None,
    ):
        self.request_id = request_id
        self.honey_pot_auth_count = honey_pot_auth_count
        self.honey_pot_count = honey_pot_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.honey_pot_auth_count is not None:
            result['HoneyPotAuthCount'] = self.honey_pot_auth_count
        if self.honey_pot_count is not None:
            result['HoneyPotCount'] = self.honey_pot_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('HoneyPotAuthCount') is not None:
            self.honey_pot_auth_count = m.get('HoneyPotAuthCount')
        if m.get('HoneyPotCount') is not None:
            self.honey_pot_count = m.get('HoneyPotCount')
        return self


class DescribeHoneyPotAuthResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeHoneyPotAuthResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeHoneyPotAuthResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeHoneyPotSuspStatisticsRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        from_: str = None,
        statistics_key_type: str = None,
        statistics_days: int = None,
    ):
        self.source_ip = source_ip
        self.from_ = from_
        self.statistics_key_type = statistics_key_type
        self.statistics_days = statistics_days

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.from_ is not None:
            result['From'] = self.from_
        if self.statistics_key_type is not None:
            result['StatisticsKeyType'] = self.statistics_key_type
        if self.statistics_days is not None:
            result['StatisticsDays'] = self.statistics_days
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('From') is not None:
            self.from_ = m.get('From')
        if m.get('StatisticsKeyType') is not None:
            self.statistics_key_type = m.get('StatisticsKeyType')
        if m.get('StatisticsDays') is not None:
            self.statistics_days = m.get('StatisticsDays')
        return self


class DescribeHoneyPotSuspStatisticsResponseBodySuspHoneyPotStatisticsResponse(TeaModel):
    def __init__(
        self,
        vpc_name: str = None,
        type: str = None,
        vpc_id: str = None,
        instance_name: str = None,
        instance_id: str = None,
        name: str = None,
        count: int = None,
    ):
        self.vpc_name = vpc_name
        self.type = type
        self.vpc_id = vpc_id
        self.instance_name = instance_name
        self.instance_id = instance_id
        self.name = name
        self.count = count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.vpc_name is not None:
            result['VpcName'] = self.vpc_name
        if self.type is not None:
            result['Type'] = self.type
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.name is not None:
            result['Name'] = self.name
        if self.count is not None:
            result['Count'] = self.count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VpcName') is not None:
            self.vpc_name = m.get('VpcName')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        return self


class DescribeHoneyPotSuspStatisticsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        susp_honey_pot_statistics_response: List[DescribeHoneyPotSuspStatisticsResponseBodySuspHoneyPotStatisticsResponse] = None,
    ):
        self.request_id = request_id
        self.susp_honey_pot_statistics_response = susp_honey_pot_statistics_response

    def validate(self):
        if self.susp_honey_pot_statistics_response:
            for k in self.susp_honey_pot_statistics_response:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['SuspHoneyPotStatisticsResponse'] = []
        if self.susp_honey_pot_statistics_response is not None:
            for k in self.susp_honey_pot_statistics_response:
                result['SuspHoneyPotStatisticsResponse'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.susp_honey_pot_statistics_response = []
        if m.get('SuspHoneyPotStatisticsResponse') is not None:
            for k in m.get('SuspHoneyPotStatisticsResponse'):
                temp_model = DescribeHoneyPotSuspStatisticsResponseBodySuspHoneyPotStatisticsResponse()
                self.susp_honey_pot_statistics_response.append(temp_model.from_map(k))
        return self


class DescribeHoneyPotSuspStatisticsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeHoneyPotSuspStatisticsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeHoneyPotSuspStatisticsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeImageGroupedVulListRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        type: str = None,
        group_id: str = None,
        cve_id: str = None,
        uuids: str = None,
        name: str = None,
        alias_name: str = None,
        patch_id: int = None,
        level: str = None,
        last_ts_start: int = None,
        last_ts_end: int = None,
        status_list: str = None,
        order_by: str = None,
        direction: str = None,
        necessity: str = None,
        dealed: str = None,
        create_ts_start: int = None,
        create_ts_end: int = None,
        current_page: int = None,
        page_size: int = None,
        remark: str = None,
        search_tags: str = None,
        repo_region_id: str = None,
        repo_instance_id: str = None,
        repo_id: str = None,
        repo_name: str = None,
        repo_namespace: str = None,
        image_tag: str = None,
        image_digest: str = None,
        image_layer: str = None,
    ):
        self.source_ip = source_ip
        self.type = type
        self.group_id = group_id
        self.cve_id = cve_id
        self.uuids = uuids
        self.name = name
        self.alias_name = alias_name
        self.patch_id = patch_id
        self.level = level
        self.last_ts_start = last_ts_start
        self.last_ts_end = last_ts_end
        self.status_list = status_list
        self.order_by = order_by
        self.direction = direction
        self.necessity = necessity
        self.dealed = dealed
        self.create_ts_start = create_ts_start
        self.create_ts_end = create_ts_end
        self.current_page = current_page
        self.page_size = page_size
        self.remark = remark
        self.search_tags = search_tags
        self.repo_region_id = repo_region_id
        self.repo_instance_id = repo_instance_id
        self.repo_id = repo_id
        self.repo_name = repo_name
        self.repo_namespace = repo_namespace
        self.image_tag = image_tag
        self.image_digest = image_digest
        self.image_layer = image_layer

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.type is not None:
            result['Type'] = self.type
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.cve_id is not None:
            result['CveId'] = self.cve_id
        if self.uuids is not None:
            result['Uuids'] = self.uuids
        if self.name is not None:
            result['Name'] = self.name
        if self.alias_name is not None:
            result['AliasName'] = self.alias_name
        if self.patch_id is not None:
            result['PatchId'] = self.patch_id
        if self.level is not None:
            result['Level'] = self.level
        if self.last_ts_start is not None:
            result['LastTsStart'] = self.last_ts_start
        if self.last_ts_end is not None:
            result['LastTsEnd'] = self.last_ts_end
        if self.status_list is not None:
            result['StatusList'] = self.status_list
        if self.order_by is not None:
            result['OrderBy'] = self.order_by
        if self.direction is not None:
            result['Direction'] = self.direction
        if self.necessity is not None:
            result['Necessity'] = self.necessity
        if self.dealed is not None:
            result['Dealed'] = self.dealed
        if self.create_ts_start is not None:
            result['CreateTsStart'] = self.create_ts_start
        if self.create_ts_end is not None:
            result['CreateTsEnd'] = self.create_ts_end
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.search_tags is not None:
            result['SearchTags'] = self.search_tags
        if self.repo_region_id is not None:
            result['RepoRegionId'] = self.repo_region_id
        if self.repo_instance_id is not None:
            result['RepoInstanceId'] = self.repo_instance_id
        if self.repo_id is not None:
            result['RepoId'] = self.repo_id
        if self.repo_name is not None:
            result['RepoName'] = self.repo_name
        if self.repo_namespace is not None:
            result['RepoNamespace'] = self.repo_namespace
        if self.image_tag is not None:
            result['ImageTag'] = self.image_tag
        if self.image_digest is not None:
            result['ImageDigest'] = self.image_digest
        if self.image_layer is not None:
            result['ImageLayer'] = self.image_layer
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('CveId') is not None:
            self.cve_id = m.get('CveId')
        if m.get('Uuids') is not None:
            self.uuids = m.get('Uuids')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('AliasName') is not None:
            self.alias_name = m.get('AliasName')
        if m.get('PatchId') is not None:
            self.patch_id = m.get('PatchId')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        if m.get('LastTsStart') is not None:
            self.last_ts_start = m.get('LastTsStart')
        if m.get('LastTsEnd') is not None:
            self.last_ts_end = m.get('LastTsEnd')
        if m.get('StatusList') is not None:
            self.status_list = m.get('StatusList')
        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')
        if m.get('Direction') is not None:
            self.direction = m.get('Direction')
        if m.get('Necessity') is not None:
            self.necessity = m.get('Necessity')
        if m.get('Dealed') is not None:
            self.dealed = m.get('Dealed')
        if m.get('CreateTsStart') is not None:
            self.create_ts_start = m.get('CreateTsStart')
        if m.get('CreateTsEnd') is not None:
            self.create_ts_end = m.get('CreateTsEnd')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('SearchTags') is not None:
            self.search_tags = m.get('SearchTags')
        if m.get('RepoRegionId') is not None:
            self.repo_region_id = m.get('RepoRegionId')
        if m.get('RepoInstanceId') is not None:
            self.repo_instance_id = m.get('RepoInstanceId')
        if m.get('RepoId') is not None:
            self.repo_id = m.get('RepoId')
        if m.get('RepoName') is not None:
            self.repo_name = m.get('RepoName')
        if m.get('RepoNamespace') is not None:
            self.repo_namespace = m.get('RepoNamespace')
        if m.get('ImageTag') is not None:
            self.image_tag = m.get('ImageTag')
        if m.get('ImageDigest') is not None:
            self.image_digest = m.get('ImageDigest')
        if m.get('ImageLayer') is not None:
            self.image_layer = m.get('ImageLayer')
        return self


class DescribeImageGroupedVulListResponseBodyGroupedVulItems(TeaModel):
    def __init__(
        self,
        status: int = None,
        type: str = None,
        nntf_count: int = None,
        gmt_last: int = None,
        last_scan_time: int = None,
        tags: str = None,
        later_count: int = None,
        alias_name: str = None,
        name: str = None,
        asap_count: int = None,
    ):
        self.status = status
        self.type = type
        self.nntf_count = nntf_count
        self.gmt_last = gmt_last
        self.last_scan_time = last_scan_time
        self.tags = tags
        self.later_count = later_count
        self.alias_name = alias_name
        self.name = name
        self.asap_count = asap_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        if self.nntf_count is not None:
            result['NntfCount'] = self.nntf_count
        if self.gmt_last is not None:
            result['GmtLast'] = self.gmt_last
        if self.last_scan_time is not None:
            result['LastScanTime'] = self.last_scan_time
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.later_count is not None:
            result['LaterCount'] = self.later_count
        if self.alias_name is not None:
            result['AliasName'] = self.alias_name
        if self.name is not None:
            result['Name'] = self.name
        if self.asap_count is not None:
            result['AsapCount'] = self.asap_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('NntfCount') is not None:
            self.nntf_count = m.get('NntfCount')
        if m.get('GmtLast') is not None:
            self.gmt_last = m.get('GmtLast')
        if m.get('LastScanTime') is not None:
            self.last_scan_time = m.get('LastScanTime')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('LaterCount') is not None:
            self.later_count = m.get('LaterCount')
        if m.get('AliasName') is not None:
            self.alias_name = m.get('AliasName')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('AsapCount') is not None:
            self.asap_count = m.get('AsapCount')
        return self


class DescribeImageGroupedVulListResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        request_id: str = None,
        page_size: int = None,
        current_page: int = None,
        grouped_vul_items: List[DescribeImageGroupedVulListResponseBodyGroupedVulItems] = None,
    ):
        self.total_count = total_count
        self.request_id = request_id
        self.page_size = page_size
        self.current_page = current_page
        self.grouped_vul_items = grouped_vul_items

    def validate(self):
        if self.grouped_vul_items:
            for k in self.grouped_vul_items:
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
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        result['GroupedVulItems'] = []
        if self.grouped_vul_items is not None:
            for k in self.grouped_vul_items:
                result['GroupedVulItems'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        self.grouped_vul_items = []
        if m.get('GroupedVulItems') is not None:
            for k in m.get('GroupedVulItems'):
                temp_model = DescribeImageGroupedVulListResponseBodyGroupedVulItems()
                self.grouped_vul_items.append(temp_model.from_map(k))
        return self


class DescribeImageGroupedVulListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeImageGroupedVulListResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeImageGroupedVulListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeImageStatisticsRequest(TeaModel):
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


class DescribeImageStatisticsResponseBody(TeaModel):
    def __init__(
        self,
        instance_count: int = None,
        request_id: str = None,
        risk_instance_count: int = None,
    ):
        self.instance_count = instance_count
        self.request_id = request_id
        self.risk_instance_count = risk_instance_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.instance_count is not None:
            result['InstanceCount'] = self.instance_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.risk_instance_count is not None:
            result['RiskInstanceCount'] = self.risk_instance_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceCount') is not None:
            self.instance_count = m.get('InstanceCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RiskInstanceCount') is not None:
            self.risk_instance_count = m.get('RiskInstanceCount')
        return self


class DescribeImageStatisticsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeImageStatisticsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeImageStatisticsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeImageVulListRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        ids: str = None,
        remark: str = None,
        group_id: str = None,
        type: str = None,
        uuids: str = None,
        name: str = None,
        alias_name: str = None,
        level: str = None,
        status_list: str = None,
        necessity: str = None,
        dealed: str = None,
        batch_name: str = None,
        resource: str = None,
        create_ts_start: int = None,
        create_ts_end: int = None,
        current_page: int = None,
        page_size: int = None,
        modify_ts_start: int = None,
        modify_ts_end: int = None,
        cve_id: str = None,
        repo_name: str = None,
        region_id: str = None,
        instance_id: str = None,
        repo_id: str = None,
        tag: str = None,
        digest: str = None,
        container_field_name: str = None,
        container_field_value: str = None,
        target_type: str = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.ids = ids
        self.remark = remark
        self.group_id = group_id
        self.type = type
        self.uuids = uuids
        self.name = name
        self.alias_name = alias_name
        self.level = level
        self.status_list = status_list
        self.necessity = necessity
        self.dealed = dealed
        self.batch_name = batch_name
        self.resource = resource
        self.create_ts_start = create_ts_start
        self.create_ts_end = create_ts_end
        self.current_page = current_page
        self.page_size = page_size
        self.modify_ts_start = modify_ts_start
        self.modify_ts_end = modify_ts_end
        self.cve_id = cve_id
        self.repo_name = repo_name
        self.region_id = region_id
        self.instance_id = instance_id
        self.repo_id = repo_id
        self.tag = tag
        self.digest = digest
        self.container_field_name = container_field_name
        self.container_field_value = container_field_value
        self.target_type = target_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.ids is not None:
            result['Ids'] = self.ids
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.type is not None:
            result['Type'] = self.type
        if self.uuids is not None:
            result['Uuids'] = self.uuids
        if self.name is not None:
            result['Name'] = self.name
        if self.alias_name is not None:
            result['AliasName'] = self.alias_name
        if self.level is not None:
            result['Level'] = self.level
        if self.status_list is not None:
            result['StatusList'] = self.status_list
        if self.necessity is not None:
            result['Necessity'] = self.necessity
        if self.dealed is not None:
            result['Dealed'] = self.dealed
        if self.batch_name is not None:
            result['BatchName'] = self.batch_name
        if self.resource is not None:
            result['Resource'] = self.resource
        if self.create_ts_start is not None:
            result['CreateTsStart'] = self.create_ts_start
        if self.create_ts_end is not None:
            result['CreateTsEnd'] = self.create_ts_end
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.modify_ts_start is not None:
            result['ModifyTsStart'] = self.modify_ts_start
        if self.modify_ts_end is not None:
            result['ModifyTsEnd'] = self.modify_ts_end
        if self.cve_id is not None:
            result['CveId'] = self.cve_id
        if self.repo_name is not None:
            result['RepoName'] = self.repo_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.repo_id is not None:
            result['RepoId'] = self.repo_id
        if self.tag is not None:
            result['Tag'] = self.tag
        if self.digest is not None:
            result['Digest'] = self.digest
        if self.container_field_name is not None:
            result['ContainerFieldName'] = self.container_field_name
        if self.container_field_value is not None:
            result['ContainerFieldValue'] = self.container_field_value
        if self.target_type is not None:
            result['TargetType'] = self.target_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('Ids') is not None:
            self.ids = m.get('Ids')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Uuids') is not None:
            self.uuids = m.get('Uuids')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('AliasName') is not None:
            self.alias_name = m.get('AliasName')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        if m.get('StatusList') is not None:
            self.status_list = m.get('StatusList')
        if m.get('Necessity') is not None:
            self.necessity = m.get('Necessity')
        if m.get('Dealed') is not None:
            self.dealed = m.get('Dealed')
        if m.get('BatchName') is not None:
            self.batch_name = m.get('BatchName')
        if m.get('Resource') is not None:
            self.resource = m.get('Resource')
        if m.get('CreateTsStart') is not None:
            self.create_ts_start = m.get('CreateTsStart')
        if m.get('CreateTsEnd') is not None:
            self.create_ts_end = m.get('CreateTsEnd')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ModifyTsStart') is not None:
            self.modify_ts_start = m.get('ModifyTsStart')
        if m.get('ModifyTsEnd') is not None:
            self.modify_ts_end = m.get('ModifyTsEnd')
        if m.get('CveId') is not None:
            self.cve_id = m.get('CveId')
        if m.get('RepoName') is not None:
            self.repo_name = m.get('RepoName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RepoId') is not None:
            self.repo_id = m.get('RepoId')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        if m.get('Digest') is not None:
            self.digest = m.get('Digest')
        if m.get('ContainerFieldName') is not None:
            self.container_field_name = m.get('ContainerFieldName')
        if m.get('ContainerFieldValue') is not None:
            self.container_field_value = m.get('ContainerFieldValue')
        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')
        return self


class DescribeImageVulListResponseBodyVulRecordsExtendContentJsonRpmEntityList(TeaModel):
    def __init__(
        self,
        layer: str = None,
        full_version: str = None,
        version: str = None,
        match_detail: str = None,
        path: str = None,
        name: str = None,
        update_cmd: str = None,
    ):
        self.layer = layer
        self.full_version = full_version
        self.version = version
        self.match_detail = match_detail
        self.path = path
        self.name = name
        self.update_cmd = update_cmd

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.layer is not None:
            result['Layer'] = self.layer
        if self.full_version is not None:
            result['FullVersion'] = self.full_version
        if self.version is not None:
            result['Version'] = self.version
        if self.match_detail is not None:
            result['MatchDetail'] = self.match_detail
        if self.path is not None:
            result['Path'] = self.path
        if self.name is not None:
            result['Name'] = self.name
        if self.update_cmd is not None:
            result['UpdateCmd'] = self.update_cmd
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Layer') is not None:
            self.layer = m.get('Layer')
        if m.get('FullVersion') is not None:
            self.full_version = m.get('FullVersion')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('MatchDetail') is not None:
            self.match_detail = m.get('MatchDetail')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('UpdateCmd') is not None:
            self.update_cmd = m.get('UpdateCmd')
        return self


class DescribeImageVulListResponseBodyVulRecordsExtendContentJson(TeaModel):
    def __init__(
        self,
        os_release: str = None,
        rpm_entity_list: List[DescribeImageVulListResponseBodyVulRecordsExtendContentJsonRpmEntityList] = None,
        os: str = None,
    ):
        self.os_release = os_release
        self.rpm_entity_list = rpm_entity_list
        self.os = os

    def validate(self):
        if self.rpm_entity_list:
            for k in self.rpm_entity_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.os_release is not None:
            result['OsRelease'] = self.os_release
        result['RpmEntityList'] = []
        if self.rpm_entity_list is not None:
            for k in self.rpm_entity_list:
                result['RpmEntityList'].append(k.to_map() if k else None)
        if self.os is not None:
            result['Os'] = self.os
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OsRelease') is not None:
            self.os_release = m.get('OsRelease')
        self.rpm_entity_list = []
        if m.get('RpmEntityList') is not None:
            for k in m.get('RpmEntityList'):
                temp_model = DescribeImageVulListResponseBodyVulRecordsExtendContentJsonRpmEntityList()
                self.rpm_entity_list.append(temp_model.from_map(k))
        if m.get('Os') is not None:
            self.os = m.get('Os')
        return self


class DescribeImageVulListResponseBodyVulRecords(TeaModel):
    def __init__(
        self,
        status: int = None,
        type: str = None,
        modify_ts: int = None,
        image_digest: str = None,
        layers: List[str] = None,
        primary_id: int = None,
        tag: str = None,
        related: str = None,
        last_ts: int = None,
        first_ts: int = None,
        necessity: str = None,
        uuid: str = None,
        alias_name: str = None,
        name: str = None,
        extend_content_json: DescribeImageVulListResponseBodyVulRecordsExtendContentJson = None,
    ):
        self.status = status
        self.type = type
        self.modify_ts = modify_ts
        self.image_digest = image_digest
        self.layers = layers
        self.primary_id = primary_id
        self.tag = tag
        self.related = related
        self.last_ts = last_ts
        self.first_ts = first_ts
        self.necessity = necessity
        self.uuid = uuid
        self.alias_name = alias_name
        self.name = name
        self.extend_content_json = extend_content_json

    def validate(self):
        if self.extend_content_json:
            self.extend_content_json.validate()

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        if self.modify_ts is not None:
            result['ModifyTs'] = self.modify_ts
        if self.image_digest is not None:
            result['ImageDigest'] = self.image_digest
        if self.layers is not None:
            result['Layers'] = self.layers
        if self.primary_id is not None:
            result['PrimaryId'] = self.primary_id
        if self.tag is not None:
            result['Tag'] = self.tag
        if self.related is not None:
            result['Related'] = self.related
        if self.last_ts is not None:
            result['LastTs'] = self.last_ts
        if self.first_ts is not None:
            result['FirstTs'] = self.first_ts
        if self.necessity is not None:
            result['Necessity'] = self.necessity
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        if self.alias_name is not None:
            result['AliasName'] = self.alias_name
        if self.name is not None:
            result['Name'] = self.name
        if self.extend_content_json is not None:
            result['ExtendContentJson'] = self.extend_content_json.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('ModifyTs') is not None:
            self.modify_ts = m.get('ModifyTs')
        if m.get('ImageDigest') is not None:
            self.image_digest = m.get('ImageDigest')
        if m.get('Layers') is not None:
            self.layers = m.get('Layers')
        if m.get('PrimaryId') is not None:
            self.primary_id = m.get('PrimaryId')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        if m.get('Related') is not None:
            self.related = m.get('Related')
        if m.get('LastTs') is not None:
            self.last_ts = m.get('LastTs')
        if m.get('FirstTs') is not None:
            self.first_ts = m.get('FirstTs')
        if m.get('Necessity') is not None:
            self.necessity = m.get('Necessity')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        if m.get('AliasName') is not None:
            self.alias_name = m.get('AliasName')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ExtendContentJson') is not None:
            temp_model = DescribeImageVulListResponseBodyVulRecordsExtendContentJson()
            self.extend_content_json = temp_model.from_map(m['ExtendContentJson'])
        return self


class DescribeImageVulListResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        request_id: str = None,
        page_size: int = None,
        vul_records: List[DescribeImageVulListResponseBodyVulRecords] = None,
        current_page: int = None,
    ):
        self.total_count = total_count
        self.request_id = request_id
        self.page_size = page_size
        self.vul_records = vul_records
        self.current_page = current_page

    def validate(self):
        if self.vul_records:
            for k in self.vul_records:
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
        result['VulRecords'] = []
        if self.vul_records is not None:
            for k in self.vul_records:
                result['VulRecords'].append(k.to_map() if k else None)
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
        self.vul_records = []
        if m.get('VulRecords') is not None:
            for k in m.get('VulRecords'):
                temp_model = DescribeImageVulListResponseBodyVulRecords()
                self.vul_records.append(temp_model.from_map(k))
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        return self


class DescribeImageVulListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeImageVulListResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeImageVulListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInstallCaptchaRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        deadline: str = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.deadline = deadline

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.deadline is not None:
            result['Deadline'] = self.deadline
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('Deadline') is not None:
            self.deadline = m.get('Deadline')
        return self


class DescribeInstallCaptchaResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        deadline: int = None,
        captcha_code: str = None,
    ):
        self.request_id = request_id
        self.deadline = deadline
        self.captcha_code = captcha_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.deadline is not None:
            result['Deadline'] = self.deadline
        if self.captcha_code is not None:
            result['CaptchaCode'] = self.captcha_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Deadline') is not None:
            self.deadline = m.get('Deadline')
        if m.get('CaptchaCode') is not None:
            self.captcha_code = m.get('CaptchaCode')
        return self


class DescribeInstallCaptchaResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeInstallCaptchaResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeInstallCaptchaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInstanceAntiBruteForceRulesRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        resource_owner_id: int = None,
        uuid_list: List[str] = None,
    ):
        self.source_ip = source_ip
        self.resource_owner_id = resource_owner_id
        self.uuid_list = uuid_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.uuid_list is not None:
            result['UuidList'] = self.uuid_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('UuidList') is not None:
            self.uuid_list = m.get('UuidList')
        return self


class DescribeInstanceAntiBruteForceRulesResponseBodyPageInfo(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        page_size: int = None,
        total_count: int = None,
        count: int = None,
    ):
        self.current_page = current_page
        self.page_size = page_size
        self.total_count = total_count
        self.count = count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.count is not None:
            result['Count'] = self.count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        return self


class DescribeInstanceAntiBruteForceRulesResponseBodyRules(TeaModel):
    def __init__(
        self,
        uuid: str = None,
        name: str = None,
        id: int = None,
    ):
        self.uuid = uuid
        self.name = name
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        if self.name is not None:
            result['Name'] = self.name
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class DescribeInstanceAntiBruteForceRulesResponseBody(TeaModel):
    def __init__(
        self,
        page_info: DescribeInstanceAntiBruteForceRulesResponseBodyPageInfo = None,
        request_id: str = None,
        rules: List[DescribeInstanceAntiBruteForceRulesResponseBodyRules] = None,
    ):
        self.page_info = page_info
        self.request_id = request_id
        self.rules = rules

    def validate(self):
        if self.page_info:
            self.page_info.validate()
        if self.rules:
            for k in self.rules:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Rules'] = []
        if self.rules is not None:
            for k in self.rules:
                result['Rules'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageInfo') is not None:
            temp_model = DescribeInstanceAntiBruteForceRulesResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m['PageInfo'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.rules = []
        if m.get('Rules') is not None:
            for k in m.get('Rules'):
                temp_model = DescribeInstanceAntiBruteForceRulesResponseBodyRules()
                self.rules.append(temp_model.from_map(k))
        return self


class DescribeInstanceAntiBruteForceRulesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeInstanceAntiBruteForceRulesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeInstanceAntiBruteForceRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInstanceStatisticsRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        uuid: str = None,
        from_: str = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.uuid = uuid
        self.from_ = from_

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
        if self.from_ is not None:
            result['From'] = self.from_
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        if m.get('From') is not None:
            self.from_ = m.get('From')
        return self


class DescribeInstanceStatisticsResponseBodyData(TeaModel):
    def __init__(
        self,
        account: int = None,
        app_num: int = None,
        sca_num: int = None,
        trojan: int = None,
        emg_num: int = None,
        cve_num: int = None,
        suspicious: int = None,
        cms_num: int = None,
        uuid: str = None,
        vul: int = None,
        health: int = None,
        sys_num: int = None,
    ):
        self.account = account
        self.app_num = app_num
        self.sca_num = sca_num
        self.trojan = trojan
        self.emg_num = emg_num
        self.cve_num = cve_num
        self.suspicious = suspicious
        self.cms_num = cms_num
        self.uuid = uuid
        self.vul = vul
        self.health = health
        self.sys_num = sys_num

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.account is not None:
            result['Account'] = self.account
        if self.app_num is not None:
            result['AppNum'] = self.app_num
        if self.sca_num is not None:
            result['ScaNum'] = self.sca_num
        if self.trojan is not None:
            result['Trojan'] = self.trojan
        if self.emg_num is not None:
            result['EmgNum'] = self.emg_num
        if self.cve_num is not None:
            result['CveNum'] = self.cve_num
        if self.suspicious is not None:
            result['Suspicious'] = self.suspicious
        if self.cms_num is not None:
            result['CmsNum'] = self.cms_num
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        if self.vul is not None:
            result['Vul'] = self.vul
        if self.health is not None:
            result['Health'] = self.health
        if self.sys_num is not None:
            result['SysNum'] = self.sys_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Account') is not None:
            self.account = m.get('Account')
        if m.get('AppNum') is not None:
            self.app_num = m.get('AppNum')
        if m.get('ScaNum') is not None:
            self.sca_num = m.get('ScaNum')
        if m.get('Trojan') is not None:
            self.trojan = m.get('Trojan')
        if m.get('EmgNum') is not None:
            self.emg_num = m.get('EmgNum')
        if m.get('CveNum') is not None:
            self.cve_num = m.get('CveNum')
        if m.get('Suspicious') is not None:
            self.suspicious = m.get('Suspicious')
        if m.get('CmsNum') is not None:
            self.cms_num = m.get('CmsNum')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        if m.get('Vul') is not None:
            self.vul = m.get('Vul')
        if m.get('Health') is not None:
            self.health = m.get('Health')
        if m.get('SysNum') is not None:
            self.sys_num = m.get('SysNum')
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


class DescribeIpInfoRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        ip: str = None,
        field: str = None,
    ):
        self.source_ip = source_ip
        self.ip = ip
        self.field = field

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.field is not None:
            result['Field'] = self.field
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('Field') is not None:
            self.field = m.get('Field')
        return self


class DescribeIpInfoResponseBody(TeaModel):
    def __init__(
        self,
        country: str = None,
        malicious_score: str = None,
        is_proxy_7d: str = None,
        day_cnt_30d_web_attack: str = None,
        is_web_attack: str = None,
        isp: str = None,
        gmt_last_c2: str = None,
        is_nat_1d: str = None,
        gmt_last_malicious_source: str = None,
        province: str = None,
        proxy_day_trace: str = None,
        gmt_last_web_attack: str = None,
        is_web_attack_7d: str = None,
        mining_pool_day_trace: str = None,
        is_c2: str = None,
        gmt_last_mining_pool: str = None,
        is_malicious_source_1d: str = None,
        is_mining_pool_1d: str = None,
        is_tor_1d: str = None,
        is_nat: str = None,
        request_id: str = None,
        ip: str = None,
        is_c27d: str = None,
        is_malicious_login_1d: str = None,
        tags: str = None,
        malicious_source_day_trace: str = None,
        is_mining_pool: str = None,
        gmt_first_mining_pool: str = None,
        is_idc: str = None,
        is_malicious_login: str = None,
        rdns: str = None,
        city: str = None,
        is_tor_7d: str = None,
        gmt_last_nat: str = None,
        gmt_last_malicious_login: str = None,
        is_nat_7d: str = None,
        is_proxy_1d: str = None,
        geo: str = None,
        gmt_first_c2: str = None,
        is_malicious_source_7d: str = None,
        is_mining_pool_7d: str = None,
        day_cnt_7d_tor: str = None,
        is_web_attack_30d: str = None,
        gmt_last_proxy: str = None,
        nat_day_trace: str = None,
        total_day_cnt_web_attack: str = None,
        is_web_attack_1d: str = None,
        malicious_login_day_trace: str = None,
        day_cnt_30d_tor: str = None,
        total_day_cnt_tor: str = None,
        is_proxy: str = None,
        c_2day_trace: str = None,
        is_c21d: str = None,
        is_malicious_source_30d: str = None,
        day_cnt_7d_web_attack: str = None,
        idc_name: str = None,
        tor_day_trace: str = None,
        is_tor: str = None,
        is_malicious_login_7d: str = None,
        gmt_last_tor: str = None,
        is_malicious_source: str = None,
        web_attack_day_trace: str = None,
    ):
        self.country = country
        self.malicious_score = malicious_score
        self.is_proxy_7d = is_proxy_7d
        self.day_cnt_30d_web_attack = day_cnt_30d_web_attack
        self.is_web_attack = is_web_attack
        self.isp = isp
        self.gmt_last_c2 = gmt_last_c2
        self.is_nat_1d = is_nat_1d
        self.gmt_last_malicious_source = gmt_last_malicious_source
        self.province = province
        self.proxy_day_trace = proxy_day_trace
        self.gmt_last_web_attack = gmt_last_web_attack
        self.is_web_attack_7d = is_web_attack_7d
        self.mining_pool_day_trace = mining_pool_day_trace
        self.is_c2 = is_c2
        self.gmt_last_mining_pool = gmt_last_mining_pool
        self.is_malicious_source_1d = is_malicious_source_1d
        self.is_mining_pool_1d = is_mining_pool_1d
        self.is_tor_1d = is_tor_1d
        self.is_nat = is_nat
        self.request_id = request_id
        self.ip = ip
        self.is_c27d = is_c27d
        self.is_malicious_login_1d = is_malicious_login_1d
        self.tags = tags
        self.malicious_source_day_trace = malicious_source_day_trace
        self.is_mining_pool = is_mining_pool
        self.gmt_first_mining_pool = gmt_first_mining_pool
        self.is_idc = is_idc
        self.is_malicious_login = is_malicious_login
        self.rdns = rdns
        self.city = city
        self.is_tor_7d = is_tor_7d
        self.gmt_last_nat = gmt_last_nat
        self.gmt_last_malicious_login = gmt_last_malicious_login
        self.is_nat_7d = is_nat_7d
        self.is_proxy_1d = is_proxy_1d
        self.geo = geo
        self.gmt_first_c2 = gmt_first_c2
        self.is_malicious_source_7d = is_malicious_source_7d
        self.is_mining_pool_7d = is_mining_pool_7d
        self.day_cnt_7d_tor = day_cnt_7d_tor
        self.is_web_attack_30d = is_web_attack_30d
        self.gmt_last_proxy = gmt_last_proxy
        self.nat_day_trace = nat_day_trace
        self.total_day_cnt_web_attack = total_day_cnt_web_attack
        self.is_web_attack_1d = is_web_attack_1d
        self.malicious_login_day_trace = malicious_login_day_trace
        self.day_cnt_30d_tor = day_cnt_30d_tor
        self.total_day_cnt_tor = total_day_cnt_tor
        self.is_proxy = is_proxy
        self.c_2day_trace = c_2day_trace
        self.is_c21d = is_c21d
        self.is_malicious_source_30d = is_malicious_source_30d
        self.day_cnt_7d_web_attack = day_cnt_7d_web_attack
        self.idc_name = idc_name
        self.tor_day_trace = tor_day_trace
        self.is_tor = is_tor
        self.is_malicious_login_7d = is_malicious_login_7d
        self.gmt_last_tor = gmt_last_tor
        self.is_malicious_source = is_malicious_source
        self.web_attack_day_trace = web_attack_day_trace

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.country is not None:
            result['country'] = self.country
        if self.malicious_score is not None:
            result['malicious_score'] = self.malicious_score
        if self.is_proxy_7d is not None:
            result['is_proxy_7d'] = self.is_proxy_7d
        if self.day_cnt_30d_web_attack is not None:
            result['day_cnt_30d_web_attack'] = self.day_cnt_30d_web_attack
        if self.is_web_attack is not None:
            result['is_web_attack'] = self.is_web_attack
        if self.isp is not None:
            result['isp'] = self.isp
        if self.gmt_last_c2 is not None:
            result['gmt_last_c2'] = self.gmt_last_c2
        if self.is_nat_1d is not None:
            result['is_nat_1d'] = self.is_nat_1d
        if self.gmt_last_malicious_source is not None:
            result['gmt_last_malicious_source'] = self.gmt_last_malicious_source
        if self.province is not None:
            result['province'] = self.province
        if self.proxy_day_trace is not None:
            result['proxy_day_trace'] = self.proxy_day_trace
        if self.gmt_last_web_attack is not None:
            result['gmt_last_web_attack'] = self.gmt_last_web_attack
        if self.is_web_attack_7d is not None:
            result['is_web_attack_7d'] = self.is_web_attack_7d
        if self.mining_pool_day_trace is not None:
            result['mining_pool_day_trace'] = self.mining_pool_day_trace
        if self.is_c2 is not None:
            result['is_c2'] = self.is_c2
        if self.gmt_last_mining_pool is not None:
            result['gmt_last_mining_pool'] = self.gmt_last_mining_pool
        if self.is_malicious_source_1d is not None:
            result['is_malicious_source_1d'] = self.is_malicious_source_1d
        if self.is_mining_pool_1d is not None:
            result['is_mining_pool_1d'] = self.is_mining_pool_1d
        if self.is_tor_1d is not None:
            result['is_tor_1d'] = self.is_tor_1d
        if self.is_nat is not None:
            result['is_nat'] = self.is_nat
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.ip is not None:
            result['ip'] = self.ip
        if self.is_c27d is not None:
            result['is_c2_7d'] = self.is_c27d
        if self.is_malicious_login_1d is not None:
            result['is_malicious_login_1d'] = self.is_malicious_login_1d
        if self.tags is not None:
            result['tags'] = self.tags
        if self.malicious_source_day_trace is not None:
            result['malicious_source_day_trace'] = self.malicious_source_day_trace
        if self.is_mining_pool is not None:
            result['is_mining_pool'] = self.is_mining_pool
        if self.gmt_first_mining_pool is not None:
            result['gmt_first_mining_pool'] = self.gmt_first_mining_pool
        if self.is_idc is not None:
            result['is_idc'] = self.is_idc
        if self.is_malicious_login is not None:
            result['is_malicious_login'] = self.is_malicious_login
        if self.rdns is not None:
            result['rdns'] = self.rdns
        if self.city is not None:
            result['city'] = self.city
        if self.is_tor_7d is not None:
            result['is_tor_7d'] = self.is_tor_7d
        if self.gmt_last_nat is not None:
            result['gmt_last_nat'] = self.gmt_last_nat
        if self.gmt_last_malicious_login is not None:
            result['gmt_last_malicious_login'] = self.gmt_last_malicious_login
        if self.is_nat_7d is not None:
            result['is_nat_7d'] = self.is_nat_7d
        if self.is_proxy_1d is not None:
            result['is_proxy_1d'] = self.is_proxy_1d
        if self.geo is not None:
            result['geo'] = self.geo
        if self.gmt_first_c2 is not None:
            result['gmt_first_c2'] = self.gmt_first_c2
        if self.is_malicious_source_7d is not None:
            result['is_malicious_source_7d'] = self.is_malicious_source_7d
        if self.is_mining_pool_7d is not None:
            result['is_mining_pool_7d'] = self.is_mining_pool_7d
        if self.day_cnt_7d_tor is not None:
            result['day_cnt_7d_tor'] = self.day_cnt_7d_tor
        if self.is_web_attack_30d is not None:
            result['is_web_attack_30d'] = self.is_web_attack_30d
        if self.gmt_last_proxy is not None:
            result['gmt_last_proxy'] = self.gmt_last_proxy
        if self.nat_day_trace is not None:
            result['nat_day_trace'] = self.nat_day_trace
        if self.total_day_cnt_web_attack is not None:
            result['total_day_cnt_web_attack'] = self.total_day_cnt_web_attack
        if self.is_web_attack_1d is not None:
            result['is_web_attack_1d'] = self.is_web_attack_1d
        if self.malicious_login_day_trace is not None:
            result['malicious_login_day_trace'] = self.malicious_login_day_trace
        if self.day_cnt_30d_tor is not None:
            result['day_cnt_30d_tor'] = self.day_cnt_30d_tor
        if self.total_day_cnt_tor is not None:
            result['total_day_cnt_tor'] = self.total_day_cnt_tor
        if self.is_proxy is not None:
            result['is_proxy'] = self.is_proxy
        if self.c_2day_trace is not None:
            result['c2_day_trace'] = self.c_2day_trace
        if self.is_c21d is not None:
            result['is_c2_1d'] = self.is_c21d
        if self.is_malicious_source_30d is not None:
            result['is_malicious_source_30d'] = self.is_malicious_source_30d
        if self.day_cnt_7d_web_attack is not None:
            result['day_cnt_7d_web_attack'] = self.day_cnt_7d_web_attack
        if self.idc_name is not None:
            result['idc_name'] = self.idc_name
        if self.tor_day_trace is not None:
            result['tor_day_trace'] = self.tor_day_trace
        if self.is_tor is not None:
            result['is_tor'] = self.is_tor
        if self.is_malicious_login_7d is not None:
            result['is_malicious_login_7d'] = self.is_malicious_login_7d
        if self.gmt_last_tor is not None:
            result['gmt_last_tor'] = self.gmt_last_tor
        if self.is_malicious_source is not None:
            result['is_malicious_source'] = self.is_malicious_source
        if self.web_attack_day_trace is not None:
            result['web_attack_day_trace'] = self.web_attack_day_trace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('country') is not None:
            self.country = m.get('country')
        if m.get('malicious_score') is not None:
            self.malicious_score = m.get('malicious_score')
        if m.get('is_proxy_7d') is not None:
            self.is_proxy_7d = m.get('is_proxy_7d')
        if m.get('day_cnt_30d_web_attack') is not None:
            self.day_cnt_30d_web_attack = m.get('day_cnt_30d_web_attack')
        if m.get('is_web_attack') is not None:
            self.is_web_attack = m.get('is_web_attack')
        if m.get('isp') is not None:
            self.isp = m.get('isp')
        if m.get('gmt_last_c2') is not None:
            self.gmt_last_c2 = m.get('gmt_last_c2')
        if m.get('is_nat_1d') is not None:
            self.is_nat_1d = m.get('is_nat_1d')
        if m.get('gmt_last_malicious_source') is not None:
            self.gmt_last_malicious_source = m.get('gmt_last_malicious_source')
        if m.get('province') is not None:
            self.province = m.get('province')
        if m.get('proxy_day_trace') is not None:
            self.proxy_day_trace = m.get('proxy_day_trace')
        if m.get('gmt_last_web_attack') is not None:
            self.gmt_last_web_attack = m.get('gmt_last_web_attack')
        if m.get('is_web_attack_7d') is not None:
            self.is_web_attack_7d = m.get('is_web_attack_7d')
        if m.get('mining_pool_day_trace') is not None:
            self.mining_pool_day_trace = m.get('mining_pool_day_trace')
        if m.get('is_c2') is not None:
            self.is_c2 = m.get('is_c2')
        if m.get('gmt_last_mining_pool') is not None:
            self.gmt_last_mining_pool = m.get('gmt_last_mining_pool')
        if m.get('is_malicious_source_1d') is not None:
            self.is_malicious_source_1d = m.get('is_malicious_source_1d')
        if m.get('is_mining_pool_1d') is not None:
            self.is_mining_pool_1d = m.get('is_mining_pool_1d')
        if m.get('is_tor_1d') is not None:
            self.is_tor_1d = m.get('is_tor_1d')
        if m.get('is_nat') is not None:
            self.is_nat = m.get('is_nat')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ip') is not None:
            self.ip = m.get('ip')
        if m.get('is_c2_7d') is not None:
            self.is_c27d = m.get('is_c2_7d')
        if m.get('is_malicious_login_1d') is not None:
            self.is_malicious_login_1d = m.get('is_malicious_login_1d')
        if m.get('tags') is not None:
            self.tags = m.get('tags')
        if m.get('malicious_source_day_trace') is not None:
            self.malicious_source_day_trace = m.get('malicious_source_day_trace')
        if m.get('is_mining_pool') is not None:
            self.is_mining_pool = m.get('is_mining_pool')
        if m.get('gmt_first_mining_pool') is not None:
            self.gmt_first_mining_pool = m.get('gmt_first_mining_pool')
        if m.get('is_idc') is not None:
            self.is_idc = m.get('is_idc')
        if m.get('is_malicious_login') is not None:
            self.is_malicious_login = m.get('is_malicious_login')
        if m.get('rdns') is not None:
            self.rdns = m.get('rdns')
        if m.get('city') is not None:
            self.city = m.get('city')
        if m.get('is_tor_7d') is not None:
            self.is_tor_7d = m.get('is_tor_7d')
        if m.get('gmt_last_nat') is not None:
            self.gmt_last_nat = m.get('gmt_last_nat')
        if m.get('gmt_last_malicious_login') is not None:
            self.gmt_last_malicious_login = m.get('gmt_last_malicious_login')
        if m.get('is_nat_7d') is not None:
            self.is_nat_7d = m.get('is_nat_7d')
        if m.get('is_proxy_1d') is not None:
            self.is_proxy_1d = m.get('is_proxy_1d')
        if m.get('geo') is not None:
            self.geo = m.get('geo')
        if m.get('gmt_first_c2') is not None:
            self.gmt_first_c2 = m.get('gmt_first_c2')
        if m.get('is_malicious_source_7d') is not None:
            self.is_malicious_source_7d = m.get('is_malicious_source_7d')
        if m.get('is_mining_pool_7d') is not None:
            self.is_mining_pool_7d = m.get('is_mining_pool_7d')
        if m.get('day_cnt_7d_tor') is not None:
            self.day_cnt_7d_tor = m.get('day_cnt_7d_tor')
        if m.get('is_web_attack_30d') is not None:
            self.is_web_attack_30d = m.get('is_web_attack_30d')
        if m.get('gmt_last_proxy') is not None:
            self.gmt_last_proxy = m.get('gmt_last_proxy')
        if m.get('nat_day_trace') is not None:
            self.nat_day_trace = m.get('nat_day_trace')
        if m.get('total_day_cnt_web_attack') is not None:
            self.total_day_cnt_web_attack = m.get('total_day_cnt_web_attack')
        if m.get('is_web_attack_1d') is not None:
            self.is_web_attack_1d = m.get('is_web_attack_1d')
        if m.get('malicious_login_day_trace') is not None:
            self.malicious_login_day_trace = m.get('malicious_login_day_trace')
        if m.get('day_cnt_30d_tor') is not None:
            self.day_cnt_30d_tor = m.get('day_cnt_30d_tor')
        if m.get('total_day_cnt_tor') is not None:
            self.total_day_cnt_tor = m.get('total_day_cnt_tor')
        if m.get('is_proxy') is not None:
            self.is_proxy = m.get('is_proxy')
        if m.get('c2_day_trace') is not None:
            self.c_2day_trace = m.get('c2_day_trace')
        if m.get('is_c2_1d') is not None:
            self.is_c21d = m.get('is_c2_1d')
        if m.get('is_malicious_source_30d') is not None:
            self.is_malicious_source_30d = m.get('is_malicious_source_30d')
        if m.get('day_cnt_7d_web_attack') is not None:
            self.day_cnt_7d_web_attack = m.get('day_cnt_7d_web_attack')
        if m.get('idc_name') is not None:
            self.idc_name = m.get('idc_name')
        if m.get('tor_day_trace') is not None:
            self.tor_day_trace = m.get('tor_day_trace')
        if m.get('is_tor') is not None:
            self.is_tor = m.get('is_tor')
        if m.get('is_malicious_login_7d') is not None:
            self.is_malicious_login_7d = m.get('is_malicious_login_7d')
        if m.get('gmt_last_tor') is not None:
            self.gmt_last_tor = m.get('gmt_last_tor')
        if m.get('is_malicious_source') is not None:
            self.is_malicious_source = m.get('is_malicious_source')
        if m.get('web_attack_day_trace') is not None:
            self.web_attack_day_trace = m.get('web_attack_day_trace')
        return self


class DescribeIpInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeIpInfoResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeIpInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeModuleConfigRequest(TeaModel):
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


class DescribeModuleConfigResponseBodyModuleConfigListItems(TeaModel):
    def __init__(
        self,
        uuid: str = None,
        group_id: int = None,
        instance_name: str = None,
        region: str = None,
        ip: str = None,
        instance_id: str = None,
    ):
        self.uuid = uuid
        self.group_id = group_id
        self.instance_name = instance_name
        self.region = region
        self.ip = ip
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.region is not None:
            result['Region'] = self.region
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DescribeModuleConfigResponseBodyModuleConfigList(TeaModel):
    def __init__(
        self,
        module_name: str = None,
        config_name: str = None,
        items: List[DescribeModuleConfigResponseBodyModuleConfigListItems] = None,
    ):
        self.module_name = module_name
        self.config_name = config_name
        self.items = items

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.module_name is not None:
            result['ModuleName'] = self.module_name
        if self.config_name is not None:
            result['ConfigName'] = self.config_name
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ModuleName') is not None:
            self.module_name = m.get('ModuleName')
        if m.get('ConfigName') is not None:
            self.config_name = m.get('ConfigName')
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = DescribeModuleConfigResponseBodyModuleConfigListItems()
                self.items.append(temp_model.from_map(k))
        return self


class DescribeModuleConfigResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        http_status_code: int = None,
        count: int = None,
        module_config_list: List[DescribeModuleConfigResponseBodyModuleConfigList] = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.http_status_code = http_status_code
        self.count = count
        self.module_config_list = module_config_list
        self.success = success

    def validate(self):
        if self.module_config_list:
            for k in self.module_config_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.count is not None:
            result['Count'] = self.count
        result['ModuleConfigList'] = []
        if self.module_config_list is not None:
            for k in self.module_config_list:
                result['ModuleConfigList'].append(k.to_map() if k else None)
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        self.module_config_list = []
        if m.get('ModuleConfigList') is not None:
            for k in m.get('ModuleConfigList'):
                temp_model = DescribeModuleConfigResponseBodyModuleConfigList()
                self.module_config_list.append(temp_model.from_map(k))
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeModuleConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeModuleConfigResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeModuleConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeNoticeConfigRequest(TeaModel):
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


class DescribeNoticeConfigResponseBodyNoticeConfigList(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        route: int = None,
        time_limit: int = None,
        ali_uid: int = None,
        project: str = None,
    ):
        self.current_page = current_page
        self.route = route
        self.time_limit = time_limit
        self.ali_uid = ali_uid
        self.project = project

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.route is not None:
            result['Route'] = self.route
        if self.time_limit is not None:
            result['TimeLimit'] = self.time_limit
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.project is not None:
            result['Project'] = self.project
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('Route') is not None:
            self.route = m.get('Route')
        if m.get('TimeLimit') is not None:
            self.time_limit = m.get('TimeLimit')
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('Project') is not None:
            self.project = m.get('Project')
        return self


class DescribeNoticeConfigResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        notice_config_list: List[DescribeNoticeConfigResponseBodyNoticeConfigList] = None,
    ):
        self.request_id = request_id
        self.notice_config_list = notice_config_list

    def validate(self):
        if self.notice_config_list:
            for k in self.notice_config_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['NoticeConfigList'] = []
        if self.notice_config_list is not None:
            for k in self.notice_config_list:
                result['NoticeConfigList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.notice_config_list = []
        if m.get('NoticeConfigList') is not None:
            for k in m.get('NoticeConfigList'):
                temp_model = DescribeNoticeConfigResponseBodyNoticeConfigList()
                self.notice_config_list.append(temp_model.from_map(k))
        return self


class DescribeNoticeConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeNoticeConfigResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeNoticeConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePropertyCountRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        type: str = None,
        uuid_list: str = None,
    ):
        self.source_ip = source_ip
        self.type = type
        self.uuid_list = uuid_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.type is not None:
            result['Type'] = self.type
        if self.uuid_list is not None:
            result['UuidList'] = self.uuid_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UuidList') is not None:
            self.uuid_list = m.get('UuidList')
        return self


class DescribePropertyCountResponseBody(TeaModel):
    def __init__(
        self,
        sca: int = None,
        user: int = None,
        request_id: str = None,
        port: int = None,
        process: int = None,
        software: int = None,
        auto_run: int = None,
        cron: int = None,
    ):
        self.sca = sca
        self.user = user
        self.request_id = request_id
        self.port = port
        self.process = process
        self.software = software
        self.auto_run = auto_run
        self.cron = cron

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.sca is not None:
            result['Sca'] = self.sca
        if self.user is not None:
            result['User'] = self.user
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.port is not None:
            result['Port'] = self.port
        if self.process is not None:
            result['Process'] = self.process
        if self.software is not None:
            result['Software'] = self.software
        if self.auto_run is not None:
            result['AutoRun'] = self.auto_run
        if self.cron is not None:
            result['Cron'] = self.cron
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Sca') is not None:
            self.sca = m.get('Sca')
        if m.get('User') is not None:
            self.user = m.get('User')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Process') is not None:
            self.process = m.get('Process')
        if m.get('Software') is not None:
            self.software = m.get('Software')
        if m.get('AutoRun') is not None:
            self.auto_run = m.get('AutoRun')
        if m.get('Cron') is not None:
            self.cron = m.get('Cron')
        return self


class DescribePropertyCountResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribePropertyCountResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribePropertyCountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePropertyCronDetailRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        remark: str = None,
        source: str = None,
        user: str = None,
        uuid: str = None,
        current_page: int = None,
        page_size: int = None,
    ):
        self.source_ip = source_ip
        self.remark = remark
        self.source = source
        self.user = user
        self.uuid = uuid
        self.current_page = current_page
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.source is not None:
            result['Source'] = self.source
        if self.user is not None:
            result['User'] = self.user
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('User') is not None:
            self.user = m.get('User')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribePropertyCronDetailResponseBodyPropertys(TeaModel):
    def __init__(
        self,
        create: str = None,
        internet_ip: str = None,
        user: str = None,
        ip: str = None,
        instance_id: str = None,
        source: str = None,
        cmd: str = None,
        intranet_ip: str = None,
        period: str = None,
        uuid: str = None,
        instance_name: str = None,
        md_5: str = None,
        create_timestamp: int = None,
    ):
        self.create = create
        self.internet_ip = internet_ip
        self.user = user
        self.ip = ip
        self.instance_id = instance_id
        self.source = source
        self.cmd = cmd
        self.intranet_ip = intranet_ip
        self.period = period
        self.uuid = uuid
        self.instance_name = instance_name
        self.md_5 = md_5
        self.create_timestamp = create_timestamp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.create is not None:
            result['Create'] = self.create
        if self.internet_ip is not None:
            result['InternetIp'] = self.internet_ip
        if self.user is not None:
            result['User'] = self.user
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.source is not None:
            result['Source'] = self.source
        if self.cmd is not None:
            result['Cmd'] = self.cmd
        if self.intranet_ip is not None:
            result['IntranetIp'] = self.intranet_ip
        if self.period is not None:
            result['Period'] = self.period
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.md_5 is not None:
            result['Md5'] = self.md_5
        if self.create_timestamp is not None:
            result['CreateTimestamp'] = self.create_timestamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Create') is not None:
            self.create = m.get('Create')
        if m.get('InternetIp') is not None:
            self.internet_ip = m.get('InternetIp')
        if m.get('User') is not None:
            self.user = m.get('User')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Cmd') is not None:
            self.cmd = m.get('Cmd')
        if m.get('IntranetIp') is not None:
            self.intranet_ip = m.get('IntranetIp')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('Md5') is not None:
            self.md_5 = m.get('Md5')
        if m.get('CreateTimestamp') is not None:
            self.create_timestamp = m.get('CreateTimestamp')
        return self


class DescribePropertyCronDetailResponseBodyPageInfo(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        page_size: int = None,
        total_count: int = None,
        count: int = None,
    ):
        self.current_page = current_page
        self.page_size = page_size
        self.total_count = total_count
        self.count = count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.count is not None:
            result['Count'] = self.count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        return self


class DescribePropertyCronDetailResponseBody(TeaModel):
    def __init__(
        self,
        propertys: List[DescribePropertyCronDetailResponseBodyPropertys] = None,
        page_info: DescribePropertyCronDetailResponseBodyPageInfo = None,
        request_id: str = None,
    ):
        self.propertys = propertys
        self.page_info = page_info
        self.request_id = request_id

    def validate(self):
        if self.propertys:
            for k in self.propertys:
                if k:
                    k.validate()
        if self.page_info:
            self.page_info.validate()

    def to_map(self):
        result = dict()
        result['Propertys'] = []
        if self.propertys is not None:
            for k in self.propertys:
                result['Propertys'].append(k.to_map() if k else None)
        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.propertys = []
        if m.get('Propertys') is not None:
            for k in m.get('Propertys'):
                temp_model = DescribePropertyCronDetailResponseBodyPropertys()
                self.propertys.append(temp_model.from_map(k))
        if m.get('PageInfo') is not None:
            temp_model = DescribePropertyCronDetailResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m['PageInfo'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribePropertyCronDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribePropertyCronDetailResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribePropertyCronDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePropertyPortDetailRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        remark: str = None,
        port: str = None,
        proc_name: str = None,
        uuid: str = None,
        current_page: int = None,
        page_size: int = None,
    ):
        self.source_ip = source_ip
        self.remark = remark
        self.port = port
        self.proc_name = proc_name
        self.uuid = uuid
        self.current_page = current_page
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.port is not None:
            result['Port'] = self.port
        if self.proc_name is not None:
            result['ProcName'] = self.proc_name
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('ProcName') is not None:
            self.proc_name = m.get('ProcName')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribePropertyPortDetailResponseBodyPropertys(TeaModel):
    def __init__(
        self,
        create: str = None,
        internet_ip: str = None,
        ip: str = None,
        bind_ip: str = None,
        instance_id: str = None,
        proc_name: str = None,
        port: str = None,
        intranet_ip: str = None,
        uuid: str = None,
        instance_name: str = None,
        create_timestamp: int = None,
        proto: str = None,
    ):
        self.create = create
        self.internet_ip = internet_ip
        self.ip = ip
        self.bind_ip = bind_ip
        self.instance_id = instance_id
        self.proc_name = proc_name
        self.port = port
        self.intranet_ip = intranet_ip
        self.uuid = uuid
        self.instance_name = instance_name
        self.create_timestamp = create_timestamp
        self.proto = proto

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.create is not None:
            result['Create'] = self.create
        if self.internet_ip is not None:
            result['InternetIp'] = self.internet_ip
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.bind_ip is not None:
            result['BindIp'] = self.bind_ip
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.proc_name is not None:
            result['ProcName'] = self.proc_name
        if self.port is not None:
            result['Port'] = self.port
        if self.intranet_ip is not None:
            result['IntranetIp'] = self.intranet_ip
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.create_timestamp is not None:
            result['CreateTimestamp'] = self.create_timestamp
        if self.proto is not None:
            result['Proto'] = self.proto
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Create') is not None:
            self.create = m.get('Create')
        if m.get('InternetIp') is not None:
            self.internet_ip = m.get('InternetIp')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('BindIp') is not None:
            self.bind_ip = m.get('BindIp')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ProcName') is not None:
            self.proc_name = m.get('ProcName')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('IntranetIp') is not None:
            self.intranet_ip = m.get('IntranetIp')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('CreateTimestamp') is not None:
            self.create_timestamp = m.get('CreateTimestamp')
        if m.get('Proto') is not None:
            self.proto = m.get('Proto')
        return self


class DescribePropertyPortDetailResponseBodyPageInfo(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        page_size: int = None,
        total_count: int = None,
        count: int = None,
    ):
        self.current_page = current_page
        self.page_size = page_size
        self.total_count = total_count
        self.count = count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.count is not None:
            result['Count'] = self.count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        return self


class DescribePropertyPortDetailResponseBody(TeaModel):
    def __init__(
        self,
        propertys: List[DescribePropertyPortDetailResponseBodyPropertys] = None,
        page_info: DescribePropertyPortDetailResponseBodyPageInfo = None,
        request_id: str = None,
    ):
        self.propertys = propertys
        self.page_info = page_info
        self.request_id = request_id

    def validate(self):
        if self.propertys:
            for k in self.propertys:
                if k:
                    k.validate()
        if self.page_info:
            self.page_info.validate()

    def to_map(self):
        result = dict()
        result['Propertys'] = []
        if self.propertys is not None:
            for k in self.propertys:
                result['Propertys'].append(k.to_map() if k else None)
        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.propertys = []
        if m.get('Propertys') is not None:
            for k in m.get('Propertys'):
                temp_model = DescribePropertyPortDetailResponseBodyPropertys()
                self.propertys.append(temp_model.from_map(k))
        if m.get('PageInfo') is not None:
            temp_model = DescribePropertyPortDetailResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m['PageInfo'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribePropertyPortDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribePropertyPortDetailResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribePropertyPortDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePropertyPortItemRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        force_flush: bool = None,
        port: str = None,
        current_page: int = None,
        page_size: int = None,
    ):
        self.source_ip = source_ip
        self.force_flush = force_flush
        self.port = port
        self.current_page = current_page
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.force_flush is not None:
            result['ForceFlush'] = self.force_flush
        if self.port is not None:
            result['Port'] = self.port
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ForceFlush') is not None:
            self.force_flush = m.get('ForceFlush')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribePropertyPortItemResponseBodyPageInfo(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        page_size: int = None,
        total_count: int = None,
        count: int = None,
    ):
        self.current_page = current_page
        self.page_size = page_size
        self.total_count = total_count
        self.count = count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.count is not None:
            result['Count'] = self.count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        return self


class DescribePropertyPortItemResponseBodyPropertyItems(TeaModel):
    def __init__(
        self,
        port: str = None,
        count: int = None,
        proto: str = None,
    ):
        self.port = port
        self.count = count
        self.proto = proto

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.port is not None:
            result['Port'] = self.port
        if self.count is not None:
            result['Count'] = self.count
        if self.proto is not None:
            result['Proto'] = self.proto
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('Proto') is not None:
            self.proto = m.get('Proto')
        return self


class DescribePropertyPortItemResponseBody(TeaModel):
    def __init__(
        self,
        page_info: DescribePropertyPortItemResponseBodyPageInfo = None,
        request_id: str = None,
        property_items: List[DescribePropertyPortItemResponseBodyPropertyItems] = None,
    ):
        self.page_info = page_info
        self.request_id = request_id
        self.property_items = property_items

    def validate(self):
        if self.page_info:
            self.page_info.validate()
        if self.property_items:
            for k in self.property_items:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['PropertyItems'] = []
        if self.property_items is not None:
            for k in self.property_items:
                result['PropertyItems'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageInfo') is not None:
            temp_model = DescribePropertyPortItemResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m['PageInfo'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.property_items = []
        if m.get('PropertyItems') is not None:
            for k in m.get('PropertyItems'):
                temp_model = DescribePropertyPortItemResponseBodyPropertyItems()
                self.property_items.append(temp_model.from_map(k))
        return self


class DescribePropertyPortItemResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribePropertyPortItemResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribePropertyPortItemResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePropertyProcDetailRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        remark: str = None,
        name: str = None,
        user: str = None,
        cmdline: str = None,
        uuid: str = None,
        current_page: int = None,
        page_size: int = None,
    ):
        self.source_ip = source_ip
        self.remark = remark
        self.name = name
        self.user = user
        self.cmdline = cmdline
        self.uuid = uuid
        self.current_page = current_page
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.name is not None:
            result['Name'] = self.name
        if self.user is not None:
            result['User'] = self.user
        if self.cmdline is not None:
            result['Cmdline'] = self.cmdline
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('User') is not None:
            self.user = m.get('User')
        if m.get('Cmdline') is not None:
            self.cmdline = m.get('Cmdline')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribePropertyProcDetailResponseBodyPropertys(TeaModel):
    def __init__(
        self,
        create: str = None,
        internet_ip: str = None,
        pid: str = None,
        user: str = None,
        instance_id: str = None,
        cmdline: str = None,
        intranet_ip: str = None,
        euid_name: str = None,
        start_time: str = None,
        uuid: str = None,
        pname: str = None,
        instance_name: str = None,
        path: str = None,
        md_5: str = None,
        name: str = None,
        create_timestamp: int = None,
    ):
        self.create = create
        self.internet_ip = internet_ip
        self.pid = pid
        self.user = user
        self.instance_id = instance_id
        self.cmdline = cmdline
        self.intranet_ip = intranet_ip
        self.euid_name = euid_name
        self.start_time = start_time
        self.uuid = uuid
        self.pname = pname
        self.instance_name = instance_name
        self.path = path
        self.md_5 = md_5
        self.name = name
        self.create_timestamp = create_timestamp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.create is not None:
            result['Create'] = self.create
        if self.internet_ip is not None:
            result['InternetIp'] = self.internet_ip
        if self.pid is not None:
            result['Pid'] = self.pid
        if self.user is not None:
            result['User'] = self.user
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.cmdline is not None:
            result['Cmdline'] = self.cmdline
        if self.intranet_ip is not None:
            result['IntranetIp'] = self.intranet_ip
        if self.euid_name is not None:
            result['EuidName'] = self.euid_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        if self.pname is not None:
            result['Pname'] = self.pname
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.path is not None:
            result['Path'] = self.path
        if self.md_5 is not None:
            result['Md5'] = self.md_5
        if self.name is not None:
            result['Name'] = self.name
        if self.create_timestamp is not None:
            result['CreateTimestamp'] = self.create_timestamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Create') is not None:
            self.create = m.get('Create')
        if m.get('InternetIp') is not None:
            self.internet_ip = m.get('InternetIp')
        if m.get('Pid') is not None:
            self.pid = m.get('Pid')
        if m.get('User') is not None:
            self.user = m.get('User')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Cmdline') is not None:
            self.cmdline = m.get('Cmdline')
        if m.get('IntranetIp') is not None:
            self.intranet_ip = m.get('IntranetIp')
        if m.get('EuidName') is not None:
            self.euid_name = m.get('EuidName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        if m.get('Pname') is not None:
            self.pname = m.get('Pname')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('Md5') is not None:
            self.md_5 = m.get('Md5')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('CreateTimestamp') is not None:
            self.create_timestamp = m.get('CreateTimestamp')
        return self


class DescribePropertyProcDetailResponseBodyPageInfo(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        page_size: int = None,
        total_count: int = None,
        count: int = None,
    ):
        self.current_page = current_page
        self.page_size = page_size
        self.total_count = total_count
        self.count = count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.count is not None:
            result['Count'] = self.count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        return self


class DescribePropertyProcDetailResponseBody(TeaModel):
    def __init__(
        self,
        propertys: List[DescribePropertyProcDetailResponseBodyPropertys] = None,
        page_info: DescribePropertyProcDetailResponseBodyPageInfo = None,
        request_id: str = None,
    ):
        self.propertys = propertys
        self.page_info = page_info
        self.request_id = request_id

    def validate(self):
        if self.propertys:
            for k in self.propertys:
                if k:
                    k.validate()
        if self.page_info:
            self.page_info.validate()

    def to_map(self):
        result = dict()
        result['Propertys'] = []
        if self.propertys is not None:
            for k in self.propertys:
                result['Propertys'].append(k.to_map() if k else None)
        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.propertys = []
        if m.get('Propertys') is not None:
            for k in m.get('Propertys'):
                temp_model = DescribePropertyProcDetailResponseBodyPropertys()
                self.propertys.append(temp_model.from_map(k))
        if m.get('PageInfo') is not None:
            temp_model = DescribePropertyProcDetailResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m['PageInfo'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribePropertyProcDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribePropertyProcDetailResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribePropertyProcDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePropertyProcItemRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        force_flush: bool = None,
        name: str = None,
        current_page: int = None,
        page_size: int = None,
    ):
        self.source_ip = source_ip
        self.force_flush = force_flush
        self.name = name
        self.current_page = current_page
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.force_flush is not None:
            result['ForceFlush'] = self.force_flush
        if self.name is not None:
            result['Name'] = self.name
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ForceFlush') is not None:
            self.force_flush = m.get('ForceFlush')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribePropertyProcItemResponseBodyPageInfo(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        page_size: int = None,
        total_count: int = None,
        count: int = None,
    ):
        self.current_page = current_page
        self.page_size = page_size
        self.total_count = total_count
        self.count = count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.count is not None:
            result['Count'] = self.count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        return self


class DescribePropertyProcItemResponseBodyPropertyItems(TeaModel):
    def __init__(
        self,
        name: str = None,
        count: int = None,
    ):
        self.name = name
        self.count = count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.count is not None:
            result['Count'] = self.count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        return self


class DescribePropertyProcItemResponseBody(TeaModel):
    def __init__(
        self,
        page_info: DescribePropertyProcItemResponseBodyPageInfo = None,
        request_id: str = None,
        property_items: List[DescribePropertyProcItemResponseBodyPropertyItems] = None,
    ):
        self.page_info = page_info
        self.request_id = request_id
        self.property_items = property_items

    def validate(self):
        if self.page_info:
            self.page_info.validate()
        if self.property_items:
            for k in self.property_items:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['PropertyItems'] = []
        if self.property_items is not None:
            for k in self.property_items:
                result['PropertyItems'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageInfo') is not None:
            temp_model = DescribePropertyProcItemResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m['PageInfo'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.property_items = []
        if m.get('PropertyItems') is not None:
            for k in m.get('PropertyItems'):
                temp_model = DescribePropertyProcItemResponseBodyPropertyItems()
                self.property_items.append(temp_model.from_map(k))
        return self


class DescribePropertyProcItemResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribePropertyProcItemResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribePropertyProcItemResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePropertyScaDetailRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        search_item: str = None,
        search_info: str = None,
        sca_name: str = None,
        biz_type: str = None,
        search_item_sub: str = None,
        search_info_sub: str = None,
        remark: str = None,
        name: int = None,
        uuid: str = None,
        current_page: int = None,
        page_size: int = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.search_item = search_item
        self.search_info = search_info
        self.sca_name = sca_name
        self.biz_type = biz_type
        self.search_item_sub = search_item_sub
        self.search_info_sub = search_info_sub
        self.remark = remark
        self.name = name
        self.uuid = uuid
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
        if self.search_item is not None:
            result['SearchItem'] = self.search_item
        if self.search_info is not None:
            result['SearchInfo'] = self.search_info
        if self.sca_name is not None:
            result['ScaName'] = self.sca_name
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.search_item_sub is not None:
            result['SearchItemSub'] = self.search_item_sub
        if self.search_info_sub is not None:
            result['SearchInfoSub'] = self.search_info_sub
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.name is not None:
            result['Name'] = self.name
        if self.uuid is not None:
            result['Uuid'] = self.uuid
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
        if m.get('SearchItem') is not None:
            self.search_item = m.get('SearchItem')
        if m.get('SearchInfo') is not None:
            self.search_info = m.get('SearchInfo')
        if m.get('ScaName') is not None:
            self.sca_name = m.get('ScaName')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('SearchItemSub') is not None:
            self.search_item_sub = m.get('SearchItemSub')
        if m.get('SearchInfoSub') is not None:
            self.search_info_sub = m.get('SearchInfoSub')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribePropertyScaDetailResponseBodyPropertys(TeaModel):
    def __init__(
        self,
        type: str = None,
        biz_type_dispaly: str = None,
        process_started: int = None,
        internet_ip: str = None,
        config_path: str = None,
        pid: str = None,
        port: str = None,
        cmdline: str = None,
        biz_type: str = None,
        listen_ip: str = None,
        version: str = None,
        instance_name: str = None,
        listen_status: str = None,
        name: str = None,
        create: str = None,
        process_user: str = None,
        ip: str = None,
        instance_id: str = None,
        web_path: str = None,
        ppid: str = None,
        intranet_ip: str = None,
        uuid: str = None,
        listen_protocol: str = None,
        image_name: str = None,
        path: str = None,
        container_name: str = None,
        proof: str = None,
        create_timestamp: int = None,
    ):
        self.type = type
        self.biz_type_dispaly = biz_type_dispaly
        self.process_started = process_started
        self.internet_ip = internet_ip
        self.config_path = config_path
        self.pid = pid
        self.port = port
        self.cmdline = cmdline
        self.biz_type = biz_type
        self.listen_ip = listen_ip
        self.version = version
        self.instance_name = instance_name
        self.listen_status = listen_status
        self.name = name
        self.create = create
        self.process_user = process_user
        self.ip = ip
        self.instance_id = instance_id
        self.web_path = web_path
        self.ppid = ppid
        self.intranet_ip = intranet_ip
        self.uuid = uuid
        self.listen_protocol = listen_protocol
        self.image_name = image_name
        self.path = path
        self.container_name = container_name
        self.proof = proof
        self.create_timestamp = create_timestamp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.biz_type_dispaly is not None:
            result['BizTypeDispaly'] = self.biz_type_dispaly
        if self.process_started is not None:
            result['ProcessStarted'] = self.process_started
        if self.internet_ip is not None:
            result['InternetIp'] = self.internet_ip
        if self.config_path is not None:
            result['ConfigPath'] = self.config_path
        if self.pid is not None:
            result['Pid'] = self.pid
        if self.port is not None:
            result['Port'] = self.port
        if self.cmdline is not None:
            result['Cmdline'] = self.cmdline
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.listen_ip is not None:
            result['ListenIp'] = self.listen_ip
        if self.version is not None:
            result['Version'] = self.version
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.listen_status is not None:
            result['ListenStatus'] = self.listen_status
        if self.name is not None:
            result['Name'] = self.name
        if self.create is not None:
            result['Create'] = self.create
        if self.process_user is not None:
            result['ProcessUser'] = self.process_user
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.web_path is not None:
            result['WebPath'] = self.web_path
        if self.ppid is not None:
            result['Ppid'] = self.ppid
        if self.intranet_ip is not None:
            result['IntranetIp'] = self.intranet_ip
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        if self.listen_protocol is not None:
            result['ListenProtocol'] = self.listen_protocol
        if self.image_name is not None:
            result['ImageName'] = self.image_name
        if self.path is not None:
            result['Path'] = self.path
        if self.container_name is not None:
            result['ContainerName'] = self.container_name
        if self.proof is not None:
            result['Proof'] = self.proof
        if self.create_timestamp is not None:
            result['CreateTimestamp'] = self.create_timestamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('BizTypeDispaly') is not None:
            self.biz_type_dispaly = m.get('BizTypeDispaly')
        if m.get('ProcessStarted') is not None:
            self.process_started = m.get('ProcessStarted')
        if m.get('InternetIp') is not None:
            self.internet_ip = m.get('InternetIp')
        if m.get('ConfigPath') is not None:
            self.config_path = m.get('ConfigPath')
        if m.get('Pid') is not None:
            self.pid = m.get('Pid')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Cmdline') is not None:
            self.cmdline = m.get('Cmdline')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('ListenIp') is not None:
            self.listen_ip = m.get('ListenIp')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('ListenStatus') is not None:
            self.listen_status = m.get('ListenStatus')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Create') is not None:
            self.create = m.get('Create')
        if m.get('ProcessUser') is not None:
            self.process_user = m.get('ProcessUser')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('WebPath') is not None:
            self.web_path = m.get('WebPath')
        if m.get('Ppid') is not None:
            self.ppid = m.get('Ppid')
        if m.get('IntranetIp') is not None:
            self.intranet_ip = m.get('IntranetIp')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        if m.get('ListenProtocol') is not None:
            self.listen_protocol = m.get('ListenProtocol')
        if m.get('ImageName') is not None:
            self.image_name = m.get('ImageName')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('ContainerName') is not None:
            self.container_name = m.get('ContainerName')
        if m.get('Proof') is not None:
            self.proof = m.get('Proof')
        if m.get('CreateTimestamp') is not None:
            self.create_timestamp = m.get('CreateTimestamp')
        return self


class DescribePropertyScaDetailResponseBodyPageInfo(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        page_size: int = None,
        total_count: int = None,
        count: int = None,
    ):
        self.current_page = current_page
        self.page_size = page_size
        self.total_count = total_count
        self.count = count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.count is not None:
            result['Count'] = self.count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        return self


class DescribePropertyScaDetailResponseBody(TeaModel):
    def __init__(
        self,
        propertys: List[DescribePropertyScaDetailResponseBodyPropertys] = None,
        page_info: DescribePropertyScaDetailResponseBodyPageInfo = None,
        request_id: str = None,
    ):
        self.propertys = propertys
        self.page_info = page_info
        self.request_id = request_id

    def validate(self):
        if self.propertys:
            for k in self.propertys:
                if k:
                    k.validate()
        if self.page_info:
            self.page_info.validate()

    def to_map(self):
        result = dict()
        result['Propertys'] = []
        if self.propertys is not None:
            for k in self.propertys:
                result['Propertys'].append(k.to_map() if k else None)
        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.propertys = []
        if m.get('Propertys') is not None:
            for k in m.get('Propertys'):
                temp_model = DescribePropertyScaDetailResponseBodyPropertys()
                self.propertys.append(temp_model.from_map(k))
        if m.get('PageInfo') is not None:
            temp_model = DescribePropertyScaDetailResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m['PageInfo'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribePropertyScaDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribePropertyScaDetailResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribePropertyScaDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePropertySoftwareDetailRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        remark: str = None,
        name: str = None,
        path: str = None,
        software_version: str = None,
        uuid: str = None,
        current_page: int = None,
        page_size: int = None,
    ):
        self.source_ip = source_ip
        self.remark = remark
        self.name = name
        self.path = path
        self.software_version = software_version
        self.uuid = uuid
        self.current_page = current_page
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.name is not None:
            result['Name'] = self.name
        if self.path is not None:
            result['Path'] = self.path
        if self.software_version is not None:
            result['SoftwareVersion'] = self.software_version
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('SoftwareVersion') is not None:
            self.software_version = m.get('SoftwareVersion')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribePropertySoftwareDetailResponseBodyPropertys(TeaModel):
    def __init__(
        self,
        create: int = None,
        internet_ip: str = None,
        ip: str = None,
        instance_id: str = None,
        intranet_ip: str = None,
        install_time: str = None,
        uuid: str = None,
        version: str = None,
        instance_name: str = None,
        path: str = None,
        name: str = None,
        create_timestamp: int = None,
    ):
        self.create = create
        self.internet_ip = internet_ip
        self.ip = ip
        self.instance_id = instance_id
        self.intranet_ip = intranet_ip
        self.install_time = install_time
        self.uuid = uuid
        self.version = version
        self.instance_name = instance_name
        self.path = path
        self.name = name
        self.create_timestamp = create_timestamp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.create is not None:
            result['Create'] = self.create
        if self.internet_ip is not None:
            result['InternetIp'] = self.internet_ip
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.intranet_ip is not None:
            result['IntranetIp'] = self.intranet_ip
        if self.install_time is not None:
            result['InstallTime'] = self.install_time
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        if self.version is not None:
            result['Version'] = self.version
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.path is not None:
            result['Path'] = self.path
        if self.name is not None:
            result['Name'] = self.name
        if self.create_timestamp is not None:
            result['CreateTimestamp'] = self.create_timestamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Create') is not None:
            self.create = m.get('Create')
        if m.get('InternetIp') is not None:
            self.internet_ip = m.get('InternetIp')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('IntranetIp') is not None:
            self.intranet_ip = m.get('IntranetIp')
        if m.get('InstallTime') is not None:
            self.install_time = m.get('InstallTime')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('CreateTimestamp') is not None:
            self.create_timestamp = m.get('CreateTimestamp')
        return self


class DescribePropertySoftwareDetailResponseBodyPageInfo(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        page_size: int = None,
        total_count: int = None,
        count: int = None,
    ):
        self.current_page = current_page
        self.page_size = page_size
        self.total_count = total_count
        self.count = count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.count is not None:
            result['Count'] = self.count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        return self


class DescribePropertySoftwareDetailResponseBody(TeaModel):
    def __init__(
        self,
        propertys: List[DescribePropertySoftwareDetailResponseBodyPropertys] = None,
        page_info: DescribePropertySoftwareDetailResponseBodyPageInfo = None,
        request_id: str = None,
    ):
        self.propertys = propertys
        self.page_info = page_info
        self.request_id = request_id

    def validate(self):
        if self.propertys:
            for k in self.propertys:
                if k:
                    k.validate()
        if self.page_info:
            self.page_info.validate()

    def to_map(self):
        result = dict()
        result['Propertys'] = []
        if self.propertys is not None:
            for k in self.propertys:
                result['Propertys'].append(k.to_map() if k else None)
        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.propertys = []
        if m.get('Propertys') is not None:
            for k in m.get('Propertys'):
                temp_model = DescribePropertySoftwareDetailResponseBodyPropertys()
                self.propertys.append(temp_model.from_map(k))
        if m.get('PageInfo') is not None:
            temp_model = DescribePropertySoftwareDetailResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m['PageInfo'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribePropertySoftwareDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribePropertySoftwareDetailResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribePropertySoftwareDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePropertySoftwareItemRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        force_flush: bool = None,
        name: str = None,
        current_page: int = None,
        page_size: int = None,
    ):
        self.source_ip = source_ip
        self.force_flush = force_flush
        self.name = name
        self.current_page = current_page
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.force_flush is not None:
            result['ForceFlush'] = self.force_flush
        if self.name is not None:
            result['Name'] = self.name
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ForceFlush') is not None:
            self.force_flush = m.get('ForceFlush')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribePropertySoftwareItemResponseBodyPageInfo(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        page_size: int = None,
        total_count: int = None,
        count: int = None,
    ):
        self.current_page = current_page
        self.page_size = page_size
        self.total_count = total_count
        self.count = count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.count is not None:
            result['Count'] = self.count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        return self


class DescribePropertySoftwareItemResponseBodyPropertyItems(TeaModel):
    def __init__(
        self,
        name: str = None,
        count: int = None,
    ):
        self.name = name
        self.count = count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.count is not None:
            result['Count'] = self.count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        return self


class DescribePropertySoftwareItemResponseBody(TeaModel):
    def __init__(
        self,
        page_info: DescribePropertySoftwareItemResponseBodyPageInfo = None,
        request_id: str = None,
        property_items: List[DescribePropertySoftwareItemResponseBodyPropertyItems] = None,
    ):
        self.page_info = page_info
        self.request_id = request_id
        self.property_items = property_items

    def validate(self):
        if self.page_info:
            self.page_info.validate()
        if self.property_items:
            for k in self.property_items:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['PropertyItems'] = []
        if self.property_items is not None:
            for k in self.property_items:
                result['PropertyItems'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageInfo') is not None:
            temp_model = DescribePropertySoftwareItemResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m['PageInfo'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.property_items = []
        if m.get('PropertyItems') is not None:
            for k in m.get('PropertyItems'):
                temp_model = DescribePropertySoftwareItemResponseBodyPropertyItems()
                self.property_items.append(temp_model.from_map(k))
        return self


class DescribePropertySoftwareItemResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribePropertySoftwareItemResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribePropertySoftwareItemResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePropertyUsageNewestRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        type: str = None,
    ):
        self.source_ip = source_ip
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribePropertyUsageNewestResponseBodyNewestStatisticItems(TeaModel):
    def __init__(
        self,
        create: int = None,
        name: str = None,
    ):
        self.create = create
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.create is not None:
            result['Create'] = self.create
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Create') is not None:
            self.create = m.get('Create')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class DescribePropertyUsageNewestResponseBody(TeaModel):
    def __init__(
        self,
        newest_statistic_items: List[DescribePropertyUsageNewestResponseBodyNewestStatisticItems] = None,
        type: str = None,
        request_id: str = None,
        item_count: int = None,
    ):
        self.newest_statistic_items = newest_statistic_items
        self.type = type
        self.request_id = request_id
        self.item_count = item_count

    def validate(self):
        if self.newest_statistic_items:
            for k in self.newest_statistic_items:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['NewestStatisticItems'] = []
        if self.newest_statistic_items is not None:
            for k in self.newest_statistic_items:
                result['NewestStatisticItems'].append(k.to_map() if k else None)
        if self.type is not None:
            result['Type'] = self.type
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.item_count is not None:
            result['ItemCount'] = self.item_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.newest_statistic_items = []
        if m.get('NewestStatisticItems') is not None:
            for k in m.get('NewestStatisticItems'):
                temp_model = DescribePropertyUsageNewestResponseBodyNewestStatisticItems()
                self.newest_statistic_items.append(temp_model.from_map(k))
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ItemCount') is not None:
            self.item_count = m.get('ItemCount')
        return self


class DescribePropertyUsageNewestResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribePropertyUsageNewestResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribePropertyUsageNewestResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePropertyUserDetailRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        remark: str = None,
        user: str = None,
        is_root: str = None,
        uuid: str = None,
        current_page: int = None,
        page_size: int = None,
    ):
        self.source_ip = source_ip
        self.remark = remark
        self.user = user
        self.is_root = is_root
        self.uuid = uuid
        self.current_page = current_page
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.user is not None:
            result['User'] = self.user
        if self.is_root is not None:
            result['IsRoot'] = self.is_root
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('User') is not None:
            self.user = m.get('User')
        if m.get('IsRoot') is not None:
            self.is_root = m.get('IsRoot')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribePropertyUserDetailResponseBodyPropertys(TeaModel):
    def __init__(
        self,
        status: str = None,
        last_login_ip: str = None,
        create: str = None,
        internet_ip: str = None,
        is_root: str = None,
        last_login_time: str = None,
        user: str = None,
        ip: str = None,
        instance_id: str = None,
        password_expiration_date: str = None,
        intranet_ip: str = None,
        group_names: List[str] = None,
        uuid: str = None,
        last_login_timestamp: int = None,
        instance_name: str = None,
        accounts_expiration_date: str = None,
        create_timestamp: int = None,
    ):
        self.status = status
        self.last_login_ip = last_login_ip
        self.create = create
        self.internet_ip = internet_ip
        self.is_root = is_root
        self.last_login_time = last_login_time
        self.user = user
        self.ip = ip
        self.instance_id = instance_id
        self.password_expiration_date = password_expiration_date
        self.intranet_ip = intranet_ip
        self.group_names = group_names
        self.uuid = uuid
        self.last_login_timestamp = last_login_timestamp
        self.instance_name = instance_name
        self.accounts_expiration_date = accounts_expiration_date
        self.create_timestamp = create_timestamp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.last_login_ip is not None:
            result['LastLoginIp'] = self.last_login_ip
        if self.create is not None:
            result['Create'] = self.create
        if self.internet_ip is not None:
            result['InternetIp'] = self.internet_ip
        if self.is_root is not None:
            result['IsRoot'] = self.is_root
        if self.last_login_time is not None:
            result['LastLoginTime'] = self.last_login_time
        if self.user is not None:
            result['User'] = self.user
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.password_expiration_date is not None:
            result['PasswordExpirationDate'] = self.password_expiration_date
        if self.intranet_ip is not None:
            result['IntranetIp'] = self.intranet_ip
        if self.group_names is not None:
            result['GroupNames'] = self.group_names
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        if self.last_login_timestamp is not None:
            result['LastLoginTimestamp'] = self.last_login_timestamp
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.accounts_expiration_date is not None:
            result['AccountsExpirationDate'] = self.accounts_expiration_date
        if self.create_timestamp is not None:
            result['CreateTimestamp'] = self.create_timestamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('LastLoginIp') is not None:
            self.last_login_ip = m.get('LastLoginIp')
        if m.get('Create') is not None:
            self.create = m.get('Create')
        if m.get('InternetIp') is not None:
            self.internet_ip = m.get('InternetIp')
        if m.get('IsRoot') is not None:
            self.is_root = m.get('IsRoot')
        if m.get('LastLoginTime') is not None:
            self.last_login_time = m.get('LastLoginTime')
        if m.get('User') is not None:
            self.user = m.get('User')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PasswordExpirationDate') is not None:
            self.password_expiration_date = m.get('PasswordExpirationDate')
        if m.get('IntranetIp') is not None:
            self.intranet_ip = m.get('IntranetIp')
        if m.get('GroupNames') is not None:
            self.group_names = m.get('GroupNames')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        if m.get('LastLoginTimestamp') is not None:
            self.last_login_timestamp = m.get('LastLoginTimestamp')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('AccountsExpirationDate') is not None:
            self.accounts_expiration_date = m.get('AccountsExpirationDate')
        if m.get('CreateTimestamp') is not None:
            self.create_timestamp = m.get('CreateTimestamp')
        return self


class DescribePropertyUserDetailResponseBodyPageInfo(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        page_size: int = None,
        total_count: int = None,
        count: int = None,
    ):
        self.current_page = current_page
        self.page_size = page_size
        self.total_count = total_count
        self.count = count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.count is not None:
            result['Count'] = self.count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        return self


class DescribePropertyUserDetailResponseBody(TeaModel):
    def __init__(
        self,
        propertys: List[DescribePropertyUserDetailResponseBodyPropertys] = None,
        page_info: DescribePropertyUserDetailResponseBodyPageInfo = None,
        request_id: str = None,
    ):
        self.propertys = propertys
        self.page_info = page_info
        self.request_id = request_id

    def validate(self):
        if self.propertys:
            for k in self.propertys:
                if k:
                    k.validate()
        if self.page_info:
            self.page_info.validate()

    def to_map(self):
        result = dict()
        result['Propertys'] = []
        if self.propertys is not None:
            for k in self.propertys:
                result['Propertys'].append(k.to_map() if k else None)
        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.propertys = []
        if m.get('Propertys') is not None:
            for k in m.get('Propertys'):
                temp_model = DescribePropertyUserDetailResponseBodyPropertys()
                self.propertys.append(temp_model.from_map(k))
        if m.get('PageInfo') is not None:
            temp_model = DescribePropertyUserDetailResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m['PageInfo'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribePropertyUserDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribePropertyUserDetailResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribePropertyUserDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePropertyUserItemRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        force_flush: bool = None,
        user: str = None,
        current_page: int = None,
        page_size: int = None,
    ):
        self.source_ip = source_ip
        self.force_flush = force_flush
        self.user = user
        self.current_page = current_page
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.force_flush is not None:
            result['ForceFlush'] = self.force_flush
        if self.user is not None:
            result['User'] = self.user
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ForceFlush') is not None:
            self.force_flush = m.get('ForceFlush')
        if m.get('User') is not None:
            self.user = m.get('User')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribePropertyUserItemResponseBodyPageInfo(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        page_size: int = None,
        total_count: int = None,
        count: int = None,
    ):
        self.current_page = current_page
        self.page_size = page_size
        self.total_count = total_count
        self.count = count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.count is not None:
            result['Count'] = self.count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        return self


class DescribePropertyUserItemResponseBodyPropertyItems(TeaModel):
    def __init__(
        self,
        user: str = None,
        count: int = None,
    ):
        self.user = user
        self.count = count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.user is not None:
            result['User'] = self.user
        if self.count is not None:
            result['Count'] = self.count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('User') is not None:
            self.user = m.get('User')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        return self


class DescribePropertyUserItemResponseBody(TeaModel):
    def __init__(
        self,
        page_info: DescribePropertyUserItemResponseBodyPageInfo = None,
        request_id: str = None,
        property_items: List[DescribePropertyUserItemResponseBodyPropertyItems] = None,
    ):
        self.page_info = page_info
        self.request_id = request_id
        self.property_items = property_items

    def validate(self):
        if self.page_info:
            self.page_info.validate()
        if self.property_items:
            for k in self.property_items:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['PropertyItems'] = []
        if self.property_items is not None:
            for k in self.property_items:
                result['PropertyItems'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageInfo') is not None:
            temp_model = DescribePropertyUserItemResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m['PageInfo'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.property_items = []
        if m.get('PropertyItems') is not None:
            for k in m.get('PropertyItems'):
                temp_model = DescribePropertyUserItemResponseBodyPropertyItems()
                self.property_items.append(temp_model.from_map(k))
        return self


class DescribePropertyUserItemResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribePropertyUserItemResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribePropertyUserItemResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRiskCheckItemResultRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        resource_owner_id: int = None,
        lang: str = None,
        item_id: int = None,
        current_page: int = None,
        page_size: int = None,
        instance_id: str = None,
    ):
        self.source_ip = source_ip
        self.resource_owner_id = resource_owner_id
        self.lang = lang
        self.item_id = item_id
        self.current_page = current_page
        self.page_size = page_size
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DescribeRiskCheckItemResultResponseBodyPageContentResource(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        content_resource: str = None,
        page_size: int = None,
        total_count: int = None,
        page_count: int = None,
        count: int = None,
    ):
        self.current_page = current_page
        self.content_resource = content_resource
        self.page_size = page_size
        self.total_count = total_count
        self.page_count = page_count
        self.count = count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.content_resource is not None:
            result['ContentResource'] = self.content_resource
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.page_count is not None:
            result['PageCount'] = self.page_count
        if self.count is not None:
            result['Count'] = self.count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('ContentResource') is not None:
            self.content_resource = m.get('ContentResource')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('PageCount') is not None:
            self.page_count = m.get('PageCount')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        return self


class DescribeRiskCheckItemResultResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        page_content_resource: DescribeRiskCheckItemResultResponseBodyPageContentResource = None,
    ):
        self.request_id = request_id
        self.page_content_resource = page_content_resource

    def validate(self):
        if self.page_content_resource:
            self.page_content_resource.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_content_resource is not None:
            result['PageContentResource'] = self.page_content_resource.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageContentResource') is not None:
            temp_model = DescribeRiskCheckItemResultResponseBodyPageContentResource()
            self.page_content_resource = temp_model.from_map(m['PageContentResource'])
        return self


class DescribeRiskCheckItemResultResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeRiskCheckItemResultResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeRiskCheckItemResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRiskCheckResultRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        resource_owner_id: int = None,
        lang: str = None,
        group_id: int = None,
        current_page: int = None,
        risk_level: str = None,
        status: str = None,
        asset_type: str = None,
        name: str = None,
        page_size: int = None,
        instance_id: str = None,
        query_flag: str = None,
        item_ids: List[str] = None,
    ):
        self.source_ip = source_ip
        self.resource_owner_id = resource_owner_id
        self.lang = lang
        self.group_id = group_id
        self.current_page = current_page
        self.risk_level = risk_level
        self.status = status
        self.asset_type = asset_type
        self.name = name
        self.page_size = page_size
        self.instance_id = instance_id
        self.query_flag = query_flag
        self.item_ids = item_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level
        if self.status is not None:
            result['Status'] = self.status
        if self.asset_type is not None:
            result['AssetType'] = self.asset_type
        if self.name is not None:
            result['Name'] = self.name
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.query_flag is not None:
            result['QueryFlag'] = self.query_flag
        if self.item_ids is not None:
            result['ItemIds'] = self.item_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('AssetType') is not None:
            self.asset_type = m.get('AssetType')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('QueryFlag') is not None:
            self.query_flag = m.get('QueryFlag')
        if m.get('ItemIds') is not None:
            self.item_ids = m.get('ItemIds')
        return self


class DescribeRiskCheckResultResponseBodyListRiskItemResources(TeaModel):
    def __init__(
        self,
        content_resource: str = None,
        resource_name: str = None,
    ):
        self.content_resource = content_resource
        self.resource_name = resource_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.content_resource is not None:
            result['ContentResource'] = self.content_resource
        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContentResource') is not None:
            self.content_resource = m.get('ContentResource')
        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')
        return self


class DescribeRiskCheckResultResponseBodyList(TeaModel):
    def __init__(
        self,
        type: str = None,
        status: str = None,
        risk_level: str = None,
        sort: int = None,
        repair_status: str = None,
        remaining_time: int = None,
        item_id: int = None,
        start_status: str = None,
        affected_count: int = None,
        risk_assert_type: str = None,
        risk_item_resources: List[DescribeRiskCheckResultResponseBodyListRiskItemResources] = None,
        title: str = None,
        task_id: int = None,
        check_time: int = None,
    ):
        self.type = type
        self.status = status
        self.risk_level = risk_level
        self.sort = sort
        self.repair_status = repair_status
        self.remaining_time = remaining_time
        self.item_id = item_id
        self.start_status = start_status
        self.affected_count = affected_count
        self.risk_assert_type = risk_assert_type
        self.risk_item_resources = risk_item_resources
        self.title = title
        self.task_id = task_id
        self.check_time = check_time

    def validate(self):
        if self.risk_item_resources:
            for k in self.risk_item_resources:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.status is not None:
            result['Status'] = self.status
        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level
        if self.sort is not None:
            result['Sort'] = self.sort
        if self.repair_status is not None:
            result['RepairStatus'] = self.repair_status
        if self.remaining_time is not None:
            result['RemainingTime'] = self.remaining_time
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        if self.start_status is not None:
            result['StartStatus'] = self.start_status
        if self.affected_count is not None:
            result['AffectedCount'] = self.affected_count
        if self.risk_assert_type is not None:
            result['RiskAssertType'] = self.risk_assert_type
        result['RiskItemResources'] = []
        if self.risk_item_resources is not None:
            for k in self.risk_item_resources:
                result['RiskItemResources'].append(k.to_map() if k else None)
        if self.title is not None:
            result['Title'] = self.title
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.check_time is not None:
            result['CheckTime'] = self.check_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')
        if m.get('Sort') is not None:
            self.sort = m.get('Sort')
        if m.get('RepairStatus') is not None:
            self.repair_status = m.get('RepairStatus')
        if m.get('RemainingTime') is not None:
            self.remaining_time = m.get('RemainingTime')
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        if m.get('StartStatus') is not None:
            self.start_status = m.get('StartStatus')
        if m.get('AffectedCount') is not None:
            self.affected_count = m.get('AffectedCount')
        if m.get('RiskAssertType') is not None:
            self.risk_assert_type = m.get('RiskAssertType')
        self.risk_item_resources = []
        if m.get('RiskItemResources') is not None:
            for k in m.get('RiskItemResources'):
                temp_model = DescribeRiskCheckResultResponseBodyListRiskItemResources()
                self.risk_item_resources.append(temp_model.from_map(k))
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('CheckTime') is not None:
            self.check_time = m.get('CheckTime')
        return self


class DescribeRiskCheckResultResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        request_id: str = None,
        page_size: int = None,
        page_count: int = None,
        current_page: int = None,
        list: List[DescribeRiskCheckResultResponseBodyList] = None,
        count: int = None,
    ):
        self.total_count = total_count
        self.request_id = request_id
        self.page_size = page_size
        self.page_count = page_count
        self.current_page = current_page
        self.list = list
        self.count = count

    def validate(self):
        if self.list:
            for k in self.list:
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
        if self.page_count is not None:
            result['PageCount'] = self.page_count
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        result['List'] = []
        if self.list is not None:
            for k in self.list:
                result['List'].append(k.to_map() if k else None)
        if self.count is not None:
            result['Count'] = self.count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageCount') is not None:
            self.page_count = m.get('PageCount')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = DescribeRiskCheckResultResponseBodyList()
                self.list.append(temp_model.from_map(k))
        if m.get('Count') is not None:
            self.count = m.get('Count')
        return self


class DescribeRiskCheckResultResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeRiskCheckResultResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeRiskCheckResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRiskCheckSummaryRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        resource_owner_id: int = None,
        lang: str = None,
        resource_directory_account_id: str = None,
    ):
        self.source_ip = source_ip
        self.resource_owner_id = resource_owner_id
        self.lang = lang
        self.resource_directory_account_id = resource_directory_account_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.resource_directory_account_id is not None:
            result['ResourceDirectoryAccountId'] = self.resource_directory_account_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('ResourceDirectoryAccountId') is not None:
            self.resource_directory_account_id = m.get('ResourceDirectoryAccountId')
        return self


class DescribeRiskCheckSummaryResponseBodyRiskCheckSummaryGroupsCountByStatus(TeaModel):
    def __init__(
        self,
        status: str = None,
        count: int = None,
    ):
        self.status = status
        self.count = count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.count is not None:
            result['Count'] = self.count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        return self


class DescribeRiskCheckSummaryResponseBodyRiskCheckSummaryGroups(TeaModel):
    def __init__(
        self,
        status: str = None,
        sort: int = None,
        remaining_time: int = None,
        count_by_status: List[DescribeRiskCheckSummaryResponseBodyRiskCheckSummaryGroupsCountByStatus] = None,
        title: str = None,
        id: int = None,
    ):
        self.status = status
        self.sort = sort
        self.remaining_time = remaining_time
        self.count_by_status = count_by_status
        self.title = title
        self.id = id

    def validate(self):
        if self.count_by_status:
            for k in self.count_by_status:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.sort is not None:
            result['Sort'] = self.sort
        if self.remaining_time is not None:
            result['RemainingTime'] = self.remaining_time
        result['CountByStatus'] = []
        if self.count_by_status is not None:
            for k in self.count_by_status:
                result['CountByStatus'].append(k.to_map() if k else None)
        if self.title is not None:
            result['Title'] = self.title
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Sort') is not None:
            self.sort = m.get('Sort')
        if m.get('RemainingTime') is not None:
            self.remaining_time = m.get('RemainingTime')
        self.count_by_status = []
        if m.get('CountByStatus') is not None:
            for k in m.get('CountByStatus'):
                temp_model = DescribeRiskCheckSummaryResponseBodyRiskCheckSummaryGroupsCountByStatus()
                self.count_by_status.append(temp_model.from_map(k))
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class DescribeRiskCheckSummaryResponseBodyRiskCheckSummaryRiskLevelCount(TeaModel):
    def __init__(
        self,
        key: str = None,
        count: int = None,
    ):
        self.key = key
        self.count = count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.count is not None:
            result['Count'] = self.count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        return self


class DescribeRiskCheckSummaryResponseBodyRiskCheckSummary(TeaModel):
    def __init__(
        self,
        item_count: int = None,
        groups: List[DescribeRiskCheckSummaryResponseBodyRiskCheckSummaryGroups] = None,
        affected_asset_count: int = None,
        disabled_risk_count: int = None,
        risk_level_count: List[DescribeRiskCheckSummaryResponseBodyRiskCheckSummaryRiskLevelCount] = None,
        risk_count: int = None,
        risk_rate: float = None,
        previous_count: int = None,
        previous_time: int = None,
        enabled_risk_count: int = None,
    ):
        self.item_count = item_count
        self.groups = groups
        self.affected_asset_count = affected_asset_count
        self.disabled_risk_count = disabled_risk_count
        self.risk_level_count = risk_level_count
        self.risk_count = risk_count
        self.risk_rate = risk_rate
        self.previous_count = previous_count
        self.previous_time = previous_time
        self.enabled_risk_count = enabled_risk_count

    def validate(self):
        if self.groups:
            for k in self.groups:
                if k:
                    k.validate()
        if self.risk_level_count:
            for k in self.risk_level_count:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.item_count is not None:
            result['ItemCount'] = self.item_count
        result['Groups'] = []
        if self.groups is not None:
            for k in self.groups:
                result['Groups'].append(k.to_map() if k else None)
        if self.affected_asset_count is not None:
            result['AffectedAssetCount'] = self.affected_asset_count
        if self.disabled_risk_count is not None:
            result['DisabledRiskCount'] = self.disabled_risk_count
        result['RiskLevelCount'] = []
        if self.risk_level_count is not None:
            for k in self.risk_level_count:
                result['RiskLevelCount'].append(k.to_map() if k else None)
        if self.risk_count is not None:
            result['RiskCount'] = self.risk_count
        if self.risk_rate is not None:
            result['RiskRate'] = self.risk_rate
        if self.previous_count is not None:
            result['PreviousCount'] = self.previous_count
        if self.previous_time is not None:
            result['PreviousTime'] = self.previous_time
        if self.enabled_risk_count is not None:
            result['EnabledRiskCount'] = self.enabled_risk_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ItemCount') is not None:
            self.item_count = m.get('ItemCount')
        self.groups = []
        if m.get('Groups') is not None:
            for k in m.get('Groups'):
                temp_model = DescribeRiskCheckSummaryResponseBodyRiskCheckSummaryGroups()
                self.groups.append(temp_model.from_map(k))
        if m.get('AffectedAssetCount') is not None:
            self.affected_asset_count = m.get('AffectedAssetCount')
        if m.get('DisabledRiskCount') is not None:
            self.disabled_risk_count = m.get('DisabledRiskCount')
        self.risk_level_count = []
        if m.get('RiskLevelCount') is not None:
            for k in m.get('RiskLevelCount'):
                temp_model = DescribeRiskCheckSummaryResponseBodyRiskCheckSummaryRiskLevelCount()
                self.risk_level_count.append(temp_model.from_map(k))
        if m.get('RiskCount') is not None:
            self.risk_count = m.get('RiskCount')
        if m.get('RiskRate') is not None:
            self.risk_rate = m.get('RiskRate')
        if m.get('PreviousCount') is not None:
            self.previous_count = m.get('PreviousCount')
        if m.get('PreviousTime') is not None:
            self.previous_time = m.get('PreviousTime')
        if m.get('EnabledRiskCount') is not None:
            self.enabled_risk_count = m.get('EnabledRiskCount')
        return self


class DescribeRiskCheckSummaryResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        risk_check_summary: DescribeRiskCheckSummaryResponseBodyRiskCheckSummary = None,
    ):
        self.request_id = request_id
        self.risk_check_summary = risk_check_summary

    def validate(self):
        if self.risk_check_summary:
            self.risk_check_summary.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.risk_check_summary is not None:
            result['RiskCheckSummary'] = self.risk_check_summary.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RiskCheckSummary') is not None:
            temp_model = DescribeRiskCheckSummaryResponseBodyRiskCheckSummary()
            self.risk_check_summary = temp_model.from_map(m['RiskCheckSummary'])
        return self


class DescribeRiskCheckSummaryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeRiskCheckSummaryResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeRiskCheckSummaryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRiskItemTypeRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        resource_owner_id: int = None,
        lang: str = None,
    ):
        self.source_ip = source_ip
        self.resource_owner_id = resource_owner_id
        self.lang = lang

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.lang is not None:
            result['Lang'] = self.lang
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        return self


class DescribeRiskItemTypeResponseBodyList(TeaModel):
    def __init__(
        self,
        title: str = None,
        id: int = None,
    ):
        self.title = title
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.title is not None:
            result['Title'] = self.title
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class DescribeRiskItemTypeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        list: List[DescribeRiskItemTypeResponseBodyList] = None,
    ):
        self.request_id = request_id
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
        result['List'] = []
        if self.list is not None:
            for k in self.list:
                result['List'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = DescribeRiskItemTypeResponseBodyList()
                self.list.append(temp_model.from_map(k))
        return self


class DescribeRiskItemTypeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeRiskItemTypeResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeRiskItemTypeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRiskListCheckResultRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        resource_owner_id: int = None,
        lang: str = None,
        current_page: int = None,
        page_size: int = None,
        instance_ids: List[str] = None,
    ):
        self.source_ip = source_ip
        self.resource_owner_id = resource_owner_id
        self.lang = lang
        self.current_page = current_page
        self.page_size = page_size
        self.instance_ids = instance_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        return self


class DescribeRiskListCheckResultResponseBodyList(TeaModel):
    def __init__(
        self,
        risk_count: int = None,
        instance_id: str = None,
    ):
        self.risk_count = risk_count
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.risk_count is not None:
            result['riskCount'] = self.risk_count
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('riskCount') is not None:
            self.risk_count = m.get('riskCount')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DescribeRiskListCheckResultResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        list: List[DescribeRiskListCheckResultResponseBodyList] = None,
    ):
        self.request_id = request_id
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
        result['List'] = []
        if self.list is not None:
            for k in self.list:
                result['List'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = DescribeRiskListCheckResultResponseBodyList()
                self.list.append(temp_model.from_map(k))
        return self


class DescribeRiskListCheckResultResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeRiskListCheckResultResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeRiskListCheckResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSasAssetStatisticsColumnRequest(TeaModel):
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


class DescribeSasAssetStatisticsColumnResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        statistics_column: str = None,
    ):
        self.request_id = request_id
        self.statistics_column = statistics_column

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.statistics_column is not None:
            result['StatisticsColumn'] = self.statistics_column
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StatisticsColumn') is not None:
            self.statistics_column = m.get('StatisticsColumn')
        return self


class DescribeSasAssetStatisticsColumnResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeSasAssetStatisticsColumnResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeSasAssetStatisticsColumnResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSearchConditionRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        type: str = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeSearchConditionResponseBodyConditionList(TeaModel):
    def __init__(
        self,
        condition_type: str = None,
        name_key: str = None,
        name: str = None,
        filter_conditions: str = None,
    ):
        self.condition_type = condition_type
        self.name_key = name_key
        self.name = name
        self.filter_conditions = filter_conditions

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.condition_type is not None:
            result['ConditionType'] = self.condition_type
        if self.name_key is not None:
            result['NameKey'] = self.name_key
        if self.name is not None:
            result['Name'] = self.name
        if self.filter_conditions is not None:
            result['FilterConditions'] = self.filter_conditions
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConditionType') is not None:
            self.condition_type = m.get('ConditionType')
        if m.get('NameKey') is not None:
            self.name_key = m.get('NameKey')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('FilterConditions') is not None:
            self.filter_conditions = m.get('FilterConditions')
        return self


class DescribeSearchConditionResponseBody(TeaModel):
    def __init__(
        self,
        condition_list: List[DescribeSearchConditionResponseBodyConditionList] = None,
        request_id: str = None,
    ):
        self.condition_list = condition_list
        self.request_id = request_id

    def validate(self):
        if self.condition_list:
            for k in self.condition_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['ConditionList'] = []
        if self.condition_list is not None:
            for k in self.condition_list:
                result['ConditionList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.condition_list = []
        if m.get('ConditionList') is not None:
            for k in m.get('ConditionList'):
                temp_model = DescribeSearchConditionResponseBodyConditionList()
                self.condition_list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeSearchConditionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeSearchConditionResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeSearchConditionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSecureSuggestionRequest(TeaModel):
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


class DescribeSecureSuggestionResponseBodySuggestionsDetail(TeaModel):
    def __init__(
        self,
        description: str = None,
        title: str = None,
        sub_type: str = None,
    ):
        self.description = description
        self.title = title
        self.sub_type = sub_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.title is not None:
            result['Title'] = self.title
        if self.sub_type is not None:
            result['SubType'] = self.sub_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('SubType') is not None:
            self.sub_type = m.get('SubType')
        return self


class DescribeSecureSuggestionResponseBodySuggestions(TeaModel):
    def __init__(
        self,
        suggest_type: str = None,
        points: int = None,
        detail: List[DescribeSecureSuggestionResponseBodySuggestionsDetail] = None,
    ):
        self.suggest_type = suggest_type
        self.points = points
        self.detail = detail

    def validate(self):
        if self.detail:
            for k in self.detail:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.suggest_type is not None:
            result['SuggestType'] = self.suggest_type
        if self.points is not None:
            result['Points'] = self.points
        result['Detail'] = []
        if self.detail is not None:
            for k in self.detail:
                result['Detail'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SuggestType') is not None:
            self.suggest_type = m.get('SuggestType')
        if m.get('Points') is not None:
            self.points = m.get('Points')
        self.detail = []
        if m.get('Detail') is not None:
            for k in m.get('Detail'):
                temp_model = DescribeSecureSuggestionResponseBodySuggestionsDetail()
                self.detail.append(temp_model.from_map(k))
        return self


class DescribeSecureSuggestionResponseBody(TeaModel):
    def __init__(
        self,
        suggestions: List[DescribeSecureSuggestionResponseBodySuggestions] = None,
        total_count: int = None,
        request_id: str = None,
    ):
        self.suggestions = suggestions
        self.total_count = total_count
        self.request_id = request_id

    def validate(self):
        if self.suggestions:
            for k in self.suggestions:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Suggestions'] = []
        if self.suggestions is not None:
            for k in self.suggestions:
                result['Suggestions'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.suggestions = []
        if m.get('Suggestions') is not None:
            for k in m.get('Suggestions'):
                temp_model = DescribeSecureSuggestionResponseBodySuggestions()
                self.suggestions.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeSecureSuggestionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeSecureSuggestionResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeSecureSuggestionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSecurityCheckScheduleConfigRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        resource_owner_id: int = None,
        lang: str = None,
    ):
        self.source_ip = source_ip
        self.resource_owner_id = resource_owner_id
        self.lang = lang

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.lang is not None:
            result['Lang'] = self.lang
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        return self


class DescribeSecurityCheckScheduleConfigResponseBodyRiskCheckJobConfig(TeaModel):
    def __init__(
        self,
        end_time: int = None,
        start_time: int = None,
        days_of_week: str = None,
    ):
        self.end_time = end_time
        self.start_time = start_time
        self.days_of_week = days_of_week

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.days_of_week is not None:
            result['DaysOfWeek'] = self.days_of_week
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('DaysOfWeek') is not None:
            self.days_of_week = m.get('DaysOfWeek')
        return self


class DescribeSecurityCheckScheduleConfigResponseBody(TeaModel):
    def __init__(
        self,
        risk_check_job_config: DescribeSecurityCheckScheduleConfigResponseBodyRiskCheckJobConfig = None,
        request_id: str = None,
    ):
        self.risk_check_job_config = risk_check_job_config
        self.request_id = request_id

    def validate(self):
        if self.risk_check_job_config:
            self.risk_check_job_config.validate()

    def to_map(self):
        result = dict()
        if self.risk_check_job_config is not None:
            result['RiskCheckJobConfig'] = self.risk_check_job_config.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RiskCheckJobConfig') is not None:
            temp_model = DescribeSecurityCheckScheduleConfigResponseBodyRiskCheckJobConfig()
            self.risk_check_job_config = temp_model.from_map(m['RiskCheckJobConfig'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeSecurityCheckScheduleConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeSecurityCheckScheduleConfigResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeSecurityCheckScheduleConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSecurityEventOperationsRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        resource_owner_id: int = None,
        security_event_id: int = None,
    ):
        self.source_ip = source_ip
        self.resource_owner_id = resource_owner_id
        self.security_event_id = security_event_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.security_event_id is not None:
            result['SecurityEventId'] = self.security_event_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SecurityEventId') is not None:
            self.security_event_id = m.get('SecurityEventId')
        return self


class DescribeSecurityEventOperationsResponseBodySecurityEventOperationsResponseMarkField(TeaModel):
    def __init__(
        self,
        mark_mis_type: str = None,
        mark_mis_value: str = None,
        supported_mis_type: List[str] = None,
        filed_name: str = None,
        filed_alias_name: str = None,
    ):
        self.mark_mis_type = mark_mis_type
        self.mark_mis_value = mark_mis_value
        self.supported_mis_type = supported_mis_type
        self.filed_name = filed_name
        self.filed_alias_name = filed_alias_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.mark_mis_type is not None:
            result['MarkMisType'] = self.mark_mis_type
        if self.mark_mis_value is not None:
            result['MarkMisValue'] = self.mark_mis_value
        if self.supported_mis_type is not None:
            result['SupportedMisType'] = self.supported_mis_type
        if self.filed_name is not None:
            result['FiledName'] = self.filed_name
        if self.filed_alias_name is not None:
            result['FiledAliasName'] = self.filed_alias_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MarkMisType') is not None:
            self.mark_mis_type = m.get('MarkMisType')
        if m.get('MarkMisValue') is not None:
            self.mark_mis_value = m.get('MarkMisValue')
        if m.get('SupportedMisType') is not None:
            self.supported_mis_type = m.get('SupportedMisType')
        if m.get('FiledName') is not None:
            self.filed_name = m.get('FiledName')
        if m.get('FiledAliasName') is not None:
            self.filed_alias_name = m.get('FiledAliasName')
        return self


class DescribeSecurityEventOperationsResponseBodySecurityEventOperationsResponseMarkFieldsSource(TeaModel):
    def __init__(
        self,
        mark_mis_value: str = None,
        supported_mis_type: List[str] = None,
        filed_name: str = None,
        filed_alias_name: str = None,
    ):
        self.mark_mis_value = mark_mis_value
        self.supported_mis_type = supported_mis_type
        self.filed_name = filed_name
        self.filed_alias_name = filed_alias_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.mark_mis_value is not None:
            result['MarkMisValue'] = self.mark_mis_value
        if self.supported_mis_type is not None:
            result['SupportedMisType'] = self.supported_mis_type
        if self.filed_name is not None:
            result['FiledName'] = self.filed_name
        if self.filed_alias_name is not None:
            result['FiledAliasName'] = self.filed_alias_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MarkMisValue') is not None:
            self.mark_mis_value = m.get('MarkMisValue')
        if m.get('SupportedMisType') is not None:
            self.supported_mis_type = m.get('SupportedMisType')
        if m.get('FiledName') is not None:
            self.filed_name = m.get('FiledName')
        if m.get('FiledAliasName') is not None:
            self.filed_alias_name = m.get('FiledAliasName')
        return self


class DescribeSecurityEventOperationsResponseBodySecurityEventOperationsResponse(TeaModel):
    def __init__(
        self,
        operation_params: str = None,
        operation_code: str = None,
        mark_field: List[DescribeSecurityEventOperationsResponseBodySecurityEventOperationsResponseMarkField] = None,
        user_can_operate: bool = None,
        mark_fields_source: List[DescribeSecurityEventOperationsResponseBodySecurityEventOperationsResponseMarkFieldsSource] = None,
    ):
        self.operation_params = operation_params
        self.operation_code = operation_code
        self.mark_field = mark_field
        self.user_can_operate = user_can_operate
        self.mark_fields_source = mark_fields_source

    def validate(self):
        if self.mark_field:
            for k in self.mark_field:
                if k:
                    k.validate()
        if self.mark_fields_source:
            for k in self.mark_fields_source:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.operation_params is not None:
            result['OperationParams'] = self.operation_params
        if self.operation_code is not None:
            result['OperationCode'] = self.operation_code
        result['MarkField'] = []
        if self.mark_field is not None:
            for k in self.mark_field:
                result['MarkField'].append(k.to_map() if k else None)
        if self.user_can_operate is not None:
            result['UserCanOperate'] = self.user_can_operate
        result['MarkFieldsSource'] = []
        if self.mark_fields_source is not None:
            for k in self.mark_fields_source:
                result['MarkFieldsSource'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OperationParams') is not None:
            self.operation_params = m.get('OperationParams')
        if m.get('OperationCode') is not None:
            self.operation_code = m.get('OperationCode')
        self.mark_field = []
        if m.get('MarkField') is not None:
            for k in m.get('MarkField'):
                temp_model = DescribeSecurityEventOperationsResponseBodySecurityEventOperationsResponseMarkField()
                self.mark_field.append(temp_model.from_map(k))
        if m.get('UserCanOperate') is not None:
            self.user_can_operate = m.get('UserCanOperate')
        self.mark_fields_source = []
        if m.get('MarkFieldsSource') is not None:
            for k in m.get('MarkFieldsSource'):
                temp_model = DescribeSecurityEventOperationsResponseBodySecurityEventOperationsResponseMarkFieldsSource()
                self.mark_fields_source.append(temp_model.from_map(k))
        return self


class DescribeSecurityEventOperationsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        security_event_operations_response: List[DescribeSecurityEventOperationsResponseBodySecurityEventOperationsResponse] = None,
    ):
        self.request_id = request_id
        self.security_event_operations_response = security_event_operations_response

    def validate(self):
        if self.security_event_operations_response:
            for k in self.security_event_operations_response:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['SecurityEventOperationsResponse'] = []
        if self.security_event_operations_response is not None:
            for k in self.security_event_operations_response:
                result['SecurityEventOperationsResponse'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.security_event_operations_response = []
        if m.get('SecurityEventOperationsResponse') is not None:
            for k in m.get('SecurityEventOperationsResponse'):
                temp_model = DescribeSecurityEventOperationsResponseBodySecurityEventOperationsResponse()
                self.security_event_operations_response.append(temp_model.from_map(k))
        return self


class DescribeSecurityEventOperationsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeSecurityEventOperationsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeSecurityEventOperationsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSecurityEventOperationStatusRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        resource_owner_id: int = None,
        task_id: int = None,
        security_event_ids: List[str] = None,
    ):
        self.source_ip = source_ip
        self.resource_owner_id = resource_owner_id
        self.task_id = task_id
        self.security_event_ids = security_event_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.security_event_ids is not None:
            result['SecurityEventIds'] = self.security_event_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('SecurityEventIds') is not None:
            self.security_event_ids = m.get('SecurityEventIds')
        return self


class DescribeSecurityEventOperationStatusResponseBodySecurityEventOperationStatusResponseSecurityEventOperationStatuses(TeaModel):
    def __init__(
        self,
        status: str = None,
        security_event_id: str = None,
        error_code: str = None,
    ):
        self.status = status
        self.security_event_id = security_event_id
        self.error_code = error_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.security_event_id is not None:
            result['SecurityEventId'] = self.security_event_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SecurityEventId') is not None:
            self.security_event_id = m.get('SecurityEventId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        return self


class DescribeSecurityEventOperationStatusResponseBodySecurityEventOperationStatusResponse(TeaModel):
    def __init__(
        self,
        task_status: str = None,
        security_event_operation_statuses: List[DescribeSecurityEventOperationStatusResponseBodySecurityEventOperationStatusResponseSecurityEventOperationStatuses] = None,
    ):
        self.task_status = task_status
        self.security_event_operation_statuses = security_event_operation_statuses

    def validate(self):
        if self.security_event_operation_statuses:
            for k in self.security_event_operation_statuses:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.task_status is not None:
            result['TaskStatus'] = self.task_status
        result['SecurityEventOperationStatuses'] = []
        if self.security_event_operation_statuses is not None:
            for k in self.security_event_operation_statuses:
                result['SecurityEventOperationStatuses'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')
        self.security_event_operation_statuses = []
        if m.get('SecurityEventOperationStatuses') is not None:
            for k in m.get('SecurityEventOperationStatuses'):
                temp_model = DescribeSecurityEventOperationStatusResponseBodySecurityEventOperationStatusResponseSecurityEventOperationStatuses()
                self.security_event_operation_statuses.append(temp_model.from_map(k))
        return self


class DescribeSecurityEventOperationStatusResponseBody(TeaModel):
    def __init__(
        self,
        security_event_operation_status_response: DescribeSecurityEventOperationStatusResponseBodySecurityEventOperationStatusResponse = None,
        request_id: str = None,
    ):
        self.security_event_operation_status_response = security_event_operation_status_response
        self.request_id = request_id

    def validate(self):
        if self.security_event_operation_status_response:
            self.security_event_operation_status_response.validate()

    def to_map(self):
        result = dict()
        if self.security_event_operation_status_response is not None:
            result['SecurityEventOperationStatusResponse'] = self.security_event_operation_status_response.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SecurityEventOperationStatusResponse') is not None:
            temp_model = DescribeSecurityEventOperationStatusResponseBodySecurityEventOperationStatusResponse()
            self.security_event_operation_status_response = temp_model.from_map(m['SecurityEventOperationStatusResponse'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeSecurityEventOperationStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeSecurityEventOperationStatusResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeSecurityEventOperationStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSecurityStatInfoRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        resource_directory_account_id: str = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.resource_directory_account_id = resource_directory_account_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.resource_directory_account_id is not None:
            result['ResourceDirectoryAccountId'] = self.resource_directory_account_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('ResourceDirectoryAccountId') is not None:
            self.resource_directory_account_id = m.get('ResourceDirectoryAccountId')
        return self


class DescribeSecurityStatInfoResponseBodySecurityEvent(TeaModel):
    def __init__(
        self,
        suspicious_count: int = None,
        remind_count: int = None,
        value_array: List[str] = None,
        time_array: List[str] = None,
        remind_list: List[str] = None,
        levels_on: List[str] = None,
        serious_count: int = None,
        total_count: int = None,
        date_array: List[str] = None,
        suspicious_list: List[str] = None,
        serious_list: List[str] = None,
    ):
        self.suspicious_count = suspicious_count
        self.remind_count = remind_count
        self.value_array = value_array
        self.time_array = time_array
        self.remind_list = remind_list
        self.levels_on = levels_on
        self.serious_count = serious_count
        self.total_count = total_count
        self.date_array = date_array
        self.suspicious_list = suspicious_list
        self.serious_list = serious_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.suspicious_count is not None:
            result['SuspiciousCount'] = self.suspicious_count
        if self.remind_count is not None:
            result['RemindCount'] = self.remind_count
        if self.value_array is not None:
            result['ValueArray'] = self.value_array
        if self.time_array is not None:
            result['TimeArray'] = self.time_array
        if self.remind_list is not None:
            result['RemindList'] = self.remind_list
        if self.levels_on is not None:
            result['LevelsOn'] = self.levels_on
        if self.serious_count is not None:
            result['SeriousCount'] = self.serious_count
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.date_array is not None:
            result['DateArray'] = self.date_array
        if self.suspicious_list is not None:
            result['SuspiciousList'] = self.suspicious_list
        if self.serious_list is not None:
            result['SeriousList'] = self.serious_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SuspiciousCount') is not None:
            self.suspicious_count = m.get('SuspiciousCount')
        if m.get('RemindCount') is not None:
            self.remind_count = m.get('RemindCount')
        if m.get('ValueArray') is not None:
            self.value_array = m.get('ValueArray')
        if m.get('TimeArray') is not None:
            self.time_array = m.get('TimeArray')
        if m.get('RemindList') is not None:
            self.remind_list = m.get('RemindList')
        if m.get('LevelsOn') is not None:
            self.levels_on = m.get('LevelsOn')
        if m.get('SeriousCount') is not None:
            self.serious_count = m.get('SeriousCount')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('DateArray') is not None:
            self.date_array = m.get('DateArray')
        if m.get('SuspiciousList') is not None:
            self.suspicious_list = m.get('SuspiciousList')
        if m.get('SeriousList') is not None:
            self.serious_list = m.get('SeriousList')
        return self


class DescribeSecurityStatInfoResponseBodyHealthCheck(TeaModel):
    def __init__(
        self,
        high_count: int = None,
        low_count: int = None,
        value_array: List[str] = None,
        time_array: List[str] = None,
        levels_on: List[str] = None,
        low_list: List[str] = None,
        medium_list: List[str] = None,
        total_count: int = None,
        medium_count: int = None,
        date_array: List[str] = None,
        high_list: List[str] = None,
    ):
        self.high_count = high_count
        self.low_count = low_count
        self.value_array = value_array
        self.time_array = time_array
        self.levels_on = levels_on
        self.low_list = low_list
        self.medium_list = medium_list
        self.total_count = total_count
        self.medium_count = medium_count
        self.date_array = date_array
        self.high_list = high_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.high_count is not None:
            result['HighCount'] = self.high_count
        if self.low_count is not None:
            result['LowCount'] = self.low_count
        if self.value_array is not None:
            result['ValueArray'] = self.value_array
        if self.time_array is not None:
            result['TimeArray'] = self.time_array
        if self.levels_on is not None:
            result['LevelsOn'] = self.levels_on
        if self.low_list is not None:
            result['LowList'] = self.low_list
        if self.medium_list is not None:
            result['MediumList'] = self.medium_list
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.medium_count is not None:
            result['MediumCount'] = self.medium_count
        if self.date_array is not None:
            result['DateArray'] = self.date_array
        if self.high_list is not None:
            result['HighList'] = self.high_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HighCount') is not None:
            self.high_count = m.get('HighCount')
        if m.get('LowCount') is not None:
            self.low_count = m.get('LowCount')
        if m.get('ValueArray') is not None:
            self.value_array = m.get('ValueArray')
        if m.get('TimeArray') is not None:
            self.time_array = m.get('TimeArray')
        if m.get('LevelsOn') is not None:
            self.levels_on = m.get('LevelsOn')
        if m.get('LowList') is not None:
            self.low_list = m.get('LowList')
        if m.get('MediumList') is not None:
            self.medium_list = m.get('MediumList')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('MediumCount') is not None:
            self.medium_count = m.get('MediumCount')
        if m.get('DateArray') is not None:
            self.date_array = m.get('DateArray')
        if m.get('HighList') is not None:
            self.high_list = m.get('HighList')
        return self


class DescribeSecurityStatInfoResponseBodyVulnerability(TeaModel):
    def __init__(
        self,
        nntf_count: int = None,
        nntf_list: List[str] = None,
        asap_list: List[str] = None,
        value_array: List[str] = None,
        time_array: List[str] = None,
        levels_on: List[str] = None,
        later_list: List[str] = None,
        later_count: int = None,
        total_count: int = None,
        date_array: List[str] = None,
        asap_count: int = None,
    ):
        self.nntf_count = nntf_count
        self.nntf_list = nntf_list
        self.asap_list = asap_list
        self.value_array = value_array
        self.time_array = time_array
        self.levels_on = levels_on
        self.later_list = later_list
        self.later_count = later_count
        self.total_count = total_count
        self.date_array = date_array
        self.asap_count = asap_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.nntf_count is not None:
            result['NntfCount'] = self.nntf_count
        if self.nntf_list is not None:
            result['NntfList'] = self.nntf_list
        if self.asap_list is not None:
            result['AsapList'] = self.asap_list
        if self.value_array is not None:
            result['ValueArray'] = self.value_array
        if self.time_array is not None:
            result['TimeArray'] = self.time_array
        if self.levels_on is not None:
            result['LevelsOn'] = self.levels_on
        if self.later_list is not None:
            result['LaterList'] = self.later_list
        if self.later_count is not None:
            result['LaterCount'] = self.later_count
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.date_array is not None:
            result['DateArray'] = self.date_array
        if self.asap_count is not None:
            result['AsapCount'] = self.asap_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NntfCount') is not None:
            self.nntf_count = m.get('NntfCount')
        if m.get('NntfList') is not None:
            self.nntf_list = m.get('NntfList')
        if m.get('AsapList') is not None:
            self.asap_list = m.get('AsapList')
        if m.get('ValueArray') is not None:
            self.value_array = m.get('ValueArray')
        if m.get('TimeArray') is not None:
            self.time_array = m.get('TimeArray')
        if m.get('LevelsOn') is not None:
            self.levels_on = m.get('LevelsOn')
        if m.get('LaterList') is not None:
            self.later_list = m.get('LaterList')
        if m.get('LaterCount') is not None:
            self.later_count = m.get('LaterCount')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('DateArray') is not None:
            self.date_array = m.get('DateArray')
        if m.get('AsapCount') is not None:
            self.asap_count = m.get('AsapCount')
        return self


class DescribeSecurityStatInfoResponseBodyAttackEvent(TeaModel):
    def __init__(
        self,
        value_array: List[str] = None,
        total_count: int = None,
        date_array: List[str] = None,
    ):
        self.value_array = value_array
        self.total_count = total_count
        self.date_array = date_array

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.value_array is not None:
            result['ValueArray'] = self.value_array
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.date_array is not None:
            result['DateArray'] = self.date_array
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ValueArray') is not None:
            self.value_array = m.get('ValueArray')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('DateArray') is not None:
            self.date_array = m.get('DateArray')
        return self


class DescribeSecurityStatInfoResponseBody(TeaModel):
    def __init__(
        self,
        security_event: DescribeSecurityStatInfoResponseBodySecurityEvent = None,
        request_id: str = None,
        health_check: DescribeSecurityStatInfoResponseBodyHealthCheck = None,
        vulnerability: DescribeSecurityStatInfoResponseBodyVulnerability = None,
        attack_event: DescribeSecurityStatInfoResponseBodyAttackEvent = None,
        success: bool = None,
    ):
        self.security_event = security_event
        self.request_id = request_id
        self.health_check = health_check
        self.vulnerability = vulnerability
        self.attack_event = attack_event
        self.success = success

    def validate(self):
        if self.security_event:
            self.security_event.validate()
        if self.health_check:
            self.health_check.validate()
        if self.vulnerability:
            self.vulnerability.validate()
        if self.attack_event:
            self.attack_event.validate()

    def to_map(self):
        result = dict()
        if self.security_event is not None:
            result['SecurityEvent'] = self.security_event.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.health_check is not None:
            result['HealthCheck'] = self.health_check.to_map()
        if self.vulnerability is not None:
            result['Vulnerability'] = self.vulnerability.to_map()
        if self.attack_event is not None:
            result['AttackEvent'] = self.attack_event.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SecurityEvent') is not None:
            temp_model = DescribeSecurityStatInfoResponseBodySecurityEvent()
            self.security_event = temp_model.from_map(m['SecurityEvent'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('HealthCheck') is not None:
            temp_model = DescribeSecurityStatInfoResponseBodyHealthCheck()
            self.health_check = temp_model.from_map(m['HealthCheck'])
        if m.get('Vulnerability') is not None:
            temp_model = DescribeSecurityStatInfoResponseBodyVulnerability()
            self.vulnerability = temp_model.from_map(m['Vulnerability'])
        if m.get('AttackEvent') is not None:
            temp_model = DescribeSecurityStatInfoResponseBodyAttackEvent()
            self.attack_event = temp_model.from_map(m['AttackEvent'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeSecurityStatInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeSecurityStatInfoResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeSecurityStatInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSimilarEventScenariosRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        resource_owner_id: int = None,
        security_event_id: int = None,
    ):
        self.source_ip = source_ip
        self.resource_owner_id = resource_owner_id
        self.security_event_id = security_event_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.security_event_id is not None:
            result['SecurityEventId'] = self.security_event_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SecurityEventId') is not None:
            self.security_event_id = m.get('SecurityEventId')
        return self


class DescribeSimilarEventScenariosResponseBodyScenarios(TeaModel):
    def __init__(
        self,
        code: str = None,
    ):
        self.code = code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class DescribeSimilarEventScenariosResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        scenarios: List[DescribeSimilarEventScenariosResponseBodyScenarios] = None,
    ):
        self.request_id = request_id
        self.scenarios = scenarios

    def validate(self):
        if self.scenarios:
            for k in self.scenarios:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Scenarios'] = []
        if self.scenarios is not None:
            for k in self.scenarios:
                result['Scenarios'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.scenarios = []
        if m.get('Scenarios') is not None:
            for k in m.get('Scenarios'):
                temp_model = DescribeSimilarEventScenariosResponseBodyScenarios()
                self.scenarios.append(temp_model.from_map(k))
        return self


class DescribeSimilarEventScenariosResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeSimilarEventScenariosResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeSimilarEventScenariosResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSimilarSecurityEventsRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        resource_owner_id: int = None,
        lang: str = None,
        task_id: int = None,
        current_page: int = None,
        page_size: int = None,
    ):
        self.source_ip = source_ip
        self.resource_owner_id = resource_owner_id
        self.lang = lang
        self.task_id = task_id
        self.current_page = current_page
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeSimilarSecurityEventsResponseBodyPageInfo(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        page_size: int = None,
        total_count: int = None,
        count: int = None,
    ):
        self.current_page = current_page
        self.page_size = page_size
        self.total_count = total_count
        self.count = count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.count is not None:
            result['Count'] = self.count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        return self


class DescribeSimilarSecurityEventsResponseBodySecurityEventsResponse(TeaModel):
    def __init__(
        self,
        last_time: int = None,
        uuid: str = None,
        event_name: str = None,
        event_type: str = None,
        security_event_id: int = None,
        occurrence_time: int = None,
    ):
        self.last_time = last_time
        self.uuid = uuid
        self.event_name = event_name
        self.event_type = event_type
        self.security_event_id = security_event_id
        self.occurrence_time = occurrence_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.last_time is not None:
            result['LastTime'] = self.last_time
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        if self.event_name is not None:
            result['EventName'] = self.event_name
        if self.event_type is not None:
            result['EventType'] = self.event_type
        if self.security_event_id is not None:
            result['SecurityEventId'] = self.security_event_id
        if self.occurrence_time is not None:
            result['OccurrenceTime'] = self.occurrence_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LastTime') is not None:
            self.last_time = m.get('LastTime')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        if m.get('EventName') is not None:
            self.event_name = m.get('EventName')
        if m.get('EventType') is not None:
            self.event_type = m.get('EventType')
        if m.get('SecurityEventId') is not None:
            self.security_event_id = m.get('SecurityEventId')
        if m.get('OccurrenceTime') is not None:
            self.occurrence_time = m.get('OccurrenceTime')
        return self


class DescribeSimilarSecurityEventsResponseBody(TeaModel):
    def __init__(
        self,
        page_info: DescribeSimilarSecurityEventsResponseBodyPageInfo = None,
        request_id: str = None,
        security_events_response: List[DescribeSimilarSecurityEventsResponseBodySecurityEventsResponse] = None,
    ):
        self.page_info = page_info
        self.request_id = request_id
        self.security_events_response = security_events_response

    def validate(self):
        if self.page_info:
            self.page_info.validate()
        if self.security_events_response:
            for k in self.security_events_response:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['SecurityEventsResponse'] = []
        if self.security_events_response is not None:
            for k in self.security_events_response:
                result['SecurityEventsResponse'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageInfo') is not None:
            temp_model = DescribeSimilarSecurityEventsResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m['PageInfo'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.security_events_response = []
        if m.get('SecurityEventsResponse') is not None:
            for k in m.get('SecurityEventsResponse'):
                temp_model = DescribeSimilarSecurityEventsResponseBodySecurityEventsResponse()
                self.security_events_response.append(temp_model.from_map(k))
        return self


class DescribeSimilarSecurityEventsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeSimilarSecurityEventsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeSimilarSecurityEventsResponseBody()
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
        instance_name: str = None,
        ip: str = None,
        intranet_ip: str = None,
        reason: str = None,
    ):
        self.instance_name = instance_name
        self.ip = ip
        self.intranet_ip = intranet_ip
        self.reason = reason

    def validate(self):
        pass

    def to_map(self):
        result = dict()
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


class DescribeSummaryInfoRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        resource_directory_account_id: str = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.resource_directory_account_id = resource_directory_account_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.resource_directory_account_id is not None:
            result['ResourceDirectoryAccountId'] = self.resource_directory_account_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('ResourceDirectoryAccountId') is not None:
            self.resource_directory_account_id = m.get('ResourceDirectoryAccountId')
        return self


class DescribeSummaryInfoResponseBody(TeaModel):
    def __init__(
        self,
        aegis_client_online_count: int = None,
        request_id: str = None,
        aegis_client_offline_count: int = None,
        security_score: int = None,
        success: bool = None,
    ):
        self.aegis_client_online_count = aegis_client_online_count
        self.request_id = request_id
        self.aegis_client_offline_count = aegis_client_offline_count
        self.security_score = security_score
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.aegis_client_online_count is not None:
            result['AegisClientOnlineCount'] = self.aegis_client_online_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.aegis_client_offline_count is not None:
            result['AegisClientOfflineCount'] = self.aegis_client_offline_count
        if self.security_score is not None:
            result['SecurityScore'] = self.security_score
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AegisClientOnlineCount') is not None:
            self.aegis_client_online_count = m.get('AegisClientOnlineCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('AegisClientOfflineCount') is not None:
            self.aegis_client_offline_count = m.get('AegisClientOfflineCount')
        if m.get('SecurityScore') is not None:
            self.security_score = m.get('SecurityScore')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeSummaryInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeSummaryInfoResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeSummaryInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSuspEventDetailRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        suspicious_event_id: int = None,
        from_: str = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.suspicious_event_id = suspicious_event_id
        self.from_ = from_

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.suspicious_event_id is not None:
            result['SuspiciousEventId'] = self.suspicious_event_id
        if self.from_ is not None:
            result['From'] = self.from_
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('SuspiciousEventId') is not None:
            self.suspicious_event_id = m.get('SuspiciousEventId')
        if m.get('From') is not None:
            self.from_ = m.get('From')
        return self


class DescribeSuspEventDetailResponseBodyDetails(TeaModel):
    def __init__(
        self,
        type: str = None,
        value: str = None,
        name: str = None,
        info_type: str = None,
    ):
        self.type = type
        self.value = value
        self.name = name
        self.info_type = info_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.value is not None:
            result['Value'] = self.value
        if self.name is not None:
            result['Name'] = self.name
        if self.info_type is not None:
            result['InfoType'] = self.info_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('InfoType') is not None:
            self.info_type = m.get('InfoType')
        return self


class DescribeSuspEventDetailResponseBody(TeaModel):
    def __init__(
        self,
        event_desc: str = None,
        request_id: str = None,
        event_type_desc: str = None,
        operate_error_code: str = None,
        event_status: str = None,
        event_name: str = None,
        sale_version: str = None,
        intranet_ip: str = None,
        data_source: str = None,
        instance_name: str = None,
        operate_msg: str = None,
        can_be_deal_on_line: bool = None,
        uuid: str = None,
        details: List[DescribeSuspEventDetailResponseBodyDetails] = None,
        internet_ip: str = None,
        level: str = None,
        id: int = None,
        last_time: str = None,
        sas_id: str = None,
    ):
        self.event_desc = event_desc
        self.request_id = request_id
        self.event_type_desc = event_type_desc
        self.operate_error_code = operate_error_code
        self.event_status = event_status
        self.event_name = event_name
        self.sale_version = sale_version
        self.intranet_ip = intranet_ip
        self.data_source = data_source
        self.instance_name = instance_name
        self.operate_msg = operate_msg
        self.can_be_deal_on_line = can_be_deal_on_line
        self.uuid = uuid
        self.details = details
        self.internet_ip = internet_ip
        self.level = level
        self.id = id
        self.last_time = last_time
        self.sas_id = sas_id

    def validate(self):
        if self.details:
            for k in self.details:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.event_desc is not None:
            result['EventDesc'] = self.event_desc
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.event_type_desc is not None:
            result['EventTypeDesc'] = self.event_type_desc
        if self.operate_error_code is not None:
            result['OperateErrorCode'] = self.operate_error_code
        if self.event_status is not None:
            result['EventStatus'] = self.event_status
        if self.event_name is not None:
            result['EventName'] = self.event_name
        if self.sale_version is not None:
            result['SaleVersion'] = self.sale_version
        if self.intranet_ip is not None:
            result['IntranetIp'] = self.intranet_ip
        if self.data_source is not None:
            result['DataSource'] = self.data_source
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.operate_msg is not None:
            result['OperateMsg'] = self.operate_msg
        if self.can_be_deal_on_line is not None:
            result['CanBeDealOnLine'] = self.can_be_deal_on_line
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        result['Details'] = []
        if self.details is not None:
            for k in self.details:
                result['Details'].append(k.to_map() if k else None)
        if self.internet_ip is not None:
            result['InternetIp'] = self.internet_ip
        if self.level is not None:
            result['Level'] = self.level
        if self.id is not None:
            result['Id'] = self.id
        if self.last_time is not None:
            result['LastTime'] = self.last_time
        if self.sas_id is not None:
            result['SasId'] = self.sas_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventDesc') is not None:
            self.event_desc = m.get('EventDesc')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('EventTypeDesc') is not None:
            self.event_type_desc = m.get('EventTypeDesc')
        if m.get('OperateErrorCode') is not None:
            self.operate_error_code = m.get('OperateErrorCode')
        if m.get('EventStatus') is not None:
            self.event_status = m.get('EventStatus')
        if m.get('EventName') is not None:
            self.event_name = m.get('EventName')
        if m.get('SaleVersion') is not None:
            self.sale_version = m.get('SaleVersion')
        if m.get('IntranetIp') is not None:
            self.intranet_ip = m.get('IntranetIp')
        if m.get('DataSource') is not None:
            self.data_source = m.get('DataSource')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('OperateMsg') is not None:
            self.operate_msg = m.get('OperateMsg')
        if m.get('CanBeDealOnLine') is not None:
            self.can_be_deal_on_line = m.get('CanBeDealOnLine')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        self.details = []
        if m.get('Details') is not None:
            for k in m.get('Details'):
                temp_model = DescribeSuspEventDetailResponseBodyDetails()
                self.details.append(temp_model.from_map(k))
        if m.get('InternetIp') is not None:
            self.internet_ip = m.get('InternetIp')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('LastTime') is not None:
            self.last_time = m.get('LastTime')
        if m.get('SasId') is not None:
            self.sas_id = m.get('SasId')
        return self


class DescribeSuspEventDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeSuspEventDetailResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeSuspEventDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSuspEventQuaraFilesRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        page_size: str = None,
        status: str = None,
        quara_tag: str = None,
        current_page: str = None,
        from_: str = None,
    ):
        self.source_ip = source_ip
        self.page_size = page_size
        self.status = status
        self.quara_tag = quara_tag
        self.current_page = current_page
        self.from_ = from_

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.status is not None:
            result['Status'] = self.status
        if self.quara_tag is not None:
            result['QuaraTag'] = self.quara_tag
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.from_ is not None:
            result['From'] = self.from_
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('QuaraTag') is not None:
            self.quara_tag = m.get('QuaraTag')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('From') is not None:
            self.from_ = m.get('From')
        return self


class DescribeSuspEventQuaraFilesResponseBodyQuaraFiles(TeaModel):
    def __init__(
        self,
        status: str = None,
        event_name: str = None,
        internet_ip: str = None,
        ip: str = None,
        tag: str = None,
        uuid: str = None,
        event_type: str = None,
        instance_name: str = None,
        path: str = None,
        md_5: str = None,
        id: int = None,
        modify_time: str = None,
    ):
        self.status = status
        self.event_name = event_name
        self.internet_ip = internet_ip
        self.ip = ip
        self.tag = tag
        self.uuid = uuid
        self.event_type = event_type
        self.instance_name = instance_name
        self.path = path
        self.md_5 = md_5
        self.id = id
        self.modify_time = modify_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.event_name is not None:
            result['EventName'] = self.event_name
        if self.internet_ip is not None:
            result['InternetIp'] = self.internet_ip
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.tag is not None:
            result['Tag'] = self.tag
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        if self.event_type is not None:
            result['EventType'] = self.event_type
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.path is not None:
            result['Path'] = self.path
        if self.md_5 is not None:
            result['Md5'] = self.md_5
        if self.id is not None:
            result['Id'] = self.id
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('EventName') is not None:
            self.event_name = m.get('EventName')
        if m.get('InternetIp') is not None:
            self.internet_ip = m.get('InternetIp')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        if m.get('EventType') is not None:
            self.event_type = m.get('EventType')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('Md5') is not None:
            self.md_5 = m.get('Md5')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        return self


class DescribeSuspEventQuaraFilesResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        page_size: int = None,
        request_id: str = None,
        current_page: int = None,
        quara_files: List[DescribeSuspEventQuaraFilesResponseBodyQuaraFiles] = None,
        count: int = None,
    ):
        self.total_count = total_count
        self.page_size = page_size
        self.request_id = request_id
        self.current_page = current_page
        self.quara_files = quara_files
        self.count = count

    def validate(self):
        if self.quara_files:
            for k in self.quara_files:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        result['QuaraFiles'] = []
        if self.quara_files is not None:
            for k in self.quara_files:
                result['QuaraFiles'].append(k.to_map() if k else None)
        if self.count is not None:
            result['Count'] = self.count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        self.quara_files = []
        if m.get('QuaraFiles') is not None:
            for k in m.get('QuaraFiles'):
                temp_model = DescribeSuspEventQuaraFilesResponseBodyQuaraFiles()
                self.quara_files.append(temp_model.from_map(k))
        if m.get('Count') is not None:
            self.count = m.get('Count')
        return self


class DescribeSuspEventQuaraFilesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeSuspEventQuaraFilesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeSuspEventQuaraFilesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSuspEventsRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        dealed: str = None,
        name: str = None,
        levels: str = None,
        parent_event_types: str = None,
        remark: str = None,
        status: str = None,
        page_size: str = None,
        current_page: str = None,
        lang: str = None,
        alarm_unique_info: str = None,
        unique_info: str = None,
        from_: str = None,
        source: str = None,
        group_id: int = None,
        uuids: str = None,
        cluster_id: str = None,
        container_field_name: str = None,
        container_field_value: str = None,
        target_type: str = None,
        operate_error_code_list: List[str] = None,
    ):
        self.source_ip = source_ip
        self.dealed = dealed
        self.name = name
        self.levels = levels
        self.parent_event_types = parent_event_types
        self.remark = remark
        self.status = status
        self.page_size = page_size
        self.current_page = current_page
        self.lang = lang
        self.alarm_unique_info = alarm_unique_info
        self.unique_info = unique_info
        self.from_ = from_
        self.source = source
        self.group_id = group_id
        self.uuids = uuids
        self.cluster_id = cluster_id
        self.container_field_name = container_field_name
        self.container_field_value = container_field_value
        self.target_type = target_type
        self.operate_error_code_list = operate_error_code_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.dealed is not None:
            result['Dealed'] = self.dealed
        if self.name is not None:
            result['Name'] = self.name
        if self.levels is not None:
            result['Levels'] = self.levels
        if self.parent_event_types is not None:
            result['ParentEventTypes'] = self.parent_event_types
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.status is not None:
            result['Status'] = self.status
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.alarm_unique_info is not None:
            result['AlarmUniqueInfo'] = self.alarm_unique_info
        if self.unique_info is not None:
            result['UniqueInfo'] = self.unique_info
        if self.from_ is not None:
            result['From'] = self.from_
        if self.source is not None:
            result['Source'] = self.source
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.uuids is not None:
            result['Uuids'] = self.uuids
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.container_field_name is not None:
            result['ContainerFieldName'] = self.container_field_name
        if self.container_field_value is not None:
            result['ContainerFieldValue'] = self.container_field_value
        if self.target_type is not None:
            result['TargetType'] = self.target_type
        if self.operate_error_code_list is not None:
            result['OperateErrorCodeList'] = self.operate_error_code_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Dealed') is not None:
            self.dealed = m.get('Dealed')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Levels') is not None:
            self.levels = m.get('Levels')
        if m.get('ParentEventTypes') is not None:
            self.parent_event_types = m.get('ParentEventTypes')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('AlarmUniqueInfo') is not None:
            self.alarm_unique_info = m.get('AlarmUniqueInfo')
        if m.get('UniqueInfo') is not None:
            self.unique_info = m.get('UniqueInfo')
        if m.get('From') is not None:
            self.from_ = m.get('From')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('Uuids') is not None:
            self.uuids = m.get('Uuids')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ContainerFieldName') is not None:
            self.container_field_name = m.get('ContainerFieldName')
        if m.get('ContainerFieldValue') is not None:
            self.container_field_value = m.get('ContainerFieldValue')
        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')
        if m.get('OperateErrorCodeList') is not None:
            self.operate_error_code_list = m.get('OperateErrorCodeList')
        return self


class DescribeSuspEventsResponseBodySuspEventsDetails(TeaModel):
    def __init__(
        self,
        type: str = None,
        value: str = None,
        name: str = None,
        name_display: str = None,
        info_type: str = None,
        value_display: str = None,
    ):
        self.type = type
        self.value = value
        self.name = name
        self.name_display = name_display
        self.info_type = info_type
        self.value_display = value_display

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.value is not None:
            result['Value'] = self.value
        if self.name is not None:
            result['Name'] = self.name
        if self.name_display is not None:
            result['NameDisplay'] = self.name_display
        if self.info_type is not None:
            result['InfoType'] = self.info_type
        if self.value_display is not None:
            result['ValueDisplay'] = self.value_display
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NameDisplay') is not None:
            self.name_display = m.get('NameDisplay')
        if m.get('InfoType') is not None:
            self.info_type = m.get('InfoType')
        if m.get('ValueDisplay') is not None:
            self.value_display = m.get('ValueDisplay')
        return self


class DescribeSuspEventsResponseBodySuspEvents(TeaModel):
    def __init__(
        self,
        stages: str = None,
        internet_ip: str = None,
        k_8s_cluster_name: str = None,
        container_image_id: str = None,
        last_time_stamp: int = None,
        occurrence_time: str = None,
        alarm_unique_info: str = None,
        desc: str = None,
        details: List[DescribeSuspEventsResponseBodySuspEventsDetails] = None,
        can_cancel_fault: bool = None,
        alarm_event_name_display: str = None,
        app_name: str = None,
        security_event_ids: str = None,
        can_be_deal_on_line: bool = None,
        mark_mis_rules: str = None,
        container_image_name: str = None,
        k_8s_cluster_id: str = None,
        contain_hw_mode: bool = None,
        instance_name: str = None,
        k_8s_node_id: str = None,
        event_status: int = None,
        sale_version: str = None,
        operate_error_code: str = None,
        name: str = None,
        has_trace_info: bool = None,
        data_source: str = None,
        operate_time: int = None,
        event_sub_type: str = None,
        advanced: bool = None,
        occurrence_time_stamp: int = None,
        alarm_event_type_display: str = None,
        intranet_ip: str = None,
        last_time: str = None,
        operate_msg: str = None,
        uuid: str = None,
        k_8s_pod_name: str = None,
        container_id: str = None,
        alarm_event_type: str = None,
        k_8s_namespace: str = None,
        auto_breaking: bool = None,
        k_8s_node_name: str = None,
        alarm_event_name: str = None,
        unique_info: str = None,
        level: str = None,
        id: int = None,
    ):
        self.stages = stages
        self.internet_ip = internet_ip
        self.k_8s_cluster_name = k_8s_cluster_name
        self.container_image_id = container_image_id
        self.last_time_stamp = last_time_stamp
        self.occurrence_time = occurrence_time
        self.alarm_unique_info = alarm_unique_info
        self.desc = desc
        self.details = details
        self.can_cancel_fault = can_cancel_fault
        self.alarm_event_name_display = alarm_event_name_display
        self.app_name = app_name
        self.security_event_ids = security_event_ids
        self.can_be_deal_on_line = can_be_deal_on_line
        self.mark_mis_rules = mark_mis_rules
        self.container_image_name = container_image_name
        self.k_8s_cluster_id = k_8s_cluster_id
        self.contain_hw_mode = contain_hw_mode
        self.instance_name = instance_name
        self.k_8s_node_id = k_8s_node_id
        self.event_status = event_status
        self.sale_version = sale_version
        self.operate_error_code = operate_error_code
        self.name = name
        self.has_trace_info = has_trace_info
        self.data_source = data_source
        self.operate_time = operate_time
        self.event_sub_type = event_sub_type
        self.advanced = advanced
        self.occurrence_time_stamp = occurrence_time_stamp
        self.alarm_event_type_display = alarm_event_type_display
        self.intranet_ip = intranet_ip
        self.last_time = last_time
        self.operate_msg = operate_msg
        self.uuid = uuid
        self.k_8s_pod_name = k_8s_pod_name
        self.container_id = container_id
        self.alarm_event_type = alarm_event_type
        self.k_8s_namespace = k_8s_namespace
        self.auto_breaking = auto_breaking
        self.k_8s_node_name = k_8s_node_name
        self.alarm_event_name = alarm_event_name
        self.unique_info = unique_info
        self.level = level
        self.id = id

    def validate(self):
        if self.details:
            for k in self.details:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.stages is not None:
            result['Stages'] = self.stages
        if self.internet_ip is not None:
            result['InternetIp'] = self.internet_ip
        if self.k_8s_cluster_name is not None:
            result['K8sClusterName'] = self.k_8s_cluster_name
        if self.container_image_id is not None:
            result['ContainerImageId'] = self.container_image_id
        if self.last_time_stamp is not None:
            result['LastTimeStamp'] = self.last_time_stamp
        if self.occurrence_time is not None:
            result['OccurrenceTime'] = self.occurrence_time
        if self.alarm_unique_info is not None:
            result['AlarmUniqueInfo'] = self.alarm_unique_info
        if self.desc is not None:
            result['Desc'] = self.desc
        result['Details'] = []
        if self.details is not None:
            for k in self.details:
                result['Details'].append(k.to_map() if k else None)
        if self.can_cancel_fault is not None:
            result['CanCancelFault'] = self.can_cancel_fault
        if self.alarm_event_name_display is not None:
            result['AlarmEventNameDisplay'] = self.alarm_event_name_display
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.security_event_ids is not None:
            result['SecurityEventIds'] = self.security_event_ids
        if self.can_be_deal_on_line is not None:
            result['CanBeDealOnLine'] = self.can_be_deal_on_line
        if self.mark_mis_rules is not None:
            result['MarkMisRules'] = self.mark_mis_rules
        if self.container_image_name is not None:
            result['ContainerImageName'] = self.container_image_name
        if self.k_8s_cluster_id is not None:
            result['K8sClusterId'] = self.k_8s_cluster_id
        if self.contain_hw_mode is not None:
            result['ContainHwMode'] = self.contain_hw_mode
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.k_8s_node_id is not None:
            result['K8sNodeId'] = self.k_8s_node_id
        if self.event_status is not None:
            result['EventStatus'] = self.event_status
        if self.sale_version is not None:
            result['SaleVersion'] = self.sale_version
        if self.operate_error_code is not None:
            result['OperateErrorCode'] = self.operate_error_code
        if self.name is not None:
            result['Name'] = self.name
        if self.has_trace_info is not None:
            result['HasTraceInfo'] = self.has_trace_info
        if self.data_source is not None:
            result['DataSource'] = self.data_source
        if self.operate_time is not None:
            result['OperateTime'] = self.operate_time
        if self.event_sub_type is not None:
            result['EventSubType'] = self.event_sub_type
        if self.advanced is not None:
            result['Advanced'] = self.advanced
        if self.occurrence_time_stamp is not None:
            result['OccurrenceTimeStamp'] = self.occurrence_time_stamp
        if self.alarm_event_type_display is not None:
            result['AlarmEventTypeDisplay'] = self.alarm_event_type_display
        if self.intranet_ip is not None:
            result['IntranetIp'] = self.intranet_ip
        if self.last_time is not None:
            result['LastTime'] = self.last_time
        if self.operate_msg is not None:
            result['OperateMsg'] = self.operate_msg
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        if self.k_8s_pod_name is not None:
            result['K8sPodName'] = self.k_8s_pod_name
        if self.container_id is not None:
            result['ContainerId'] = self.container_id
        if self.alarm_event_type is not None:
            result['AlarmEventType'] = self.alarm_event_type
        if self.k_8s_namespace is not None:
            result['K8sNamespace'] = self.k_8s_namespace
        if self.auto_breaking is not None:
            result['AutoBreaking'] = self.auto_breaking
        if self.k_8s_node_name is not None:
            result['K8sNodeName'] = self.k_8s_node_name
        if self.alarm_event_name is not None:
            result['AlarmEventName'] = self.alarm_event_name
        if self.unique_info is not None:
            result['UniqueInfo'] = self.unique_info
        if self.level is not None:
            result['Level'] = self.level
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Stages') is not None:
            self.stages = m.get('Stages')
        if m.get('InternetIp') is not None:
            self.internet_ip = m.get('InternetIp')
        if m.get('K8sClusterName') is not None:
            self.k_8s_cluster_name = m.get('K8sClusterName')
        if m.get('ContainerImageId') is not None:
            self.container_image_id = m.get('ContainerImageId')
        if m.get('LastTimeStamp') is not None:
            self.last_time_stamp = m.get('LastTimeStamp')
        if m.get('OccurrenceTime') is not None:
            self.occurrence_time = m.get('OccurrenceTime')
        if m.get('AlarmUniqueInfo') is not None:
            self.alarm_unique_info = m.get('AlarmUniqueInfo')
        if m.get('Desc') is not None:
            self.desc = m.get('Desc')
        self.details = []
        if m.get('Details') is not None:
            for k in m.get('Details'):
                temp_model = DescribeSuspEventsResponseBodySuspEventsDetails()
                self.details.append(temp_model.from_map(k))
        if m.get('CanCancelFault') is not None:
            self.can_cancel_fault = m.get('CanCancelFault')
        if m.get('AlarmEventNameDisplay') is not None:
            self.alarm_event_name_display = m.get('AlarmEventNameDisplay')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('SecurityEventIds') is not None:
            self.security_event_ids = m.get('SecurityEventIds')
        if m.get('CanBeDealOnLine') is not None:
            self.can_be_deal_on_line = m.get('CanBeDealOnLine')
        if m.get('MarkMisRules') is not None:
            self.mark_mis_rules = m.get('MarkMisRules')
        if m.get('ContainerImageName') is not None:
            self.container_image_name = m.get('ContainerImageName')
        if m.get('K8sClusterId') is not None:
            self.k_8s_cluster_id = m.get('K8sClusterId')
        if m.get('ContainHwMode') is not None:
            self.contain_hw_mode = m.get('ContainHwMode')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('K8sNodeId') is not None:
            self.k_8s_node_id = m.get('K8sNodeId')
        if m.get('EventStatus') is not None:
            self.event_status = m.get('EventStatus')
        if m.get('SaleVersion') is not None:
            self.sale_version = m.get('SaleVersion')
        if m.get('OperateErrorCode') is not None:
            self.operate_error_code = m.get('OperateErrorCode')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('HasTraceInfo') is not None:
            self.has_trace_info = m.get('HasTraceInfo')
        if m.get('DataSource') is not None:
            self.data_source = m.get('DataSource')
        if m.get('OperateTime') is not None:
            self.operate_time = m.get('OperateTime')
        if m.get('EventSubType') is not None:
            self.event_sub_type = m.get('EventSubType')
        if m.get('Advanced') is not None:
            self.advanced = m.get('Advanced')
        if m.get('OccurrenceTimeStamp') is not None:
            self.occurrence_time_stamp = m.get('OccurrenceTimeStamp')
        if m.get('AlarmEventTypeDisplay') is not None:
            self.alarm_event_type_display = m.get('AlarmEventTypeDisplay')
        if m.get('IntranetIp') is not None:
            self.intranet_ip = m.get('IntranetIp')
        if m.get('LastTime') is not None:
            self.last_time = m.get('LastTime')
        if m.get('OperateMsg') is not None:
            self.operate_msg = m.get('OperateMsg')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        if m.get('K8sPodName') is not None:
            self.k_8s_pod_name = m.get('K8sPodName')
        if m.get('ContainerId') is not None:
            self.container_id = m.get('ContainerId')
        if m.get('AlarmEventType') is not None:
            self.alarm_event_type = m.get('AlarmEventType')
        if m.get('K8sNamespace') is not None:
            self.k_8s_namespace = m.get('K8sNamespace')
        if m.get('AutoBreaking') is not None:
            self.auto_breaking = m.get('AutoBreaking')
        if m.get('K8sNodeName') is not None:
            self.k_8s_node_name = m.get('K8sNodeName')
        if m.get('AlarmEventName') is not None:
            self.alarm_event_name = m.get('AlarmEventName')
        if m.get('UniqueInfo') is not None:
            self.unique_info = m.get('UniqueInfo')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class DescribeSuspEventsResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        page_size: int = None,
        request_id: str = None,
        current_page: int = None,
        count: int = None,
        susp_events: List[DescribeSuspEventsResponseBodySuspEvents] = None,
    ):
        self.total_count = total_count
        self.page_size = page_size
        self.request_id = request_id
        self.current_page = current_page
        self.count = count
        self.susp_events = susp_events

    def validate(self):
        if self.susp_events:
            for k in self.susp_events:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.count is not None:
            result['Count'] = self.count
        result['SuspEvents'] = []
        if self.susp_events is not None:
            for k in self.susp_events:
                result['SuspEvents'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        self.susp_events = []
        if m.get('SuspEvents') is not None:
            for k in m.get('SuspEvents'):
                temp_model = DescribeSuspEventsResponseBodySuspEvents()
                self.susp_events.append(temp_model.from_map(k))
        return self


class DescribeSuspEventsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeSuspEventsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeSuspEventsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeUserBaselineAuthorizationRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        resource_owner_id: int = None,
        lang: str = None,
    ):
        self.source_ip = source_ip
        self.resource_owner_id = resource_owner_id
        self.lang = lang

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.lang is not None:
            result['Lang'] = self.lang
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        return self


class DescribeUserBaselineAuthorizationResponseBodyUserBaselineAuthorization(TeaModel):
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


class DescribeUserBaselineAuthorizationResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        user_baseline_authorization: DescribeUserBaselineAuthorizationResponseBodyUserBaselineAuthorization = None,
    ):
        self.request_id = request_id
        self.user_baseline_authorization = user_baseline_authorization

    def validate(self):
        if self.user_baseline_authorization:
            self.user_baseline_authorization.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.user_baseline_authorization is not None:
            result['UserBaselineAuthorization'] = self.user_baseline_authorization.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('UserBaselineAuthorization') is not None:
            temp_model = DescribeUserBaselineAuthorizationResponseBodyUserBaselineAuthorization()
            self.user_baseline_authorization = temp_model.from_map(m['UserBaselineAuthorization'])
        return self


class DescribeUserBaselineAuthorizationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeUserBaselineAuthorizationResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeUserBaselineAuthorizationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeUserLayoutAuthorizationRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        resource_owner_id: int = None,
        lang: str = None,
    ):
        self.source_ip = source_ip
        self.resource_owner_id = resource_owner_id
        self.lang = lang

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.lang is not None:
            result['Lang'] = self.lang
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        return self


class DescribeUserLayoutAuthorizationResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        authorized: bool = None,
    ):
        self.request_id = request_id
        self.authorized = authorized

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.authorized is not None:
            result['Authorized'] = self.authorized
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Authorized') is not None:
            self.authorized = m.get('Authorized')
        return self


class DescribeUserLayoutAuthorizationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeUserLayoutAuthorizationResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeUserLayoutAuthorizationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVersionConfigRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        resource_directory_account_id: str = None,
    ):
        self.source_ip = source_ip
        self.resource_directory_account_id = resource_directory_account_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_directory_account_id is not None:
            result['ResourceDirectoryAccountId'] = self.resource_directory_account_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceDirectoryAccountId') is not None:
            self.resource_directory_account_id = m.get('ResourceDirectoryAccountId')
        return self


class DescribeVersionConfigResponseBody(TeaModel):
    def __init__(
        self,
        image_scan_capacity: int = None,
        app_white_list_auth_count: int = None,
        sas_log: int = None,
        version: int = None,
        last_trail_end_time: int = None,
        web_lock_auth_count: int = None,
        sls_capacity: int = None,
        user_defined_alarms: int = None,
        web_lock: int = None,
        is_over_balance: bool = None,
        vm_cores: int = None,
        honeypot_capacity: int = None,
        request_id: str = None,
        asset_level: int = None,
        instance_id: str = None,
        sas_screen: int = None,
        release_time: int = None,
        is_trial_version: int = None,
        app_white_list: int = None,
    ):
        self.image_scan_capacity = image_scan_capacity
        self.app_white_list_auth_count = app_white_list_auth_count
        self.sas_log = sas_log
        self.version = version
        self.last_trail_end_time = last_trail_end_time
        self.web_lock_auth_count = web_lock_auth_count
        self.sls_capacity = sls_capacity
        self.user_defined_alarms = user_defined_alarms
        self.web_lock = web_lock
        self.is_over_balance = is_over_balance
        self.vm_cores = vm_cores
        self.honeypot_capacity = honeypot_capacity
        self.request_id = request_id
        self.asset_level = asset_level
        self.instance_id = instance_id
        self.sas_screen = sas_screen
        self.release_time = release_time
        self.is_trial_version = is_trial_version
        self.app_white_list = app_white_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.image_scan_capacity is not None:
            result['ImageScanCapacity'] = self.image_scan_capacity
        if self.app_white_list_auth_count is not None:
            result['AppWhiteListAuthCount'] = self.app_white_list_auth_count
        if self.sas_log is not None:
            result['SasLog'] = self.sas_log
        if self.version is not None:
            result['Version'] = self.version
        if self.last_trail_end_time is not None:
            result['LastTrailEndTime'] = self.last_trail_end_time
        if self.web_lock_auth_count is not None:
            result['WebLockAuthCount'] = self.web_lock_auth_count
        if self.sls_capacity is not None:
            result['SlsCapacity'] = self.sls_capacity
        if self.user_defined_alarms is not None:
            result['UserDefinedAlarms'] = self.user_defined_alarms
        if self.web_lock is not None:
            result['WebLock'] = self.web_lock
        if self.is_over_balance is not None:
            result['IsOverBalance'] = self.is_over_balance
        if self.vm_cores is not None:
            result['VmCores'] = self.vm_cores
        if self.honeypot_capacity is not None:
            result['HoneypotCapacity'] = self.honeypot_capacity
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.asset_level is not None:
            result['AssetLevel'] = self.asset_level
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.sas_screen is not None:
            result['SasScreen'] = self.sas_screen
        if self.release_time is not None:
            result['ReleaseTime'] = self.release_time
        if self.is_trial_version is not None:
            result['IsTrialVersion'] = self.is_trial_version
        if self.app_white_list is not None:
            result['AppWhiteList'] = self.app_white_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageScanCapacity') is not None:
            self.image_scan_capacity = m.get('ImageScanCapacity')
        if m.get('AppWhiteListAuthCount') is not None:
            self.app_white_list_auth_count = m.get('AppWhiteListAuthCount')
        if m.get('SasLog') is not None:
            self.sas_log = m.get('SasLog')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('LastTrailEndTime') is not None:
            self.last_trail_end_time = m.get('LastTrailEndTime')
        if m.get('WebLockAuthCount') is not None:
            self.web_lock_auth_count = m.get('WebLockAuthCount')
        if m.get('SlsCapacity') is not None:
            self.sls_capacity = m.get('SlsCapacity')
        if m.get('UserDefinedAlarms') is not None:
            self.user_defined_alarms = m.get('UserDefinedAlarms')
        if m.get('WebLock') is not None:
            self.web_lock = m.get('WebLock')
        if m.get('IsOverBalance') is not None:
            self.is_over_balance = m.get('IsOverBalance')
        if m.get('VmCores') is not None:
            self.vm_cores = m.get('VmCores')
        if m.get('HoneypotCapacity') is not None:
            self.honeypot_capacity = m.get('HoneypotCapacity')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('AssetLevel') is not None:
            self.asset_level = m.get('AssetLevel')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('SasScreen') is not None:
            self.sas_screen = m.get('SasScreen')
        if m.get('ReleaseTime') is not None:
            self.release_time = m.get('ReleaseTime')
        if m.get('IsTrialVersion') is not None:
            self.is_trial_version = m.get('IsTrialVersion')
        if m.get('AppWhiteList') is not None:
            self.app_white_list = m.get('AppWhiteList')
        return self


class DescribeVersionConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeVersionConfigResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeVersionConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVolDingdingMessageRequest(TeaModel):
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


class DescribeVolDingdingMessageResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        dingding_url: str = None,
    ):
        self.request_id = request_id
        self.dingding_url = dingding_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.dingding_url is not None:
            result['DingdingUrl'] = self.dingding_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DingdingUrl') is not None:
            self.dingding_url = m.get('DingdingUrl')
        return self


class DescribeVolDingdingMessageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeVolDingdingMessageResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeVolDingdingMessageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVpcHoneyPotCriteriaRequest(TeaModel):
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


class DescribeVpcHoneyPotCriteriaResponseBodyCriteriaList(TeaModel):
    def __init__(
        self,
        type: str = None,
        values: str = None,
        name: str = None,
    ):
        self.type = type
        self.values = values
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.values is not None:
            result['Values'] = self.values
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Values') is not None:
            self.values = m.get('Values')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class DescribeVpcHoneyPotCriteriaResponseBody(TeaModel):
    def __init__(
        self,
        criteria_list: List[DescribeVpcHoneyPotCriteriaResponseBodyCriteriaList] = None,
        request_id: str = None,
    ):
        self.criteria_list = criteria_list
        self.request_id = request_id

    def validate(self):
        if self.criteria_list:
            for k in self.criteria_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['CriteriaList'] = []
        if self.criteria_list is not None:
            for k in self.criteria_list:
                result['CriteriaList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.criteria_list = []
        if m.get('CriteriaList') is not None:
            for k in m.get('CriteriaList'):
                temp_model = DescribeVpcHoneyPotCriteriaResponseBodyCriteriaList()
                self.criteria_list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeVpcHoneyPotCriteriaResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeVpcHoneyPotCriteriaResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeVpcHoneyPotCriteriaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVpcHoneyPotListRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        vpc_id: str = None,
        vpc_name: str = None,
        vpc_region_id: str = None,
        honey_pot_existence: bool = None,
        page_size: int = None,
        current_page: int = None,
    ):
        self.source_ip = source_ip
        self.vpc_id = vpc_id
        self.vpc_name = vpc_name
        self.vpc_region_id = vpc_region_id
        self.honey_pot_existence = honey_pot_existence
        self.page_size = page_size
        self.current_page = current_page

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.vpc_name is not None:
            result['VpcName'] = self.vpc_name
        if self.vpc_region_id is not None:
            result['VpcRegionId'] = self.vpc_region_id
        if self.honey_pot_existence is not None:
            result['HoneyPotExistence'] = self.honey_pot_existence
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VpcName') is not None:
            self.vpc_name = m.get('VpcName')
        if m.get('VpcRegionId') is not None:
            self.vpc_region_id = m.get('VpcRegionId')
        if m.get('HoneyPotExistence') is not None:
            self.honey_pot_existence = m.get('HoneyPotExistence')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        return self


class DescribeVpcHoneyPotListResponseBodyVpcHoneyPotDTOList(TeaModel):
    def __init__(
        self,
        vpc_id: str = None,
        vpc_status: str = None,
        create_time: int = None,
        honey_pot_existence: bool = None,
        vpc_region_id: str = None,
        honey_pot_instance_status: str = None,
        honey_pot_vswitch_id: str = None,
        vpc_switch_id_list: List[str] = None,
        vpc_name: str = None,
        honey_pot_eni_instance_id: str = None,
        cidr_block: str = None,
        honey_pot_ecs_instance_status: str = None,
    ):
        self.vpc_id = vpc_id
        self.vpc_status = vpc_status
        self.create_time = create_time
        self.honey_pot_existence = honey_pot_existence
        self.vpc_region_id = vpc_region_id
        self.honey_pot_instance_status = honey_pot_instance_status
        self.honey_pot_vswitch_id = honey_pot_vswitch_id
        self.vpc_switch_id_list = vpc_switch_id_list
        self.vpc_name = vpc_name
        self.honey_pot_eni_instance_id = honey_pot_eni_instance_id
        self.cidr_block = cidr_block
        self.honey_pot_ecs_instance_status = honey_pot_ecs_instance_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.vpc_status is not None:
            result['VpcStatus'] = self.vpc_status
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.honey_pot_existence is not None:
            result['HoneyPotExistence'] = self.honey_pot_existence
        if self.vpc_region_id is not None:
            result['VpcRegionId'] = self.vpc_region_id
        if self.honey_pot_instance_status is not None:
            result['HoneyPotInstanceStatus'] = self.honey_pot_instance_status
        if self.honey_pot_vswitch_id is not None:
            result['HoneyPotVSwitchId'] = self.honey_pot_vswitch_id
        if self.vpc_switch_id_list is not None:
            result['VpcSwitchIdList'] = self.vpc_switch_id_list
        if self.vpc_name is not None:
            result['VpcName'] = self.vpc_name
        if self.honey_pot_eni_instance_id is not None:
            result['HoneyPotEniInstanceId'] = self.honey_pot_eni_instance_id
        if self.cidr_block is not None:
            result['CidrBlock'] = self.cidr_block
        if self.honey_pot_ecs_instance_status is not None:
            result['HoneyPotEcsInstanceStatus'] = self.honey_pot_ecs_instance_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VpcStatus') is not None:
            self.vpc_status = m.get('VpcStatus')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('HoneyPotExistence') is not None:
            self.honey_pot_existence = m.get('HoneyPotExistence')
        if m.get('VpcRegionId') is not None:
            self.vpc_region_id = m.get('VpcRegionId')
        if m.get('HoneyPotInstanceStatus') is not None:
            self.honey_pot_instance_status = m.get('HoneyPotInstanceStatus')
        if m.get('HoneyPotVSwitchId') is not None:
            self.honey_pot_vswitch_id = m.get('HoneyPotVSwitchId')
        if m.get('VpcSwitchIdList') is not None:
            self.vpc_switch_id_list = m.get('VpcSwitchIdList')
        if m.get('VpcName') is not None:
            self.vpc_name = m.get('VpcName')
        if m.get('HoneyPotEniInstanceId') is not None:
            self.honey_pot_eni_instance_id = m.get('HoneyPotEniInstanceId')
        if m.get('CidrBlock') is not None:
            self.cidr_block = m.get('CidrBlock')
        if m.get('HoneyPotEcsInstanceStatus') is not None:
            self.honey_pot_ecs_instance_status = m.get('HoneyPotEcsInstanceStatus')
        return self


class DescribeVpcHoneyPotListResponseBodyPageInfo(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        page_size: int = None,
        total_count: int = None,
        count: int = None,
    ):
        self.current_page = current_page
        self.page_size = page_size
        self.total_count = total_count
        self.count = count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.count is not None:
            result['Count'] = self.count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        return self


class DescribeVpcHoneyPotListResponseBody(TeaModel):
    def __init__(
        self,
        vpc_honey_pot_dtolist: List[DescribeVpcHoneyPotListResponseBodyVpcHoneyPotDTOList] = None,
        page_info: DescribeVpcHoneyPotListResponseBodyPageInfo = None,
        request_id: str = None,
    ):
        self.vpc_honey_pot_dtolist = vpc_honey_pot_dtolist
        self.page_info = page_info
        self.request_id = request_id

    def validate(self):
        if self.vpc_honey_pot_dtolist:
            for k in self.vpc_honey_pot_dtolist:
                if k:
                    k.validate()
        if self.page_info:
            self.page_info.validate()

    def to_map(self):
        result = dict()
        result['VpcHoneyPotDTOList'] = []
        if self.vpc_honey_pot_dtolist is not None:
            for k in self.vpc_honey_pot_dtolist:
                result['VpcHoneyPotDTOList'].append(k.to_map() if k else None)
        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.vpc_honey_pot_dtolist = []
        if m.get('VpcHoneyPotDTOList') is not None:
            for k in m.get('VpcHoneyPotDTOList'):
                temp_model = DescribeVpcHoneyPotListResponseBodyVpcHoneyPotDTOList()
                self.vpc_honey_pot_dtolist.append(temp_model.from_map(k))
        if m.get('PageInfo') is not None:
            temp_model = DescribeVpcHoneyPotListResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m['PageInfo'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeVpcHoneyPotListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeVpcHoneyPotListResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeVpcHoneyPotListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVpcListRequest(TeaModel):
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


class DescribeVpcListResponseBodyVpcList(TeaModel):
    def __init__(
        self,
        instance_desc: str = None,
        instance_name: str = None,
        ecs_count: int = None,
        instance_id: str = None,
        region_id: str = None,
    ):
        self.instance_desc = instance_desc
        self.instance_name = instance_name
        self.ecs_count = ecs_count
        self.instance_id = instance_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.instance_desc is not None:
            result['InstanceDesc'] = self.instance_desc
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.ecs_count is not None:
            result['EcsCount'] = self.ecs_count
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceDesc') is not None:
            self.instance_desc = m.get('InstanceDesc')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('EcsCount') is not None:
            self.ecs_count = m.get('EcsCount')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeVpcListResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        vpc_list: List[DescribeVpcListResponseBodyVpcList] = None,
        count: int = None,
    ):
        self.request_id = request_id
        self.vpc_list = vpc_list
        self.count = count

    def validate(self):
        if self.vpc_list:
            for k in self.vpc_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['VpcList'] = []
        if self.vpc_list is not None:
            for k in self.vpc_list:
                result['VpcList'].append(k.to_map() if k else None)
        if self.count is not None:
            result['Count'] = self.count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.vpc_list = []
        if m.get('VpcList') is not None:
            for k in m.get('VpcList'):
                temp_model = DescribeVpcListResponseBodyVpcList()
                self.vpc_list.append(temp_model.from_map(k))
        if m.get('Count') is not None:
            self.count = m.get('Count')
        return self


class DescribeVpcListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeVpcListResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeVpcListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVulDetailsRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        type: str = None,
        name: str = None,
        alias_name: str = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.type = type
        self.name = name
        self.alias_name = alias_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.type is not None:
            result['Type'] = self.type
        if self.name is not None:
            result['Name'] = self.name
        if self.alias_name is not None:
            result['AliasName'] = self.alias_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('AliasName') is not None:
            self.alias_name = m.get('AliasName')
        return self


class DescribeVulDetailsResponseBodyCvesClassifys(TeaModel):
    def __init__(
        self,
        description: str = None,
        classify: str = None,
        demo_video_url: str = None,
    ):
        self.description = description
        self.classify = classify
        self.demo_video_url = demo_video_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.classify is not None:
            result['Classify'] = self.classify
        if self.demo_video_url is not None:
            result['DemoVideoUrl'] = self.demo_video_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Classify') is not None:
            self.classify = m.get('Classify')
        if m.get('DemoVideoUrl') is not None:
            self.demo_video_url = m.get('DemoVideoUrl')
        return self


class DescribeVulDetailsResponseBodyCves(TeaModel):
    def __init__(
        self,
        complexity: str = None,
        summary: str = None,
        product: str = None,
        poc_create_time: int = None,
        cve_id: str = None,
        cnvd_id: str = None,
        reference: str = None,
        cvss_score: str = None,
        vendor: str = None,
        poc_disclosure_time: int = None,
        cvss_vector: str = None,
        classify: str = None,
        vul_level: str = None,
        release_time: int = None,
        title: str = None,
        solution: str = None,
        content: str = None,
        poc: str = None,
        classifys: List[DescribeVulDetailsResponseBodyCvesClassifys] = None,
    ):
        self.complexity = complexity
        self.summary = summary
        self.product = product
        self.poc_create_time = poc_create_time
        self.cve_id = cve_id
        self.cnvd_id = cnvd_id
        self.reference = reference
        self.cvss_score = cvss_score
        self.vendor = vendor
        self.poc_disclosure_time = poc_disclosure_time
        self.cvss_vector = cvss_vector
        self.classify = classify
        self.vul_level = vul_level
        self.release_time = release_time
        self.title = title
        self.solution = solution
        self.content = content
        self.poc = poc
        self.classifys = classifys

    def validate(self):
        if self.classifys:
            for k in self.classifys:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.complexity is not None:
            result['Complexity'] = self.complexity
        if self.summary is not None:
            result['Summary'] = self.summary
        if self.product is not None:
            result['Product'] = self.product
        if self.poc_create_time is not None:
            result['PocCreateTime'] = self.poc_create_time
        if self.cve_id is not None:
            result['CveId'] = self.cve_id
        if self.cnvd_id is not None:
            result['CnvdId'] = self.cnvd_id
        if self.reference is not None:
            result['Reference'] = self.reference
        if self.cvss_score is not None:
            result['CvssScore'] = self.cvss_score
        if self.vendor is not None:
            result['Vendor'] = self.vendor
        if self.poc_disclosure_time is not None:
            result['PocDisclosureTime'] = self.poc_disclosure_time
        if self.cvss_vector is not None:
            result['CvssVector'] = self.cvss_vector
        if self.classify is not None:
            result['Classify'] = self.classify
        if self.vul_level is not None:
            result['VulLevel'] = self.vul_level
        if self.release_time is not None:
            result['ReleaseTime'] = self.release_time
        if self.title is not None:
            result['Title'] = self.title
        if self.solution is not None:
            result['Solution'] = self.solution
        if self.content is not None:
            result['Content'] = self.content
        if self.poc is not None:
            result['Poc'] = self.poc
        result['Classifys'] = []
        if self.classifys is not None:
            for k in self.classifys:
                result['Classifys'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Complexity') is not None:
            self.complexity = m.get('Complexity')
        if m.get('Summary') is not None:
            self.summary = m.get('Summary')
        if m.get('Product') is not None:
            self.product = m.get('Product')
        if m.get('PocCreateTime') is not None:
            self.poc_create_time = m.get('PocCreateTime')
        if m.get('CveId') is not None:
            self.cve_id = m.get('CveId')
        if m.get('CnvdId') is not None:
            self.cnvd_id = m.get('CnvdId')
        if m.get('Reference') is not None:
            self.reference = m.get('Reference')
        if m.get('CvssScore') is not None:
            self.cvss_score = m.get('CvssScore')
        if m.get('Vendor') is not None:
            self.vendor = m.get('Vendor')
        if m.get('PocDisclosureTime') is not None:
            self.poc_disclosure_time = m.get('PocDisclosureTime')
        if m.get('CvssVector') is not None:
            self.cvss_vector = m.get('CvssVector')
        if m.get('Classify') is not None:
            self.classify = m.get('Classify')
        if m.get('VulLevel') is not None:
            self.vul_level = m.get('VulLevel')
        if m.get('ReleaseTime') is not None:
            self.release_time = m.get('ReleaseTime')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Solution') is not None:
            self.solution = m.get('Solution')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Poc') is not None:
            self.poc = m.get('Poc')
        self.classifys = []
        if m.get('Classifys') is not None:
            for k in m.get('Classifys'):
                temp_model = DescribeVulDetailsResponseBodyCvesClassifys()
                self.classifys.append(temp_model.from_map(k))
        return self


class DescribeVulDetailsResponseBody(TeaModel):
    def __init__(
        self,
        cves: List[DescribeVulDetailsResponseBodyCves] = None,
        request_id: str = None,
    ):
        self.cves = cves
        self.request_id = request_id

    def validate(self):
        if self.cves:
            for k in self.cves:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Cves'] = []
        if self.cves is not None:
            for k in self.cves:
                result['Cves'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.cves = []
        if m.get('Cves') is not None:
            for k in m.get('Cves'):
                temp_model = DescribeVulDetailsResponseBodyCves()
                self.cves.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeVulDetailsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeVulDetailsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeVulDetailsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVulListRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        ids: str = None,
        remark: str = None,
        group_id: str = None,
        type: str = None,
        uuids: str = None,
        name: str = None,
        alias_name: str = None,
        level: str = None,
        status_list: str = None,
        necessity: str = None,
        dealed: str = None,
        batch_name: str = None,
        resource: str = None,
        create_ts_start: int = None,
        create_ts_end: int = None,
        current_page: int = None,
        page_size: int = None,
        modify_ts_start: int = None,
        modify_ts_end: int = None,
        attach_types: str = None,
        container_field_name: str = None,
        container_field_value: str = None,
        target_type: str = None,
        cluster_id: str = None,
        min_score: int = None,
        vpc_instance_ids: str = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.ids = ids
        self.remark = remark
        self.group_id = group_id
        self.type = type
        self.uuids = uuids
        self.name = name
        self.alias_name = alias_name
        self.level = level
        self.status_list = status_list
        self.necessity = necessity
        self.dealed = dealed
        self.batch_name = batch_name
        self.resource = resource
        self.create_ts_start = create_ts_start
        self.create_ts_end = create_ts_end
        self.current_page = current_page
        self.page_size = page_size
        self.modify_ts_start = modify_ts_start
        self.modify_ts_end = modify_ts_end
        self.attach_types = attach_types
        self.container_field_name = container_field_name
        self.container_field_value = container_field_value
        self.target_type = target_type
        self.cluster_id = cluster_id
        self.min_score = min_score
        self.vpc_instance_ids = vpc_instance_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.ids is not None:
            result['Ids'] = self.ids
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.type is not None:
            result['Type'] = self.type
        if self.uuids is not None:
            result['Uuids'] = self.uuids
        if self.name is not None:
            result['Name'] = self.name
        if self.alias_name is not None:
            result['AliasName'] = self.alias_name
        if self.level is not None:
            result['Level'] = self.level
        if self.status_list is not None:
            result['StatusList'] = self.status_list
        if self.necessity is not None:
            result['Necessity'] = self.necessity
        if self.dealed is not None:
            result['Dealed'] = self.dealed
        if self.batch_name is not None:
            result['BatchName'] = self.batch_name
        if self.resource is not None:
            result['Resource'] = self.resource
        if self.create_ts_start is not None:
            result['CreateTsStart'] = self.create_ts_start
        if self.create_ts_end is not None:
            result['CreateTsEnd'] = self.create_ts_end
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.modify_ts_start is not None:
            result['ModifyTsStart'] = self.modify_ts_start
        if self.modify_ts_end is not None:
            result['ModifyTsEnd'] = self.modify_ts_end
        if self.attach_types is not None:
            result['AttachTypes'] = self.attach_types
        if self.container_field_name is not None:
            result['ContainerFieldName'] = self.container_field_name
        if self.container_field_value is not None:
            result['ContainerFieldValue'] = self.container_field_value
        if self.target_type is not None:
            result['TargetType'] = self.target_type
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.min_score is not None:
            result['MinScore'] = self.min_score
        if self.vpc_instance_ids is not None:
            result['VpcInstanceIds'] = self.vpc_instance_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('Ids') is not None:
            self.ids = m.get('Ids')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Uuids') is not None:
            self.uuids = m.get('Uuids')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('AliasName') is not None:
            self.alias_name = m.get('AliasName')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        if m.get('StatusList') is not None:
            self.status_list = m.get('StatusList')
        if m.get('Necessity') is not None:
            self.necessity = m.get('Necessity')
        if m.get('Dealed') is not None:
            self.dealed = m.get('Dealed')
        if m.get('BatchName') is not None:
            self.batch_name = m.get('BatchName')
        if m.get('Resource') is not None:
            self.resource = m.get('Resource')
        if m.get('CreateTsStart') is not None:
            self.create_ts_start = m.get('CreateTsStart')
        if m.get('CreateTsEnd') is not None:
            self.create_ts_end = m.get('CreateTsEnd')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ModifyTsStart') is not None:
            self.modify_ts_start = m.get('ModifyTsStart')
        if m.get('ModifyTsEnd') is not None:
            self.modify_ts_end = m.get('ModifyTsEnd')
        if m.get('AttachTypes') is not None:
            self.attach_types = m.get('AttachTypes')
        if m.get('ContainerFieldName') is not None:
            self.container_field_name = m.get('ContainerFieldName')
        if m.get('ContainerFieldValue') is not None:
            self.container_field_value = m.get('ContainerFieldValue')
        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('MinScore') is not None:
            self.min_score = m.get('MinScore')
        if m.get('VpcInstanceIds') is not None:
            self.vpc_instance_ids = m.get('VpcInstanceIds')
        return self


class DescribeVulListResponseBodyVulRecordsExtendContentJsonRpmEntityList(TeaModel):
    def __init__(
        self,
        full_version: str = None,
        version: str = None,
        match_detail: str = None,
        path: str = None,
        name: str = None,
        update_cmd: str = None,
    ):
        self.full_version = full_version
        self.version = version
        self.match_detail = match_detail
        self.path = path
        self.name = name
        self.update_cmd = update_cmd

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.full_version is not None:
            result['FullVersion'] = self.full_version
        if self.version is not None:
            result['Version'] = self.version
        if self.match_detail is not None:
            result['MatchDetail'] = self.match_detail
        if self.path is not None:
            result['Path'] = self.path
        if self.name is not None:
            result['Name'] = self.name
        if self.update_cmd is not None:
            result['UpdateCmd'] = self.update_cmd
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FullVersion') is not None:
            self.full_version = m.get('FullVersion')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('MatchDetail') is not None:
            self.match_detail = m.get('MatchDetail')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('UpdateCmd') is not None:
            self.update_cmd = m.get('UpdateCmd')
        return self


class DescribeVulListResponseBodyVulRecordsExtendContentJsonNecessity(TeaModel):
    def __init__(
        self,
        status: str = None,
        time_factor: str = None,
        enviroment_factor: str = None,
        is_calc: str = None,
        total_score: str = None,
        cvss_factor: str = None,
        assets_factor: str = None,
    ):
        self.status = status
        self.time_factor = time_factor
        self.enviroment_factor = enviroment_factor
        self.is_calc = is_calc
        self.total_score = total_score
        self.cvss_factor = cvss_factor
        self.assets_factor = assets_factor

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.time_factor is not None:
            result['Time_factor'] = self.time_factor
        if self.enviroment_factor is not None:
            result['Enviroment_factor'] = self.enviroment_factor
        if self.is_calc is not None:
            result['Is_calc'] = self.is_calc
        if self.total_score is not None:
            result['Total_score'] = self.total_score
        if self.cvss_factor is not None:
            result['Cvss_factor'] = self.cvss_factor
        if self.assets_factor is not None:
            result['Assets_factor'] = self.assets_factor
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Time_factor') is not None:
            self.time_factor = m.get('Time_factor')
        if m.get('Enviroment_factor') is not None:
            self.enviroment_factor = m.get('Enviroment_factor')
        if m.get('Is_calc') is not None:
            self.is_calc = m.get('Is_calc')
        if m.get('Total_score') is not None:
            self.total_score = m.get('Total_score')
        if m.get('Cvss_factor') is not None:
            self.cvss_factor = m.get('Cvss_factor')
        if m.get('Assets_factor') is not None:
            self.assets_factor = m.get('Assets_factor')
        return self


class DescribeVulListResponseBodyVulRecordsExtendContentJson(TeaModel):
    def __init__(
        self,
        status: int = None,
        cve_list: List[str] = None,
        primary_id: int = None,
        tag: str = None,
        os_release: str = None,
        rpm_entity_list: List[DescribeVulListResponseBodyVulRecordsExtendContentJsonRpmEntityList] = None,
        ip: str = None,
        os: str = None,
        last_ts: int = None,
        necessity: DescribeVulListResponseBodyVulRecordsExtendContentJsonNecessity = None,
        alias_name: str = None,
        absolute_path: str = None,
    ):
        self.status = status
        self.cve_list = cve_list
        self.primary_id = primary_id
        self.tag = tag
        self.os_release = os_release
        self.rpm_entity_list = rpm_entity_list
        self.ip = ip
        self.os = os
        self.last_ts = last_ts
        self.necessity = necessity
        self.alias_name = alias_name
        self.absolute_path = absolute_path

    def validate(self):
        if self.rpm_entity_list:
            for k in self.rpm_entity_list:
                if k:
                    k.validate()
        if self.necessity:
            self.necessity.validate()

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.cve_list is not None:
            result['cveList'] = self.cve_list
        if self.primary_id is not None:
            result['PrimaryId'] = self.primary_id
        if self.tag is not None:
            result['Tag'] = self.tag
        if self.os_release is not None:
            result['OsRelease'] = self.os_release
        result['RpmEntityList'] = []
        if self.rpm_entity_list is not None:
            for k in self.rpm_entity_list:
                result['RpmEntityList'].append(k.to_map() if k else None)
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.os is not None:
            result['Os'] = self.os
        if self.last_ts is not None:
            result['LastTs'] = self.last_ts
        if self.necessity is not None:
            result['Necessity'] = self.necessity.to_map()
        if self.alias_name is not None:
            result['AliasName'] = self.alias_name
        if self.absolute_path is not None:
            result['AbsolutePath'] = self.absolute_path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('cveList') is not None:
            self.cve_list = m.get('cveList')
        if m.get('PrimaryId') is not None:
            self.primary_id = m.get('PrimaryId')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        if m.get('OsRelease') is not None:
            self.os_release = m.get('OsRelease')
        self.rpm_entity_list = []
        if m.get('RpmEntityList') is not None:
            for k in m.get('RpmEntityList'):
                temp_model = DescribeVulListResponseBodyVulRecordsExtendContentJsonRpmEntityList()
                self.rpm_entity_list.append(temp_model.from_map(k))
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('Os') is not None:
            self.os = m.get('Os')
        if m.get('LastTs') is not None:
            self.last_ts = m.get('LastTs')
        if m.get('Necessity') is not None:
            temp_model = DescribeVulListResponseBodyVulRecordsExtendContentJsonNecessity()
            self.necessity = temp_model.from_map(m['Necessity'])
        if m.get('AliasName') is not None:
            self.alias_name = m.get('AliasName')
        if m.get('AbsolutePath') is not None:
            self.absolute_path = m.get('AbsolutePath')
        return self


class DescribeVulListResponseBodyVulRecords(TeaModel):
    def __init__(
        self,
        status: int = None,
        type: str = None,
        modify_ts: int = None,
        internet_ip: str = None,
        container_image_id: str = None,
        primary_id: int = None,
        tag: str = None,
        k_8s_cluster_id: str = None,
        container_image_name: str = None,
        k_8s_node_id: str = None,
        instance_name: str = None,
        online: bool = None,
        container_inner_path: str = None,
        os_version: str = None,
        name: str = None,
        extend_content_json: DescribeVulListResponseBodyVulRecordsExtendContentJson = None,
        result_code: str = None,
        instance_id: str = None,
        related: str = None,
        intranet_ip: str = None,
        last_ts: int = None,
        first_ts: int = None,
        necessity: str = None,
        repair_ts: int = None,
        uuid: str = None,
        k_8s_pod_name: str = None,
        container_id: str = None,
        group_id: int = None,
        result_message: str = None,
        k_8s_namespace: str = None,
        alias_name: str = None,
        k_8s_node_name: str = None,
        container_name: str = None,
    ):
        self.status = status
        self.type = type
        self.modify_ts = modify_ts
        self.internet_ip = internet_ip
        self.container_image_id = container_image_id
        self.primary_id = primary_id
        self.tag = tag
        self.k_8s_cluster_id = k_8s_cluster_id
        self.container_image_name = container_image_name
        self.k_8s_node_id = k_8s_node_id
        self.instance_name = instance_name
        self.online = online
        self.container_inner_path = container_inner_path
        self.os_version = os_version
        self.name = name
        self.extend_content_json = extend_content_json
        self.result_code = result_code
        self.instance_id = instance_id
        self.related = related
        self.intranet_ip = intranet_ip
        self.last_ts = last_ts
        self.first_ts = first_ts
        self.necessity = necessity
        self.repair_ts = repair_ts
        self.uuid = uuid
        self.k_8s_pod_name = k_8s_pod_name
        self.container_id = container_id
        self.group_id = group_id
        self.result_message = result_message
        self.k_8s_namespace = k_8s_namespace
        self.alias_name = alias_name
        self.k_8s_node_name = k_8s_node_name
        self.container_name = container_name

    def validate(self):
        if self.extend_content_json:
            self.extend_content_json.validate()

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        if self.modify_ts is not None:
            result['ModifyTs'] = self.modify_ts
        if self.internet_ip is not None:
            result['InternetIp'] = self.internet_ip
        if self.container_image_id is not None:
            result['ContainerImageId'] = self.container_image_id
        if self.primary_id is not None:
            result['PrimaryId'] = self.primary_id
        if self.tag is not None:
            result['Tag'] = self.tag
        if self.k_8s_cluster_id is not None:
            result['K8sClusterId'] = self.k_8s_cluster_id
        if self.container_image_name is not None:
            result['ContainerImageName'] = self.container_image_name
        if self.k_8s_node_id is not None:
            result['K8sNodeId'] = self.k_8s_node_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.online is not None:
            result['Online'] = self.online
        if self.container_inner_path is not None:
            result['ContainerInnerPath'] = self.container_inner_path
        if self.os_version is not None:
            result['OsVersion'] = self.os_version
        if self.name is not None:
            result['Name'] = self.name
        if self.extend_content_json is not None:
            result['ExtendContentJson'] = self.extend_content_json.to_map()
        if self.result_code is not None:
            result['ResultCode'] = self.result_code
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.related is not None:
            result['Related'] = self.related
        if self.intranet_ip is not None:
            result['IntranetIp'] = self.intranet_ip
        if self.last_ts is not None:
            result['LastTs'] = self.last_ts
        if self.first_ts is not None:
            result['FirstTs'] = self.first_ts
        if self.necessity is not None:
            result['Necessity'] = self.necessity
        if self.repair_ts is not None:
            result['RepairTs'] = self.repair_ts
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        if self.k_8s_pod_name is not None:
            result['K8sPodName'] = self.k_8s_pod_name
        if self.container_id is not None:
            result['ContainerId'] = self.container_id
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.result_message is not None:
            result['ResultMessage'] = self.result_message
        if self.k_8s_namespace is not None:
            result['K8sNamespace'] = self.k_8s_namespace
        if self.alias_name is not None:
            result['AliasName'] = self.alias_name
        if self.k_8s_node_name is not None:
            result['K8sNodeName'] = self.k_8s_node_name
        if self.container_name is not None:
            result['ContainerName'] = self.container_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('ModifyTs') is not None:
            self.modify_ts = m.get('ModifyTs')
        if m.get('InternetIp') is not None:
            self.internet_ip = m.get('InternetIp')
        if m.get('ContainerImageId') is not None:
            self.container_image_id = m.get('ContainerImageId')
        if m.get('PrimaryId') is not None:
            self.primary_id = m.get('PrimaryId')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        if m.get('K8sClusterId') is not None:
            self.k_8s_cluster_id = m.get('K8sClusterId')
        if m.get('ContainerImageName') is not None:
            self.container_image_name = m.get('ContainerImageName')
        if m.get('K8sNodeId') is not None:
            self.k_8s_node_id = m.get('K8sNodeId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('Online') is not None:
            self.online = m.get('Online')
        if m.get('ContainerInnerPath') is not None:
            self.container_inner_path = m.get('ContainerInnerPath')
        if m.get('OsVersion') is not None:
            self.os_version = m.get('OsVersion')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ExtendContentJson') is not None:
            temp_model = DescribeVulListResponseBodyVulRecordsExtendContentJson()
            self.extend_content_json = temp_model.from_map(m['ExtendContentJson'])
        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Related') is not None:
            self.related = m.get('Related')
        if m.get('IntranetIp') is not None:
            self.intranet_ip = m.get('IntranetIp')
        if m.get('LastTs') is not None:
            self.last_ts = m.get('LastTs')
        if m.get('FirstTs') is not None:
            self.first_ts = m.get('FirstTs')
        if m.get('Necessity') is not None:
            self.necessity = m.get('Necessity')
        if m.get('RepairTs') is not None:
            self.repair_ts = m.get('RepairTs')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        if m.get('K8sPodName') is not None:
            self.k_8s_pod_name = m.get('K8sPodName')
        if m.get('ContainerId') is not None:
            self.container_id = m.get('ContainerId')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('ResultMessage') is not None:
            self.result_message = m.get('ResultMessage')
        if m.get('K8sNamespace') is not None:
            self.k_8s_namespace = m.get('K8sNamespace')
        if m.get('AliasName') is not None:
            self.alias_name = m.get('AliasName')
        if m.get('K8sNodeName') is not None:
            self.k_8s_node_name = m.get('K8sNodeName')
        if m.get('ContainerName') is not None:
            self.container_name = m.get('ContainerName')
        return self


class DescribeVulListResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        request_id: str = None,
        page_size: int = None,
        vul_records: List[DescribeVulListResponseBodyVulRecords] = None,
        current_page: int = None,
    ):
        self.total_count = total_count
        self.request_id = request_id
        self.page_size = page_size
        self.vul_records = vul_records
        self.current_page = current_page

    def validate(self):
        if self.vul_records:
            for k in self.vul_records:
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
        result['VulRecords'] = []
        if self.vul_records is not None:
            for k in self.vul_records:
                result['VulRecords'].append(k.to_map() if k else None)
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
        self.vul_records = []
        if m.get('VulRecords') is not None:
            for k in m.get('VulRecords'):
                temp_model = DescribeVulListResponseBodyVulRecords()
                self.vul_records.append(temp_model.from_map(k))
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        return self


class DescribeVulListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeVulListResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeVulListResponseBody()
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


class DescribeWarningMachinesRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        machine_name: str = None,
        uuids: str = None,
        risk_id: int = None,
        strategy_id: int = None,
        page_size: int = None,
        current_page: int = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.machine_name = machine_name
        self.uuids = uuids
        self.risk_id = risk_id
        self.strategy_id = strategy_id
        self.page_size = page_size
        self.current_page = current_page

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.machine_name is not None:
            result['MachineName'] = self.machine_name
        if self.uuids is not None:
            result['Uuids'] = self.uuids
        if self.risk_id is not None:
            result['RiskId'] = self.risk_id
        if self.strategy_id is not None:
            result['StrategyId'] = self.strategy_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('MachineName') is not None:
            self.machine_name = m.get('MachineName')
        if m.get('Uuids') is not None:
            self.uuids = m.get('Uuids')
        if m.get('RiskId') is not None:
            self.risk_id = m.get('RiskId')
        if m.get('StrategyId') is not None:
            self.strategy_id = m.get('StrategyId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        return self


class DescribeWarningMachinesResponseBodyWarningMachines(TeaModel):
    def __init__(
        self,
        status: int = None,
        low_warning_count: int = None,
        uuid: str = None,
        medium_warning_count: int = None,
        pass_count: int = None,
        internet_ip: str = None,
        instance_name: str = None,
        instance_id: str = None,
        high_warning_count: int = None,
        intranet_ip: str = None,
        region_id: str = None,
    ):
        self.status = status
        self.low_warning_count = low_warning_count
        self.uuid = uuid
        self.medium_warning_count = medium_warning_count
        self.pass_count = pass_count
        self.internet_ip = internet_ip
        self.instance_name = instance_name
        self.instance_id = instance_id
        self.high_warning_count = high_warning_count
        self.intranet_ip = intranet_ip
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.low_warning_count is not None:
            result['LowWarningCount'] = self.low_warning_count
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        if self.medium_warning_count is not None:
            result['MediumWarningCount'] = self.medium_warning_count
        if self.pass_count is not None:
            result['PassCount'] = self.pass_count
        if self.internet_ip is not None:
            result['InternetIp'] = self.internet_ip
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.high_warning_count is not None:
            result['HighWarningCount'] = self.high_warning_count
        if self.intranet_ip is not None:
            result['IntranetIp'] = self.intranet_ip
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('LowWarningCount') is not None:
            self.low_warning_count = m.get('LowWarningCount')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        if m.get('MediumWarningCount') is not None:
            self.medium_warning_count = m.get('MediumWarningCount')
        if m.get('PassCount') is not None:
            self.pass_count = m.get('PassCount')
        if m.get('InternetIp') is not None:
            self.internet_ip = m.get('InternetIp')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('HighWarningCount') is not None:
            self.high_warning_count = m.get('HighWarningCount')
        if m.get('IntranetIp') is not None:
            self.intranet_ip = m.get('IntranetIp')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeWarningMachinesResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        page_size: int = None,
        request_id: str = None,
        current_page: int = None,
        warning_machines: List[DescribeWarningMachinesResponseBodyWarningMachines] = None,
        count: int = None,
    ):
        self.total_count = total_count
        self.page_size = page_size
        self.request_id = request_id
        self.current_page = current_page
        self.warning_machines = warning_machines
        self.count = count

    def validate(self):
        if self.warning_machines:
            for k in self.warning_machines:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        result['WarningMachines'] = []
        if self.warning_machines is not None:
            for k in self.warning_machines:
                result['WarningMachines'].append(k.to_map() if k else None)
        if self.count is not None:
            result['Count'] = self.count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        self.warning_machines = []
        if m.get('WarningMachines') is not None:
            for k in m.get('WarningMachines'):
                temp_model = DescribeWarningMachinesResponseBodyWarningMachines()
                self.warning_machines.append(temp_model.from_map(k))
        if m.get('Count') is not None:
            self.count = m.get('Count')
        return self


class DescribeWarningMachinesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeWarningMachinesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeWarningMachinesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeWebLockBindListRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        remark: str = None,
        status: str = None,
        current_page: int = None,
        page_size: int = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.remark = remark
        self.status = status
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
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.status is not None:
            result['Status'] = self.status
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
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeWebLockBindListResponseBodyBindList(TeaModel):
    def __init__(
        self,
        status: str = None,
        percent: int = None,
        service_detail: str = None,
        internet_ip: str = None,
        os: str = None,
        service_status: str = None,
        intranet_ip: str = None,
        audit_count: str = None,
        uuid: str = None,
        service_code: str = None,
        instance_name: str = None,
        dir_count: str = None,
        block_count: str = None,
    ):
        self.status = status
        self.percent = percent
        self.service_detail = service_detail
        self.internet_ip = internet_ip
        self.os = os
        self.service_status = service_status
        self.intranet_ip = intranet_ip
        self.audit_count = audit_count
        self.uuid = uuid
        self.service_code = service_code
        self.instance_name = instance_name
        self.dir_count = dir_count
        self.block_count = block_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.percent is not None:
            result['Percent'] = self.percent
        if self.service_detail is not None:
            result['ServiceDetail'] = self.service_detail
        if self.internet_ip is not None:
            result['InternetIp'] = self.internet_ip
        if self.os is not None:
            result['Os'] = self.os
        if self.service_status is not None:
            result['ServiceStatus'] = self.service_status
        if self.intranet_ip is not None:
            result['IntranetIp'] = self.intranet_ip
        if self.audit_count is not None:
            result['AuditCount'] = self.audit_count
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.dir_count is not None:
            result['DirCount'] = self.dir_count
        if self.block_count is not None:
            result['BlockCount'] = self.block_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Percent') is not None:
            self.percent = m.get('Percent')
        if m.get('ServiceDetail') is not None:
            self.service_detail = m.get('ServiceDetail')
        if m.get('InternetIp') is not None:
            self.internet_ip = m.get('InternetIp')
        if m.get('Os') is not None:
            self.os = m.get('Os')
        if m.get('ServiceStatus') is not None:
            self.service_status = m.get('ServiceStatus')
        if m.get('IntranetIp') is not None:
            self.intranet_ip = m.get('IntranetIp')
        if m.get('AuditCount') is not None:
            self.audit_count = m.get('AuditCount')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('DirCount') is not None:
            self.dir_count = m.get('DirCount')
        if m.get('BlockCount') is not None:
            self.block_count = m.get('BlockCount')
        return self


class DescribeWebLockBindListResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        request_id: str = None,
        page_size: int = None,
        current_page: int = None,
        bind_list: List[DescribeWebLockBindListResponseBodyBindList] = None,
    ):
        self.total_count = total_count
        self.request_id = request_id
        self.page_size = page_size
        self.current_page = current_page
        self.bind_list = bind_list

    def validate(self):
        if self.bind_list:
            for k in self.bind_list:
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
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        result['BindList'] = []
        if self.bind_list is not None:
            for k in self.bind_list:
                result['BindList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        self.bind_list = []
        if m.get('BindList') is not None:
            for k in m.get('BindList'):
                temp_model = DescribeWebLockBindListResponseBodyBindList()
                self.bind_list.append(temp_model.from_map(k))
        return self


class DescribeWebLockBindListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeWebLockBindListResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeWebLockBindListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeWebLockConfigListRequest(TeaModel):
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


class DescribeWebLockConfigListResponseBodyConfigList(TeaModel):
    def __init__(
        self,
        exclusive_dir: str = None,
        uuid: str = None,
        inclusive_file_type: str = None,
        defence_mode: str = None,
        exclusive_file_type: str = None,
        inclusive_file: str = None,
        mode: str = None,
        dir: str = None,
        exclusive_file: str = None,
        id: str = None,
        local_backup_dir: str = None,
    ):
        self.exclusive_dir = exclusive_dir
        self.uuid = uuid
        self.inclusive_file_type = inclusive_file_type
        self.defence_mode = defence_mode
        self.exclusive_file_type = exclusive_file_type
        self.inclusive_file = inclusive_file
        self.mode = mode
        self.dir = dir
        self.exclusive_file = exclusive_file
        self.id = id
        self.local_backup_dir = local_backup_dir

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.exclusive_dir is not None:
            result['ExclusiveDir'] = self.exclusive_dir
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        if self.inclusive_file_type is not None:
            result['InclusiveFileType'] = self.inclusive_file_type
        if self.defence_mode is not None:
            result['DefenceMode'] = self.defence_mode
        if self.exclusive_file_type is not None:
            result['ExclusiveFileType'] = self.exclusive_file_type
        if self.inclusive_file is not None:
            result['InclusiveFile'] = self.inclusive_file
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.dir is not None:
            result['Dir'] = self.dir
        if self.exclusive_file is not None:
            result['ExclusiveFile'] = self.exclusive_file
        if self.id is not None:
            result['Id'] = self.id
        if self.local_backup_dir is not None:
            result['LocalBackupDir'] = self.local_backup_dir
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExclusiveDir') is not None:
            self.exclusive_dir = m.get('ExclusiveDir')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        if m.get('InclusiveFileType') is not None:
            self.inclusive_file_type = m.get('InclusiveFileType')
        if m.get('DefenceMode') is not None:
            self.defence_mode = m.get('DefenceMode')
        if m.get('ExclusiveFileType') is not None:
            self.exclusive_file_type = m.get('ExclusiveFileType')
        if m.get('InclusiveFile') is not None:
            self.inclusive_file = m.get('InclusiveFile')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('Dir') is not None:
            self.dir = m.get('Dir')
        if m.get('ExclusiveFile') is not None:
            self.exclusive_file = m.get('ExclusiveFile')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('LocalBackupDir') is not None:
            self.local_backup_dir = m.get('LocalBackupDir')
        return self


class DescribeWebLockConfigListResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        request_id: str = None,
        config_list: List[DescribeWebLockConfigListResponseBodyConfigList] = None,
    ):
        self.total_count = total_count
        self.request_id = request_id
        self.config_list = config_list

    def validate(self):
        if self.config_list:
            for k in self.config_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['ConfigList'] = []
        if self.config_list is not None:
            for k in self.config_list:
                result['ConfigList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.config_list = []
        if m.get('ConfigList') is not None:
            for k in m.get('ConfigList'):
                temp_model = DescribeWebLockConfigListResponseBodyConfigList()
                self.config_list.append(temp_model.from_map(k))
        return self


class DescribeWebLockConfigListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeWebLockConfigListResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeWebLockConfigListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ExportRecordRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        params: str = None,
        export_type: str = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.params = params
        self.export_type = export_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.params is not None:
            result['Params'] = self.params
        if self.export_type is not None:
            result['ExportType'] = self.export_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('Params') is not None:
            self.params = m.get('Params')
        if m.get('ExportType') is not None:
            self.export_type = m.get('ExportType')
        return self


class ExportRecordResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        file_name: str = None,
        id: int = None,
    ):
        self.request_id = request_id
        self.file_name = file_name
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class ExportRecordResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ExportRecordResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ExportRecordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class FixCheckWarningsRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        risk_id: int = None,
        check_params: str = None,
        uuids: str = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.risk_id = risk_id
        self.check_params = check_params
        self.uuids = uuids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.risk_id is not None:
            result['RiskId'] = self.risk_id
        if self.check_params is not None:
            result['CheckParams'] = self.check_params
        if self.uuids is not None:
            result['Uuids'] = self.uuids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('RiskId') is not None:
            self.risk_id = m.get('RiskId')
        if m.get('CheckParams') is not None:
            self.check_params = m.get('CheckParams')
        if m.get('Uuids') is not None:
            self.uuids = m.get('Uuids')
        return self


class FixCheckWarningsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        batch_id: int = None,
    ):
        self.request_id = request_id
        self.batch_id = batch_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.batch_id is not None:
            result['BatchId'] = self.batch_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('BatchId') is not None:
            self.batch_id = m.get('BatchId')
        return self


class FixCheckWarningsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: FixCheckWarningsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = FixCheckWarningsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetIncIOCsRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        type: str = None,
        date: str = None,
    ):
        self.source_ip = source_ip
        self.type = type
        self.date = date

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.type is not None:
            result['Type'] = self.type
        if self.date is not None:
            result['Date'] = self.date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Date') is not None:
            self.date = m.get('Date')
        return self


class GetIncIOCsResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.data is not None:
            result['data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetIncIOCsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetIncIOCsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetIncIOCsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetIOCsRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        type: str = None,
        date: str = None,
    ):
        self.source_ip = source_ip
        self.type = type
        self.date = date

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.type is not None:
            result['Type'] = self.type
        if self.date is not None:
            result['Date'] = self.date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Date') is not None:
            self.date = m.get('Date')
        return self


class GetIOCsResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.data is not None:
            result['data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetIOCsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetIOCsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetIOCsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class HandleSecurityEventsRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        resource_owner_id: int = None,
        operation_code: str = None,
        operation_params: str = None,
        mark_miss_param: str = None,
        security_event_ids: List[str] = None,
    ):
        self.source_ip = source_ip
        self.resource_owner_id = resource_owner_id
        self.operation_code = operation_code
        self.operation_params = operation_params
        self.mark_miss_param = mark_miss_param
        self.security_event_ids = security_event_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.operation_code is not None:
            result['OperationCode'] = self.operation_code
        if self.operation_params is not None:
            result['OperationParams'] = self.operation_params
        if self.mark_miss_param is not None:
            result['MarkMissParam'] = self.mark_miss_param
        if self.security_event_ids is not None:
            result['SecurityEventIds'] = self.security_event_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OperationCode') is not None:
            self.operation_code = m.get('OperationCode')
        if m.get('OperationParams') is not None:
            self.operation_params = m.get('OperationParams')
        if m.get('MarkMissParam') is not None:
            self.mark_miss_param = m.get('MarkMissParam')
        if m.get('SecurityEventIds') is not None:
            self.security_event_ids = m.get('SecurityEventIds')
        return self


class HandleSecurityEventsResponseBodyHandleSecurityEventsResponse(TeaModel):
    def __init__(
        self,
        task_id: int = None,
    ):
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class HandleSecurityEventsResponseBody(TeaModel):
    def __init__(
        self,
        handle_security_events_response: HandleSecurityEventsResponseBodyHandleSecurityEventsResponse = None,
        request_id: str = None,
    ):
        self.handle_security_events_response = handle_security_events_response
        self.request_id = request_id

    def validate(self):
        if self.handle_security_events_response:
            self.handle_security_events_response.validate()

    def to_map(self):
        result = dict()
        if self.handle_security_events_response is not None:
            result['HandleSecurityEventsResponse'] = self.handle_security_events_response.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HandleSecurityEventsResponse') is not None:
            temp_model = HandleSecurityEventsResponseBodyHandleSecurityEventsResponse()
            self.handle_security_events_response = temp_model.from_map(m['HandleSecurityEventsResponse'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class HandleSecurityEventsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: HandleSecurityEventsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = HandleSecurityEventsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class HandleSimilarSecurityEventsRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        resource_owner_id: int = None,
        task_id: int = None,
        operation_code: str = None,
        operation_params: str = None,
        mark_miss_param: str = None,
    ):
        self.source_ip = source_ip
        self.resource_owner_id = resource_owner_id
        self.task_id = task_id
        self.operation_code = operation_code
        self.operation_params = operation_params
        self.mark_miss_param = mark_miss_param

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.operation_code is not None:
            result['OperationCode'] = self.operation_code
        if self.operation_params is not None:
            result['OperationParams'] = self.operation_params
        if self.mark_miss_param is not None:
            result['MarkMissParam'] = self.mark_miss_param
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('OperationCode') is not None:
            self.operation_code = m.get('OperationCode')
        if m.get('OperationParams') is not None:
            self.operation_params = m.get('OperationParams')
        if m.get('MarkMissParam') is not None:
            self.mark_miss_param = m.get('MarkMissParam')
        return self


class HandleSimilarSecurityEventsResponseBody(TeaModel):
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


class HandleSimilarSecurityEventsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: HandleSimilarSecurityEventsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = HandleSimilarSecurityEventsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class IgnoreHcCheckWarningsRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        check_warning_ids: str = None,
        check_ids: str = None,
        risk_id: str = None,
        type: int = None,
        reason: str = None,
    ):
        self.source_ip = source_ip
        self.check_warning_ids = check_warning_ids
        self.check_ids = check_ids
        self.risk_id = risk_id
        self.type = type
        self.reason = reason

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.check_warning_ids is not None:
            result['CheckWarningIds'] = self.check_warning_ids
        if self.check_ids is not None:
            result['CheckIds'] = self.check_ids
        if self.risk_id is not None:
            result['RiskId'] = self.risk_id
        if self.type is not None:
            result['Type'] = self.type
        if self.reason is not None:
            result['Reason'] = self.reason
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('CheckWarningIds') is not None:
            self.check_warning_ids = m.get('CheckWarningIds')
        if m.get('CheckIds') is not None:
            self.check_ids = m.get('CheckIds')
        if m.get('RiskId') is not None:
            self.risk_id = m.get('RiskId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        return self


class IgnoreHcCheckWarningsResponseBody(TeaModel):
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


class IgnoreHcCheckWarningsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: IgnoreHcCheckWarningsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = IgnoreHcCheckWarningsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyAntiBruteForceRuleRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        resource_owner_id: int = None,
        id: int = None,
        name: str = None,
        span: int = None,
        fail_count: int = None,
        forbidden_time: int = None,
        enable_smart_rule: bool = None,
        default_rule: bool = None,
        uuid_list: List[str] = None,
    ):
        self.source_ip = source_ip
        self.resource_owner_id = resource_owner_id
        self.id = id
        self.name = name
        self.span = span
        self.fail_count = fail_count
        self.forbidden_time = forbidden_time
        self.enable_smart_rule = enable_smart_rule
        self.default_rule = default_rule
        self.uuid_list = uuid_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.span is not None:
            result['Span'] = self.span
        if self.fail_count is not None:
            result['FailCount'] = self.fail_count
        if self.forbidden_time is not None:
            result['ForbiddenTime'] = self.forbidden_time
        if self.enable_smart_rule is not None:
            result['EnableSmartRule'] = self.enable_smart_rule
        if self.default_rule is not None:
            result['DefaultRule'] = self.default_rule
        if self.uuid_list is not None:
            result['UuidList'] = self.uuid_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Span') is not None:
            self.span = m.get('Span')
        if m.get('FailCount') is not None:
            self.fail_count = m.get('FailCount')
        if m.get('ForbiddenTime') is not None:
            self.forbidden_time = m.get('ForbiddenTime')
        if m.get('EnableSmartRule') is not None:
            self.enable_smart_rule = m.get('EnableSmartRule')
        if m.get('DefaultRule') is not None:
            self.default_rule = m.get('DefaultRule')
        if m.get('UuidList') is not None:
            self.uuid_list = m.get('UuidList')
        return self


class ModifyAntiBruteForceRuleResponseBody(TeaModel):
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


class ModifyAntiBruteForceRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyAntiBruteForceRuleResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyAntiBruteForceRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyCreateVulWhitelistRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        whitelist: str = None,
        reason: str = None,
    ):
        self.source_ip = source_ip
        self.whitelist = whitelist
        self.reason = reason

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.whitelist is not None:
            result['Whitelist'] = self.whitelist
        if self.reason is not None:
            result['Reason'] = self.reason
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Whitelist') is not None:
            self.whitelist = m.get('Whitelist')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        return self


class ModifyCreateVulWhitelistResponseBody(TeaModel):
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


class ModifyCreateVulWhitelistResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyCreateVulWhitelistResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyCreateVulWhitelistResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyEmgVulSubmitRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        name: str = None,
        user_agreement: str = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.name = name
        self.user_agreement = user_agreement

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.name is not None:
            result['Name'] = self.name
        if self.user_agreement is not None:
            result['UserAgreement'] = self.user_agreement
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('UserAgreement') is not None:
            self.user_agreement = m.get('UserAgreement')
        return self


class ModifyEmgVulSubmitResponseBody(TeaModel):
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


class ModifyEmgVulSubmitResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyEmgVulSubmitResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyEmgVulSubmitResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyGroupPropertyRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        data: str = None,
    ):
        self.source_ip = source_ip
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.data is not None:
            result['Data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        return self


class ModifyGroupPropertyResponseBody(TeaModel):
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


class ModifyGroupPropertyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyGroupPropertyResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyGroupPropertyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyInstanceAntiBruteForceRuleRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        resource_owner_id: int = None,
        uuid: str = None,
        new_rule_id: int = None,
    ):
        self.source_ip = source_ip
        self.resource_owner_id = resource_owner_id
        self.uuid = uuid
        self.new_rule_id = new_rule_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        if self.new_rule_id is not None:
            result['NewRuleId'] = self.new_rule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        if m.get('NewRuleId') is not None:
            self.new_rule_id = m.get('NewRuleId')
        return self


class ModifyInstanceAntiBruteForceRuleResponseBody(TeaModel):
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


class ModifyInstanceAntiBruteForceRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyInstanceAntiBruteForceRuleResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyInstanceAntiBruteForceRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyLoginBaseConfigRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        type: str = None,
        config: str = None,
        target: str = None,
    ):
        self.source_ip = source_ip
        self.type = type
        self.config = config
        self.target = target

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.type is not None:
            result['Type'] = self.type
        if self.config is not None:
            result['Config'] = self.config
        if self.target is not None:
            result['Target'] = self.target
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Config') is not None:
            self.config = m.get('Config')
        if m.get('Target') is not None:
            self.target = m.get('Target')
        return self


class ModifyLoginBaseConfigResponseBody(TeaModel):
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


class ModifyLoginBaseConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyLoginBaseConfigResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyLoginBaseConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyLoginSwitchConfigRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        item: str = None,
        status: int = None,
    ):
        self.source_ip = source_ip
        self.item = item
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.item is not None:
            result['Item'] = self.item
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Item') is not None:
            self.item = m.get('Item')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ModifyLoginSwitchConfigResponseBody(TeaModel):
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


class ModifyLoginSwitchConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyLoginSwitchConfigResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyLoginSwitchConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyNoticeConfigRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        route: int = None,
        project: str = None,
        time_limit: int = None,
    ):
        self.source_ip = source_ip
        self.route = route
        self.project = project
        self.time_limit = time_limit

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.route is not None:
            result['Route'] = self.route
        if self.project is not None:
            result['Project'] = self.project
        if self.time_limit is not None:
            result['TimeLimit'] = self.time_limit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Route') is not None:
            self.route = m.get('Route')
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('TimeLimit') is not None:
            self.time_limit = m.get('TimeLimit')
        return self


class ModifyNoticeConfigResponseBody(TeaModel):
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


class ModifyNoticeConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyNoticeConfigResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyNoticeConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyOperateVulRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        info: str = None,
        operate_type: str = None,
        type: str = None,
        reason: str = None,
    ):
        self.source_ip = source_ip
        self.info = info
        self.operate_type = operate_type
        self.type = type
        self.reason = reason

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.info is not None:
            result['Info'] = self.info
        if self.operate_type is not None:
            result['OperateType'] = self.operate_type
        if self.type is not None:
            result['Type'] = self.type
        if self.reason is not None:
            result['Reason'] = self.reason
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Info') is not None:
            self.info = m.get('Info')
        if m.get('OperateType') is not None:
            self.operate_type = m.get('OperateType')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        return self


class ModifyOperateVulResponseBody(TeaModel):
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


class ModifyOperateVulResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyOperateVulResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyOperateVulResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyPushAllTaskRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        uuids: str = None,
        tasks: str = None,
    ):
        self.source_ip = source_ip
        self.uuids = uuids
        self.tasks = tasks

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.uuids is not None:
            result['Uuids'] = self.uuids
        if self.tasks is not None:
            result['Tasks'] = self.tasks
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Uuids') is not None:
            self.uuids = m.get('Uuids')
        if m.get('Tasks') is not None:
            self.tasks = m.get('Tasks')
        return self


class ModifyPushAllTaskResponseBodyPushTaskRspPushTaskResultList(TeaModel):
    def __init__(
        self,
        uuid: str = None,
        group_id: int = None,
        success: bool = None,
        region: str = None,
        instance_name: str = None,
        online: bool = None,
        message: str = None,
        ip: str = None,
        os_version: str = None,
        instance_id: str = None,
    ):
        self.uuid = uuid
        self.group_id = group_id
        self.success = success
        self.region = region
        self.instance_name = instance_name
        self.online = online
        self.message = message
        self.ip = ip
        self.os_version = os_version
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.success is not None:
            result['Success'] = self.success
        if self.region is not None:
            result['Region'] = self.region
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.online is not None:
            result['Online'] = self.online
        if self.message is not None:
            result['Message'] = self.message
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.os_version is not None:
            result['OsVersion'] = self.os_version
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('Online') is not None:
            self.online = m.get('Online')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('OsVersion') is not None:
            self.os_version = m.get('OsVersion')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class ModifyPushAllTaskResponseBodyPushTaskRsp(TeaModel):
    def __init__(
        self,
        push_task_result_list: List[ModifyPushAllTaskResponseBodyPushTaskRspPushTaskResultList] = None,
    ):
        self.push_task_result_list = push_task_result_list

    def validate(self):
        if self.push_task_result_list:
            for k in self.push_task_result_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['PushTaskResultList'] = []
        if self.push_task_result_list is not None:
            for k in self.push_task_result_list:
                result['PushTaskResultList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.push_task_result_list = []
        if m.get('PushTaskResultList') is not None:
            for k in m.get('PushTaskResultList'):
                temp_model = ModifyPushAllTaskResponseBodyPushTaskRspPushTaskResultList()
                self.push_task_result_list.append(temp_model.from_map(k))
        return self


class ModifyPushAllTaskResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        push_task_rsp: ModifyPushAllTaskResponseBodyPushTaskRsp = None,
    ):
        self.request_id = request_id
        self.push_task_rsp = push_task_rsp

    def validate(self):
        if self.push_task_rsp:
            self.push_task_rsp.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.push_task_rsp is not None:
            result['PushTaskRsp'] = self.push_task_rsp.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PushTaskRsp') is not None:
            temp_model = ModifyPushAllTaskResponseBodyPushTaskRsp()
            self.push_task_rsp = temp_model.from_map(m['PushTaskRsp'])
        return self


class ModifyPushAllTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyPushAllTaskResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyPushAllTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyRiskCheckStatusRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        resource_owner_id: int = None,
        lang: str = None,
        item_id: int = None,
        task_id: int = None,
        status: str = None,
    ):
        self.source_ip = source_ip
        self.resource_owner_id = resource_owner_id
        self.lang = lang
        self.item_id = item_id
        self.task_id = task_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ModifyRiskCheckStatusResponseBody(TeaModel):
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


class ModifyRiskCheckStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyRiskCheckStatusResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyRiskCheckStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyRiskSingleResultStatusRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        resource_owner_id: int = None,
        lang: str = None,
        status: str = None,
        task_id: int = None,
        ids: List[str] = None,
    ):
        self.source_ip = source_ip
        self.resource_owner_id = resource_owner_id
        self.lang = lang
        self.status = status
        self.task_id = task_id
        self.ids = ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.status is not None:
            result['Status'] = self.status
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.ids is not None:
            result['Ids'] = self.ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('Ids') is not None:
            self.ids = m.get('Ids')
        return self


class ModifyRiskSingleResultStatusResponseBody(TeaModel):
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


class ModifyRiskSingleResultStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyRiskSingleResultStatusResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyRiskSingleResultStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifySecurityCheckScheduleConfigRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        resource_owner_id: int = None,
        lang: str = None,
        days_of_week: str = None,
        start_time: int = None,
        end_time: int = None,
    ):
        self.source_ip = source_ip
        self.resource_owner_id = resource_owner_id
        self.lang = lang
        self.days_of_week = days_of_week
        self.start_time = start_time
        self.end_time = end_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.days_of_week is not None:
            result['DaysOfWeek'] = self.days_of_week
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('DaysOfWeek') is not None:
            self.days_of_week = m.get('DaysOfWeek')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        return self


class ModifySecurityCheckScheduleConfigResponseBody(TeaModel):
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


class ModifySecurityCheckScheduleConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifySecurityCheckScheduleConfigResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifySecurityCheckScheduleConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyStartVulScanRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        types: str = None,
        uuids: str = None,
    ):
        self.source_ip = source_ip
        self.types = types
        self.uuids = uuids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.types is not None:
            result['Types'] = self.types
        if self.uuids is not None:
            result['Uuids'] = self.uuids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Types') is not None:
            self.types = m.get('Types')
        if m.get('Uuids') is not None:
            self.uuids = m.get('Uuids')
        return self


class ModifyStartVulScanResponseBody(TeaModel):
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


class ModifyStartVulScanResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyStartVulScanResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyStartVulScanResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyTagWithUuidRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        uuid_list: str = None,
        tag_list: str = None,
        tag_id: str = None,
        machine_types: str = None,
    ):
        self.source_ip = source_ip
        self.uuid_list = uuid_list
        self.tag_list = tag_list
        self.tag_id = tag_id
        self.machine_types = machine_types

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.uuid_list is not None:
            result['UuidList'] = self.uuid_list
        if self.tag_list is not None:
            result['TagList'] = self.tag_list
        if self.tag_id is not None:
            result['TagId'] = self.tag_id
        if self.machine_types is not None:
            result['MachineTypes'] = self.machine_types
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('UuidList') is not None:
            self.uuid_list = m.get('UuidList')
        if m.get('TagList') is not None:
            self.tag_list = m.get('TagList')
        if m.get('TagId') is not None:
            self.tag_id = m.get('TagId')
        if m.get('MachineTypes') is not None:
            self.machine_types = m.get('MachineTypes')
        return self


class ModifyTagWithUuidResponseBody(TeaModel):
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


class ModifyTagWithUuidResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyTagWithUuidResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyTagWithUuidResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyVpcHoneyPotRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        vpc_id: str = None,
        honey_pot_action: str = None,
    ):
        self.source_ip = source_ip
        self.vpc_id = vpc_id
        self.honey_pot_action = honey_pot_action

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.honey_pot_action is not None:
            result['HoneyPotAction'] = self.honey_pot_action
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('HoneyPotAction') is not None:
            self.honey_pot_action = m.get('HoneyPotAction')
        return self


class ModifyVpcHoneyPotResponseBody(TeaModel):
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


class ModifyVpcHoneyPotResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyVpcHoneyPotResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyVpcHoneyPotResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyVulTargetConfigRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        type: str = None,
        uuid: str = None,
        config: str = None,
    ):
        self.source_ip = source_ip
        self.type = type
        self.uuid = uuid
        self.config = config

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.type is not None:
            result['Type'] = self.type
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        if self.config is not None:
            result['Config'] = self.config
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        if m.get('Config') is not None:
            self.config = m.get('Config')
        return self


class ModifyVulTargetConfigResponseBody(TeaModel):
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


class ModifyVulTargetConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyVulTargetConfigResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyVulTargetConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyWebLockCreateConfigRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        uuid: str = None,
        dir: str = None,
        exclusive_dir: str = None,
        exclusive_file_type: str = None,
        local_backup_dir: str = None,
        mode: str = None,
        inclusive_file_type: str = None,
        exclusive_file: str = None,
        inclusive_file: str = None,
        defence_mode: str = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.uuid = uuid
        self.dir = dir
        self.exclusive_dir = exclusive_dir
        self.exclusive_file_type = exclusive_file_type
        self.local_backup_dir = local_backup_dir
        self.mode = mode
        self.inclusive_file_type = inclusive_file_type
        self.exclusive_file = exclusive_file
        self.inclusive_file = inclusive_file
        self.defence_mode = defence_mode

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
        if self.dir is not None:
            result['Dir'] = self.dir
        if self.exclusive_dir is not None:
            result['ExclusiveDir'] = self.exclusive_dir
        if self.exclusive_file_type is not None:
            result['ExclusiveFileType'] = self.exclusive_file_type
        if self.local_backup_dir is not None:
            result['LocalBackupDir'] = self.local_backup_dir
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.inclusive_file_type is not None:
            result['InclusiveFileType'] = self.inclusive_file_type
        if self.exclusive_file is not None:
            result['ExclusiveFile'] = self.exclusive_file
        if self.inclusive_file is not None:
            result['InclusiveFile'] = self.inclusive_file
        if self.defence_mode is not None:
            result['DefenceMode'] = self.defence_mode
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        if m.get('Dir') is not None:
            self.dir = m.get('Dir')
        if m.get('ExclusiveDir') is not None:
            self.exclusive_dir = m.get('ExclusiveDir')
        if m.get('ExclusiveFileType') is not None:
            self.exclusive_file_type = m.get('ExclusiveFileType')
        if m.get('LocalBackupDir') is not None:
            self.local_backup_dir = m.get('LocalBackupDir')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('InclusiveFileType') is not None:
            self.inclusive_file_type = m.get('InclusiveFileType')
        if m.get('ExclusiveFile') is not None:
            self.exclusive_file = m.get('ExclusiveFile')
        if m.get('InclusiveFile') is not None:
            self.inclusive_file = m.get('InclusiveFile')
        if m.get('DefenceMode') is not None:
            self.defence_mode = m.get('DefenceMode')
        return self


class ModifyWebLockCreateConfigResponseBody(TeaModel):
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


class ModifyWebLockCreateConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyWebLockCreateConfigResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyWebLockCreateConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyWebLockDeleteConfigRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        id: int = None,
        uuid: str = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.id = id
        self.uuid = uuid

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
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        return self


class ModifyWebLockDeleteConfigResponseBody(TeaModel):
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


class ModifyWebLockDeleteConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyWebLockDeleteConfigResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyWebLockDeleteConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyWebLockStartRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        mode: str = None,
        local_backup_dir: str = None,
        exclusive_file: str = None,
        dir: str = None,
        inclusive_file_type: str = None,
        uuid: str = None,
        exclusive_file_type: str = None,
        exclusive_dir: str = None,
        defence_mode: str = None,
    ):
        self.source_ip = source_ip
        self.mode = mode
        self.local_backup_dir = local_backup_dir
        self.exclusive_file = exclusive_file
        self.dir = dir
        self.inclusive_file_type = inclusive_file_type
        self.uuid = uuid
        self.exclusive_file_type = exclusive_file_type
        self.exclusive_dir = exclusive_dir
        self.defence_mode = defence_mode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.local_backup_dir is not None:
            result['LocalBackupDir'] = self.local_backup_dir
        if self.exclusive_file is not None:
            result['ExclusiveFile'] = self.exclusive_file
        if self.dir is not None:
            result['Dir'] = self.dir
        if self.inclusive_file_type is not None:
            result['InclusiveFileType'] = self.inclusive_file_type
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        if self.exclusive_file_type is not None:
            result['ExclusiveFileType'] = self.exclusive_file_type
        if self.exclusive_dir is not None:
            result['ExclusiveDir'] = self.exclusive_dir
        if self.defence_mode is not None:
            result['DefenceMode'] = self.defence_mode
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('LocalBackupDir') is not None:
            self.local_backup_dir = m.get('LocalBackupDir')
        if m.get('ExclusiveFile') is not None:
            self.exclusive_file = m.get('ExclusiveFile')
        if m.get('Dir') is not None:
            self.dir = m.get('Dir')
        if m.get('InclusiveFileType') is not None:
            self.inclusive_file_type = m.get('InclusiveFileType')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        if m.get('ExclusiveFileType') is not None:
            self.exclusive_file_type = m.get('ExclusiveFileType')
        if m.get('ExclusiveDir') is not None:
            self.exclusive_dir = m.get('ExclusiveDir')
        if m.get('DefenceMode') is not None:
            self.defence_mode = m.get('DefenceMode')
        return self


class ModifyWebLockStartResponseBody(TeaModel):
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


class ModifyWebLockStartResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyWebLockStartResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyWebLockStartResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyWebLockUnbindRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        uuid: str = None,
    ):
        self.source_ip = source_ip
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        return self


class ModifyWebLockUnbindResponseBody(TeaModel):
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


class ModifyWebLockUnbindResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyWebLockUnbindResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyWebLockUnbindResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyWebLockUpdateConfigRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        id: int = None,
        uuid: str = None,
        dir: str = None,
        exclusive_dir: str = None,
        exclusive_file_type: str = None,
        local_backup_dir: str = None,
        mode: str = None,
        inclusive_file_type: str = None,
        exclusive_file: str = None,
        inclusive_file: str = None,
        defence_mode: str = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.id = id
        self.uuid = uuid
        self.dir = dir
        self.exclusive_dir = exclusive_dir
        self.exclusive_file_type = exclusive_file_type
        self.local_backup_dir = local_backup_dir
        self.mode = mode
        self.inclusive_file_type = inclusive_file_type
        self.exclusive_file = exclusive_file
        self.inclusive_file = inclusive_file
        self.defence_mode = defence_mode

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
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        if self.dir is not None:
            result['Dir'] = self.dir
        if self.exclusive_dir is not None:
            result['ExclusiveDir'] = self.exclusive_dir
        if self.exclusive_file_type is not None:
            result['ExclusiveFileType'] = self.exclusive_file_type
        if self.local_backup_dir is not None:
            result['LocalBackupDir'] = self.local_backup_dir
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.inclusive_file_type is not None:
            result['InclusiveFileType'] = self.inclusive_file_type
        if self.exclusive_file is not None:
            result['ExclusiveFile'] = self.exclusive_file
        if self.inclusive_file is not None:
            result['InclusiveFile'] = self.inclusive_file
        if self.defence_mode is not None:
            result['DefenceMode'] = self.defence_mode
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        if m.get('Dir') is not None:
            self.dir = m.get('Dir')
        if m.get('ExclusiveDir') is not None:
            self.exclusive_dir = m.get('ExclusiveDir')
        if m.get('ExclusiveFileType') is not None:
            self.exclusive_file_type = m.get('ExclusiveFileType')
        if m.get('LocalBackupDir') is not None:
            self.local_backup_dir = m.get('LocalBackupDir')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('InclusiveFileType') is not None:
            self.inclusive_file_type = m.get('InclusiveFileType')
        if m.get('ExclusiveFile') is not None:
            self.exclusive_file = m.get('ExclusiveFile')
        if m.get('InclusiveFile') is not None:
            self.inclusive_file = m.get('InclusiveFile')
        if m.get('DefenceMode') is not None:
            self.defence_mode = m.get('DefenceMode')
        return self


class ModifyWebLockUpdateConfigResponseBody(TeaModel):
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


class ModifyWebLockUpdateConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyWebLockUpdateConfigResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyWebLockUpdateConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OperateSuspiciousTargetConfigRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        type: str = None,
        target_type: str = None,
        target_operations: str = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.type = type
        self.target_type = target_type
        self.target_operations = target_operations

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.type is not None:
            result['Type'] = self.type
        if self.target_type is not None:
            result['TargetType'] = self.target_type
        if self.target_operations is not None:
            result['TargetOperations'] = self.target_operations
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')
        if m.get('TargetOperations') is not None:
            self.target_operations = m.get('TargetOperations')
        return self


class OperateSuspiciousTargetConfigResponseBody(TeaModel):
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


class OperateSuspiciousTargetConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: OperateSuspiciousTargetConfigResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = OperateSuspiciousTargetConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OperationSuspEventsRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        suspicious_event_ids: str = None,
        operation: str = None,
        sub_operation: str = None,
        from_: str = None,
        warn_type: str = None,
    ):
        self.source_ip = source_ip
        self.suspicious_event_ids = suspicious_event_ids
        self.operation = operation
        self.sub_operation = sub_operation
        self.from_ = from_
        self.warn_type = warn_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.suspicious_event_ids is not None:
            result['SuspiciousEventIds'] = self.suspicious_event_ids
        if self.operation is not None:
            result['Operation'] = self.operation
        if self.sub_operation is not None:
            result['SubOperation'] = self.sub_operation
        if self.from_ is not None:
            result['From'] = self.from_
        if self.warn_type is not None:
            result['WarnType'] = self.warn_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('SuspiciousEventIds') is not None:
            self.suspicious_event_ids = m.get('SuspiciousEventIds')
        if m.get('Operation') is not None:
            self.operation = m.get('Operation')
        if m.get('SubOperation') is not None:
            self.sub_operation = m.get('SubOperation')
        if m.get('From') is not None:
            self.from_ = m.get('From')
        if m.get('WarnType') is not None:
            self.warn_type = m.get('WarnType')
        return self


class OperationSuspEventsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        access_code: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.access_code = access_code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.access_code is not None:
            result['AccessCode'] = self.access_code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('AccessCode') is not None:
            self.access_code = m.get('AccessCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class OperationSuspEventsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: OperationSuspEventsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = OperationSuspEventsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PauseClientRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        uuids: str = None,
        value: str = None,
        app_name: str = None,
    ):
        self.source_ip = source_ip
        self.uuids = uuids
        self.value = value
        self.app_name = app_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.uuids is not None:
            result['Uuids'] = self.uuids
        if self.value is not None:
            result['Value'] = self.value
        if self.app_name is not None:
            result['AppName'] = self.app_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Uuids') is not None:
            self.uuids = m.get('Uuids')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        return self


class PauseClientResponseBody(TeaModel):
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


class PauseClientResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: PauseClientResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = PauseClientResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RefreshContainerAssetsRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        asset_type: str = None,
    ):
        self.source_ip = source_ip
        self.asset_type = asset_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.asset_type is not None:
            result['AssetType'] = self.asset_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('AssetType') is not None:
            self.asset_type = m.get('AssetType')
        return self


class RefreshContainerAssetsResponseBody(TeaModel):
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


class RefreshContainerAssetsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RefreshContainerAssetsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = RefreshContainerAssetsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RollbackSuspEventQuaraFileRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        quara_file_id: int = None,
        from_: str = None,
    ):
        self.source_ip = source_ip
        self.quara_file_id = quara_file_id
        self.from_ = from_

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.quara_file_id is not None:
            result['QuaraFileId'] = self.quara_file_id
        if self.from_ is not None:
            result['From'] = self.from_
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('QuaraFileId') is not None:
            self.quara_file_id = m.get('QuaraFileId')
        if m.get('From') is not None:
            self.from_ = m.get('From')
        return self


class RollbackSuspEventQuaraFileResponseBody(TeaModel):
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


class RollbackSuspEventQuaraFileResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RollbackSuspEventQuaraFileResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = RollbackSuspEventQuaraFileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SasInstallCodeRequest(TeaModel):
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


class SasInstallCodeResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.data is not None:
            result['data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SasInstallCodeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SasInstallCodeResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = SasInstallCodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartBaselineSecurityCheckRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        resource_owner_id: int = None,
        lang: str = None,
        type: str = None,
        item_ids: List[int] = None,
        assets: List[str] = None,
    ):
        self.source_ip = source_ip
        self.resource_owner_id = resource_owner_id
        self.lang = lang
        self.type = type
        self.item_ids = item_ids
        self.assets = assets

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.type is not None:
            result['Type'] = self.type
        if self.item_ids is not None:
            result['ItemIds'] = self.item_ids
        if self.assets is not None:
            result['Assets'] = self.assets
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('ItemIds') is not None:
            self.item_ids = m.get('ItemIds')
        if m.get('Assets') is not None:
            self.assets = m.get('Assets')
        return self


class StartBaselineSecurityCheckResponseBody(TeaModel):
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


class StartBaselineSecurityCheckResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: StartBaselineSecurityCheckResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = StartBaselineSecurityCheckResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartImageVulScanRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        repo_region_id: str = None,
        repo_instance_id: str = None,
        repo_id: str = None,
        rep_name: str = None,
        repo_namespace: str = None,
        image_tag: str = None,
        image_digest: str = None,
        image_layer: str = None,
        registry_types: List[str] = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.repo_region_id = repo_region_id
        self.repo_instance_id = repo_instance_id
        self.repo_id = repo_id
        self.rep_name = rep_name
        self.repo_namespace = repo_namespace
        self.image_tag = image_tag
        self.image_digest = image_digest
        self.image_layer = image_layer
        self.registry_types = registry_types

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.repo_region_id is not None:
            result['RepoRegionId'] = self.repo_region_id
        if self.repo_instance_id is not None:
            result['RepoInstanceId'] = self.repo_instance_id
        if self.repo_id is not None:
            result['RepoId'] = self.repo_id
        if self.rep_name is not None:
            result['RepName'] = self.rep_name
        if self.repo_namespace is not None:
            result['RepoNamespace'] = self.repo_namespace
        if self.image_tag is not None:
            result['ImageTag'] = self.image_tag
        if self.image_digest is not None:
            result['ImageDigest'] = self.image_digest
        if self.image_layer is not None:
            result['ImageLayer'] = self.image_layer
        if self.registry_types is not None:
            result['RegistryTypes'] = self.registry_types
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('RepoRegionId') is not None:
            self.repo_region_id = m.get('RepoRegionId')
        if m.get('RepoInstanceId') is not None:
            self.repo_instance_id = m.get('RepoInstanceId')
        if m.get('RepoId') is not None:
            self.repo_id = m.get('RepoId')
        if m.get('RepName') is not None:
            self.rep_name = m.get('RepName')
        if m.get('RepoNamespace') is not None:
            self.repo_namespace = m.get('RepoNamespace')
        if m.get('ImageTag') is not None:
            self.image_tag = m.get('ImageTag')
        if m.get('ImageDigest') is not None:
            self.image_digest = m.get('ImageDigest')
        if m.get('ImageLayer') is not None:
            self.image_layer = m.get('ImageLayer')
        if m.get('RegistryTypes') is not None:
            self.registry_types = m.get('RegistryTypes')
        return self


class StartImageVulScanResponseBody(TeaModel):
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


class StartImageVulScanResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: StartImageVulScanResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = StartImageVulScanResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ValidateHcWarningsRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        risk_ids: str = None,
        uuids: str = None,
    ):
        self.source_ip = source_ip
        self.risk_ids = risk_ids
        self.uuids = uuids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.risk_ids is not None:
            result['RiskIds'] = self.risk_ids
        if self.uuids is not None:
            result['Uuids'] = self.uuids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('RiskIds') is not None:
            self.risk_ids = m.get('RiskIds')
        if m.get('Uuids') is not None:
            self.uuids = m.get('Uuids')
        return self


class ValidateHcWarningsResponseBody(TeaModel):
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


class ValidateHcWarningsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ValidateHcWarningsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ValidateHcWarningsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


