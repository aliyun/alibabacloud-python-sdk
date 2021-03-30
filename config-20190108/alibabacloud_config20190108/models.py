# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict, Any


class ActiveConfigRulesRequest(TeaModel):
    def __init__(
        self,
        config_rule_ids: str = None,
    ):
        self.config_rule_ids = config_rule_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_rule_ids is not None:
            result['ConfigRuleIds'] = self.config_rule_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigRuleIds') is not None:
            self.config_rule_ids = m.get('ConfigRuleIds')
        return self


class ActiveConfigRulesResponseBodyOperateRuleResultOperateRuleItemList(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        success: bool = None,
        config_rule_id: str = None,
    ):
        self.error_code = error_code
        self.success = success
        self.config_rule_id = config_rule_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        if self.config_rule_id is not None:
            result['ConfigRuleId'] = self.config_rule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ConfigRuleId') is not None:
            self.config_rule_id = m.get('ConfigRuleId')
        return self


class ActiveConfigRulesResponseBodyOperateRuleResult(TeaModel):
    def __init__(
        self,
        operate_rule_item_list: List[ActiveConfigRulesResponseBodyOperateRuleResultOperateRuleItemList] = None,
    ):
        self.operate_rule_item_list = operate_rule_item_list

    def validate(self):
        if self.operate_rule_item_list:
            for k in self.operate_rule_item_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['OperateRuleItemList'] = []
        if self.operate_rule_item_list is not None:
            for k in self.operate_rule_item_list:
                result['OperateRuleItemList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.operate_rule_item_list = []
        if m.get('OperateRuleItemList') is not None:
            for k in m.get('OperateRuleItemList'):
                temp_model = ActiveConfigRulesResponseBodyOperateRuleResultOperateRuleItemList()
                self.operate_rule_item_list.append(temp_model.from_map(k))
        return self


class ActiveConfigRulesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        operate_rule_result: ActiveConfigRulesResponseBodyOperateRuleResult = None,
    ):
        self.request_id = request_id
        self.operate_rule_result = operate_rule_result

    def validate(self):
        if self.operate_rule_result:
            self.operate_rule_result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.operate_rule_result is not None:
            result['OperateRuleResult'] = self.operate_rule_result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('OperateRuleResult') is not None:
            temp_model = ActiveConfigRulesResponseBodyOperateRuleResult()
            self.operate_rule_result = temp_model.from_map(m['OperateRuleResult'])
        return self


class ActiveConfigRulesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ActiveConfigRulesResponseBody = None,
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
            temp_model = ActiveConfigRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteConfigRulesRequest(TeaModel):
    def __init__(
        self,
        config_rule_ids: str = None,
    ):
        self.config_rule_ids = config_rule_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_rule_ids is not None:
            result['ConfigRuleIds'] = self.config_rule_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigRuleIds') is not None:
            self.config_rule_ids = m.get('ConfigRuleIds')
        return self


class DeleteConfigRulesResponseBodyOperateRuleResultOperateRuleItemList(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        success: bool = None,
        config_rule_id: str = None,
    ):
        self.error_code = error_code
        self.success = success
        self.config_rule_id = config_rule_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        if self.config_rule_id is not None:
            result['ConfigRuleId'] = self.config_rule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ConfigRuleId') is not None:
            self.config_rule_id = m.get('ConfigRuleId')
        return self


class DeleteConfigRulesResponseBodyOperateRuleResult(TeaModel):
    def __init__(
        self,
        operate_rule_item_list: List[DeleteConfigRulesResponseBodyOperateRuleResultOperateRuleItemList] = None,
    ):
        self.operate_rule_item_list = operate_rule_item_list

    def validate(self):
        if self.operate_rule_item_list:
            for k in self.operate_rule_item_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['OperateRuleItemList'] = []
        if self.operate_rule_item_list is not None:
            for k in self.operate_rule_item_list:
                result['OperateRuleItemList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.operate_rule_item_list = []
        if m.get('OperateRuleItemList') is not None:
            for k in m.get('OperateRuleItemList'):
                temp_model = DeleteConfigRulesResponseBodyOperateRuleResultOperateRuleItemList()
                self.operate_rule_item_list.append(temp_model.from_map(k))
        return self


class DeleteConfigRulesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        operate_rule_result: DeleteConfigRulesResponseBodyOperateRuleResult = None,
    ):
        self.request_id = request_id
        self.operate_rule_result = operate_rule_result

    def validate(self):
        if self.operate_rule_result:
            self.operate_rule_result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.operate_rule_result is not None:
            result['OperateRuleResult'] = self.operate_rule_result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('OperateRuleResult') is not None:
            temp_model = DeleteConfigRulesResponseBodyOperateRuleResult()
            self.operate_rule_result = temp_model.from_map(m['OperateRuleResult'])
        return self


class DeleteConfigRulesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteConfigRulesResponseBody = None,
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
            temp_model = DeleteConfigRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeComplianceRequest(TeaModel):
    def __init__(
        self,
        resource_type: str = None,
        resource_id: str = None,
        compliance_type: str = None,
        config_rule_id: str = None,
        multi_account: bool = None,
        member_id: int = None,
    ):
        self.resource_type = resource_type
        self.resource_id = resource_id
        self.compliance_type = compliance_type
        self.config_rule_id = config_rule_id
        self.multi_account = multi_account
        self.member_id = member_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.compliance_type is not None:
            result['ComplianceType'] = self.compliance_type
        if self.config_rule_id is not None:
            result['ConfigRuleId'] = self.config_rule_id
        if self.multi_account is not None:
            result['MultiAccount'] = self.multi_account
        if self.member_id is not None:
            result['MemberId'] = self.member_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ComplianceType') is not None:
            self.compliance_type = m.get('ComplianceType')
        if m.get('ConfigRuleId') is not None:
            self.config_rule_id = m.get('ConfigRuleId')
        if m.get('MultiAccount') is not None:
            self.multi_account = m.get('MultiAccount')
        if m.get('MemberId') is not None:
            self.member_id = m.get('MemberId')
        return self


class DescribeComplianceResponseBodyComplianceResultCompliances(TeaModel):
    def __init__(
        self,
        compliance_type: str = None,
        count: int = None,
    ):
        self.compliance_type = compliance_type
        self.count = count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compliance_type is not None:
            result['ComplianceType'] = self.compliance_type
        if self.count is not None:
            result['Count'] = self.count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComplianceType') is not None:
            self.compliance_type = m.get('ComplianceType')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        return self


class DescribeComplianceResponseBodyComplianceResult(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        compliances: List[DescribeComplianceResponseBodyComplianceResultCompliances] = None,
    ):
        self.total_count = total_count
        self.compliances = compliances

    def validate(self):
        if self.compliances:
            for k in self.compliances:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['Compliances'] = []
        if self.compliances is not None:
            for k in self.compliances:
                result['Compliances'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.compliances = []
        if m.get('Compliances') is not None:
            for k in m.get('Compliances'):
                temp_model = DescribeComplianceResponseBodyComplianceResultCompliances()
                self.compliances.append(temp_model.from_map(k))
        return self


class DescribeComplianceResponseBody(TeaModel):
    def __init__(
        self,
        compliance_result: DescribeComplianceResponseBodyComplianceResult = None,
        request_id: str = None,
    ):
        self.compliance_result = compliance_result
        self.request_id = request_id

    def validate(self):
        if self.compliance_result:
            self.compliance_result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compliance_result is not None:
            result['ComplianceResult'] = self.compliance_result.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComplianceResult') is not None:
            temp_model = DescribeComplianceResponseBodyComplianceResult()
            self.compliance_result = temp_model.from_map(m['ComplianceResult'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeComplianceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeComplianceResponseBody = None,
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
            temp_model = DescribeComplianceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeComplianceSummaryRequest(TeaModel):
    def __init__(
        self,
        multi_account: bool = None,
        member_id: int = None,
    ):
        self.multi_account = multi_account
        self.member_id = member_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.multi_account is not None:
            result['MultiAccount'] = self.multi_account
        if self.member_id is not None:
            result['MemberId'] = self.member_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MultiAccount') is not None:
            self.multi_account = m.get('MultiAccount')
        if m.get('MemberId') is not None:
            self.member_id = m.get('MemberId')
        return self


class DescribeComplianceSummaryResponseBodyComplianceSummaryComplianceSummaryByResource(TeaModel):
    def __init__(
        self,
        compliant_count: int = None,
        non_compliant_count: int = None,
        compliance_summary_timestamp: int = None,
        total_count: int = None,
    ):
        self.compliant_count = compliant_count
        self.non_compliant_count = non_compliant_count
        self.compliance_summary_timestamp = compliance_summary_timestamp
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compliant_count is not None:
            result['CompliantCount'] = self.compliant_count
        if self.non_compliant_count is not None:
            result['NonCompliantCount'] = self.non_compliant_count
        if self.compliance_summary_timestamp is not None:
            result['ComplianceSummaryTimestamp'] = self.compliance_summary_timestamp
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompliantCount') is not None:
            self.compliant_count = m.get('CompliantCount')
        if m.get('NonCompliantCount') is not None:
            self.non_compliant_count = m.get('NonCompliantCount')
        if m.get('ComplianceSummaryTimestamp') is not None:
            self.compliance_summary_timestamp = m.get('ComplianceSummaryTimestamp')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeComplianceSummaryResponseBodyComplianceSummaryComplianceSummaryByConfigRule(TeaModel):
    def __init__(
        self,
        compliant_count: int = None,
        non_compliant_count: int = None,
        compliance_summary_timestamp: int = None,
        total_count: int = None,
    ):
        self.compliant_count = compliant_count
        self.non_compliant_count = non_compliant_count
        self.compliance_summary_timestamp = compliance_summary_timestamp
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compliant_count is not None:
            result['CompliantCount'] = self.compliant_count
        if self.non_compliant_count is not None:
            result['NonCompliantCount'] = self.non_compliant_count
        if self.compliance_summary_timestamp is not None:
            result['ComplianceSummaryTimestamp'] = self.compliance_summary_timestamp
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompliantCount') is not None:
            self.compliant_count = m.get('CompliantCount')
        if m.get('NonCompliantCount') is not None:
            self.non_compliant_count = m.get('NonCompliantCount')
        if m.get('ComplianceSummaryTimestamp') is not None:
            self.compliance_summary_timestamp = m.get('ComplianceSummaryTimestamp')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeComplianceSummaryResponseBodyComplianceSummary(TeaModel):
    def __init__(
        self,
        compliance_summary_by_resource: DescribeComplianceSummaryResponseBodyComplianceSummaryComplianceSummaryByResource = None,
        compliance_summary_by_config_rule: DescribeComplianceSummaryResponseBodyComplianceSummaryComplianceSummaryByConfigRule = None,
    ):
        self.compliance_summary_by_resource = compliance_summary_by_resource
        self.compliance_summary_by_config_rule = compliance_summary_by_config_rule

    def validate(self):
        if self.compliance_summary_by_resource:
            self.compliance_summary_by_resource.validate()
        if self.compliance_summary_by_config_rule:
            self.compliance_summary_by_config_rule.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compliance_summary_by_resource is not None:
            result['ComplianceSummaryByResource'] = self.compliance_summary_by_resource.to_map()
        if self.compliance_summary_by_config_rule is not None:
            result['ComplianceSummaryByConfigRule'] = self.compliance_summary_by_config_rule.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComplianceSummaryByResource') is not None:
            temp_model = DescribeComplianceSummaryResponseBodyComplianceSummaryComplianceSummaryByResource()
            self.compliance_summary_by_resource = temp_model.from_map(m['ComplianceSummaryByResource'])
        if m.get('ComplianceSummaryByConfigRule') is not None:
            temp_model = DescribeComplianceSummaryResponseBodyComplianceSummaryComplianceSummaryByConfigRule()
            self.compliance_summary_by_config_rule = temp_model.from_map(m['ComplianceSummaryByConfigRule'])
        return self


class DescribeComplianceSummaryResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        compliance_summary: DescribeComplianceSummaryResponseBodyComplianceSummary = None,
    ):
        self.request_id = request_id
        self.compliance_summary = compliance_summary

    def validate(self):
        if self.compliance_summary:
            self.compliance_summary.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.compliance_summary is not None:
            result['ComplianceSummary'] = self.compliance_summary.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ComplianceSummary') is not None:
            temp_model = DescribeComplianceSummaryResponseBodyComplianceSummary()
            self.compliance_summary = temp_model.from_map(m['ComplianceSummary'])
        return self


class DescribeComplianceSummaryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeComplianceSummaryResponseBody = None,
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
            temp_model = DescribeComplianceSummaryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeConfigRuleRequest(TeaModel):
    def __init__(
        self,
        config_rule_id: str = None,
        multi_account: bool = None,
        member_id: int = None,
    ):
        self.config_rule_id = config_rule_id
        self.multi_account = multi_account
        self.member_id = member_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_rule_id is not None:
            result['ConfigRuleId'] = self.config_rule_id
        if self.multi_account is not None:
            result['MultiAccount'] = self.multi_account
        if self.member_id is not None:
            result['MemberId'] = self.member_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigRuleId') is not None:
            self.config_rule_id = m.get('ConfigRuleId')
        if m.get('MultiAccount') is not None:
            self.multi_account = m.get('MultiAccount')
        if m.get('MemberId') is not None:
            self.member_id = m.get('MemberId')
        return self


class DescribeConfigRuleResponseBodyConfigRuleSourceSourceDetails(TeaModel):
    def __init__(
        self,
        message_type: str = None,
        event_source: str = None,
        maximum_execution_frequency: str = None,
    ):
        self.message_type = message_type
        self.event_source = event_source
        self.maximum_execution_frequency = maximum_execution_frequency

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message_type is not None:
            result['MessageType'] = self.message_type
        if self.event_source is not None:
            result['EventSource'] = self.event_source
        if self.maximum_execution_frequency is not None:
            result['MaximumExecutionFrequency'] = self.maximum_execution_frequency
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MessageType') is not None:
            self.message_type = m.get('MessageType')
        if m.get('EventSource') is not None:
            self.event_source = m.get('EventSource')
        if m.get('MaximumExecutionFrequency') is not None:
            self.maximum_execution_frequency = m.get('MaximumExecutionFrequency')
        return self


class DescribeConfigRuleResponseBodyConfigRuleSourceSourceConditions(TeaModel):
    def __init__(
        self,
        desired_value: str = None,
        tips: str = None,
        operator: str = None,
        name: str = None,
    ):
        self.desired_value = desired_value
        self.tips = tips
        self.operator = operator
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.desired_value is not None:
            result['DesiredValue'] = self.desired_value
        if self.tips is not None:
            result['Tips'] = self.tips
        if self.operator is not None:
            result['Operator'] = self.operator
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DesiredValue') is not None:
            self.desired_value = m.get('DesiredValue')
        if m.get('Tips') is not None:
            self.tips = m.get('Tips')
        if m.get('Operator') is not None:
            self.operator = m.get('Operator')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class DescribeConfigRuleResponseBodyConfigRuleSource(TeaModel):
    def __init__(
        self,
        source_details: List[DescribeConfigRuleResponseBodyConfigRuleSourceSourceDetails] = None,
        owner: str = None,
        source_conditions: List[DescribeConfigRuleResponseBodyConfigRuleSourceSourceConditions] = None,
        identifier: str = None,
    ):
        self.source_details = source_details
        self.owner = owner
        self.source_conditions = source_conditions
        self.identifier = identifier

    def validate(self):
        if self.source_details:
            for k in self.source_details:
                if k:
                    k.validate()
        if self.source_conditions:
            for k in self.source_conditions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['SourceDetails'] = []
        if self.source_details is not None:
            for k in self.source_details:
                result['SourceDetails'].append(k.to_map() if k else None)
        if self.owner is not None:
            result['Owner'] = self.owner
        result['SourceConditions'] = []
        if self.source_conditions is not None:
            for k in self.source_conditions:
                result['SourceConditions'].append(k.to_map() if k else None)
        if self.identifier is not None:
            result['Identifier'] = self.identifier
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.source_details = []
        if m.get('SourceDetails') is not None:
            for k in m.get('SourceDetails'):
                temp_model = DescribeConfigRuleResponseBodyConfigRuleSourceSourceDetails()
                self.source_details.append(temp_model.from_map(k))
        if m.get('Owner') is not None:
            self.owner = m.get('Owner')
        self.source_conditions = []
        if m.get('SourceConditions') is not None:
            for k in m.get('SourceConditions'):
                temp_model = DescribeConfigRuleResponseBodyConfigRuleSourceSourceConditions()
                self.source_conditions.append(temp_model.from_map(k))
        if m.get('Identifier') is not None:
            self.identifier = m.get('Identifier')
        return self


class DescribeConfigRuleResponseBodyConfigRuleManagedRuleSourceDetails(TeaModel):
    def __init__(
        self,
        message_type: str = None,
        event_source: str = None,
        maximum_execution_frequency: str = None,
    ):
        self.message_type = message_type
        self.event_source = event_source
        self.maximum_execution_frequency = maximum_execution_frequency

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message_type is not None:
            result['MessageType'] = self.message_type
        if self.event_source is not None:
            result['EventSource'] = self.event_source
        if self.maximum_execution_frequency is not None:
            result['MaximumExecutionFrequency'] = self.maximum_execution_frequency
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MessageType') is not None:
            self.message_type = m.get('MessageType')
        if m.get('EventSource') is not None:
            self.event_source = m.get('EventSource')
        if m.get('MaximumExecutionFrequency') is not None:
            self.maximum_execution_frequency = m.get('MaximumExecutionFrequency')
        return self


class DescribeConfigRuleResponseBodyConfigRuleManagedRule(TeaModel):
    def __init__(
        self,
        source_details: List[DescribeConfigRuleResponseBodyConfigRuleManagedRuleSourceDetails] = None,
        description: str = None,
        labels: List[str] = None,
        identifier: str = None,
        optional_input_parameter_details: Dict[str, Any] = None,
        managed_rule_name: str = None,
        compulsory_input_parameter_details: Dict[str, Any] = None,
    ):
        self.source_details = source_details
        self.description = description
        self.labels = labels
        self.identifier = identifier
        self.optional_input_parameter_details = optional_input_parameter_details
        self.managed_rule_name = managed_rule_name
        self.compulsory_input_parameter_details = compulsory_input_parameter_details

    def validate(self):
        if self.source_details:
            for k in self.source_details:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['SourceDetails'] = []
        if self.source_details is not None:
            for k in self.source_details:
                result['SourceDetails'].append(k.to_map() if k else None)
        if self.description is not None:
            result['Description'] = self.description
        if self.labels is not None:
            result['Labels'] = self.labels
        if self.identifier is not None:
            result['Identifier'] = self.identifier
        if self.optional_input_parameter_details is not None:
            result['OptionalInputParameterDetails'] = self.optional_input_parameter_details
        if self.managed_rule_name is not None:
            result['ManagedRuleName'] = self.managed_rule_name
        if self.compulsory_input_parameter_details is not None:
            result['CompulsoryInputParameterDetails'] = self.compulsory_input_parameter_details
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.source_details = []
        if m.get('SourceDetails') is not None:
            for k in m.get('SourceDetails'):
                temp_model = DescribeConfigRuleResponseBodyConfigRuleManagedRuleSourceDetails()
                self.source_details.append(temp_model.from_map(k))
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Labels') is not None:
            self.labels = m.get('Labels')
        if m.get('Identifier') is not None:
            self.identifier = m.get('Identifier')
        if m.get('OptionalInputParameterDetails') is not None:
            self.optional_input_parameter_details = m.get('OptionalInputParameterDetails')
        if m.get('ManagedRuleName') is not None:
            self.managed_rule_name = m.get('ManagedRuleName')
        if m.get('CompulsoryInputParameterDetails') is not None:
            self.compulsory_input_parameter_details = m.get('CompulsoryInputParameterDetails')
        return self


class DescribeConfigRuleResponseBodyConfigRuleCreateBy(TeaModel):
    def __init__(
        self,
        config_rule_scene_id: str = None,
        creator_name: str = None,
        creator_type: str = None,
        creator_id: str = None,
        config_rule_scene_name: str = None,
    ):
        self.config_rule_scene_id = config_rule_scene_id
        self.creator_name = creator_name
        self.creator_type = creator_type
        self.creator_id = creator_id
        self.config_rule_scene_name = config_rule_scene_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_rule_scene_id is not None:
            result['ConfigRuleSceneId'] = self.config_rule_scene_id
        if self.creator_name is not None:
            result['CreatorName'] = self.creator_name
        if self.creator_type is not None:
            result['CreatorType'] = self.creator_type
        if self.creator_id is not None:
            result['CreatorId'] = self.creator_id
        if self.config_rule_scene_name is not None:
            result['ConfigRuleSceneName'] = self.config_rule_scene_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigRuleSceneId') is not None:
            self.config_rule_scene_id = m.get('ConfigRuleSceneId')
        if m.get('CreatorName') is not None:
            self.creator_name = m.get('CreatorName')
        if m.get('CreatorType') is not None:
            self.creator_type = m.get('CreatorType')
        if m.get('CreatorId') is not None:
            self.creator_id = m.get('CreatorId')
        if m.get('ConfigRuleSceneName') is not None:
            self.config_rule_scene_name = m.get('ConfigRuleSceneName')
        return self


class DescribeConfigRuleResponseBodyConfigRuleScope(TeaModel):
    def __init__(
        self,
        compliance_resource_types: List[str] = None,
        compliance_resource_id: str = None,
    ):
        self.compliance_resource_types = compliance_resource_types
        self.compliance_resource_id = compliance_resource_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compliance_resource_types is not None:
            result['ComplianceResourceTypes'] = self.compliance_resource_types
        if self.compliance_resource_id is not None:
            result['ComplianceResourceId'] = self.compliance_resource_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComplianceResourceTypes') is not None:
            self.compliance_resource_types = m.get('ComplianceResourceTypes')
        if m.get('ComplianceResourceId') is not None:
            self.compliance_resource_id = m.get('ComplianceResourceId')
        return self


class DescribeConfigRuleResponseBodyConfigRuleConfigRuleEvaluationStatus(TeaModel):
    def __init__(
        self,
        last_error_code: str = None,
        last_successful_evaluation_timestamp: int = None,
        first_activated_timestamp: int = None,
        first_evaluation_started: bool = None,
        last_successful_invocation_timestamp: int = None,
        last_error_message: str = None,
        last_failed_evaluation_timestamp: int = None,
        last_failed_invocation_timestamp: int = None,
    ):
        self.last_error_code = last_error_code
        self.last_successful_evaluation_timestamp = last_successful_evaluation_timestamp
        self.first_activated_timestamp = first_activated_timestamp
        self.first_evaluation_started = first_evaluation_started
        self.last_successful_invocation_timestamp = last_successful_invocation_timestamp
        self.last_error_message = last_error_message
        self.last_failed_evaluation_timestamp = last_failed_evaluation_timestamp
        self.last_failed_invocation_timestamp = last_failed_invocation_timestamp

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.last_error_code is not None:
            result['LastErrorCode'] = self.last_error_code
        if self.last_successful_evaluation_timestamp is not None:
            result['LastSuccessfulEvaluationTimestamp'] = self.last_successful_evaluation_timestamp
        if self.first_activated_timestamp is not None:
            result['FirstActivatedTimestamp'] = self.first_activated_timestamp
        if self.first_evaluation_started is not None:
            result['FirstEvaluationStarted'] = self.first_evaluation_started
        if self.last_successful_invocation_timestamp is not None:
            result['LastSuccessfulInvocationTimestamp'] = self.last_successful_invocation_timestamp
        if self.last_error_message is not None:
            result['LastErrorMessage'] = self.last_error_message
        if self.last_failed_evaluation_timestamp is not None:
            result['LastFailedEvaluationTimestamp'] = self.last_failed_evaluation_timestamp
        if self.last_failed_invocation_timestamp is not None:
            result['LastFailedInvocationTimestamp'] = self.last_failed_invocation_timestamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LastErrorCode') is not None:
            self.last_error_code = m.get('LastErrorCode')
        if m.get('LastSuccessfulEvaluationTimestamp') is not None:
            self.last_successful_evaluation_timestamp = m.get('LastSuccessfulEvaluationTimestamp')
        if m.get('FirstActivatedTimestamp') is not None:
            self.first_activated_timestamp = m.get('FirstActivatedTimestamp')
        if m.get('FirstEvaluationStarted') is not None:
            self.first_evaluation_started = m.get('FirstEvaluationStarted')
        if m.get('LastSuccessfulInvocationTimestamp') is not None:
            self.last_successful_invocation_timestamp = m.get('LastSuccessfulInvocationTimestamp')
        if m.get('LastErrorMessage') is not None:
            self.last_error_message = m.get('LastErrorMessage')
        if m.get('LastFailedEvaluationTimestamp') is not None:
            self.last_failed_evaluation_timestamp = m.get('LastFailedEvaluationTimestamp')
        if m.get('LastFailedInvocationTimestamp') is not None:
            self.last_failed_invocation_timestamp = m.get('LastFailedInvocationTimestamp')
        return self


class DescribeConfigRuleResponseBodyConfigRule(TeaModel):
    def __init__(
        self,
        risk_level: int = None,
        input_parameters: Dict[str, Any] = None,
        source: DescribeConfigRuleResponseBodyConfigRuleSource = None,
        config_rule_state: str = None,
        maximum_execution_frequency: str = None,
        managed_rule: DescribeConfigRuleResponseBodyConfigRuleManagedRule = None,
        config_rule_arn: str = None,
        description: str = None,
        create_by: DescribeConfigRuleResponseBodyConfigRuleCreateBy = None,
        config_rule_name: str = None,
        scope: DescribeConfigRuleResponseBodyConfigRuleScope = None,
        config_rule_evaluation_status: DescribeConfigRuleResponseBodyConfigRuleConfigRuleEvaluationStatus = None,
        config_rule_id: str = None,
        modified_timestamp: int = None,
        create_timestamp: int = None,
    ):
        self.risk_level = risk_level
        self.input_parameters = input_parameters
        self.source = source
        self.config_rule_state = config_rule_state
        self.maximum_execution_frequency = maximum_execution_frequency
        self.managed_rule = managed_rule
        self.config_rule_arn = config_rule_arn
        self.description = description
        self.create_by = create_by
        self.config_rule_name = config_rule_name
        self.scope = scope
        self.config_rule_evaluation_status = config_rule_evaluation_status
        self.config_rule_id = config_rule_id
        self.modified_timestamp = modified_timestamp
        self.create_timestamp = create_timestamp

    def validate(self):
        if self.source:
            self.source.validate()
        if self.managed_rule:
            self.managed_rule.validate()
        if self.create_by:
            self.create_by.validate()
        if self.scope:
            self.scope.validate()
        if self.config_rule_evaluation_status:
            self.config_rule_evaluation_status.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level
        if self.input_parameters is not None:
            result['InputParameters'] = self.input_parameters
        if self.source is not None:
            result['Source'] = self.source.to_map()
        if self.config_rule_state is not None:
            result['ConfigRuleState'] = self.config_rule_state
        if self.maximum_execution_frequency is not None:
            result['MaximumExecutionFrequency'] = self.maximum_execution_frequency
        if self.managed_rule is not None:
            result['ManagedRule'] = self.managed_rule.to_map()
        if self.config_rule_arn is not None:
            result['ConfigRuleArn'] = self.config_rule_arn
        if self.description is not None:
            result['Description'] = self.description
        if self.create_by is not None:
            result['CreateBy'] = self.create_by.to_map()
        if self.config_rule_name is not None:
            result['ConfigRuleName'] = self.config_rule_name
        if self.scope is not None:
            result['Scope'] = self.scope.to_map()
        if self.config_rule_evaluation_status is not None:
            result['ConfigRuleEvaluationStatus'] = self.config_rule_evaluation_status.to_map()
        if self.config_rule_id is not None:
            result['ConfigRuleId'] = self.config_rule_id
        if self.modified_timestamp is not None:
            result['ModifiedTimestamp'] = self.modified_timestamp
        if self.create_timestamp is not None:
            result['CreateTimestamp'] = self.create_timestamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')
        if m.get('InputParameters') is not None:
            self.input_parameters = m.get('InputParameters')
        if m.get('Source') is not None:
            temp_model = DescribeConfigRuleResponseBodyConfigRuleSource()
            self.source = temp_model.from_map(m['Source'])
        if m.get('ConfigRuleState') is not None:
            self.config_rule_state = m.get('ConfigRuleState')
        if m.get('MaximumExecutionFrequency') is not None:
            self.maximum_execution_frequency = m.get('MaximumExecutionFrequency')
        if m.get('ManagedRule') is not None:
            temp_model = DescribeConfigRuleResponseBodyConfigRuleManagedRule()
            self.managed_rule = temp_model.from_map(m['ManagedRule'])
        if m.get('ConfigRuleArn') is not None:
            self.config_rule_arn = m.get('ConfigRuleArn')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('CreateBy') is not None:
            temp_model = DescribeConfigRuleResponseBodyConfigRuleCreateBy()
            self.create_by = temp_model.from_map(m['CreateBy'])
        if m.get('ConfigRuleName') is not None:
            self.config_rule_name = m.get('ConfigRuleName')
        if m.get('Scope') is not None:
            temp_model = DescribeConfigRuleResponseBodyConfigRuleScope()
            self.scope = temp_model.from_map(m['Scope'])
        if m.get('ConfigRuleEvaluationStatus') is not None:
            temp_model = DescribeConfigRuleResponseBodyConfigRuleConfigRuleEvaluationStatus()
            self.config_rule_evaluation_status = temp_model.from_map(m['ConfigRuleEvaluationStatus'])
        if m.get('ConfigRuleId') is not None:
            self.config_rule_id = m.get('ConfigRuleId')
        if m.get('ModifiedTimestamp') is not None:
            self.modified_timestamp = m.get('ModifiedTimestamp')
        if m.get('CreateTimestamp') is not None:
            self.create_timestamp = m.get('CreateTimestamp')
        return self


class DescribeConfigRuleResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        config_rule: DescribeConfigRuleResponseBodyConfigRule = None,
    ):
        self.request_id = request_id
        self.config_rule = config_rule

    def validate(self):
        if self.config_rule:
            self.config_rule.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.config_rule is not None:
            result['ConfigRule'] = self.config_rule.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ConfigRule') is not None:
            temp_model = DescribeConfigRuleResponseBodyConfigRule()
            self.config_rule = temp_model.from_map(m['ConfigRule'])
        return self


class DescribeConfigRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeConfigRuleResponseBody = None,
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
            temp_model = DescribeConfigRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeConfigurationRecorderResponseBodyConfigurationRecorder(TeaModel):
    def __init__(
        self,
        organization_enable_status: str = None,
        configuration_recorder_status: str = None,
        organization_master_id: int = None,
        account_id: int = None,
        resource_types: List[str] = None,
    ):
        self.organization_enable_status = organization_enable_status
        self.configuration_recorder_status = configuration_recorder_status
        self.organization_master_id = organization_master_id
        self.account_id = account_id
        self.resource_types = resource_types

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.organization_enable_status is not None:
            result['OrganizationEnableStatus'] = self.organization_enable_status
        if self.configuration_recorder_status is not None:
            result['ConfigurationRecorderStatus'] = self.configuration_recorder_status
        if self.organization_master_id is not None:
            result['OrganizationMasterId'] = self.organization_master_id
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.resource_types is not None:
            result['ResourceTypes'] = self.resource_types
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrganizationEnableStatus') is not None:
            self.organization_enable_status = m.get('OrganizationEnableStatus')
        if m.get('ConfigurationRecorderStatus') is not None:
            self.configuration_recorder_status = m.get('ConfigurationRecorderStatus')
        if m.get('OrganizationMasterId') is not None:
            self.organization_master_id = m.get('OrganizationMasterId')
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('ResourceTypes') is not None:
            self.resource_types = m.get('ResourceTypes')
        return self


class DescribeConfigurationRecorderResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        configuration_recorder: DescribeConfigurationRecorderResponseBodyConfigurationRecorder = None,
    ):
        self.request_id = request_id
        self.configuration_recorder = configuration_recorder

    def validate(self):
        if self.configuration_recorder:
            self.configuration_recorder.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.configuration_recorder is not None:
            result['ConfigurationRecorder'] = self.configuration_recorder.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ConfigurationRecorder') is not None:
            temp_model = DescribeConfigurationRecorderResponseBodyConfigurationRecorder()
            self.configuration_recorder = temp_model.from_map(m['ConfigurationRecorder'])
        return self


class DescribeConfigurationRecorderResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeConfigurationRecorderResponseBody = None,
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
            temp_model = DescribeConfigurationRecorderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDeliveryChannelsRequest(TeaModel):
    def __init__(
        self,
        delivery_channel_ids: str = None,
    ):
        self.delivery_channel_ids = delivery_channel_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.delivery_channel_ids is not None:
            result['DeliveryChannelIds'] = self.delivery_channel_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeliveryChannelIds') is not None:
            self.delivery_channel_ids = m.get('DeliveryChannelIds')
        return self


class DescribeDeliveryChannelsResponseBodyDeliveryChannels(TeaModel):
    def __init__(
        self,
        status: int = None,
        delivery_channel_name: str = None,
        delivery_channel_id: str = None,
        delivery_channel_type: str = None,
        delivery_channel_assume_role_arn: str = None,
        description: str = None,
        delivery_channel_condition: str = None,
        delivery_channel_target_arn: str = None,
    ):
        self.status = status
        self.delivery_channel_name = delivery_channel_name
        self.delivery_channel_id = delivery_channel_id
        self.delivery_channel_type = delivery_channel_type
        self.delivery_channel_assume_role_arn = delivery_channel_assume_role_arn
        self.description = description
        self.delivery_channel_condition = delivery_channel_condition
        self.delivery_channel_target_arn = delivery_channel_target_arn

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.delivery_channel_name is not None:
            result['DeliveryChannelName'] = self.delivery_channel_name
        if self.delivery_channel_id is not None:
            result['DeliveryChannelId'] = self.delivery_channel_id
        if self.delivery_channel_type is not None:
            result['DeliveryChannelType'] = self.delivery_channel_type
        if self.delivery_channel_assume_role_arn is not None:
            result['DeliveryChannelAssumeRoleArn'] = self.delivery_channel_assume_role_arn
        if self.description is not None:
            result['Description'] = self.description
        if self.delivery_channel_condition is not None:
            result['DeliveryChannelCondition'] = self.delivery_channel_condition
        if self.delivery_channel_target_arn is not None:
            result['DeliveryChannelTargetArn'] = self.delivery_channel_target_arn
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('DeliveryChannelName') is not None:
            self.delivery_channel_name = m.get('DeliveryChannelName')
        if m.get('DeliveryChannelId') is not None:
            self.delivery_channel_id = m.get('DeliveryChannelId')
        if m.get('DeliveryChannelType') is not None:
            self.delivery_channel_type = m.get('DeliveryChannelType')
        if m.get('DeliveryChannelAssumeRoleArn') is not None:
            self.delivery_channel_assume_role_arn = m.get('DeliveryChannelAssumeRoleArn')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DeliveryChannelCondition') is not None:
            self.delivery_channel_condition = m.get('DeliveryChannelCondition')
        if m.get('DeliveryChannelTargetArn') is not None:
            self.delivery_channel_target_arn = m.get('DeliveryChannelTargetArn')
        return self


class DescribeDeliveryChannelsResponseBody(TeaModel):
    def __init__(
        self,
        delivery_channels: List[DescribeDeliveryChannelsResponseBodyDeliveryChannels] = None,
        request_id: str = None,
    ):
        self.delivery_channels = delivery_channels
        self.request_id = request_id

    def validate(self):
        if self.delivery_channels:
            for k in self.delivery_channels:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DeliveryChannels'] = []
        if self.delivery_channels is not None:
            for k in self.delivery_channels:
                result['DeliveryChannels'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.delivery_channels = []
        if m.get('DeliveryChannels') is not None:
            for k in m.get('DeliveryChannels'):
                temp_model = DescribeDeliveryChannelsResponseBodyDeliveryChannels()
                self.delivery_channels.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDeliveryChannelsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDeliveryChannelsResponseBody = None,
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
            temp_model = DescribeDeliveryChannelsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDiscoveredResourceRequest(TeaModel):
    def __init__(
        self,
        resource_id: str = None,
        resource_type: str = None,
        region: str = None,
        multi_account: bool = None,
        member_id: int = None,
    ):
        self.resource_id = resource_id
        self.resource_type = resource_type
        self.region = region
        self.multi_account = multi_account
        self.member_id = member_id

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
        if self.region is not None:
            result['Region'] = self.region
        if self.multi_account is not None:
            result['MultiAccount'] = self.multi_account
        if self.member_id is not None:
            result['MemberId'] = self.member_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('MultiAccount') is not None:
            self.multi_account = m.get('MultiAccount')
        if m.get('MemberId') is not None:
            self.member_id = m.get('MemberId')
        return self


class DescribeDiscoveredResourceResponseBodyDiscoveredResourceDetail(TeaModel):
    def __init__(
        self,
        availability_zone: str = None,
        resource_type: str = None,
        configuration: str = None,
        region: str = None,
        resource_creation_time: int = None,
        tags: str = None,
        account_id: int = None,
        resource_id: str = None,
        resource_deleted: int = None,
        resource_name: str = None,
        resource_status: str = None,
    ):
        self.availability_zone = availability_zone
        self.resource_type = resource_type
        self.configuration = configuration
        self.region = region
        self.resource_creation_time = resource_creation_time
        self.tags = tags
        self.account_id = account_id
        self.resource_id = resource_id
        self.resource_deleted = resource_deleted
        self.resource_name = resource_name
        self.resource_status = resource_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.availability_zone is not None:
            result['AvailabilityZone'] = self.availability_zone
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.configuration is not None:
            result['Configuration'] = self.configuration
        if self.region is not None:
            result['Region'] = self.region
        if self.resource_creation_time is not None:
            result['ResourceCreationTime'] = self.resource_creation_time
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_deleted is not None:
            result['ResourceDeleted'] = self.resource_deleted
        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name
        if self.resource_status is not None:
            result['ResourceStatus'] = self.resource_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvailabilityZone') is not None:
            self.availability_zone = m.get('AvailabilityZone')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('Configuration') is not None:
            self.configuration = m.get('Configuration')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('ResourceCreationTime') is not None:
            self.resource_creation_time = m.get('ResourceCreationTime')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceDeleted') is not None:
            self.resource_deleted = m.get('ResourceDeleted')
        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')
        if m.get('ResourceStatus') is not None:
            self.resource_status = m.get('ResourceStatus')
        return self


class DescribeDiscoveredResourceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        discovered_resource_detail: DescribeDiscoveredResourceResponseBodyDiscoveredResourceDetail = None,
    ):
        self.request_id = request_id
        self.discovered_resource_detail = discovered_resource_detail

    def validate(self):
        if self.discovered_resource_detail:
            self.discovered_resource_detail.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.discovered_resource_detail is not None:
            result['DiscoveredResourceDetail'] = self.discovered_resource_detail.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DiscoveredResourceDetail') is not None:
            temp_model = DescribeDiscoveredResourceResponseBodyDiscoveredResourceDetail()
            self.discovered_resource_detail = temp_model.from_map(m['DiscoveredResourceDetail'])
        return self


class DescribeDiscoveredResourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDiscoveredResourceResponseBody = None,
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
            temp_model = DescribeDiscoveredResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeEvaluationResultsRequest(TeaModel):
    def __init__(
        self,
        resource_type: str = None,
        resource_id: str = None,
        compliance_type: str = None,
        page_number: int = None,
        page_size: int = None,
        config_rule_id: str = None,
        multi_account: bool = None,
        member_id: int = None,
    ):
        self.resource_type = resource_type
        self.resource_id = resource_id
        self.compliance_type = compliance_type
        self.page_number = page_number
        self.page_size = page_size
        self.config_rule_id = config_rule_id
        self.multi_account = multi_account
        self.member_id = member_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.compliance_type is not None:
            result['ComplianceType'] = self.compliance_type
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.config_rule_id is not None:
            result['ConfigRuleId'] = self.config_rule_id
        if self.multi_account is not None:
            result['MultiAccount'] = self.multi_account
        if self.member_id is not None:
            result['MemberId'] = self.member_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ComplianceType') is not None:
            self.compliance_type = m.get('ComplianceType')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ConfigRuleId') is not None:
            self.config_rule_id = m.get('ConfigRuleId')
        if m.get('MultiAccount') is not None:
            self.multi_account = m.get('MultiAccount')
        if m.get('MemberId') is not None:
            self.member_id = m.get('MemberId')
        return self


class DescribeEvaluationResultsResponseBodyEvaluationResultsEvaluationResultListEvaluationResultIdentifierEvaluationResultQualifier(TeaModel):
    def __init__(
        self,
        config_rule_arn: str = None,
        resource_type: str = None,
        config_rule_name: str = None,
        resource_id: str = None,
        config_rule_id: str = None,
        resource_name: str = None,
        region_id: str = None,
    ):
        self.config_rule_arn = config_rule_arn
        self.resource_type = resource_type
        self.config_rule_name = config_rule_name
        self.resource_id = resource_id
        self.config_rule_id = config_rule_id
        self.resource_name = resource_name
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_rule_arn is not None:
            result['ConfigRuleArn'] = self.config_rule_arn
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.config_rule_name is not None:
            result['ConfigRuleName'] = self.config_rule_name
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.config_rule_id is not None:
            result['ConfigRuleId'] = self.config_rule_id
        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigRuleArn') is not None:
            self.config_rule_arn = m.get('ConfigRuleArn')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('ConfigRuleName') is not None:
            self.config_rule_name = m.get('ConfigRuleName')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ConfigRuleId') is not None:
            self.config_rule_id = m.get('ConfigRuleId')
        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeEvaluationResultsResponseBodyEvaluationResultsEvaluationResultListEvaluationResultIdentifier(TeaModel):
    def __init__(
        self,
        ordering_timestamp: int = None,
        evaluation_result_qualifier: DescribeEvaluationResultsResponseBodyEvaluationResultsEvaluationResultListEvaluationResultIdentifierEvaluationResultQualifier = None,
    ):
        self.ordering_timestamp = ordering_timestamp
        self.evaluation_result_qualifier = evaluation_result_qualifier

    def validate(self):
        if self.evaluation_result_qualifier:
            self.evaluation_result_qualifier.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ordering_timestamp is not None:
            result['OrderingTimestamp'] = self.ordering_timestamp
        if self.evaluation_result_qualifier is not None:
            result['EvaluationResultQualifier'] = self.evaluation_result_qualifier.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrderingTimestamp') is not None:
            self.ordering_timestamp = m.get('OrderingTimestamp')
        if m.get('EvaluationResultQualifier') is not None:
            temp_model = DescribeEvaluationResultsResponseBodyEvaluationResultsEvaluationResultListEvaluationResultIdentifierEvaluationResultQualifier()
            self.evaluation_result_qualifier = temp_model.from_map(m['EvaluationResultQualifier'])
        return self


class DescribeEvaluationResultsResponseBodyEvaluationResultsEvaluationResultList(TeaModel):
    def __init__(
        self,
        risk_level: int = None,
        compliance_type: str = None,
        result_recorded_timestamp: int = None,
        annotation: str = None,
        config_rule_invoked_timestamp: int = None,
        invoking_event_message_type: str = None,
        evaluation_result_identifier: DescribeEvaluationResultsResponseBodyEvaluationResultsEvaluationResultListEvaluationResultIdentifier = None,
        remediation_enabled: bool = None,
    ):
        self.risk_level = risk_level
        self.compliance_type = compliance_type
        self.result_recorded_timestamp = result_recorded_timestamp
        self.annotation = annotation
        self.config_rule_invoked_timestamp = config_rule_invoked_timestamp
        self.invoking_event_message_type = invoking_event_message_type
        self.evaluation_result_identifier = evaluation_result_identifier
        self.remediation_enabled = remediation_enabled

    def validate(self):
        if self.evaluation_result_identifier:
            self.evaluation_result_identifier.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level
        if self.compliance_type is not None:
            result['ComplianceType'] = self.compliance_type
        if self.result_recorded_timestamp is not None:
            result['ResultRecordedTimestamp'] = self.result_recorded_timestamp
        if self.annotation is not None:
            result['Annotation'] = self.annotation
        if self.config_rule_invoked_timestamp is not None:
            result['ConfigRuleInvokedTimestamp'] = self.config_rule_invoked_timestamp
        if self.invoking_event_message_type is not None:
            result['InvokingEventMessageType'] = self.invoking_event_message_type
        if self.evaluation_result_identifier is not None:
            result['EvaluationResultIdentifier'] = self.evaluation_result_identifier.to_map()
        if self.remediation_enabled is not None:
            result['RemediationEnabled'] = self.remediation_enabled
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')
        if m.get('ComplianceType') is not None:
            self.compliance_type = m.get('ComplianceType')
        if m.get('ResultRecordedTimestamp') is not None:
            self.result_recorded_timestamp = m.get('ResultRecordedTimestamp')
        if m.get('Annotation') is not None:
            self.annotation = m.get('Annotation')
        if m.get('ConfigRuleInvokedTimestamp') is not None:
            self.config_rule_invoked_timestamp = m.get('ConfigRuleInvokedTimestamp')
        if m.get('InvokingEventMessageType') is not None:
            self.invoking_event_message_type = m.get('InvokingEventMessageType')
        if m.get('EvaluationResultIdentifier') is not None:
            temp_model = DescribeEvaluationResultsResponseBodyEvaluationResultsEvaluationResultListEvaluationResultIdentifier()
            self.evaluation_result_identifier = temp_model.from_map(m['EvaluationResultIdentifier'])
        if m.get('RemediationEnabled') is not None:
            self.remediation_enabled = m.get('RemediationEnabled')
        return self


class DescribeEvaluationResultsResponseBodyEvaluationResults(TeaModel):
    def __init__(
        self,
        evaluation_result_list: List[DescribeEvaluationResultsResponseBodyEvaluationResultsEvaluationResultList] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.evaluation_result_list = evaluation_result_list
        self.page_number = page_number
        self.page_size = page_size
        self.total_count = total_count

    def validate(self):
        if self.evaluation_result_list:
            for k in self.evaluation_result_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['EvaluationResultList'] = []
        if self.evaluation_result_list is not None:
            for k in self.evaluation_result_list:
                result['EvaluationResultList'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.evaluation_result_list = []
        if m.get('EvaluationResultList') is not None:
            for k in m.get('EvaluationResultList'):
                temp_model = DescribeEvaluationResultsResponseBodyEvaluationResultsEvaluationResultList()
                self.evaluation_result_list.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeEvaluationResultsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        evaluation_results: DescribeEvaluationResultsResponseBodyEvaluationResults = None,
    ):
        self.request_id = request_id
        self.evaluation_results = evaluation_results

    def validate(self):
        if self.evaluation_results:
            self.evaluation_results.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.evaluation_results is not None:
            result['EvaluationResults'] = self.evaluation_results.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('EvaluationResults') is not None:
            temp_model = DescribeEvaluationResultsResponseBodyEvaluationResults()
            self.evaluation_results = temp_model.from_map(m['EvaluationResults'])
        return self


class DescribeEvaluationResultsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeEvaluationResultsResponseBody = None,
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
            temp_model = DescribeEvaluationResultsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDiscoveredResourceCountsRequest(TeaModel):
    def __init__(
        self,
        group_by_key: str = None,
        multi_account: bool = None,
        member_id: int = None,
    ):
        self.group_by_key = group_by_key
        self.multi_account = multi_account
        self.member_id = member_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_by_key is not None:
            result['GroupByKey'] = self.group_by_key
        if self.multi_account is not None:
            result['MultiAccount'] = self.multi_account
        if self.member_id is not None:
            result['MemberId'] = self.member_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupByKey') is not None:
            self.group_by_key = m.get('GroupByKey')
        if m.get('MultiAccount') is not None:
            self.multi_account = m.get('MultiAccount')
        if m.get('MemberId') is not None:
            self.member_id = m.get('MemberId')
        return self


class GetDiscoveredResourceCountsResponseBodyGroupedResourceCountsGroupedResourceCountList(TeaModel):
    def __init__(
        self,
        resource_count: int = None,
        group_name: str = None,
    ):
        self.resource_count = resource_count
        self.group_name = group_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_count is not None:
            result['ResourceCount'] = self.resource_count
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceCount') is not None:
            self.resource_count = m.get('ResourceCount')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        return self


class GetDiscoveredResourceCountsResponseBodyGroupedResourceCounts(TeaModel):
    def __init__(
        self,
        grouped_resource_count_list: List[GetDiscoveredResourceCountsResponseBodyGroupedResourceCountsGroupedResourceCountList] = None,
        group_by_key: str = None,
    ):
        self.grouped_resource_count_list = grouped_resource_count_list
        self.group_by_key = group_by_key

    def validate(self):
        if self.grouped_resource_count_list:
            for k in self.grouped_resource_count_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['GroupedResourceCountList'] = []
        if self.grouped_resource_count_list is not None:
            for k in self.grouped_resource_count_list:
                result['GroupedResourceCountList'].append(k.to_map() if k else None)
        if self.group_by_key is not None:
            result['GroupByKey'] = self.group_by_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.grouped_resource_count_list = []
        if m.get('GroupedResourceCountList') is not None:
            for k in m.get('GroupedResourceCountList'):
                temp_model = GetDiscoveredResourceCountsResponseBodyGroupedResourceCountsGroupedResourceCountList()
                self.grouped_resource_count_list.append(temp_model.from_map(k))
        if m.get('GroupByKey') is not None:
            self.group_by_key = m.get('GroupByKey')
        return self


class GetDiscoveredResourceCountsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        grouped_resource_counts: GetDiscoveredResourceCountsResponseBodyGroupedResourceCounts = None,
    ):
        self.request_id = request_id
        self.grouped_resource_counts = grouped_resource_counts

    def validate(self):
        if self.grouped_resource_counts:
            self.grouped_resource_counts.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.grouped_resource_counts is not None:
            result['GroupedResourceCounts'] = self.grouped_resource_counts.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('GroupedResourceCounts') is not None:
            temp_model = GetDiscoveredResourceCountsResponseBodyGroupedResourceCounts()
            self.grouped_resource_counts = temp_model.from_map(m['GroupedResourceCounts'])
        return self


class GetDiscoveredResourceCountsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetDiscoveredResourceCountsResponseBody = None,
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
            temp_model = GetDiscoveredResourceCountsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDiscoveredResourceSummaryRequest(TeaModel):
    def __init__(
        self,
        multi_account: bool = None,
        member_id: int = None,
    ):
        self.multi_account = multi_account
        self.member_id = member_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.multi_account is not None:
            result['MultiAccount'] = self.multi_account
        if self.member_id is not None:
            result['MemberId'] = self.member_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MultiAccount') is not None:
            self.multi_account = m.get('MultiAccount')
        if m.get('MemberId') is not None:
            self.member_id = m.get('MemberId')
        return self


class GetDiscoveredResourceSummaryResponseBodyDiscoveredResourceSummary(TeaModel):
    def __init__(
        self,
        region_count: int = None,
        resource_count: int = None,
        resource_type_count: int = None,
    ):
        self.region_count = region_count
        self.resource_count = resource_count
        self.resource_type_count = resource_type_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_count is not None:
            result['RegionCount'] = self.region_count
        if self.resource_count is not None:
            result['ResourceCount'] = self.resource_count
        if self.resource_type_count is not None:
            result['ResourceTypeCount'] = self.resource_type_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionCount') is not None:
            self.region_count = m.get('RegionCount')
        if m.get('ResourceCount') is not None:
            self.resource_count = m.get('ResourceCount')
        if m.get('ResourceTypeCount') is not None:
            self.resource_type_count = m.get('ResourceTypeCount')
        return self


class GetDiscoveredResourceSummaryResponseBody(TeaModel):
    def __init__(
        self,
        discovered_resource_summary: GetDiscoveredResourceSummaryResponseBodyDiscoveredResourceSummary = None,
        request_id: str = None,
    ):
        self.discovered_resource_summary = discovered_resource_summary
        self.request_id = request_id

    def validate(self):
        if self.discovered_resource_summary:
            self.discovered_resource_summary.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.discovered_resource_summary is not None:
            result['DiscoveredResourceSummary'] = self.discovered_resource_summary.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DiscoveredResourceSummary') is not None:
            temp_model = GetDiscoveredResourceSummaryResponseBodyDiscoveredResourceSummary()
            self.discovered_resource_summary = temp_model.from_map(m['DiscoveredResourceSummary'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetDiscoveredResourceSummaryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetDiscoveredResourceSummaryResponseBody = None,
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
            temp_model = GetDiscoveredResourceSummaryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetResourceComplianceTimelineRequest(TeaModel):
    def __init__(
        self,
        resource_type: str = None,
        resource_id: str = None,
        start_time: int = None,
        end_time: int = None,
        limit: int = None,
        multi_account: bool = None,
        member_id: str = None,
        region: str = None,
        next_token: str = None,
    ):
        self.resource_type = resource_type
        self.resource_id = resource_id
        self.start_time = start_time
        self.end_time = end_time
        self.limit = limit
        self.multi_account = multi_account
        self.member_id = member_id
        self.region = region
        self.next_token = next_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.limit is not None:
            result['Limit'] = self.limit
        if self.multi_account is not None:
            result['MultiAccount'] = self.multi_account
        if self.member_id is not None:
            result['MemberId'] = self.member_id
        if self.region is not None:
            result['Region'] = self.region
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        if m.get('MultiAccount') is not None:
            self.multi_account = m.get('MultiAccount')
        if m.get('MemberId') is not None:
            self.member_id = m.get('MemberId')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        return self


class GetResourceComplianceTimelineResponseBodyResourceComplianceTimelineComplianceList(TeaModel):
    def __init__(
        self,
        tags: str = None,
        account_id: str = None,
        availability_zone: str = None,
        resource_type: str = None,
        resource_create_time: int = None,
        region: str = None,
        configuration: str = None,
        capture_time: int = None,
        configuration_diff: str = None,
        resource_id: str = None,
        resource_name: str = None,
        resource_status: str = None,
    ):
        self.tags = tags
        self.account_id = account_id
        self.availability_zone = availability_zone
        self.resource_type = resource_type
        self.resource_create_time = resource_create_time
        self.region = region
        self.configuration = configuration
        self.capture_time = capture_time
        self.configuration_diff = configuration_diff
        self.resource_id = resource_id
        self.resource_name = resource_name
        self.resource_status = resource_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.availability_zone is not None:
            result['AvailabilityZone'] = self.availability_zone
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.resource_create_time is not None:
            result['ResourceCreateTime'] = self.resource_create_time
        if self.region is not None:
            result['Region'] = self.region
        if self.configuration is not None:
            result['Configuration'] = self.configuration
        if self.capture_time is not None:
            result['CaptureTime'] = self.capture_time
        if self.configuration_diff is not None:
            result['ConfigurationDiff'] = self.configuration_diff
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name
        if self.resource_status is not None:
            result['ResourceStatus'] = self.resource_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('AvailabilityZone') is not None:
            self.availability_zone = m.get('AvailabilityZone')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('ResourceCreateTime') is not None:
            self.resource_create_time = m.get('ResourceCreateTime')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('Configuration') is not None:
            self.configuration = m.get('Configuration')
        if m.get('CaptureTime') is not None:
            self.capture_time = m.get('CaptureTime')
        if m.get('ConfigurationDiff') is not None:
            self.configuration_diff = m.get('ConfigurationDiff')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')
        if m.get('ResourceStatus') is not None:
            self.resource_status = m.get('ResourceStatus')
        return self


class GetResourceComplianceTimelineResponseBodyResourceComplianceTimeline(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        limit: int = None,
        compliance_list: List[GetResourceComplianceTimelineResponseBodyResourceComplianceTimelineComplianceList] = None,
        total_count: int = None,
    ):
        self.next_token = next_token
        self.limit = limit
        self.compliance_list = compliance_list
        self.total_count = total_count

    def validate(self):
        if self.compliance_list:
            for k in self.compliance_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.limit is not None:
            result['Limit'] = self.limit
        result['ComplianceList'] = []
        if self.compliance_list is not None:
            for k in self.compliance_list:
                result['ComplianceList'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        self.compliance_list = []
        if m.get('ComplianceList') is not None:
            for k in m.get('ComplianceList'):
                temp_model = GetResourceComplianceTimelineResponseBodyResourceComplianceTimelineComplianceList()
                self.compliance_list.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class GetResourceComplianceTimelineResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        resource_compliance_timeline: GetResourceComplianceTimelineResponseBodyResourceComplianceTimeline = None,
    ):
        self.request_id = request_id
        self.resource_compliance_timeline = resource_compliance_timeline

    def validate(self):
        if self.resource_compliance_timeline:
            self.resource_compliance_timeline.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_compliance_timeline is not None:
            result['ResourceComplianceTimeline'] = self.resource_compliance_timeline.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceComplianceTimeline') is not None:
            temp_model = GetResourceComplianceTimelineResponseBodyResourceComplianceTimeline()
            self.resource_compliance_timeline = temp_model.from_map(m['ResourceComplianceTimeline'])
        return self


class GetResourceComplianceTimelineResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetResourceComplianceTimelineResponseBody = None,
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
            temp_model = GetResourceComplianceTimelineResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetResourceConfigurationTimelineRequest(TeaModel):
    def __init__(
        self,
        resource_id: str = None,
        start_time: int = None,
        end_time: int = None,
        limit: int = None,
        resource_type: str = None,
        region: str = None,
        multi_account: bool = None,
        member_id: int = None,
        next_token: str = None,
    ):
        self.resource_id = resource_id
        self.start_time = start_time
        self.end_time = end_time
        self.limit = limit
        self.resource_type = resource_type
        self.region = region
        self.multi_account = multi_account
        self.member_id = member_id
        self.next_token = next_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.limit is not None:
            result['Limit'] = self.limit
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.region is not None:
            result['Region'] = self.region
        if self.multi_account is not None:
            result['MultiAccount'] = self.multi_account
        if self.member_id is not None:
            result['MemberId'] = self.member_id
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('MultiAccount') is not None:
            self.multi_account = m.get('MultiAccount')
        if m.get('MemberId') is not None:
            self.member_id = m.get('MemberId')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        return self


class GetResourceConfigurationTimelineResponseBodyResourceConfigurationTimelineConfigurationList(TeaModel):
    def __init__(
        self,
        tags: str = None,
        account_id: int = None,
        resource_event_type: str = None,
        availability_zone: str = None,
        resource_type: str = None,
        resource_create_time: str = None,
        region: str = None,
        capture_time: str = None,
        configuration_diff: str = None,
        resource_id: str = None,
        resource_name: str = None,
    ):
        self.tags = tags
        self.account_id = account_id
        self.resource_event_type = resource_event_type
        self.availability_zone = availability_zone
        self.resource_type = resource_type
        self.resource_create_time = resource_create_time
        self.region = region
        self.capture_time = capture_time
        self.configuration_diff = configuration_diff
        self.resource_id = resource_id
        self.resource_name = resource_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.resource_event_type is not None:
            result['ResourceEventType'] = self.resource_event_type
        if self.availability_zone is not None:
            result['AvailabilityZone'] = self.availability_zone
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.resource_create_time is not None:
            result['ResourceCreateTime'] = self.resource_create_time
        if self.region is not None:
            result['Region'] = self.region
        if self.capture_time is not None:
            result['CaptureTime'] = self.capture_time
        if self.configuration_diff is not None:
            result['ConfigurationDiff'] = self.configuration_diff
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('ResourceEventType') is not None:
            self.resource_event_type = m.get('ResourceEventType')
        if m.get('AvailabilityZone') is not None:
            self.availability_zone = m.get('AvailabilityZone')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('ResourceCreateTime') is not None:
            self.resource_create_time = m.get('ResourceCreateTime')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('CaptureTime') is not None:
            self.capture_time = m.get('CaptureTime')
        if m.get('ConfigurationDiff') is not None:
            self.configuration_diff = m.get('ConfigurationDiff')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')
        return self


class GetResourceConfigurationTimelineResponseBodyResourceConfigurationTimeline(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        limit: int = None,
        configuration_list: List[GetResourceConfigurationTimelineResponseBodyResourceConfigurationTimelineConfigurationList] = None,
        total_count: int = None,
    ):
        self.next_token = next_token
        self.limit = limit
        self.configuration_list = configuration_list
        self.total_count = total_count

    def validate(self):
        if self.configuration_list:
            for k in self.configuration_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.limit is not None:
            result['Limit'] = self.limit
        result['ConfigurationList'] = []
        if self.configuration_list is not None:
            for k in self.configuration_list:
                result['ConfigurationList'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        self.configuration_list = []
        if m.get('ConfigurationList') is not None:
            for k in m.get('ConfigurationList'):
                temp_model = GetResourceConfigurationTimelineResponseBodyResourceConfigurationTimelineConfigurationList()
                self.configuration_list.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class GetResourceConfigurationTimelineResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        resource_configuration_timeline: GetResourceConfigurationTimelineResponseBodyResourceConfigurationTimeline = None,
    ):
        self.request_id = request_id
        self.resource_configuration_timeline = resource_configuration_timeline

    def validate(self):
        if self.resource_configuration_timeline:
            self.resource_configuration_timeline.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_configuration_timeline is not None:
            result['ResourceConfigurationTimeline'] = self.resource_configuration_timeline.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceConfigurationTimeline') is not None:
            temp_model = GetResourceConfigurationTimelineResponseBodyResourceConfigurationTimeline()
            self.resource_configuration_timeline = temp_model.from_map(m['ResourceConfigurationTimeline'])
        return self


class GetResourceConfigurationTimelineResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetResourceConfigurationTimelineResponseBody = None,
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
            temp_model = GetResourceConfigurationTimelineResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSupportedResourceTypesResponseBody(TeaModel):
    def __init__(
        self,
        resource_types: List[str] = None,
        request_id: str = None,
    ):
        self.resource_types = resource_types
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_types is not None:
            result['ResourceTypes'] = self.resource_types
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceTypes') is not None:
            self.resource_types = m.get('ResourceTypes')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetSupportedResourceTypesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetSupportedResourceTypesResponseBody = None,
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
            temp_model = GetSupportedResourceTypesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListConfigRulesRequest(TeaModel):
    def __init__(
        self,
        config_rule_state: str = None,
        compliance_type: str = None,
        risk_level: int = None,
        message_type: str = None,
        page_number: int = None,
        page_size: int = None,
        multi_account: bool = None,
        member_id: int = None,
        config_rule_name: str = None,
    ):
        self.config_rule_state = config_rule_state
        self.compliance_type = compliance_type
        self.risk_level = risk_level
        self.message_type = message_type
        self.page_number = page_number
        self.page_size = page_size
        self.multi_account = multi_account
        self.member_id = member_id
        self.config_rule_name = config_rule_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_rule_state is not None:
            result['ConfigRuleState'] = self.config_rule_state
        if self.compliance_type is not None:
            result['ComplianceType'] = self.compliance_type
        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level
        if self.message_type is not None:
            result['MessageType'] = self.message_type
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.multi_account is not None:
            result['MultiAccount'] = self.multi_account
        if self.member_id is not None:
            result['MemberId'] = self.member_id
        if self.config_rule_name is not None:
            result['ConfigRuleName'] = self.config_rule_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigRuleState') is not None:
            self.config_rule_state = m.get('ConfigRuleState')
        if m.get('ComplianceType') is not None:
            self.compliance_type = m.get('ComplianceType')
        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')
        if m.get('MessageType') is not None:
            self.message_type = m.get('MessageType')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('MultiAccount') is not None:
            self.multi_account = m.get('MultiAccount')
        if m.get('MemberId') is not None:
            self.member_id = m.get('MemberId')
        if m.get('ConfigRuleName') is not None:
            self.config_rule_name = m.get('ConfigRuleName')
        return self


class ListConfigRulesResponseBodyConfigRulesConfigRuleListCompliance(TeaModel):
    def __init__(
        self,
        compliance_type: str = None,
        count: int = None,
    ):
        self.compliance_type = compliance_type
        self.count = count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compliance_type is not None:
            result['ComplianceType'] = self.compliance_type
        if self.count is not None:
            result['Count'] = self.count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComplianceType') is not None:
            self.compliance_type = m.get('ComplianceType')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        return self


class ListConfigRulesResponseBodyConfigRulesConfigRuleListCreateBy(TeaModel):
    def __init__(
        self,
        config_rule_scene_id: str = None,
        creator_name: str = None,
        creator_type: str = None,
        creator_id: str = None,
        config_rule_scene_name: str = None,
    ):
        self.config_rule_scene_id = config_rule_scene_id
        self.creator_name = creator_name
        self.creator_type = creator_type
        self.creator_id = creator_id
        self.config_rule_scene_name = config_rule_scene_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_rule_scene_id is not None:
            result['ConfigRuleSceneId'] = self.config_rule_scene_id
        if self.creator_name is not None:
            result['CreatorName'] = self.creator_name
        if self.creator_type is not None:
            result['CreatorType'] = self.creator_type
        if self.creator_id is not None:
            result['CreatorId'] = self.creator_id
        if self.config_rule_scene_name is not None:
            result['ConfigRuleSceneName'] = self.config_rule_scene_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigRuleSceneId') is not None:
            self.config_rule_scene_id = m.get('ConfigRuleSceneId')
        if m.get('CreatorName') is not None:
            self.creator_name = m.get('CreatorName')
        if m.get('CreatorType') is not None:
            self.creator_type = m.get('CreatorType')
        if m.get('CreatorId') is not None:
            self.creator_id = m.get('CreatorId')
        if m.get('ConfigRuleSceneName') is not None:
            self.config_rule_scene_name = m.get('ConfigRuleSceneName')
        return self


class ListConfigRulesResponseBodyConfigRulesConfigRuleList(TeaModel):
    def __init__(
        self,
        risk_level: int = None,
        source_owner: str = None,
        account_id: int = None,
        config_rule_state: str = None,
        compliance: ListConfigRulesResponseBodyConfigRulesConfigRuleListCompliance = None,
        source_identifier: str = None,
        config_rule_arn: str = None,
        description: str = None,
        create_by: ListConfigRulesResponseBodyConfigRulesConfigRuleListCreateBy = None,
        automation_type: str = None,
        config_rule_name: str = None,
        config_rule_id: str = None,
    ):
        self.risk_level = risk_level
        self.source_owner = source_owner
        self.account_id = account_id
        self.config_rule_state = config_rule_state
        self.compliance = compliance
        self.source_identifier = source_identifier
        self.config_rule_arn = config_rule_arn
        self.description = description
        self.create_by = create_by
        self.automation_type = automation_type
        self.config_rule_name = config_rule_name
        self.config_rule_id = config_rule_id

    def validate(self):
        if self.compliance:
            self.compliance.validate()
        if self.create_by:
            self.create_by.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level
        if self.source_owner is not None:
            result['SourceOwner'] = self.source_owner
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.config_rule_state is not None:
            result['ConfigRuleState'] = self.config_rule_state
        if self.compliance is not None:
            result['Compliance'] = self.compliance.to_map()
        if self.source_identifier is not None:
            result['SourceIdentifier'] = self.source_identifier
        if self.config_rule_arn is not None:
            result['ConfigRuleArn'] = self.config_rule_arn
        if self.description is not None:
            result['Description'] = self.description
        if self.create_by is not None:
            result['CreateBy'] = self.create_by.to_map()
        if self.automation_type is not None:
            result['AutomationType'] = self.automation_type
        if self.config_rule_name is not None:
            result['ConfigRuleName'] = self.config_rule_name
        if self.config_rule_id is not None:
            result['ConfigRuleId'] = self.config_rule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')
        if m.get('SourceOwner') is not None:
            self.source_owner = m.get('SourceOwner')
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('ConfigRuleState') is not None:
            self.config_rule_state = m.get('ConfigRuleState')
        if m.get('Compliance') is not None:
            temp_model = ListConfigRulesResponseBodyConfigRulesConfigRuleListCompliance()
            self.compliance = temp_model.from_map(m['Compliance'])
        if m.get('SourceIdentifier') is not None:
            self.source_identifier = m.get('SourceIdentifier')
        if m.get('ConfigRuleArn') is not None:
            self.config_rule_arn = m.get('ConfigRuleArn')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('CreateBy') is not None:
            temp_model = ListConfigRulesResponseBodyConfigRulesConfigRuleListCreateBy()
            self.create_by = temp_model.from_map(m['CreateBy'])
        if m.get('AutomationType') is not None:
            self.automation_type = m.get('AutomationType')
        if m.get('ConfigRuleName') is not None:
            self.config_rule_name = m.get('ConfigRuleName')
        if m.get('ConfigRuleId') is not None:
            self.config_rule_id = m.get('ConfigRuleId')
        return self


class ListConfigRulesResponseBodyConfigRules(TeaModel):
    def __init__(
        self,
        config_rule_list: List[ListConfigRulesResponseBodyConfigRulesConfigRuleList] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.config_rule_list = config_rule_list
        self.page_number = page_number
        self.page_size = page_size
        self.total_count = total_count

    def validate(self):
        if self.config_rule_list:
            for k in self.config_rule_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ConfigRuleList'] = []
        if self.config_rule_list is not None:
            for k in self.config_rule_list:
                result['ConfigRuleList'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.config_rule_list = []
        if m.get('ConfigRuleList') is not None:
            for k in m.get('ConfigRuleList'):
                temp_model = ListConfigRulesResponseBodyConfigRulesConfigRuleList()
                self.config_rule_list.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListConfigRulesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        config_rules: ListConfigRulesResponseBodyConfigRules = None,
    ):
        self.request_id = request_id
        self.config_rules = config_rules

    def validate(self):
        if self.config_rules:
            self.config_rules.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.config_rules is not None:
            result['ConfigRules'] = self.config_rules.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ConfigRules') is not None:
            temp_model = ListConfigRulesResponseBodyConfigRules()
            self.config_rules = temp_model.from_map(m['ConfigRules'])
        return self


class ListConfigRulesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListConfigRulesResponseBody = None,
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
            temp_model = ListConfigRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDiscoveredResourcesRequest(TeaModel):
    def __init__(
        self,
        resource_id: str = None,
        resource_deleted: int = None,
        page_size: int = None,
        page_number: int = None,
        resource_types: str = None,
        regions: str = None,
        compliance_type: str = None,
        multi_account: bool = None,
        member_id: int = None,
    ):
        self.resource_id = resource_id
        self.resource_deleted = resource_deleted
        self.page_size = page_size
        self.page_number = page_number
        self.resource_types = resource_types
        self.regions = regions
        self.compliance_type = compliance_type
        self.multi_account = multi_account
        self.member_id = member_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_deleted is not None:
            result['ResourceDeleted'] = self.resource_deleted
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.resource_types is not None:
            result['ResourceTypes'] = self.resource_types
        if self.regions is not None:
            result['Regions'] = self.regions
        if self.compliance_type is not None:
            result['ComplianceType'] = self.compliance_type
        if self.multi_account is not None:
            result['MultiAccount'] = self.multi_account
        if self.member_id is not None:
            result['MemberId'] = self.member_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceDeleted') is not None:
            self.resource_deleted = m.get('ResourceDeleted')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('ResourceTypes') is not None:
            self.resource_types = m.get('ResourceTypes')
        if m.get('Regions') is not None:
            self.regions = m.get('Regions')
        if m.get('ComplianceType') is not None:
            self.compliance_type = m.get('ComplianceType')
        if m.get('MultiAccount') is not None:
            self.multi_account = m.get('MultiAccount')
        if m.get('MemberId') is not None:
            self.member_id = m.get('MemberId')
        return self


class ListDiscoveredResourcesResponseBodyDiscoveredResourceProfilesDiscoveredResourceProfileList(TeaModel):
    def __init__(
        self,
        resource_type: str = None,
        region: str = None,
        resource_creation_time: int = None,
        tags: str = None,
        account_id: int = None,
        resource_id: str = None,
        resource_name: str = None,
        resource_deleted: int = None,
        resource_status: str = None,
    ):
        self.resource_type = resource_type
        self.region = region
        self.resource_creation_time = resource_creation_time
        self.tags = tags
        self.account_id = account_id
        self.resource_id = resource_id
        self.resource_name = resource_name
        self.resource_deleted = resource_deleted
        self.resource_status = resource_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.region is not None:
            result['Region'] = self.region
        if self.resource_creation_time is not None:
            result['ResourceCreationTime'] = self.resource_creation_time
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name
        if self.resource_deleted is not None:
            result['ResourceDeleted'] = self.resource_deleted
        if self.resource_status is not None:
            result['ResourceStatus'] = self.resource_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('ResourceCreationTime') is not None:
            self.resource_creation_time = m.get('ResourceCreationTime')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')
        if m.get('ResourceDeleted') is not None:
            self.resource_deleted = m.get('ResourceDeleted')
        if m.get('ResourceStatus') is not None:
            self.resource_status = m.get('ResourceStatus')
        return self


class ListDiscoveredResourcesResponseBodyDiscoveredResourceProfiles(TeaModel):
    def __init__(
        self,
        discovered_resource_profile_list: List[ListDiscoveredResourcesResponseBodyDiscoveredResourceProfilesDiscoveredResourceProfileList] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.discovered_resource_profile_list = discovered_resource_profile_list
        self.page_number = page_number
        self.page_size = page_size
        self.total_count = total_count

    def validate(self):
        if self.discovered_resource_profile_list:
            for k in self.discovered_resource_profile_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DiscoveredResourceProfileList'] = []
        if self.discovered_resource_profile_list is not None:
            for k in self.discovered_resource_profile_list:
                result['DiscoveredResourceProfileList'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.discovered_resource_profile_list = []
        if m.get('DiscoveredResourceProfileList') is not None:
            for k in m.get('DiscoveredResourceProfileList'):
                temp_model = ListDiscoveredResourcesResponseBodyDiscoveredResourceProfilesDiscoveredResourceProfileList()
                self.discovered_resource_profile_list.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListDiscoveredResourcesResponseBody(TeaModel):
    def __init__(
        self,
        discovered_resource_profiles: ListDiscoveredResourcesResponseBodyDiscoveredResourceProfiles = None,
        request_id: str = None,
    ):
        self.discovered_resource_profiles = discovered_resource_profiles
        self.request_id = request_id

    def validate(self):
        if self.discovered_resource_profiles:
            self.discovered_resource_profiles.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.discovered_resource_profiles is not None:
            result['DiscoveredResourceProfiles'] = self.discovered_resource_profiles.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DiscoveredResourceProfiles') is not None:
            temp_model = ListDiscoveredResourcesResponseBodyDiscoveredResourceProfiles()
            self.discovered_resource_profiles = temp_model.from_map(m['DiscoveredResourceProfiles'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListDiscoveredResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListDiscoveredResourcesResponseBody = None,
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
            temp_model = ListDiscoveredResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PutConfigRuleRequest(TeaModel):
    def __init__(
        self,
        config_rule_id: str = None,
        config_rule_name: str = None,
        description: str = None,
        input_parameters: str = None,
        source_owner: str = None,
        source_identifier: str = None,
        source_detail_message_type: str = None,
        source_maximum_execution_frequency: str = None,
        scope_compliance_resource_id: str = None,
        scope_compliance_resource_types: str = None,
        risk_level: int = None,
        client_token: str = None,
        multi_account: bool = None,
        member_id: int = None,
        scope_compliance_resource_ids: str = None,
        scope_compliance_exclude_resource_ids: str = None,
        scope_compliance_region_ids: str = None,
    ):
        self.config_rule_id = config_rule_id
        self.config_rule_name = config_rule_name
        self.description = description
        self.input_parameters = input_parameters
        self.source_owner = source_owner
        self.source_identifier = source_identifier
        self.source_detail_message_type = source_detail_message_type
        self.source_maximum_execution_frequency = source_maximum_execution_frequency
        self.scope_compliance_resource_id = scope_compliance_resource_id
        self.scope_compliance_resource_types = scope_compliance_resource_types
        self.risk_level = risk_level
        self.client_token = client_token
        self.multi_account = multi_account
        self.member_id = member_id
        self.scope_compliance_resource_ids = scope_compliance_resource_ids
        self.scope_compliance_exclude_resource_ids = scope_compliance_exclude_resource_ids
        self.scope_compliance_region_ids = scope_compliance_region_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_rule_id is not None:
            result['ConfigRuleId'] = self.config_rule_id
        if self.config_rule_name is not None:
            result['ConfigRuleName'] = self.config_rule_name
        if self.description is not None:
            result['Description'] = self.description
        if self.input_parameters is not None:
            result['InputParameters'] = self.input_parameters
        if self.source_owner is not None:
            result['SourceOwner'] = self.source_owner
        if self.source_identifier is not None:
            result['SourceIdentifier'] = self.source_identifier
        if self.source_detail_message_type is not None:
            result['SourceDetailMessageType'] = self.source_detail_message_type
        if self.source_maximum_execution_frequency is not None:
            result['SourceMaximumExecutionFrequency'] = self.source_maximum_execution_frequency
        if self.scope_compliance_resource_id is not None:
            result['ScopeComplianceResourceId'] = self.scope_compliance_resource_id
        if self.scope_compliance_resource_types is not None:
            result['ScopeComplianceResourceTypes'] = self.scope_compliance_resource_types
        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.multi_account is not None:
            result['MultiAccount'] = self.multi_account
        if self.member_id is not None:
            result['MemberId'] = self.member_id
        if self.scope_compliance_resource_ids is not None:
            result['ScopeComplianceResourceIds'] = self.scope_compliance_resource_ids
        if self.scope_compliance_exclude_resource_ids is not None:
            result['ScopeComplianceExcludeResourceIds'] = self.scope_compliance_exclude_resource_ids
        if self.scope_compliance_region_ids is not None:
            result['ScopeComplianceRegionIds'] = self.scope_compliance_region_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigRuleId') is not None:
            self.config_rule_id = m.get('ConfigRuleId')
        if m.get('ConfigRuleName') is not None:
            self.config_rule_name = m.get('ConfigRuleName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('InputParameters') is not None:
            self.input_parameters = m.get('InputParameters')
        if m.get('SourceOwner') is not None:
            self.source_owner = m.get('SourceOwner')
        if m.get('SourceIdentifier') is not None:
            self.source_identifier = m.get('SourceIdentifier')
        if m.get('SourceDetailMessageType') is not None:
            self.source_detail_message_type = m.get('SourceDetailMessageType')
        if m.get('SourceMaximumExecutionFrequency') is not None:
            self.source_maximum_execution_frequency = m.get('SourceMaximumExecutionFrequency')
        if m.get('ScopeComplianceResourceId') is not None:
            self.scope_compliance_resource_id = m.get('ScopeComplianceResourceId')
        if m.get('ScopeComplianceResourceTypes') is not None:
            self.scope_compliance_resource_types = m.get('ScopeComplianceResourceTypes')
        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('MultiAccount') is not None:
            self.multi_account = m.get('MultiAccount')
        if m.get('MemberId') is not None:
            self.member_id = m.get('MemberId')
        if m.get('ScopeComplianceResourceIds') is not None:
            self.scope_compliance_resource_ids = m.get('ScopeComplianceResourceIds')
        if m.get('ScopeComplianceExcludeResourceIds') is not None:
            self.scope_compliance_exclude_resource_ids = m.get('ScopeComplianceExcludeResourceIds')
        if m.get('ScopeComplianceRegionIds') is not None:
            self.scope_compliance_region_ids = m.get('ScopeComplianceRegionIds')
        return self


class PutConfigRuleResponseBody(TeaModel):
    def __init__(
        self,
        config_rule_id: str = None,
        request_id: str = None,
    ):
        self.config_rule_id = config_rule_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_rule_id is not None:
            result['ConfigRuleId'] = self.config_rule_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigRuleId') is not None:
            self.config_rule_id = m.get('ConfigRuleId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class PutConfigRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: PutConfigRuleResponseBody = None,
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
            temp_model = PutConfigRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PutConfigurationRecorderRequest(TeaModel):
    def __init__(
        self,
        resource_types: str = None,
    ):
        self.resource_types = resource_types

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_types is not None:
            result['ResourceTypes'] = self.resource_types
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceTypes') is not None:
            self.resource_types = m.get('ResourceTypes')
        return self


class PutConfigurationRecorderResponseBodyConfigurationRecorder(TeaModel):
    def __init__(
        self,
        configuration_recorder_status: str = None,
        account_id: int = None,
        resource_types: List[str] = None,
    ):
        self.configuration_recorder_status = configuration_recorder_status
        self.account_id = account_id
        self.resource_types = resource_types

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.configuration_recorder_status is not None:
            result['ConfigurationRecorderStatus'] = self.configuration_recorder_status
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.resource_types is not None:
            result['ResourceTypes'] = self.resource_types
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigurationRecorderStatus') is not None:
            self.configuration_recorder_status = m.get('ConfigurationRecorderStatus')
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('ResourceTypes') is not None:
            self.resource_types = m.get('ResourceTypes')
        return self


class PutConfigurationRecorderResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        configuration_recorder: PutConfigurationRecorderResponseBodyConfigurationRecorder = None,
    ):
        self.request_id = request_id
        self.configuration_recorder = configuration_recorder

    def validate(self):
        if self.configuration_recorder:
            self.configuration_recorder.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.configuration_recorder is not None:
            result['ConfigurationRecorder'] = self.configuration_recorder.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ConfigurationRecorder') is not None:
            temp_model = PutConfigurationRecorderResponseBodyConfigurationRecorder()
            self.configuration_recorder = temp_model.from_map(m['ConfigurationRecorder'])
        return self


class PutConfigurationRecorderResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: PutConfigurationRecorderResponseBody = None,
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
            temp_model = PutConfigurationRecorderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PutDeliveryChannelRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        delivery_channel_id: str = None,
        delivery_channel_name: str = None,
        delivery_channel_type: str = None,
        delivery_channel_target_arn: str = None,
        delivery_channel_assume_role_arn: str = None,
        delivery_channel_condition: str = None,
        description: str = None,
        status: int = None,
    ):
        self.client_token = client_token
        self.delivery_channel_id = delivery_channel_id
        self.delivery_channel_name = delivery_channel_name
        self.delivery_channel_type = delivery_channel_type
        self.delivery_channel_target_arn = delivery_channel_target_arn
        self.delivery_channel_assume_role_arn = delivery_channel_assume_role_arn
        self.delivery_channel_condition = delivery_channel_condition
        self.description = description
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.delivery_channel_id is not None:
            result['DeliveryChannelId'] = self.delivery_channel_id
        if self.delivery_channel_name is not None:
            result['DeliveryChannelName'] = self.delivery_channel_name
        if self.delivery_channel_type is not None:
            result['DeliveryChannelType'] = self.delivery_channel_type
        if self.delivery_channel_target_arn is not None:
            result['DeliveryChannelTargetArn'] = self.delivery_channel_target_arn
        if self.delivery_channel_assume_role_arn is not None:
            result['DeliveryChannelAssumeRoleArn'] = self.delivery_channel_assume_role_arn
        if self.delivery_channel_condition is not None:
            result['DeliveryChannelCondition'] = self.delivery_channel_condition
        if self.description is not None:
            result['Description'] = self.description
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DeliveryChannelId') is not None:
            self.delivery_channel_id = m.get('DeliveryChannelId')
        if m.get('DeliveryChannelName') is not None:
            self.delivery_channel_name = m.get('DeliveryChannelName')
        if m.get('DeliveryChannelType') is not None:
            self.delivery_channel_type = m.get('DeliveryChannelType')
        if m.get('DeliveryChannelTargetArn') is not None:
            self.delivery_channel_target_arn = m.get('DeliveryChannelTargetArn')
        if m.get('DeliveryChannelAssumeRoleArn') is not None:
            self.delivery_channel_assume_role_arn = m.get('DeliveryChannelAssumeRoleArn')
        if m.get('DeliveryChannelCondition') is not None:
            self.delivery_channel_condition = m.get('DeliveryChannelCondition')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class PutDeliveryChannelResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        delivery_channel_id: str = None,
    ):
        self.request_id = request_id
        self.delivery_channel_id = delivery_channel_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.delivery_channel_id is not None:
            result['DeliveryChannelId'] = self.delivery_channel_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DeliveryChannelId') is not None:
            self.delivery_channel_id = m.get('DeliveryChannelId')
        return self


class PutDeliveryChannelResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: PutDeliveryChannelResponseBody = None,
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
            temp_model = PutDeliveryChannelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PutEvaluationsRequest(TeaModel):
    def __init__(
        self,
        result_token: str = None,
        evaluations: str = None,
    ):
        self.result_token = result_token
        self.evaluations = evaluations

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result_token is not None:
            result['ResultToken'] = self.result_token
        if self.evaluations is not None:
            result['Evaluations'] = self.evaluations
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResultToken') is not None:
            self.result_token = m.get('ResultToken')
        if m.get('Evaluations') is not None:
            self.evaluations = m.get('Evaluations')
        return self


class PutEvaluationsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: bool = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class PutEvaluationsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: PutEvaluationsResponseBody = None,
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
            temp_model = PutEvaluationsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartConfigRuleEvaluationRequest(TeaModel):
    def __init__(
        self,
        config_rule_id: str = None,
        multi_account: bool = None,
        member_id: int = None,
    ):
        self.config_rule_id = config_rule_id
        self.multi_account = multi_account
        self.member_id = member_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_rule_id is not None:
            result['ConfigRuleId'] = self.config_rule_id
        if self.multi_account is not None:
            result['MultiAccount'] = self.multi_account
        if self.member_id is not None:
            result['MemberId'] = self.member_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigRuleId') is not None:
            self.config_rule_id = m.get('ConfigRuleId')
        if m.get('MultiAccount') is not None:
            self.multi_account = m.get('MultiAccount')
        if m.get('MemberId') is not None:
            self.member_id = m.get('MemberId')
        return self


class StartConfigRuleEvaluationResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: bool = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class StartConfigRuleEvaluationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: StartConfigRuleEvaluationResponseBody = None,
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
            temp_model = StartConfigRuleEvaluationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartConfigurationRecorderRequest(TeaModel):
    def __init__(
        self,
        enterprise_edition: bool = None,
    ):
        self.enterprise_edition = enterprise_edition

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enterprise_edition is not None:
            result['EnterpriseEdition'] = self.enterprise_edition
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnterpriseEdition') is not None:
            self.enterprise_edition = m.get('EnterpriseEdition')
        return self


class StartConfigurationRecorderResponseBodyConfigurationRecorder(TeaModel):
    def __init__(
        self,
        organization_enable_status: str = None,
        configuration_recorder_status: str = None,
        organization_master_id: int = None,
        account_id: int = None,
        resource_types: List[str] = None,
    ):
        self.organization_enable_status = organization_enable_status
        self.configuration_recorder_status = configuration_recorder_status
        self.organization_master_id = organization_master_id
        self.account_id = account_id
        self.resource_types = resource_types

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.organization_enable_status is not None:
            result['OrganizationEnableStatus'] = self.organization_enable_status
        if self.configuration_recorder_status is not None:
            result['ConfigurationRecorderStatus'] = self.configuration_recorder_status
        if self.organization_master_id is not None:
            result['OrganizationMasterId'] = self.organization_master_id
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.resource_types is not None:
            result['ResourceTypes'] = self.resource_types
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrganizationEnableStatus') is not None:
            self.organization_enable_status = m.get('OrganizationEnableStatus')
        if m.get('ConfigurationRecorderStatus') is not None:
            self.configuration_recorder_status = m.get('ConfigurationRecorderStatus')
        if m.get('OrganizationMasterId') is not None:
            self.organization_master_id = m.get('OrganizationMasterId')
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('ResourceTypes') is not None:
            self.resource_types = m.get('ResourceTypes')
        return self


class StartConfigurationRecorderResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        configuration_recorder: StartConfigurationRecorderResponseBodyConfigurationRecorder = None,
    ):
        self.request_id = request_id
        self.configuration_recorder = configuration_recorder

    def validate(self):
        if self.configuration_recorder:
            self.configuration_recorder.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.configuration_recorder is not None:
            result['ConfigurationRecorder'] = self.configuration_recorder.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ConfigurationRecorder') is not None:
            temp_model = StartConfigurationRecorderResponseBodyConfigurationRecorder()
            self.configuration_recorder = temp_model.from_map(m['ConfigurationRecorder'])
        return self


class StartConfigurationRecorderResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: StartConfigurationRecorderResponseBody = None,
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
            temp_model = StartConfigurationRecorderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopConfigRulesRequest(TeaModel):
    def __init__(
        self,
        config_rule_ids: str = None,
    ):
        self.config_rule_ids = config_rule_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_rule_ids is not None:
            result['ConfigRuleIds'] = self.config_rule_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigRuleIds') is not None:
            self.config_rule_ids = m.get('ConfigRuleIds')
        return self


class StopConfigRulesResponseBodyOperateRuleResultOperateRuleItemList(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        success: bool = None,
        config_rule_id: str = None,
    ):
        self.error_code = error_code
        self.success = success
        self.config_rule_id = config_rule_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        if self.config_rule_id is not None:
            result['ConfigRuleId'] = self.config_rule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ConfigRuleId') is not None:
            self.config_rule_id = m.get('ConfigRuleId')
        return self


class StopConfigRulesResponseBodyOperateRuleResult(TeaModel):
    def __init__(
        self,
        operate_rule_item_list: List[StopConfigRulesResponseBodyOperateRuleResultOperateRuleItemList] = None,
    ):
        self.operate_rule_item_list = operate_rule_item_list

    def validate(self):
        if self.operate_rule_item_list:
            for k in self.operate_rule_item_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['OperateRuleItemList'] = []
        if self.operate_rule_item_list is not None:
            for k in self.operate_rule_item_list:
                result['OperateRuleItemList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.operate_rule_item_list = []
        if m.get('OperateRuleItemList') is not None:
            for k in m.get('OperateRuleItemList'):
                temp_model = StopConfigRulesResponseBodyOperateRuleResultOperateRuleItemList()
                self.operate_rule_item_list.append(temp_model.from_map(k))
        return self


class StopConfigRulesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        operate_rule_result: StopConfigRulesResponseBodyOperateRuleResult = None,
    ):
        self.request_id = request_id
        self.operate_rule_result = operate_rule_result

    def validate(self):
        if self.operate_rule_result:
            self.operate_rule_result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.operate_rule_result is not None:
            result['OperateRuleResult'] = self.operate_rule_result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('OperateRuleResult') is not None:
            temp_model = StopConfigRulesResponseBodyOperateRuleResult()
            self.operate_rule_result = temp_model.from_map(m['OperateRuleResult'])
        return self


class StopConfigRulesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: StopConfigRulesResponseBody = None,
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
            temp_model = StopConfigRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


