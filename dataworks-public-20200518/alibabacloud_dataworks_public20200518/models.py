# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
try:
    from typing import List, Dict, Any
except ImportError:
    pass


class ListQualityResultsByEntityRequest(TeaModel):
    def __init__(self, entity_id=None, start_date=None, end_date=None, page_size=None, page_number=None,
                 project_name=None):
        self.entity_id = entity_id      # type: int
        self.start_date = start_date    # type: str
        self.end_date = end_date        # type: str
        self.page_size = page_size      # type: int
        self.page_number = page_number  # type: int
        self.project_name = project_name  # type: str

    def validate(self):
        self.validate_required(self.entity_id, 'entity_id')
        self.validate_required(self.start_date, 'start_date')
        self.validate_required(self.end_date, 'end_date')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.project_name, 'project_name')

    def to_map(self):
        result = {}
        result['EntityId'] = self.entity_id
        result['StartDate'] = self.start_date
        result['EndDate'] = self.end_date
        result['PageSize'] = self.page_size
        result['PageNumber'] = self.page_number
        result['ProjectName'] = self.project_name
        return result

    def from_map(self, map={}):
        self.entity_id = map.get('EntityId')
        self.start_date = map.get('StartDate')
        self.end_date = map.get('EndDate')
        self.page_size = map.get('PageSize')
        self.page_number = map.get('PageNumber')
        self.project_name = map.get('ProjectName')
        return self


class ListQualityResultsByEntityResponse(TeaModel):
    def __init__(self, request_id=None, quality_results=None):
        self.request_id = request_id    # type: str
        self.quality_results = quality_results  # type: ListQualityResultsByEntityResponseQualityResults

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.quality_results, 'quality_results')
        if self.quality_results:
            self.quality_results.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        if self.quality_results is not None:
            result['QualityResults'] = self.quality_results.to_map()
        else:
            result['QualityResults'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('QualityResults') is not None:
            temp_model = ListQualityResultsByEntityResponseQualityResults()
            self.quality_results = temp_model.from_map(map['QualityResults'])
        else:
            self.quality_results = None
        return self


class ListQualityResultsByEntityResponseQualityResultsRuleChecksReferenceValue(TeaModel):
    def __init__(self, biz_date=None, discrete_property=None, value=None, threshold=None, single_check_result=None):
        self.biz_date = biz_date        # type: int
        self.discrete_property = discrete_property  # type: str
        self.value = value              # type: float
        self.threshold = threshold      # type: float
        self.single_check_result = single_check_result  # type: int

    def validate(self):
        self.validate_required(self.biz_date, 'biz_date')
        self.validate_required(self.discrete_property, 'discrete_property')
        self.validate_required(self.value, 'value')
        self.validate_required(self.threshold, 'threshold')
        self.validate_required(self.single_check_result, 'single_check_result')

    def to_map(self):
        result = {}
        result['BizDate'] = self.biz_date
        result['DiscreteProperty'] = self.discrete_property
        result['Value'] = self.value
        result['Threshold'] = self.threshold
        result['SingleCheckResult'] = self.single_check_result
        return result

    def from_map(self, map={}):
        self.biz_date = map.get('BizDate')
        self.discrete_property = map.get('DiscreteProperty')
        self.value = map.get('Value')
        self.threshold = map.get('Threshold')
        self.single_check_result = map.get('SingleCheckResult')
        return self


class ListQualityResultsByEntityResponseQualityResultsRuleChecksSampleValue(TeaModel):
    def __init__(self, biz_date=None, discrete_property=None, value=None):
        self.biz_date = biz_date        # type: int
        self.discrete_property = discrete_property  # type: str
        self.value = value              # type: float

    def validate(self):
        self.validate_required(self.biz_date, 'biz_date')
        self.validate_required(self.discrete_property, 'discrete_property')
        self.validate_required(self.value, 'value')

    def to_map(self):
        result = {}
        result['BizDate'] = self.biz_date
        result['DiscreteProperty'] = self.discrete_property
        result['Value'] = self.value
        return result

    def from_map(self, map={}):
        self.biz_date = map.get('BizDate')
        self.discrete_property = map.get('DiscreteProperty')
        self.value = map.get('Value')
        return self


class ListQualityResultsByEntityResponseQualityResultsRuleChecks(TeaModel):
    def __init__(self, id=None, task_id=None, entity_id=None, rule_id=None, property=None, biz_date=None,
                 date_type=None, actual_expression=None, match_expression=None, block_type=None, check_result=None,
                 check_result_status=None, method_name=None, comment=None, where_condition=None, begin_time=None, end_time=None,
                 time_cost=None, external_type=None, external_id=None, discrete_check=None, fixed_check=None, trend=None,
                 warning_threshold=None, critical_threshold=None, expect_value=None, op=None, project_name=None, table_name=None,
                 template_id=None, template_name=None, result_string=None, checker_id=None, checker_type=None, rule_name=None,
                 is_prediction=None, upper_value=None, lower_value=None, checker_name=None, reference_value=None,
                 sample_value=None):
        self.id = id                    # type: int
        self.task_id = task_id          # type: str
        self.entity_id = entity_id      # type: int
        self.rule_id = rule_id          # type: int
        self.property = property        # type: str
        self.biz_date = biz_date        # type: int
        self.date_type = date_type      # type: str
        self.actual_expression = actual_expression  # type: str
        self.match_expression = match_expression  # type: str
        self.block_type = block_type    # type: int
        self.check_result = check_result  # type: int
        self.check_result_status = check_result_status  # type: int
        self.method_name = method_name  # type: str
        self.comment = comment          # type: str
        self.where_condition = where_condition  # type: str
        self.begin_time = begin_time    # type: int
        self.end_time = end_time        # type: int
        self.time_cost = time_cost      # type: str
        self.external_type = external_type  # type: str
        self.external_id = external_id  # type: str
        self.discrete_check = discrete_check  # type: bool
        self.fixed_check = fixed_check  # type: bool
        self.trend = trend              # type: str
        self.warning_threshold = warning_threshold  # type: float
        self.critical_threshold = critical_threshold  # type: float
        self.expect_value = expect_value  # type: float
        self.op = op                    # type: str
        self.project_name = project_name  # type: str
        self.table_name = table_name    # type: str
        self.template_id = template_id  # type: int
        self.template_name = template_name  # type: str
        self.result_string = result_string  # type: str
        self.checker_id = checker_id    # type: int
        self.checker_type = checker_type  # type: int
        self.rule_name = rule_name      # type: str
        self.is_prediction = is_prediction  # type: bool
        self.upper_value = upper_value  # type: float
        self.lower_value = lower_value  # type: float
        self.checker_name = checker_name  # type: str
        self.reference_value = reference_value  # type: List[ListQualityResultsByEntityResponseQualityResultsRuleChecksReferenceValue]
        self.sample_value = sample_value  # type: List[ListQualityResultsByEntityResponseQualityResultsRuleChecksSampleValue]

    def validate(self):
        self.validate_required(self.id, 'id')
        self.validate_required(self.task_id, 'task_id')
        self.validate_required(self.entity_id, 'entity_id')
        self.validate_required(self.rule_id, 'rule_id')
        self.validate_required(self.property, 'property')
        self.validate_required(self.biz_date, 'biz_date')
        self.validate_required(self.date_type, 'date_type')
        self.validate_required(self.actual_expression, 'actual_expression')
        self.validate_required(self.match_expression, 'match_expression')
        self.validate_required(self.block_type, 'block_type')
        self.validate_required(self.check_result, 'check_result')
        self.validate_required(self.check_result_status, 'check_result_status')
        self.validate_required(self.method_name, 'method_name')
        self.validate_required(self.comment, 'comment')
        self.validate_required(self.where_condition, 'where_condition')
        self.validate_required(self.begin_time, 'begin_time')
        self.validate_required(self.end_time, 'end_time')
        self.validate_required(self.time_cost, 'time_cost')
        self.validate_required(self.external_type, 'external_type')
        self.validate_required(self.external_id, 'external_id')
        self.validate_required(self.discrete_check, 'discrete_check')
        self.validate_required(self.fixed_check, 'fixed_check')
        self.validate_required(self.trend, 'trend')
        self.validate_required(self.warning_threshold, 'warning_threshold')
        self.validate_required(self.critical_threshold, 'critical_threshold')
        self.validate_required(self.expect_value, 'expect_value')
        self.validate_required(self.op, 'op')
        self.validate_required(self.project_name, 'project_name')
        self.validate_required(self.table_name, 'table_name')
        self.validate_required(self.template_id, 'template_id')
        self.validate_required(self.template_name, 'template_name')
        self.validate_required(self.result_string, 'result_string')
        self.validate_required(self.checker_id, 'checker_id')
        self.validate_required(self.checker_type, 'checker_type')
        self.validate_required(self.rule_name, 'rule_name')
        self.validate_required(self.is_prediction, 'is_prediction')
        self.validate_required(self.upper_value, 'upper_value')
        self.validate_required(self.lower_value, 'lower_value')
        self.validate_required(self.checker_name, 'checker_name')
        self.validate_required(self.reference_value, 'reference_value')
        if self.reference_value:
            for k in self.reference_value:
                if k:
                    k.validate()
        self.validate_required(self.sample_value, 'sample_value')
        if self.sample_value:
            for k in self.sample_value:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['Id'] = self.id
        result['TaskId'] = self.task_id
        result['EntityId'] = self.entity_id
        result['RuleId'] = self.rule_id
        result['Property'] = self.property
        result['BizDate'] = self.biz_date
        result['DateType'] = self.date_type
        result['ActualExpression'] = self.actual_expression
        result['MatchExpression'] = self.match_expression
        result['BlockType'] = self.block_type
        result['CheckResult'] = self.check_result
        result['CheckResultStatus'] = self.check_result_status
        result['MethodName'] = self.method_name
        result['Comment'] = self.comment
        result['WhereCondition'] = self.where_condition
        result['BeginTime'] = self.begin_time
        result['EndTime'] = self.end_time
        result['TimeCost'] = self.time_cost
        result['ExternalType'] = self.external_type
        result['ExternalId'] = self.external_id
        result['DiscreteCheck'] = self.discrete_check
        result['FixedCheck'] = self.fixed_check
        result['Trend'] = self.trend
        result['WarningThreshold'] = self.warning_threshold
        result['CriticalThreshold'] = self.critical_threshold
        result['ExpectValue'] = self.expect_value
        result['Op'] = self.op
        result['ProjectName'] = self.project_name
        result['TableName'] = self.table_name
        result['TemplateId'] = self.template_id
        result['TemplateName'] = self.template_name
        result['ResultString'] = self.result_string
        result['CheckerId'] = self.checker_id
        result['CheckerType'] = self.checker_type
        result['RuleName'] = self.rule_name
        result['IsPrediction'] = self.is_prediction
        result['UpperValue'] = self.upper_value
        result['LowerValue'] = self.lower_value
        result['CheckerName'] = self.checker_name
        result['ReferenceValue'] = []
        if self.reference_value is not None:
            for k in self.reference_value:
                result['ReferenceValue'].append(k.to_map() if k else None)
        else:
            result['ReferenceValue'] = None
        result['SampleValue'] = []
        if self.sample_value is not None:
            for k in self.sample_value:
                result['SampleValue'].append(k.to_map() if k else None)
        else:
            result['SampleValue'] = None
        return result

    def from_map(self, map={}):
        self.id = map.get('Id')
        self.task_id = map.get('TaskId')
        self.entity_id = map.get('EntityId')
        self.rule_id = map.get('RuleId')
        self.property = map.get('Property')
        self.biz_date = map.get('BizDate')
        self.date_type = map.get('DateType')
        self.actual_expression = map.get('ActualExpression')
        self.match_expression = map.get('MatchExpression')
        self.block_type = map.get('BlockType')
        self.check_result = map.get('CheckResult')
        self.check_result_status = map.get('CheckResultStatus')
        self.method_name = map.get('MethodName')
        self.comment = map.get('Comment')
        self.where_condition = map.get('WhereCondition')
        self.begin_time = map.get('BeginTime')
        self.end_time = map.get('EndTime')
        self.time_cost = map.get('TimeCost')
        self.external_type = map.get('ExternalType')
        self.external_id = map.get('ExternalId')
        self.discrete_check = map.get('DiscreteCheck')
        self.fixed_check = map.get('FixedCheck')
        self.trend = map.get('Trend')
        self.warning_threshold = map.get('WarningThreshold')
        self.critical_threshold = map.get('CriticalThreshold')
        self.expect_value = map.get('ExpectValue')
        self.op = map.get('Op')
        self.project_name = map.get('ProjectName')
        self.table_name = map.get('TableName')
        self.template_id = map.get('TemplateId')
        self.template_name = map.get('TemplateName')
        self.result_string = map.get('ResultString')
        self.checker_id = map.get('CheckerId')
        self.checker_type = map.get('CheckerType')
        self.rule_name = map.get('RuleName')
        self.is_prediction = map.get('IsPrediction')
        self.upper_value = map.get('UpperValue')
        self.lower_value = map.get('LowerValue')
        self.checker_name = map.get('CheckerName')
        self.reference_value = []
        if map.get('ReferenceValue') is not None:
            for k in map.get('ReferenceValue'):
                temp_model = ListQualityResultsByEntityResponseQualityResultsRuleChecksReferenceValue()
                self.reference_value.append(temp_model.from_map(k))
        else:
            self.reference_value = None
        self.sample_value = []
        if map.get('SampleValue') is not None:
            for k in map.get('SampleValue'):
                temp_model = ListQualityResultsByEntityResponseQualityResultsRuleChecksSampleValue()
                self.sample_value.append(temp_model.from_map(k))
        else:
            self.sample_value = None
        return self


class ListQualityResultsByEntityResponseQualityResults(TeaModel):
    def __init__(self, total_count=None, page_number=None, page_size=None, rule_checks=None):
        self.total_count = total_count  # type: int
        self.page_number = page_number  # type: int
        self.page_size = page_size      # type: int
        self.rule_checks = rule_checks  # type: List[ListQualityResultsByEntityResponseQualityResultsRuleChecks]

    def validate(self):
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.rule_checks, 'rule_checks')
        if self.rule_checks:
            for k in self.rule_checks:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['TotalCount'] = self.total_count
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        result['RuleChecks'] = []
        if self.rule_checks is not None:
            for k in self.rule_checks:
                result['RuleChecks'].append(k.to_map() if k else None)
        else:
            result['RuleChecks'] = None
        return result

    def from_map(self, map={}):
        self.total_count = map.get('TotalCount')
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        self.rule_checks = []
        if map.get('RuleChecks') is not None:
            for k in map.get('RuleChecks'):
                temp_model = ListQualityResultsByEntityResponseQualityResultsRuleChecks()
                self.rule_checks.append(temp_model.from_map(k))
        else:
            self.rule_checks = None
        return self


class GetNodeTypeListInfoRequest(TeaModel):
    def __init__(self, project_id=None, project_identifier=None, page_number=None, page_size=None, keyword=None,
                 locale=None):
        self.project_id = project_id    # type: int
        self.project_identifier = project_identifier  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size      # type: int
        self.keyword = keyword          # type: str
        self.locale = locale            # type: str

    def validate(self):
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_size, 'page_size')

    def to_map(self):
        result = {}
        result['ProjectId'] = self.project_id
        result['ProjectIdentifier'] = self.project_identifier
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        result['Keyword'] = self.keyword
        result['Locale'] = self.locale
        return result

    def from_map(self, map={}):
        self.project_id = map.get('ProjectId')
        self.project_identifier = map.get('ProjectIdentifier')
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        self.keyword = map.get('Keyword')
        self.locale = map.get('Locale')
        return self


class GetNodeTypeListInfoResponse(TeaModel):
    def __init__(self, request_id=None, node_type_info_list=None):
        self.request_id = request_id    # type: str
        self.node_type_info_list = node_type_info_list  # type: GetNodeTypeListInfoResponseNodeTypeInfoList

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.node_type_info_list, 'node_type_info_list')
        if self.node_type_info_list:
            self.node_type_info_list.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        if self.node_type_info_list is not None:
            result['NodeTypeInfoList'] = self.node_type_info_list.to_map()
        else:
            result['NodeTypeInfoList'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('NodeTypeInfoList') is not None:
            temp_model = GetNodeTypeListInfoResponseNodeTypeInfoList()
            self.node_type_info_list = temp_model.from_map(map['NodeTypeInfoList'])
        else:
            self.node_type_info_list = None
        return self


class GetNodeTypeListInfoResponseNodeTypeInfoListNodeTypeInfo(TeaModel):
    def __init__(self, node_type=None, node_type_name=None):
        self.node_type = node_type      # type: int
        self.node_type_name = node_type_name  # type: str

    def validate(self):
        self.validate_required(self.node_type, 'node_type')
        self.validate_required(self.node_type_name, 'node_type_name')

    def to_map(self):
        result = {}
        result['NodeType'] = self.node_type
        result['NodeTypeName'] = self.node_type_name
        return result

    def from_map(self, map={}):
        self.node_type = map.get('NodeType')
        self.node_type_name = map.get('NodeTypeName')
        return self


class GetNodeTypeListInfoResponseNodeTypeInfoList(TeaModel):
    def __init__(self, page_number=None, page_size=None, total_count=None, node_type_info=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size      # type: int
        self.total_count = total_count  # type: int
        self.node_type_info = node_type_info  # type: List[GetNodeTypeListInfoResponseNodeTypeInfoListNodeTypeInfo]

    def validate(self):
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.node_type_info, 'node_type_info')
        if self.node_type_info:
            for k in self.node_type_info:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        result['TotalCount'] = self.total_count
        result['NodeTypeInfo'] = []
        if self.node_type_info is not None:
            for k in self.node_type_info:
                result['NodeTypeInfo'].append(k.to_map() if k else None)
        else:
            result['NodeTypeInfo'] = None
        return result

    def from_map(self, map={}):
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        self.total_count = map.get('TotalCount')
        self.node_type_info = []
        if map.get('NodeTypeInfo') is not None:
            for k in map.get('NodeTypeInfo'):
                temp_model = GetNodeTypeListInfoResponseNodeTypeInfoListNodeTypeInfo()
                self.node_type_info.append(temp_model.from_map(k))
        else:
            self.node_type_info = None
        return self


class GetInstanceStatusCountRequest(TeaModel):
    def __init__(self, project_id=None, project_env=None, biz_date=None):
        self.project_id = project_id    # type: int
        self.project_env = project_env  # type: str
        self.biz_date = biz_date        # type: str

    def validate(self):
        self.validate_required(self.project_id, 'project_id')
        self.validate_required(self.project_env, 'project_env')
        self.validate_required(self.biz_date, 'biz_date')

    def to_map(self):
        result = {}
        result['ProjectId'] = self.project_id
        result['ProjectEnv'] = self.project_env
        result['BizDate'] = self.biz_date
        return result

    def from_map(self, map={}):
        self.project_id = map.get('ProjectId')
        self.project_env = map.get('ProjectEnv')
        self.biz_date = map.get('BizDate')
        return self


class GetInstanceStatusCountResponse(TeaModel):
    def __init__(self, request_id=None, status_count=None):
        self.request_id = request_id    # type: str
        self.status_count = status_count  # type: GetInstanceStatusCountResponseStatusCount

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.status_count, 'status_count')
        if self.status_count:
            self.status_count.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        if self.status_count is not None:
            result['StatusCount'] = self.status_count.to_map()
        else:
            result['StatusCount'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('StatusCount') is not None:
            temp_model = GetInstanceStatusCountResponseStatusCount()
            self.status_count = temp_model.from_map(map['StatusCount'])
        else:
            self.status_count = None
        return self


class GetInstanceStatusCountResponseStatusCount(TeaModel):
    def __init__(self, total_count=None, not_run_count=None, wait_time_count=None, wait_res_count=None,
                 running_count=None, failure_count=None, success_count=None):
        self.total_count = total_count  # type: int
        self.not_run_count = not_run_count  # type: int
        self.wait_time_count = wait_time_count  # type: int
        self.wait_res_count = wait_res_count  # type: int
        self.running_count = running_count  # type: int
        self.failure_count = failure_count  # type: int
        self.success_count = success_count  # type: int

    def validate(self):
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.not_run_count, 'not_run_count')
        self.validate_required(self.wait_time_count, 'wait_time_count')
        self.validate_required(self.wait_res_count, 'wait_res_count')
        self.validate_required(self.running_count, 'running_count')
        self.validate_required(self.failure_count, 'failure_count')
        self.validate_required(self.success_count, 'success_count')

    def to_map(self):
        result = {}
        result['TotalCount'] = self.total_count
        result['NotRunCount'] = self.not_run_count
        result['WaitTimeCount'] = self.wait_time_count
        result['WaitResCount'] = self.wait_res_count
        result['RunningCount'] = self.running_count
        result['FailureCount'] = self.failure_count
        result['SuccessCount'] = self.success_count
        return result

    def from_map(self, map={}):
        self.total_count = map.get('TotalCount')
        self.not_run_count = map.get('NotRunCount')
        self.wait_time_count = map.get('WaitTimeCount')
        self.wait_res_count = map.get('WaitResCount')
        self.running_count = map.get('RunningCount')
        self.failure_count = map.get('FailureCount')
        self.success_count = map.get('SuccessCount')
        return self


class ListDataServiceFoldersRequest(TeaModel):
    def __init__(self, page_number=None, page_size=None, project_id=None, tenant_id=None, group_id=None,
                 folder_name_keyword=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size      # type: int
        self.project_id = project_id    # type: int
        self.tenant_id = tenant_id      # type: int
        self.group_id = group_id        # type: str
        self.folder_name_keyword = folder_name_keyword  # type: str

    def validate(self):
        self.validate_required(self.project_id, 'project_id')
        self.validate_required(self.tenant_id, 'tenant_id')

    def to_map(self):
        result = {}
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        result['ProjectId'] = self.project_id
        result['TenantId'] = self.tenant_id
        result['GroupId'] = self.group_id
        result['FolderNameKeyword'] = self.folder_name_keyword
        return result

    def from_map(self, map={}):
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        self.project_id = map.get('ProjectId')
        self.tenant_id = map.get('TenantId')
        self.group_id = map.get('GroupId')
        self.folder_name_keyword = map.get('FolderNameKeyword')
        return self


class ListDataServiceFoldersResponse(TeaModel):
    def __init__(self, request_id=None, folder_paging_result=None):
        self.request_id = request_id    # type: str
        self.folder_paging_result = folder_paging_result  # type: ListDataServiceFoldersResponseFolderPagingResult

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.folder_paging_result, 'folder_paging_result')
        if self.folder_paging_result:
            self.folder_paging_result.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        if self.folder_paging_result is not None:
            result['FolderPagingResult'] = self.folder_paging_result.to_map()
        else:
            result['FolderPagingResult'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('FolderPagingResult') is not None:
            temp_model = ListDataServiceFoldersResponseFolderPagingResult()
            self.folder_paging_result = temp_model.from_map(map['FolderPagingResult'])
        else:
            self.folder_paging_result = None
        return self


class ListDataServiceFoldersResponseFolderPagingResultFolders(TeaModel):
    def __init__(self, folder_id=None, folder_name=None, project_id=None, tenant_id=None, created_time=None,
                 modified_time=None, group_id=None, parent_id=None):
        self.folder_id = folder_id      # type: int
        self.folder_name = folder_name  # type: str
        self.project_id = project_id    # type: int
        self.tenant_id = tenant_id      # type: int
        self.created_time = created_time  # type: str
        self.modified_time = modified_time  # type: str
        self.group_id = group_id        # type: str
        self.parent_id = parent_id      # type: int

    def validate(self):
        self.validate_required(self.folder_id, 'folder_id')
        self.validate_required(self.folder_name, 'folder_name')
        self.validate_required(self.project_id, 'project_id')
        self.validate_required(self.tenant_id, 'tenant_id')
        self.validate_required(self.created_time, 'created_time')
        self.validate_required(self.modified_time, 'modified_time')
        self.validate_required(self.group_id, 'group_id')
        self.validate_required(self.parent_id, 'parent_id')

    def to_map(self):
        result = {}
        result['FolderId'] = self.folder_id
        result['FolderName'] = self.folder_name
        result['ProjectId'] = self.project_id
        result['TenantId'] = self.tenant_id
        result['CreatedTime'] = self.created_time
        result['ModifiedTime'] = self.modified_time
        result['GroupId'] = self.group_id
        result['ParentId'] = self.parent_id
        return result

    def from_map(self, map={}):
        self.folder_id = map.get('FolderId')
        self.folder_name = map.get('FolderName')
        self.project_id = map.get('ProjectId')
        self.tenant_id = map.get('TenantId')
        self.created_time = map.get('CreatedTime')
        self.modified_time = map.get('ModifiedTime')
        self.group_id = map.get('GroupId')
        self.parent_id = map.get('ParentId')
        return self


class ListDataServiceFoldersResponseFolderPagingResult(TeaModel):
    def __init__(self, page_number=None, page_size=None, total_count=None, folders=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size      # type: int
        self.total_count = total_count  # type: int
        self.folders = folders          # type: List[ListDataServiceFoldersResponseFolderPagingResultFolders]

    def validate(self):
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.folders, 'folders')
        if self.folders:
            for k in self.folders:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        result['TotalCount'] = self.total_count
        result['Folders'] = []
        if self.folders is not None:
            for k in self.folders:
                result['Folders'].append(k.to_map() if k else None)
        else:
            result['Folders'] = None
        return result

    def from_map(self, map={}):
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        self.total_count = map.get('TotalCount')
        self.folders = []
        if map.get('Folders') is not None:
            for k in map.get('Folders'):
                temp_model = ListDataServiceFoldersResponseFolderPagingResultFolders()
                self.folders.append(temp_model.from_map(k))
        else:
            self.folders = None
        return self


class ListQualityResultsByRuleRequest(TeaModel):
    def __init__(self, rule_id=None, start_date=None, end_date=None, page_size=None, page_number=None,
                 project_name=None):
        self.rule_id = rule_id          # type: int
        self.start_date = start_date    # type: str
        self.end_date = end_date        # type: str
        self.page_size = page_size      # type: int
        self.page_number = page_number  # type: int
        self.project_name = project_name  # type: str

    def validate(self):
        self.validate_required(self.rule_id, 'rule_id')
        self.validate_required(self.start_date, 'start_date')
        self.validate_required(self.end_date, 'end_date')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.project_name, 'project_name')

    def to_map(self):
        result = {}
        result['RuleId'] = self.rule_id
        result['StartDate'] = self.start_date
        result['EndDate'] = self.end_date
        result['PageSize'] = self.page_size
        result['PageNumber'] = self.page_number
        result['ProjectName'] = self.project_name
        return result

    def from_map(self, map={}):
        self.rule_id = map.get('RuleId')
        self.start_date = map.get('StartDate')
        self.end_date = map.get('EndDate')
        self.page_size = map.get('PageSize')
        self.page_number = map.get('PageNumber')
        self.project_name = map.get('ProjectName')
        return self


class ListQualityResultsByRuleResponse(TeaModel):
    def __init__(self, request_id=None, quality_results=None):
        self.request_id = request_id    # type: str
        self.quality_results = quality_results  # type: ListQualityResultsByRuleResponseQualityResults

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.quality_results, 'quality_results')
        if self.quality_results:
            self.quality_results.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        if self.quality_results is not None:
            result['QualityResults'] = self.quality_results.to_map()
        else:
            result['QualityResults'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('QualityResults') is not None:
            temp_model = ListQualityResultsByRuleResponseQualityResults()
            self.quality_results = temp_model.from_map(map['QualityResults'])
        else:
            self.quality_results = None
        return self


class ListQualityResultsByRuleResponseQualityResultsRuleChecksReferenceValue(TeaModel):
    def __init__(self, biz_date=None, discrete_property=None, value=None, threshold=None, single_check_result=None):
        self.biz_date = biz_date        # type: int
        self.discrete_property = discrete_property  # type: str
        self.value = value              # type: float
        self.threshold = threshold      # type: float
        self.single_check_result = single_check_result  # type: int

    def validate(self):
        self.validate_required(self.biz_date, 'biz_date')
        self.validate_required(self.discrete_property, 'discrete_property')
        self.validate_required(self.value, 'value')
        self.validate_required(self.threshold, 'threshold')
        self.validate_required(self.single_check_result, 'single_check_result')

    def to_map(self):
        result = {}
        result['BizDate'] = self.biz_date
        result['DiscreteProperty'] = self.discrete_property
        result['Value'] = self.value
        result['Threshold'] = self.threshold
        result['SingleCheckResult'] = self.single_check_result
        return result

    def from_map(self, map={}):
        self.biz_date = map.get('BizDate')
        self.discrete_property = map.get('DiscreteProperty')
        self.value = map.get('Value')
        self.threshold = map.get('Threshold')
        self.single_check_result = map.get('SingleCheckResult')
        return self


class ListQualityResultsByRuleResponseQualityResultsRuleChecksSampleValue(TeaModel):
    def __init__(self, biz_date=None, discrete_property=None, value=None):
        self.biz_date = biz_date        # type: int
        self.discrete_property = discrete_property  # type: str
        self.value = value              # type: float

    def validate(self):
        self.validate_required(self.biz_date, 'biz_date')
        self.validate_required(self.discrete_property, 'discrete_property')
        self.validate_required(self.value, 'value')

    def to_map(self):
        result = {}
        result['BizDate'] = self.biz_date
        result['DiscreteProperty'] = self.discrete_property
        result['Value'] = self.value
        return result

    def from_map(self, map={}):
        self.biz_date = map.get('BizDate')
        self.discrete_property = map.get('DiscreteProperty')
        self.value = map.get('Value')
        return self


class ListQualityResultsByRuleResponseQualityResultsRuleChecks(TeaModel):
    def __init__(self, id=None, task_id=None, entity_id=None, rule_id=None, property=None, biz_date=None,
                 date_type=None, actual_expression=None, match_expression=None, block_type=None, check_result=None,
                 check_result_status=None, method_name=None, comment=None, where_condition=None, begin_time=None, end_time=None,
                 time_cost=None, external_type=None, external_id=None, discrete_check=None, fixed_check=None, trend=None,
                 warning_threshold=None, critical_threshold=None, expect_value=None, op=None, project_name=None, table_name=None,
                 template_id=None, template_name=None, result_string=None, checker_id=None, checker_type=None, rule_name=None,
                 is_prediction=None, upper_value=None, lower_value=None, checker_name=None, reference_value=None,
                 sample_value=None):
        self.id = id                    # type: int
        self.task_id = task_id          # type: str
        self.entity_id = entity_id      # type: int
        self.rule_id = rule_id          # type: int
        self.property = property        # type: str
        self.biz_date = biz_date        # type: int
        self.date_type = date_type      # type: str
        self.actual_expression = actual_expression  # type: str
        self.match_expression = match_expression  # type: str
        self.block_type = block_type    # type: int
        self.check_result = check_result  # type: int
        self.check_result_status = check_result_status  # type: int
        self.method_name = method_name  # type: str
        self.comment = comment          # type: str
        self.where_condition = where_condition  # type: str
        self.begin_time = begin_time    # type: int
        self.end_time = end_time        # type: int
        self.time_cost = time_cost      # type: str
        self.external_type = external_type  # type: str
        self.external_id = external_id  # type: str
        self.discrete_check = discrete_check  # type: bool
        self.fixed_check = fixed_check  # type: bool
        self.trend = trend              # type: str
        self.warning_threshold = warning_threshold  # type: float
        self.critical_threshold = critical_threshold  # type: float
        self.expect_value = expect_value  # type: float
        self.op = op                    # type: str
        self.project_name = project_name  # type: str
        self.table_name = table_name    # type: str
        self.template_id = template_id  # type: int
        self.template_name = template_name  # type: str
        self.result_string = result_string  # type: str
        self.checker_id = checker_id    # type: int
        self.checker_type = checker_type  # type: int
        self.rule_name = rule_name      # type: str
        self.is_prediction = is_prediction  # type: bool
        self.upper_value = upper_value  # type: float
        self.lower_value = lower_value  # type: float
        self.checker_name = checker_name  # type: str
        self.reference_value = reference_value  # type: List[ListQualityResultsByRuleResponseQualityResultsRuleChecksReferenceValue]
        self.sample_value = sample_value  # type: List[ListQualityResultsByRuleResponseQualityResultsRuleChecksSampleValue]

    def validate(self):
        self.validate_required(self.id, 'id')
        self.validate_required(self.task_id, 'task_id')
        self.validate_required(self.entity_id, 'entity_id')
        self.validate_required(self.rule_id, 'rule_id')
        self.validate_required(self.property, 'property')
        self.validate_required(self.biz_date, 'biz_date')
        self.validate_required(self.date_type, 'date_type')
        self.validate_required(self.actual_expression, 'actual_expression')
        self.validate_required(self.match_expression, 'match_expression')
        self.validate_required(self.block_type, 'block_type')
        self.validate_required(self.check_result, 'check_result')
        self.validate_required(self.check_result_status, 'check_result_status')
        self.validate_required(self.method_name, 'method_name')
        self.validate_required(self.comment, 'comment')
        self.validate_required(self.where_condition, 'where_condition')
        self.validate_required(self.begin_time, 'begin_time')
        self.validate_required(self.end_time, 'end_time')
        self.validate_required(self.time_cost, 'time_cost')
        self.validate_required(self.external_type, 'external_type')
        self.validate_required(self.external_id, 'external_id')
        self.validate_required(self.discrete_check, 'discrete_check')
        self.validate_required(self.fixed_check, 'fixed_check')
        self.validate_required(self.trend, 'trend')
        self.validate_required(self.warning_threshold, 'warning_threshold')
        self.validate_required(self.critical_threshold, 'critical_threshold')
        self.validate_required(self.expect_value, 'expect_value')
        self.validate_required(self.op, 'op')
        self.validate_required(self.project_name, 'project_name')
        self.validate_required(self.table_name, 'table_name')
        self.validate_required(self.template_id, 'template_id')
        self.validate_required(self.template_name, 'template_name')
        self.validate_required(self.result_string, 'result_string')
        self.validate_required(self.checker_id, 'checker_id')
        self.validate_required(self.checker_type, 'checker_type')
        self.validate_required(self.rule_name, 'rule_name')
        self.validate_required(self.is_prediction, 'is_prediction')
        self.validate_required(self.upper_value, 'upper_value')
        self.validate_required(self.lower_value, 'lower_value')
        self.validate_required(self.checker_name, 'checker_name')
        self.validate_required(self.reference_value, 'reference_value')
        if self.reference_value:
            for k in self.reference_value:
                if k:
                    k.validate()
        self.validate_required(self.sample_value, 'sample_value')
        if self.sample_value:
            for k in self.sample_value:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['Id'] = self.id
        result['TaskId'] = self.task_id
        result['EntityId'] = self.entity_id
        result['RuleId'] = self.rule_id
        result['Property'] = self.property
        result['BizDate'] = self.biz_date
        result['DateType'] = self.date_type
        result['ActualExpression'] = self.actual_expression
        result['MatchExpression'] = self.match_expression
        result['BlockType'] = self.block_type
        result['CheckResult'] = self.check_result
        result['CheckResultStatus'] = self.check_result_status
        result['MethodName'] = self.method_name
        result['Comment'] = self.comment
        result['WhereCondition'] = self.where_condition
        result['BeginTime'] = self.begin_time
        result['EndTime'] = self.end_time
        result['TimeCost'] = self.time_cost
        result['ExternalType'] = self.external_type
        result['ExternalId'] = self.external_id
        result['DiscreteCheck'] = self.discrete_check
        result['FixedCheck'] = self.fixed_check
        result['Trend'] = self.trend
        result['WarningThreshold'] = self.warning_threshold
        result['CriticalThreshold'] = self.critical_threshold
        result['ExpectValue'] = self.expect_value
        result['Op'] = self.op
        result['ProjectName'] = self.project_name
        result['TableName'] = self.table_name
        result['TemplateId'] = self.template_id
        result['TemplateName'] = self.template_name
        result['ResultString'] = self.result_string
        result['CheckerId'] = self.checker_id
        result['CheckerType'] = self.checker_type
        result['RuleName'] = self.rule_name
        result['IsPrediction'] = self.is_prediction
        result['UpperValue'] = self.upper_value
        result['LowerValue'] = self.lower_value
        result['CheckerName'] = self.checker_name
        result['ReferenceValue'] = []
        if self.reference_value is not None:
            for k in self.reference_value:
                result['ReferenceValue'].append(k.to_map() if k else None)
        else:
            result['ReferenceValue'] = None
        result['SampleValue'] = []
        if self.sample_value is not None:
            for k in self.sample_value:
                result['SampleValue'].append(k.to_map() if k else None)
        else:
            result['SampleValue'] = None
        return result

    def from_map(self, map={}):
        self.id = map.get('Id')
        self.task_id = map.get('TaskId')
        self.entity_id = map.get('EntityId')
        self.rule_id = map.get('RuleId')
        self.property = map.get('Property')
        self.biz_date = map.get('BizDate')
        self.date_type = map.get('DateType')
        self.actual_expression = map.get('ActualExpression')
        self.match_expression = map.get('MatchExpression')
        self.block_type = map.get('BlockType')
        self.check_result = map.get('CheckResult')
        self.check_result_status = map.get('CheckResultStatus')
        self.method_name = map.get('MethodName')
        self.comment = map.get('Comment')
        self.where_condition = map.get('WhereCondition')
        self.begin_time = map.get('BeginTime')
        self.end_time = map.get('EndTime')
        self.time_cost = map.get('TimeCost')
        self.external_type = map.get('ExternalType')
        self.external_id = map.get('ExternalId')
        self.discrete_check = map.get('DiscreteCheck')
        self.fixed_check = map.get('FixedCheck')
        self.trend = map.get('Trend')
        self.warning_threshold = map.get('WarningThreshold')
        self.critical_threshold = map.get('CriticalThreshold')
        self.expect_value = map.get('ExpectValue')
        self.op = map.get('Op')
        self.project_name = map.get('ProjectName')
        self.table_name = map.get('TableName')
        self.template_id = map.get('TemplateId')
        self.template_name = map.get('TemplateName')
        self.result_string = map.get('ResultString')
        self.checker_id = map.get('CheckerId')
        self.checker_type = map.get('CheckerType')
        self.rule_name = map.get('RuleName')
        self.is_prediction = map.get('IsPrediction')
        self.upper_value = map.get('UpperValue')
        self.lower_value = map.get('LowerValue')
        self.checker_name = map.get('CheckerName')
        self.reference_value = []
        if map.get('ReferenceValue') is not None:
            for k in map.get('ReferenceValue'):
                temp_model = ListQualityResultsByRuleResponseQualityResultsRuleChecksReferenceValue()
                self.reference_value.append(temp_model.from_map(k))
        else:
            self.reference_value = None
        self.sample_value = []
        if map.get('SampleValue') is not None:
            for k in map.get('SampleValue'):
                temp_model = ListQualityResultsByRuleResponseQualityResultsRuleChecksSampleValue()
                self.sample_value.append(temp_model.from_map(k))
        else:
            self.sample_value = None
        return self


class ListQualityResultsByRuleResponseQualityResults(TeaModel):
    def __init__(self, total_count=None, page_number=None, page_size=None, rule_checks=None):
        self.total_count = total_count  # type: int
        self.page_number = page_number  # type: int
        self.page_size = page_size      # type: int
        self.rule_checks = rule_checks  # type: List[ListQualityResultsByRuleResponseQualityResultsRuleChecks]

    def validate(self):
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.rule_checks, 'rule_checks')
        if self.rule_checks:
            for k in self.rule_checks:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['TotalCount'] = self.total_count
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        result['RuleChecks'] = []
        if self.rule_checks is not None:
            for k in self.rule_checks:
                result['RuleChecks'].append(k.to_map() if k else None)
        else:
            result['RuleChecks'] = None
        return result

    def from_map(self, map={}):
        self.total_count = map.get('TotalCount')
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        self.rule_checks = []
        if map.get('RuleChecks') is not None:
            for k in map.get('RuleChecks'):
                temp_model = ListQualityResultsByRuleResponseQualityResultsRuleChecks()
                self.rule_checks.append(temp_model.from_map(k))
        else:
            self.rule_checks = None
        return self


class ListMetaDBRequest(TeaModel):
    def __init__(self, project_id=None, data_source_type=None):
        self.project_id = project_id    # type: int
        self.data_source_type = data_source_type  # type: str

    def validate(self):
        self.validate_required(self.project_id, 'project_id')
        self.validate_required(self.data_source_type, 'data_source_type')

    def to_map(self):
        result = {}
        result['ProjectId'] = self.project_id
        result['DataSourceType'] = self.data_source_type
        return result

    def from_map(self, map={}):
        self.project_id = map.get('ProjectId')
        self.data_source_type = map.get('DataSourceType')
        return self


class ListMetaDBResponse(TeaModel):
    def __init__(self, request_id=None, database_info=None):
        self.request_id = request_id    # type: str
        self.database_info = database_info  # type: ListMetaDBResponseDatabaseInfo

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.database_info, 'database_info')
        if self.database_info:
            self.database_info.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        if self.database_info is not None:
            result['DatabaseInfo'] = self.database_info.to_map()
        else:
            result['DatabaseInfo'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('DatabaseInfo') is not None:
            temp_model = ListMetaDBResponseDatabaseInfo()
            self.database_info = temp_model.from_map(map['DatabaseInfo'])
        else:
            self.database_info = None
        return self


class ListMetaDBResponseDatabaseInfoDbList(TeaModel):
    def __init__(self, name=None, type=None, owner_id=None, location=None, create_time_stamp=None,
                 modified_time_stamp=None, uuid=None):
        self.name = name                # type: str
        self.type = type                # type: str
        self.owner_id = owner_id        # type: str
        self.location = location        # type: str
        self.create_time_stamp = create_time_stamp  # type: int
        self.modified_time_stamp = modified_time_stamp  # type: int
        self.uuid = uuid                # type: str

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.type, 'type')
        self.validate_required(self.owner_id, 'owner_id')
        self.validate_required(self.location, 'location')
        self.validate_required(self.create_time_stamp, 'create_time_stamp')
        self.validate_required(self.modified_time_stamp, 'modified_time_stamp')
        self.validate_required(self.uuid, 'uuid')

    def to_map(self):
        result = {}
        result['Name'] = self.name
        result['Type'] = self.type
        result['OwnerId'] = self.owner_id
        result['Location'] = self.location
        result['CreateTimeStamp'] = self.create_time_stamp
        result['ModifiedTimeStamp'] = self.modified_time_stamp
        result['UUID'] = self.uuid
        return result

    def from_map(self, map={}):
        self.name = map.get('Name')
        self.type = map.get('Type')
        self.owner_id = map.get('OwnerId')
        self.location = map.get('Location')
        self.create_time_stamp = map.get('CreateTimeStamp')
        self.modified_time_stamp = map.get('ModifiedTimeStamp')
        self.uuid = map.get('UUID')
        return self


class ListMetaDBResponseDatabaseInfo(TeaModel):
    def __init__(self, total_count=None, db_list=None):
        self.total_count = total_count  # type: int
        self.db_list = db_list          # type: List[ListMetaDBResponseDatabaseInfoDbList]

    def validate(self):
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.db_list, 'db_list')
        if self.db_list:
            for k in self.db_list:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['TotalCount'] = self.total_count
        result['DbList'] = []
        if self.db_list is not None:
            for k in self.db_list:
                result['DbList'].append(k.to_map() if k else None)
        else:
            result['DbList'] = None
        return result

    def from_map(self, map={}):
        self.total_count = map.get('TotalCount')
        self.db_list = []
        if map.get('DbList') is not None:
            for k in map.get('DbList'):
                temp_model = ListMetaDBResponseDatabaseInfoDbList()
                self.db_list.append(temp_model.from_map(k))
        else:
            self.db_list = None
        return self


class CreateTableRequest(TeaModel):
    def __init__(self, has_part=None, columns=None, is_view=None, visibility=None, life_cycle=None, category_id=None,
                 logical_level_id=None, physics_level_id=None, external_table_type=None, location=None, project_id=None,
                 table_name=None, endpoint=None, env_type=None, themes=None, app_guid=None):
        self.has_part = has_part        # type: int
        self.columns = columns          # type: List[CreateTableRequestColumns]
        self.is_view = is_view          # type: int
        self.visibility = visibility    # type: int
        self.life_cycle = life_cycle    # type: int
        self.category_id = category_id  # type: int
        self.logical_level_id = logical_level_id  # type: int
        self.physics_level_id = physics_level_id  # type: int
        self.external_table_type = external_table_type  # type: str
        self.location = location        # type: str
        self.project_id = project_id    # type: int
        self.table_name = table_name    # type: str
        self.endpoint = endpoint        # type: str
        self.env_type = env_type        # type: int
        self.themes = themes            # type: List[CreateTableRequestThemes]
        self.app_guid = app_guid        # type: str

    def validate(self):
        self.validate_required(self.columns, 'columns')
        if self.columns:
            for k in self.columns:
                if k:
                    k.validate()
        self.validate_required(self.table_name, 'table_name')
        if self.themes:
            for k in self.themes:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['HasPart'] = self.has_part
        result['Columns'] = []
        if self.columns is not None:
            for k in self.columns:
                result['Columns'].append(k.to_map() if k else None)
        else:
            result['Columns'] = None
        result['IsView'] = self.is_view
        result['Visibility'] = self.visibility
        result['LifeCycle'] = self.life_cycle
        result['CategoryId'] = self.category_id
        result['LogicalLevelId'] = self.logical_level_id
        result['PhysicsLevelId'] = self.physics_level_id
        result['ExternalTableType'] = self.external_table_type
        result['Location'] = self.location
        result['ProjectId'] = self.project_id
        result['TableName'] = self.table_name
        result['Endpoint'] = self.endpoint
        result['EnvType'] = self.env_type
        result['Themes'] = []
        if self.themes is not None:
            for k in self.themes:
                result['Themes'].append(k.to_map() if k else None)
        else:
            result['Themes'] = None
        result['AppGuid'] = self.app_guid
        return result

    def from_map(self, map={}):
        self.has_part = map.get('HasPart')
        self.columns = []
        if map.get('Columns') is not None:
            for k in map.get('Columns'):
                temp_model = CreateTableRequestColumns()
                self.columns.append(temp_model.from_map(k))
        else:
            self.columns = None
        self.is_view = map.get('IsView')
        self.visibility = map.get('Visibility')
        self.life_cycle = map.get('LifeCycle')
        self.category_id = map.get('CategoryId')
        self.logical_level_id = map.get('LogicalLevelId')
        self.physics_level_id = map.get('PhysicsLevelId')
        self.external_table_type = map.get('ExternalTableType')
        self.location = map.get('Location')
        self.project_id = map.get('ProjectId')
        self.table_name = map.get('TableName')
        self.endpoint = map.get('Endpoint')
        self.env_type = map.get('EnvType')
        self.themes = []
        if map.get('Themes') is not None:
            for k in map.get('Themes'):
                temp_model = CreateTableRequestThemes()
                self.themes.append(temp_model.from_map(k))
        else:
            self.themes = None
        self.app_guid = map.get('AppGuid')
        return self


class CreateTableRequestColumns(TeaModel):
    def __init__(self, column_name=None, column_name_cn=None, column_type=None, seq_number=None, length=None,
                 is_partition_col=None, is_primary_key=None, is_nullable=None, comment=None):
        self.column_name = column_name  # type: str
        self.column_name_cn = column_name_cn  # type: str
        self.column_type = column_type  # type: str
        self.seq_number = seq_number    # type: int
        self.length = length            # type: int
        self.is_partition_col = is_partition_col  # type: int
        self.is_primary_key = is_primary_key  # type: int
        self.is_nullable = is_nullable  # type: int
        self.comment = comment          # type: str

    def validate(self):
        self.validate_required(self.column_name, 'column_name')
        self.validate_required(self.column_type, 'column_type')

    def to_map(self):
        result = {}
        result['ColumnName'] = self.column_name
        result['ColumnNameCn'] = self.column_name_cn
        result['ColumnType'] = self.column_type
        result['SeqNumber'] = self.seq_number
        result['Length'] = self.length
        result['IsPartitionCol'] = self.is_partition_col
        result['IsPrimaryKey'] = self.is_primary_key
        result['IsNullable'] = self.is_nullable
        result['Comment'] = self.comment
        return result

    def from_map(self, map={}):
        self.column_name = map.get('ColumnName')
        self.column_name_cn = map.get('ColumnNameCn')
        self.column_type = map.get('ColumnType')
        self.seq_number = map.get('SeqNumber')
        self.length = map.get('Length')
        self.is_partition_col = map.get('IsPartitionCol')
        self.is_primary_key = map.get('IsPrimaryKey')
        self.is_nullable = map.get('IsNullable')
        self.comment = map.get('Comment')
        return self


class CreateTableRequestThemes(TeaModel):
    def __init__(self, theme_id=None, theme_level=None):
        self.theme_id = theme_id        # type: int
        self.theme_level = theme_level  # type: int

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['ThemeId'] = self.theme_id
        result['ThemeLevel'] = self.theme_level
        return result

    def from_map(self, map={}):
        self.theme_id = map.get('ThemeId')
        self.theme_level = map.get('ThemeLevel')
        return self


class CreateTableResponse(TeaModel):
    def __init__(self, request_id=None, task_info=None):
        self.request_id = request_id    # type: str
        self.task_info = task_info      # type: CreateTableResponseTaskInfo

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.task_info, 'task_info')
        if self.task_info:
            self.task_info.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        if self.task_info is not None:
            result['TaskInfo'] = self.task_info.to_map()
        else:
            result['TaskInfo'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('TaskInfo') is not None:
            temp_model = CreateTableResponseTaskInfo()
            self.task_info = temp_model.from_map(map['TaskInfo'])
        else:
            self.task_info = None
        return self


class CreateTableResponseTaskInfo(TeaModel):
    def __init__(self, task_id=None, content=None, status=None, next_task_id=None):
        self.task_id = task_id          # type: str
        self.content = content          # type: str
        self.status = status            # type: str
        self.next_task_id = next_task_id  # type: str

    def validate(self):
        self.validate_required(self.task_id, 'task_id')
        self.validate_required(self.content, 'content')
        self.validate_required(self.status, 'status')
        self.validate_required(self.next_task_id, 'next_task_id')

    def to_map(self):
        result = {}
        result['TaskId'] = self.task_id
        result['Content'] = self.content
        result['Status'] = self.status
        result['NextTaskId'] = self.next_task_id
        return result

    def from_map(self, map={}):
        self.task_id = map.get('TaskId')
        self.content = map.get('Content')
        self.status = map.get('Status')
        self.next_task_id = map.get('NextTaskId')
        return self


class CreateTableThemeRequest(TeaModel):
    def __init__(self, project_id=None, level=None, name=None, parent_id=None):
        self.project_id = project_id    # type: int
        self.level = level              # type: int
        self.name = name                # type: str
        self.parent_id = parent_id      # type: int

    def validate(self):
        self.validate_required(self.level, 'level')
        self.validate_required(self.name, 'name')

    def to_map(self):
        result = {}
        result['ProjectId'] = self.project_id
        result['Level'] = self.level
        result['Name'] = self.name
        result['ParentId'] = self.parent_id
        return result

    def from_map(self, map={}):
        self.project_id = map.get('ProjectId')
        self.level = map.get('Level')
        self.name = map.get('Name')
        self.parent_id = map.get('ParentId')
        return self


class CreateTableThemeResponse(TeaModel):
    def __init__(self, request_id=None, error_code=None, error_message=None, http_status_code=None, success=None,
                 theme_id=None):
        self.request_id = request_id    # type: str
        self.error_code = error_code    # type: str
        self.error_message = error_message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.success = success          # type: bool
        self.theme_id = theme_id        # type: int

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.error_code, 'error_code')
        self.validate_required(self.error_message, 'error_message')
        self.validate_required(self.http_status_code, 'http_status_code')
        self.validate_required(self.success, 'success')
        self.validate_required(self.theme_id, 'theme_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['ErrorCode'] = self.error_code
        result['ErrorMessage'] = self.error_message
        result['HttpStatusCode'] = self.http_status_code
        result['Success'] = self.success
        result['ThemeId'] = self.theme_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.error_code = map.get('ErrorCode')
        self.error_message = map.get('ErrorMessage')
        self.http_status_code = map.get('HttpStatusCode')
        self.success = map.get('Success')
        self.theme_id = map.get('ThemeId')
        return self


class GetInstanceErrorRankRequest(TeaModel):
    def __init__(self, project_id=None):
        self.project_id = project_id    # type: int

    def validate(self):
        self.validate_required(self.project_id, 'project_id')

    def to_map(self):
        result = {}
        result['ProjectId'] = self.project_id
        return result

    def from_map(self, map={}):
        self.project_id = map.get('ProjectId')
        return self


class GetInstanceErrorRankResponse(TeaModel):
    def __init__(self, request_id=None, instance_error_rank=None):
        self.request_id = request_id    # type: str
        self.instance_error_rank = instance_error_rank  # type: GetInstanceErrorRankResponseInstanceErrorRank

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.instance_error_rank, 'instance_error_rank')
        if self.instance_error_rank:
            self.instance_error_rank.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        if self.instance_error_rank is not None:
            result['InstanceErrorRank'] = self.instance_error_rank.to_map()
        else:
            result['InstanceErrorRank'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('InstanceErrorRank') is not None:
            temp_model = GetInstanceErrorRankResponseInstanceErrorRank()
            self.instance_error_rank = temp_model.from_map(map['InstanceErrorRank'])
        else:
            self.instance_error_rank = None
        return self


class GetInstanceErrorRankResponseInstanceErrorRankErrorRank(TeaModel):
    def __init__(self, node_id=None, node_name=None, owner=None, count=None, project_id=None, prg_type=None):
        self.node_id = node_id          # type: int
        self.node_name = node_name      # type: str
        self.owner = owner              # type: str
        self.count = count              # type: int
        self.project_id = project_id    # type: int
        self.prg_type = prg_type        # type: int

    def validate(self):
        self.validate_required(self.node_id, 'node_id')
        self.validate_required(self.node_name, 'node_name')
        self.validate_required(self.owner, 'owner')
        self.validate_required(self.count, 'count')
        self.validate_required(self.project_id, 'project_id')
        self.validate_required(self.prg_type, 'prg_type')

    def to_map(self):
        result = {}
        result['NodeId'] = self.node_id
        result['NodeName'] = self.node_name
        result['Owner'] = self.owner
        result['Count'] = self.count
        result['ProjectId'] = self.project_id
        result['PrgType'] = self.prg_type
        return result

    def from_map(self, map={}):
        self.node_id = map.get('NodeId')
        self.node_name = map.get('NodeName')
        self.owner = map.get('Owner')
        self.count = map.get('Count')
        self.project_id = map.get('ProjectId')
        self.prg_type = map.get('PrgType')
        return self


class GetInstanceErrorRankResponseInstanceErrorRank(TeaModel):
    def __init__(self, update_time=None, error_rank=None):
        self.update_time = update_time  # type: int
        self.error_rank = error_rank    # type: List[GetInstanceErrorRankResponseInstanceErrorRankErrorRank]

    def validate(self):
        self.validate_required(self.update_time, 'update_time')
        self.validate_required(self.error_rank, 'error_rank')
        if self.error_rank:
            for k in self.error_rank:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['UpdateTime'] = self.update_time
        result['ErrorRank'] = []
        if self.error_rank is not None:
            for k in self.error_rank:
                result['ErrorRank'].append(k.to_map() if k else None)
        else:
            result['ErrorRank'] = None
        return result

    def from_map(self, map={}):
        self.update_time = map.get('UpdateTime')
        self.error_rank = []
        if map.get('ErrorRank') is not None:
            for k in map.get('ErrorRank'):
                temp_model = GetInstanceErrorRankResponseInstanceErrorRankErrorRank()
                self.error_rank.append(temp_model.from_map(k))
        else:
            self.error_rank = None
        return self


class GetDDLJobStatusRequest(TeaModel):
    def __init__(self, task_id=None):
        self.task_id = task_id          # type: str

    def validate(self):
        self.validate_required(self.task_id, 'task_id')

    def to_map(self):
        result = {}
        result['TaskId'] = self.task_id
        return result

    def from_map(self, map={}):
        self.task_id = map.get('TaskId')
        return self


class GetDDLJobStatusResponse(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = request_id    # type: str
        self.data = data                # type: GetDDLJobStatusResponseData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('Data') is not None:
            temp_model = GetDDLJobStatusResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class GetDDLJobStatusResponseData(TeaModel):
    def __init__(self, next_task_id=None, content=None, status=None, task_id=None):
        self.next_task_id = next_task_id  # type: str
        self.content = content          # type: str
        self.status = status            # type: str
        self.task_id = task_id          # type: str

    def validate(self):
        self.validate_required(self.next_task_id, 'next_task_id')
        self.validate_required(self.content, 'content')
        self.validate_required(self.status, 'status')
        self.validate_required(self.task_id, 'task_id')

    def to_map(self):
        result = {}
        result['NextTaskId'] = self.next_task_id
        result['Content'] = self.content
        result['Status'] = self.status
        result['TaskId'] = self.task_id
        return result

    def from_map(self, map={}):
        self.next_task_id = map.get('NextTaskId')
        self.content = map.get('Content')
        self.status = map.get('Status')
        self.task_id = map.get('TaskId')
        return self


class GetInstanceConsumeTimeRankRequest(TeaModel):
    def __init__(self, project_id=None, bizdate=None):
        self.project_id = project_id    # type: int
        self.bizdate = bizdate          # type: str

    def validate(self):
        self.validate_required(self.project_id, 'project_id')
        self.validate_required(self.bizdate, 'bizdate')

    def to_map(self):
        result = {}
        result['ProjectId'] = self.project_id
        result['Bizdate'] = self.bizdate
        return result

    def from_map(self, map={}):
        self.project_id = map.get('ProjectId')
        self.bizdate = map.get('Bizdate')
        return self


class GetInstanceConsumeTimeRankResponse(TeaModel):
    def __init__(self, request_id=None, instance_consume_time_rank=None):
        self.request_id = request_id    # type: str
        self.instance_consume_time_rank = instance_consume_time_rank  # type: GetInstanceConsumeTimeRankResponseInstanceConsumeTimeRank

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.instance_consume_time_rank, 'instance_consume_time_rank')
        if self.instance_consume_time_rank:
            self.instance_consume_time_rank.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        if self.instance_consume_time_rank is not None:
            result['InstanceConsumeTimeRank'] = self.instance_consume_time_rank.to_map()
        else:
            result['InstanceConsumeTimeRank'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('InstanceConsumeTimeRank') is not None:
            temp_model = GetInstanceConsumeTimeRankResponseInstanceConsumeTimeRank()
            self.instance_consume_time_rank = temp_model.from_map(map['InstanceConsumeTimeRank'])
        else:
            self.instance_consume_time_rank = None
        return self


class GetInstanceConsumeTimeRankResponseInstanceConsumeTimeRankConsumeTimeRank(TeaModel):
    def __init__(self, node_name=None, node_id=None, bizdate=None, owner=None, consumed=None, instance_id=None,
                 prg_type=None):
        self.node_name = node_name      # type: str
        self.node_id = node_id          # type: int
        self.bizdate = bizdate          # type: int
        self.owner = owner              # type: str
        self.consumed = consumed        # type: int
        self.instance_id = instance_id  # type: int
        self.prg_type = prg_type        # type: int

    def validate(self):
        self.validate_required(self.node_name, 'node_name')
        self.validate_required(self.node_id, 'node_id')
        self.validate_required(self.bizdate, 'bizdate')
        self.validate_required(self.owner, 'owner')
        self.validate_required(self.consumed, 'consumed')
        self.validate_required(self.instance_id, 'instance_id')
        self.validate_required(self.prg_type, 'prg_type')

    def to_map(self):
        result = {}
        result['NodeName'] = self.node_name
        result['NodeId'] = self.node_id
        result['Bizdate'] = self.bizdate
        result['Owner'] = self.owner
        result['Consumed'] = self.consumed
        result['InstanceId'] = self.instance_id
        result['PrgType'] = self.prg_type
        return result

    def from_map(self, map={}):
        self.node_name = map.get('NodeName')
        self.node_id = map.get('NodeId')
        self.bizdate = map.get('Bizdate')
        self.owner = map.get('Owner')
        self.consumed = map.get('Consumed')
        self.instance_id = map.get('InstanceId')
        self.prg_type = map.get('PrgType')
        return self


class GetInstanceConsumeTimeRankResponseInstanceConsumeTimeRank(TeaModel):
    def __init__(self, update_time=None, consume_time_rank=None):
        self.update_time = update_time  # type: int
        self.consume_time_rank = consume_time_rank  # type: List[GetInstanceConsumeTimeRankResponseInstanceConsumeTimeRankConsumeTimeRank]

    def validate(self):
        self.validate_required(self.update_time, 'update_time')
        self.validate_required(self.consume_time_rank, 'consume_time_rank')
        if self.consume_time_rank:
            for k in self.consume_time_rank:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['UpdateTime'] = self.update_time
        result['ConsumeTimeRank'] = []
        if self.consume_time_rank is not None:
            for k in self.consume_time_rank:
                result['ConsumeTimeRank'].append(k.to_map() if k else None)
        else:
            result['ConsumeTimeRank'] = None
        return result

    def from_map(self, map={}):
        self.update_time = map.get('UpdateTime')
        self.consume_time_rank = []
        if map.get('ConsumeTimeRank') is not None:
            for k in map.get('ConsumeTimeRank'):
                temp_model = GetInstanceConsumeTimeRankResponseInstanceConsumeTimeRankConsumeTimeRank()
                self.consume_time_rank.append(temp_model.from_map(k))
        else:
            self.consume_time_rank = None
        return self


class CreateDataServiceApiAuthorityRequest(TeaModel):
    def __init__(self, tenant_id=None, project_id=None, api_id=None, authorized_project_id=None, end_time=None):
        self.tenant_id = tenant_id      # type: int
        self.project_id = project_id    # type: int
        self.api_id = api_id            # type: int
        self.authorized_project_id = authorized_project_id  # type: int
        self.end_time = end_time        # type: int

    def validate(self):
        self.validate_required(self.tenant_id, 'tenant_id')
        self.validate_required(self.project_id, 'project_id')
        self.validate_required(self.api_id, 'api_id')
        self.validate_required(self.authorized_project_id, 'authorized_project_id')
        self.validate_required(self.end_time, 'end_time')

    def to_map(self):
        result = {}
        result['TenantId'] = self.tenant_id
        result['ProjectId'] = self.project_id
        result['ApiId'] = self.api_id
        result['AuthorizedProjectId'] = self.authorized_project_id
        result['EndTime'] = self.end_time
        return result

    def from_map(self, map={}):
        self.tenant_id = map.get('TenantId')
        self.project_id = map.get('ProjectId')
        self.api_id = map.get('ApiId')
        self.authorized_project_id = map.get('AuthorizedProjectId')
        self.end_time = map.get('EndTime')
        return self


class CreateDataServiceApiAuthorityResponse(TeaModel):
    def __init__(self, success=None, request_id=None):
        self.success = success          # type: bool
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.success, 'success')
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['Success'] = self.success
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.success = map.get('Success')
        self.request_id = map.get('RequestId')
        return self


class DeleteDataServiceApiAuthorityRequest(TeaModel):
    def __init__(self, tenant_id=None, project_id=None, api_id=None, authorized_project_id=None):
        self.tenant_id = tenant_id      # type: int
        self.project_id = project_id    # type: int
        self.api_id = api_id            # type: int
        self.authorized_project_id = authorized_project_id  # type: int

    def validate(self):
        self.validate_required(self.tenant_id, 'tenant_id')
        self.validate_required(self.project_id, 'project_id')
        self.validate_required(self.api_id, 'api_id')
        self.validate_required(self.authorized_project_id, 'authorized_project_id')

    def to_map(self):
        result = {}
        result['TenantId'] = self.tenant_id
        result['ProjectId'] = self.project_id
        result['ApiId'] = self.api_id
        result['AuthorizedProjectId'] = self.authorized_project_id
        return result

    def from_map(self, map={}):
        self.tenant_id = map.get('TenantId')
        self.project_id = map.get('ProjectId')
        self.api_id = map.get('ApiId')
        self.authorized_project_id = map.get('AuthorizedProjectId')
        return self


class DeleteDataServiceApiAuthorityResponse(TeaModel):
    def __init__(self, success=None, request_id=None):
        self.success = success          # type: bool
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.success, 'success')
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['Success'] = self.success
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.success = map.get('Success')
        self.request_id = map.get('RequestId')
        return self


class CreateDataServiceGroupRequest(TeaModel):
    def __init__(self, tenant_id=None, project_id=None, api_gateway_group_id=None, group_name=None,
                 description=None):
        self.tenant_id = tenant_id      # type: int
        self.project_id = project_id    # type: int
        self.api_gateway_group_id = api_gateway_group_id  # type: str
        self.group_name = group_name    # type: str
        self.description = description  # type: str

    def validate(self):
        self.validate_required(self.tenant_id, 'tenant_id')
        self.validate_required(self.project_id, 'project_id')
        self.validate_required(self.api_gateway_group_id, 'api_gateway_group_id')
        self.validate_required(self.group_name, 'group_name')

    def to_map(self):
        result = {}
        result['TenantId'] = self.tenant_id
        result['ProjectId'] = self.project_id
        result['ApiGatewayGroupId'] = self.api_gateway_group_id
        result['GroupName'] = self.group_name
        result['Description'] = self.description
        return result

    def from_map(self, map={}):
        self.tenant_id = map.get('TenantId')
        self.project_id = map.get('ProjectId')
        self.api_gateway_group_id = map.get('ApiGatewayGroupId')
        self.group_name = map.get('GroupName')
        self.description = map.get('Description')
        return self


class CreateDataServiceGroupResponse(TeaModel):
    def __init__(self, group_id=None, request_id=None):
        self.group_id = group_id        # type: str
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.group_id, 'group_id')
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['GroupId'] = self.group_id
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.group_id = map.get('GroupId')
        self.request_id = map.get('RequestId')
        return self


class UpdateMetaTableRequest(TeaModel):
    def __init__(self, project_id=None, table_name=None, env_type=None, table_guid=None, new_owner_id=None,
                 added_labels=None, removed_labels=None, category_id=None, visibility=None, caption=None):
        self.project_id = project_id    # type: int
        self.table_name = table_name    # type: str
        self.env_type = env_type        # type: int
        self.table_guid = table_guid    # type: str
        self.new_owner_id = new_owner_id  # type: str
        self.added_labels = added_labels  # type: str
        self.removed_labels = removed_labels  # type: str
        self.category_id = category_id  # type: int
        self.visibility = visibility    # type: int
        self.caption = caption          # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['ProjectId'] = self.project_id
        result['TableName'] = self.table_name
        result['EnvType'] = self.env_type
        result['TableGuid'] = self.table_guid
        result['NewOwnerId'] = self.new_owner_id
        result['AddedLabels'] = self.added_labels
        result['RemovedLabels'] = self.removed_labels
        result['CategoryId'] = self.category_id
        result['Visibility'] = self.visibility
        result['Caption'] = self.caption
        return result

    def from_map(self, map={}):
        self.project_id = map.get('ProjectId')
        self.table_name = map.get('TableName')
        self.env_type = map.get('EnvType')
        self.table_guid = map.get('TableGuid')
        self.new_owner_id = map.get('NewOwnerId')
        self.added_labels = map.get('AddedLabels')
        self.removed_labels = map.get('RemovedLabels')
        self.category_id = map.get('CategoryId')
        self.visibility = map.get('Visibility')
        self.caption = map.get('Caption')
        return self


class UpdateMetaTableResponse(TeaModel):
    def __init__(self, request_id=None, update_result=None):
        self.request_id = request_id    # type: str
        self.update_result = update_result  # type: bool

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.update_result, 'update_result')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['UpdateResult'] = self.update_result
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.update_result = map.get('UpdateResult')
        return self


class GetInstanceCountTrendRequest(TeaModel):
    def __init__(self, project_id=None, begin_date=None, end_date=None):
        self.project_id = project_id    # type: int
        self.begin_date = begin_date    # type: str
        self.end_date = end_date        # type: str

    def validate(self):
        self.validate_required(self.project_id, 'project_id')
        self.validate_required(self.begin_date, 'begin_date')
        self.validate_required(self.end_date, 'end_date')

    def to_map(self):
        result = {}
        result['ProjectId'] = self.project_id
        result['BeginDate'] = self.begin_date
        result['EndDate'] = self.end_date
        return result

    def from_map(self, map={}):
        self.project_id = map.get('ProjectId')
        self.begin_date = map.get('BeginDate')
        self.end_date = map.get('EndDate')
        return self


class GetInstanceCountTrendResponse(TeaModel):
    def __init__(self, request_id=None, instance_counts=None):
        self.request_id = request_id    # type: str
        self.instance_counts = instance_counts  # type: List[GetInstanceCountTrendResponseInstanceCounts]

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.instance_counts, 'instance_counts')
        if self.instance_counts:
            for k in self.instance_counts:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['InstanceCounts'] = []
        if self.instance_counts is not None:
            for k in self.instance_counts:
                result['InstanceCounts'].append(k.to_map() if k else None)
        else:
            result['InstanceCounts'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.instance_counts = []
        if map.get('InstanceCounts') is not None:
            for k in map.get('InstanceCounts'):
                temp_model = GetInstanceCountTrendResponseInstanceCounts()
                self.instance_counts.append(temp_model.from_map(k))
        else:
            self.instance_counts = None
        return self


class GetInstanceCountTrendResponseInstanceCounts(TeaModel):
    def __init__(self, date=None, count=None):
        self.date = date                # type: int
        self.count = count              # type: int

    def validate(self):
        self.validate_required(self.date, 'date')
        self.validate_required(self.count, 'count')

    def to_map(self):
        result = {}
        result['Date'] = self.date
        result['Count'] = self.count
        return result

    def from_map(self, map={}):
        self.date = map.get('Date')
        self.count = map.get('Count')
        return self


class DeleteTableRequest(TeaModel):
    def __init__(self, project_id=None, table_name=None, env_type=None, app_guid=None):
        self.project_id = project_id    # type: int
        self.table_name = table_name    # type: str
        self.env_type = env_type        # type: int
        self.app_guid = app_guid        # type: str

    def validate(self):
        self.validate_required(self.table_name, 'table_name')

    def to_map(self):
        result = {}
        result['ProjectId'] = self.project_id
        result['TableName'] = self.table_name
        result['EnvType'] = self.env_type
        result['AppGuid'] = self.app_guid
        return result

    def from_map(self, map={}):
        self.project_id = map.get('ProjectId')
        self.table_name = map.get('TableName')
        self.env_type = map.get('EnvType')
        self.app_guid = map.get('AppGuid')
        return self


class DeleteTableResponse(TeaModel):
    def __init__(self, request_id=None, task_info=None):
        self.request_id = request_id    # type: str
        self.task_info = task_info      # type: DeleteTableResponseTaskInfo

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.task_info, 'task_info')
        if self.task_info:
            self.task_info.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        if self.task_info is not None:
            result['TaskInfo'] = self.task_info.to_map()
        else:
            result['TaskInfo'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('TaskInfo') is not None:
            temp_model = DeleteTableResponseTaskInfo()
            self.task_info = temp_model.from_map(map['TaskInfo'])
        else:
            self.task_info = None
        return self


class DeleteTableResponseTaskInfo(TeaModel):
    def __init__(self, task_id=None, content=None, status=None, next_task_id=None):
        self.task_id = task_id          # type: str
        self.content = content          # type: str
        self.status = status            # type: str
        self.next_task_id = next_task_id  # type: str

    def validate(self):
        self.validate_required(self.task_id, 'task_id')
        self.validate_required(self.content, 'content')
        self.validate_required(self.status, 'status')
        self.validate_required(self.next_task_id, 'next_task_id')

    def to_map(self):
        result = {}
        result['TaskId'] = self.task_id
        result['Content'] = self.content
        result['Status'] = self.status
        result['NextTaskId'] = self.next_task_id
        return result

    def from_map(self, map={}):
        self.task_id = map.get('TaskId')
        self.content = map.get('Content')
        self.status = map.get('Status')
        self.next_task_id = map.get('NextTaskId')
        return self


class ListTableThemeRequest(TeaModel):
    def __init__(self, project_id=None, parent_id=None, page_num=None, page_size=None):
        self.project_id = project_id    # type: int
        self.parent_id = parent_id      # type: int
        self.page_num = page_num        # type: int
        self.page_size = page_size      # type: int

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['ProjectId'] = self.project_id
        result['ParentId'] = self.parent_id
        result['PageNum'] = self.page_num
        result['PageSize'] = self.page_size
        return result

    def from_map(self, map={}):
        self.project_id = map.get('ProjectId')
        self.parent_id = map.get('ParentId')
        self.page_num = map.get('PageNum')
        self.page_size = map.get('PageSize')
        return self


class ListTableThemeResponse(TeaModel):
    def __init__(self, request_id=None, error_code=None, error_message=None, http_status_code=None, success=None,
                 data=None):
        self.request_id = request_id    # type: str
        self.error_code = error_code    # type: str
        self.error_message = error_message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.success = success          # type: bool
        self.data = data                # type: ListTableThemeResponseData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.error_code, 'error_code')
        self.validate_required(self.error_message, 'error_message')
        self.validate_required(self.http_status_code, 'http_status_code')
        self.validate_required(self.success, 'success')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['ErrorCode'] = self.error_code
        result['ErrorMessage'] = self.error_message
        result['HttpStatusCode'] = self.http_status_code
        result['Success'] = self.success
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.error_code = map.get('ErrorCode')
        self.error_message = map.get('ErrorMessage')
        self.http_status_code = map.get('HttpStatusCode')
        self.success = map.get('Success')
        if map.get('Data') is not None:
            temp_model = ListTableThemeResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class ListTableThemeResponseDataThemeList(TeaModel):
    def __init__(self, theme_id=None, name=None, level=None, parent_id=None, project_id=None, creator=None,
                 create_time_stamp=None):
        self.theme_id = theme_id        # type: int
        self.name = name                # type: str
        self.level = level              # type: int
        self.parent_id = parent_id      # type: int
        self.project_id = project_id    # type: int
        self.creator = creator          # type: str
        self.create_time_stamp = create_time_stamp  # type: int

    def validate(self):
        self.validate_required(self.theme_id, 'theme_id')
        self.validate_required(self.name, 'name')
        self.validate_required(self.level, 'level')
        self.validate_required(self.parent_id, 'parent_id')
        self.validate_required(self.project_id, 'project_id')
        self.validate_required(self.creator, 'creator')
        self.validate_required(self.create_time_stamp, 'create_time_stamp')

    def to_map(self):
        result = {}
        result['ThemeId'] = self.theme_id
        result['Name'] = self.name
        result['Level'] = self.level
        result['ParentId'] = self.parent_id
        result['ProjectId'] = self.project_id
        result['Creator'] = self.creator
        result['CreateTimeStamp'] = self.create_time_stamp
        return result

    def from_map(self, map={}):
        self.theme_id = map.get('ThemeId')
        self.name = map.get('Name')
        self.level = map.get('Level')
        self.parent_id = map.get('ParentId')
        self.project_id = map.get('ProjectId')
        self.creator = map.get('Creator')
        self.create_time_stamp = map.get('CreateTimeStamp')
        return self


class ListTableThemeResponseData(TeaModel):
    def __init__(self, total_count=None, theme_list=None):
        self.total_count = total_count  # type: int
        self.theme_list = theme_list    # type: List[ListTableThemeResponseDataThemeList]

    def validate(self):
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.theme_list, 'theme_list')
        if self.theme_list:
            for k in self.theme_list:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['TotalCount'] = self.total_count
        result['ThemeList'] = []
        if self.theme_list is not None:
            for k in self.theme_list:
                result['ThemeList'].append(k.to_map() if k else None)
        else:
            result['ThemeList'] = None
        return result

    def from_map(self, map={}):
        self.total_count = map.get('TotalCount')
        self.theme_list = []
        if map.get('ThemeList') is not None:
            for k in map.get('ThemeList'):
                temp_model = ListTableThemeResponseDataThemeList()
                self.theme_list.append(temp_model.from_map(k))
        else:
            self.theme_list = None
        return self


class GetSuccessInstanceTrendRequest(TeaModel):
    def __init__(self, project_id=None):
        self.project_id = project_id    # type: int

    def validate(self):
        self.validate_required(self.project_id, 'project_id')

    def to_map(self):
        result = {}
        result['ProjectId'] = self.project_id
        return result

    def from_map(self, map={}):
        self.project_id = map.get('ProjectId')
        return self


class GetSuccessInstanceTrendResponse(TeaModel):
    def __init__(self, request_id=None, instance_status_trend=None):
        self.request_id = request_id    # type: str
        self.instance_status_trend = instance_status_trend  # type: GetSuccessInstanceTrendResponseInstanceStatusTrend

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.instance_status_trend, 'instance_status_trend')
        if self.instance_status_trend:
            self.instance_status_trend.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        if self.instance_status_trend is not None:
            result['InstanceStatusTrend'] = self.instance_status_trend.to_map()
        else:
            result['InstanceStatusTrend'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('InstanceStatusTrend') is not None:
            temp_model = GetSuccessInstanceTrendResponseInstanceStatusTrend()
            self.instance_status_trend = temp_model.from_map(map['InstanceStatusTrend'])
        else:
            self.instance_status_trend = None
        return self


class GetSuccessInstanceTrendResponseInstanceStatusTrendTodayTrend(TeaModel):
    def __init__(self, count=None, time_point=None):
        self.count = count              # type: int
        self.time_point = time_point    # type: str

    def validate(self):
        self.validate_required(self.count, 'count')
        self.validate_required(self.time_point, 'time_point')

    def to_map(self):
        result = {}
        result['Count'] = self.count
        result['TimePoint'] = self.time_point
        return result

    def from_map(self, map={}):
        self.count = map.get('Count')
        self.time_point = map.get('TimePoint')
        return self


class GetSuccessInstanceTrendResponseInstanceStatusTrendYesterdayTrend(TeaModel):
    def __init__(self, count=None, time_point=None):
        self.count = count              # type: int
        self.time_point = time_point    # type: str

    def validate(self):
        self.validate_required(self.count, 'count')
        self.validate_required(self.time_point, 'time_point')

    def to_map(self):
        result = {}
        result['Count'] = self.count
        result['TimePoint'] = self.time_point
        return result

    def from_map(self, map={}):
        self.count = map.get('Count')
        self.time_point = map.get('TimePoint')
        return self


class GetSuccessInstanceTrendResponseInstanceStatusTrendAvgTrend(TeaModel):
    def __init__(self, count=None, time_point=None):
        self.count = count              # type: int
        self.time_point = time_point    # type: str

    def validate(self):
        self.validate_required(self.count, 'count')
        self.validate_required(self.time_point, 'time_point')

    def to_map(self):
        result = {}
        result['Count'] = self.count
        result['TimePoint'] = self.time_point
        return result

    def from_map(self, map={}):
        self.count = map.get('Count')
        self.time_point = map.get('TimePoint')
        return self


class GetSuccessInstanceTrendResponseInstanceStatusTrend(TeaModel):
    def __init__(self, today_trend=None, yesterday_trend=None, avg_trend=None):
        self.today_trend = today_trend  # type: List[GetSuccessInstanceTrendResponseInstanceStatusTrendTodayTrend]
        self.yesterday_trend = yesterday_trend  # type: List[GetSuccessInstanceTrendResponseInstanceStatusTrendYesterdayTrend]
        self.avg_trend = avg_trend      # type: List[GetSuccessInstanceTrendResponseInstanceStatusTrendAvgTrend]

    def validate(self):
        self.validate_required(self.today_trend, 'today_trend')
        if self.today_trend:
            for k in self.today_trend:
                if k:
                    k.validate()
        self.validate_required(self.yesterday_trend, 'yesterday_trend')
        if self.yesterday_trend:
            for k in self.yesterday_trend:
                if k:
                    k.validate()
        self.validate_required(self.avg_trend, 'avg_trend')
        if self.avg_trend:
            for k in self.avg_trend:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['TodayTrend'] = []
        if self.today_trend is not None:
            for k in self.today_trend:
                result['TodayTrend'].append(k.to_map() if k else None)
        else:
            result['TodayTrend'] = None
        result['YesterdayTrend'] = []
        if self.yesterday_trend is not None:
            for k in self.yesterday_trend:
                result['YesterdayTrend'].append(k.to_map() if k else None)
        else:
            result['YesterdayTrend'] = None
        result['AvgTrend'] = []
        if self.avg_trend is not None:
            for k in self.avg_trend:
                result['AvgTrend'].append(k.to_map() if k else None)
        else:
            result['AvgTrend'] = None
        return result

    def from_map(self, map={}):
        self.today_trend = []
        if map.get('TodayTrend') is not None:
            for k in map.get('TodayTrend'):
                temp_model = GetSuccessInstanceTrendResponseInstanceStatusTrendTodayTrend()
                self.today_trend.append(temp_model.from_map(k))
        else:
            self.today_trend = None
        self.yesterday_trend = []
        if map.get('YesterdayTrend') is not None:
            for k in map.get('YesterdayTrend'):
                temp_model = GetSuccessInstanceTrendResponseInstanceStatusTrendYesterdayTrend()
                self.yesterday_trend.append(temp_model.from_map(k))
        else:
            self.yesterday_trend = None
        self.avg_trend = []
        if map.get('AvgTrend') is not None:
            for k in map.get('AvgTrend'):
                temp_model = GetSuccessInstanceTrendResponseInstanceStatusTrendAvgTrend()
                self.avg_trend.append(temp_model.from_map(k))
        else:
            self.avg_trend = None
        return self


class UpdateTableRequest(TeaModel):
    def __init__(self, has_part=None, columns=None, is_view=None, visibility=None, life_cycle=None, category_id=None,
                 logical_level_id=None, physics_level_id=None, external_table_type=None, location=None, project_id=None,
                 table_name=None, endpoint=None, env_type=None, themes=None, app_guid=None, create_if_not_exists=None):
        self.has_part = has_part        # type: int
        self.columns = columns          # type: List[UpdateTableRequestColumns]
        self.is_view = is_view          # type: int
        self.visibility = visibility    # type: int
        self.life_cycle = life_cycle    # type: int
        self.category_id = category_id  # type: int
        self.logical_level_id = logical_level_id  # type: int
        self.physics_level_id = physics_level_id  # type: int
        self.external_table_type = external_table_type  # type: str
        self.location = location        # type: str
        self.project_id = project_id    # type: int
        self.table_name = table_name    # type: str
        self.endpoint = endpoint        # type: str
        self.env_type = env_type        # type: int
        self.themes = themes            # type: List[UpdateTableRequestThemes]
        self.app_guid = app_guid        # type: str
        self.create_if_not_exists = create_if_not_exists  # type: bool

    def validate(self):
        self.validate_required(self.columns, 'columns')
        if self.columns:
            for k in self.columns:
                if k:
                    k.validate()
        self.validate_required(self.table_name, 'table_name')
        if self.themes:
            for k in self.themes:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['HasPart'] = self.has_part
        result['Columns'] = []
        if self.columns is not None:
            for k in self.columns:
                result['Columns'].append(k.to_map() if k else None)
        else:
            result['Columns'] = None
        result['IsView'] = self.is_view
        result['Visibility'] = self.visibility
        result['LifeCycle'] = self.life_cycle
        result['CategoryId'] = self.category_id
        result['LogicalLevelId'] = self.logical_level_id
        result['PhysicsLevelId'] = self.physics_level_id
        result['ExternalTableType'] = self.external_table_type
        result['Location'] = self.location
        result['ProjectId'] = self.project_id
        result['TableName'] = self.table_name
        result['Endpoint'] = self.endpoint
        result['EnvType'] = self.env_type
        result['Themes'] = []
        if self.themes is not None:
            for k in self.themes:
                result['Themes'].append(k.to_map() if k else None)
        else:
            result['Themes'] = None
        result['AppGuid'] = self.app_guid
        result['CreateIfNotExists'] = self.create_if_not_exists
        return result

    def from_map(self, map={}):
        self.has_part = map.get('HasPart')
        self.columns = []
        if map.get('Columns') is not None:
            for k in map.get('Columns'):
                temp_model = UpdateTableRequestColumns()
                self.columns.append(temp_model.from_map(k))
        else:
            self.columns = None
        self.is_view = map.get('IsView')
        self.visibility = map.get('Visibility')
        self.life_cycle = map.get('LifeCycle')
        self.category_id = map.get('CategoryId')
        self.logical_level_id = map.get('LogicalLevelId')
        self.physics_level_id = map.get('PhysicsLevelId')
        self.external_table_type = map.get('ExternalTableType')
        self.location = map.get('Location')
        self.project_id = map.get('ProjectId')
        self.table_name = map.get('TableName')
        self.endpoint = map.get('Endpoint')
        self.env_type = map.get('EnvType')
        self.themes = []
        if map.get('Themes') is not None:
            for k in map.get('Themes'):
                temp_model = UpdateTableRequestThemes()
                self.themes.append(temp_model.from_map(k))
        else:
            self.themes = None
        self.app_guid = map.get('AppGuid')
        self.create_if_not_exists = map.get('CreateIfNotExists')
        return self


class UpdateTableRequestColumns(TeaModel):
    def __init__(self, column_name=None, column_name_cn=None, column_type=None, seq_number=None, length=None,
                 is_partition_col=None, is_primary_key=None, is_nullable=None, comment=None):
        self.column_name = column_name  # type: str
        self.column_name_cn = column_name_cn  # type: str
        self.column_type = column_type  # type: str
        self.seq_number = seq_number    # type: int
        self.length = length            # type: int
        self.is_partition_col = is_partition_col  # type: int
        self.is_primary_key = is_primary_key  # type: int
        self.is_nullable = is_nullable  # type: int
        self.comment = comment          # type: str

    def validate(self):
        self.validate_required(self.column_name, 'column_name')
        self.validate_required(self.column_type, 'column_type')

    def to_map(self):
        result = {}
        result['ColumnName'] = self.column_name
        result['ColumnNameCn'] = self.column_name_cn
        result['ColumnType'] = self.column_type
        result['SeqNumber'] = self.seq_number
        result['Length'] = self.length
        result['IsPartitionCol'] = self.is_partition_col
        result['IsPrimaryKey'] = self.is_primary_key
        result['IsNullable'] = self.is_nullable
        result['Comment'] = self.comment
        return result

    def from_map(self, map={}):
        self.column_name = map.get('ColumnName')
        self.column_name_cn = map.get('ColumnNameCn')
        self.column_type = map.get('ColumnType')
        self.seq_number = map.get('SeqNumber')
        self.length = map.get('Length')
        self.is_partition_col = map.get('IsPartitionCol')
        self.is_primary_key = map.get('IsPrimaryKey')
        self.is_nullable = map.get('IsNullable')
        self.comment = map.get('Comment')
        return self


class UpdateTableRequestThemes(TeaModel):
    def __init__(self, theme_id=None, theme_level=None):
        self.theme_id = theme_id        # type: int
        self.theme_level = theme_level  # type: int

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['ThemeId'] = self.theme_id
        result['ThemeLevel'] = self.theme_level
        return result

    def from_map(self, map={}):
        self.theme_id = map.get('ThemeId')
        self.theme_level = map.get('ThemeLevel')
        return self


class UpdateTableResponse(TeaModel):
    def __init__(self, request_id=None, task_info=None):
        self.request_id = request_id    # type: str
        self.task_info = task_info      # type: UpdateTableResponseTaskInfo

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.task_info, 'task_info')
        if self.task_info:
            self.task_info.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        if self.task_info is not None:
            result['TaskInfo'] = self.task_info.to_map()
        else:
            result['TaskInfo'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('TaskInfo') is not None:
            temp_model = UpdateTableResponseTaskInfo()
            self.task_info = temp_model.from_map(map['TaskInfo'])
        else:
            self.task_info = None
        return self


class UpdateTableResponseTaskInfo(TeaModel):
    def __init__(self, task_id=None, content=None, status=None, next_task_id=None):
        self.task_id = task_id          # type: str
        self.content = content          # type: str
        self.status = status            # type: str
        self.next_task_id = next_task_id  # type: str

    def validate(self):
        self.validate_required(self.task_id, 'task_id')
        self.validate_required(self.content, 'content')
        self.validate_required(self.status, 'status')
        self.validate_required(self.next_task_id, 'next_task_id')

    def to_map(self):
        result = {}
        result['TaskId'] = self.task_id
        result['Content'] = self.content
        result['Status'] = self.status
        result['NextTaskId'] = self.next_task_id
        return result

    def from_map(self, map={}):
        self.task_id = map.get('TaskId')
        self.content = map.get('Content')
        self.status = map.get('Status')
        self.next_task_id = map.get('NextTaskId')
        return self


class GetDataServiceFolderRequest(TeaModel):
    def __init__(self, tenant_id=None, project_id=None, folder_id=None):
        self.tenant_id = tenant_id      # type: int
        self.project_id = project_id    # type: int
        self.folder_id = folder_id      # type: int

    def validate(self):
        self.validate_required(self.tenant_id, 'tenant_id')
        self.validate_required(self.project_id, 'project_id')
        self.validate_required(self.folder_id, 'folder_id')

    def to_map(self):
        result = {}
        result['TenantId'] = self.tenant_id
        result['ProjectId'] = self.project_id
        result['FolderId'] = self.folder_id
        return result

    def from_map(self, map={}):
        self.tenant_id = map.get('TenantId')
        self.project_id = map.get('ProjectId')
        self.folder_id = map.get('FolderId')
        return self


class GetDataServiceFolderResponse(TeaModel):
    def __init__(self, request_id=None, folder=None):
        self.request_id = request_id    # type: str
        self.folder = folder            # type: GetDataServiceFolderResponseFolder

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.folder, 'folder')
        if self.folder:
            self.folder.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        if self.folder is not None:
            result['Folder'] = self.folder.to_map()
        else:
            result['Folder'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('Folder') is not None:
            temp_model = GetDataServiceFolderResponseFolder()
            self.folder = temp_model.from_map(map['Folder'])
        else:
            self.folder = None
        return self


class GetDataServiceFolderResponseFolder(TeaModel):
    def __init__(self, tenant_id=None, project_id=None, folder_id=None, folder_name=None, created_time=None,
                 modified_time=None, group_id=None, parent_id=None):
        self.tenant_id = tenant_id      # type: int
        self.project_id = project_id    # type: int
        self.folder_id = folder_id      # type: int
        self.folder_name = folder_name  # type: str
        self.created_time = created_time  # type: str
        self.modified_time = modified_time  # type: str
        self.group_id = group_id        # type: str
        self.parent_id = parent_id      # type: int

    def validate(self):
        self.validate_required(self.tenant_id, 'tenant_id')
        self.validate_required(self.project_id, 'project_id')
        self.validate_required(self.folder_id, 'folder_id')
        self.validate_required(self.folder_name, 'folder_name')
        self.validate_required(self.created_time, 'created_time')
        self.validate_required(self.modified_time, 'modified_time')
        self.validate_required(self.group_id, 'group_id')
        self.validate_required(self.parent_id, 'parent_id')

    def to_map(self):
        result = {}
        result['TenantId'] = self.tenant_id
        result['ProjectId'] = self.project_id
        result['FolderId'] = self.folder_id
        result['FolderName'] = self.folder_name
        result['CreatedTime'] = self.created_time
        result['ModifiedTime'] = self.modified_time
        result['GroupId'] = self.group_id
        result['ParentId'] = self.parent_id
        return result

    def from_map(self, map={}):
        self.tenant_id = map.get('TenantId')
        self.project_id = map.get('ProjectId')
        self.folder_id = map.get('FolderId')
        self.folder_name = map.get('FolderName')
        self.created_time = map.get('CreatedTime')
        self.modified_time = map.get('ModifiedTime')
        self.group_id = map.get('GroupId')
        self.parent_id = map.get('ParentId')
        return self


class ListTableLevelRequest(TeaModel):
    def __init__(self, project_id=None, level_type=None):
        self.project_id = project_id    # type: int
        self.level_type = level_type    # type: int

    def validate(self):
        self.validate_required(self.project_id, 'project_id')
        self.validate_required(self.level_type, 'level_type')

    def to_map(self):
        result = {}
        result['ProjectId'] = self.project_id
        result['LevelType'] = self.level_type
        return result

    def from_map(self, map={}):
        self.project_id = map.get('ProjectId')
        self.level_type = map.get('LevelType')
        return self


class ListTableLevelResponse(TeaModel):
    def __init__(self, request_id=None, error_code=None, error_message=None, http_status_code=None, success=None,
                 table_level_info=None):
        self.request_id = request_id    # type: str
        self.error_code = error_code    # type: str
        self.error_message = error_message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.success = success          # type: bool
        self.table_level_info = table_level_info  # type: ListTableLevelResponseTableLevelInfo

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.error_code, 'error_code')
        self.validate_required(self.error_message, 'error_message')
        self.validate_required(self.http_status_code, 'http_status_code')
        self.validate_required(self.success, 'success')
        self.validate_required(self.table_level_info, 'table_level_info')
        if self.table_level_info:
            self.table_level_info.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['ErrorCode'] = self.error_code
        result['ErrorMessage'] = self.error_message
        result['HttpStatusCode'] = self.http_status_code
        result['Success'] = self.success
        if self.table_level_info is not None:
            result['TableLevelInfo'] = self.table_level_info.to_map()
        else:
            result['TableLevelInfo'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.error_code = map.get('ErrorCode')
        self.error_message = map.get('ErrorMessage')
        self.http_status_code = map.get('HttpStatusCode')
        self.success = map.get('Success')
        if map.get('TableLevelInfo') is not None:
            temp_model = ListTableLevelResponseTableLevelInfo()
            self.table_level_info = temp_model.from_map(map['TableLevelInfo'])
        else:
            self.table_level_info = None
        return self


class ListTableLevelResponseTableLevelInfoLevelList(TeaModel):
    def __init__(self, level_id=None, name=None, project_id=None, level_type=None, description=None):
        self.level_id = level_id        # type: int
        self.name = name                # type: str
        self.project_id = project_id    # type: int
        self.level_type = level_type    # type: int
        self.description = description  # type: str

    def validate(self):
        self.validate_required(self.level_id, 'level_id')
        self.validate_required(self.name, 'name')
        self.validate_required(self.project_id, 'project_id')
        self.validate_required(self.level_type, 'level_type')
        self.validate_required(self.description, 'description')

    def to_map(self):
        result = {}
        result['LevelId'] = self.level_id
        result['Name'] = self.name
        result['ProjectId'] = self.project_id
        result['LevelType'] = self.level_type
        result['Description'] = self.description
        return result

    def from_map(self, map={}):
        self.level_id = map.get('LevelId')
        self.name = map.get('Name')
        self.project_id = map.get('ProjectId')
        self.level_type = map.get('LevelType')
        self.description = map.get('Description')
        return self


class ListTableLevelResponseTableLevelInfo(TeaModel):
    def __init__(self, total_count=None, level_list=None):
        self.total_count = total_count  # type: int
        self.level_list = level_list    # type: List[ListTableLevelResponseTableLevelInfoLevelList]

    def validate(self):
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.level_list, 'level_list')
        if self.level_list:
            for k in self.level_list:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['TotalCount'] = self.total_count
        result['LevelList'] = []
        if self.level_list is not None:
            for k in self.level_list:
                result['LevelList'].append(k.to_map() if k else None)
        else:
            result['LevelList'] = None
        return result

    def from_map(self, map={}):
        self.total_count = map.get('TotalCount')
        self.level_list = []
        if map.get('LevelList') is not None:
            for k in map.get('LevelList'):
                temp_model = ListTableLevelResponseTableLevelInfoLevelList()
                self.level_list.append(temp_model.from_map(k))
        else:
            self.level_list = None
        return self


class ListDataServiceGroupsRequest(TeaModel):
    def __init__(self, page_number=None, page_size=None, project_id=None, tenant_id=None, group_name_keyword=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size      # type: int
        self.project_id = project_id    # type: int
        self.tenant_id = tenant_id      # type: int
        self.group_name_keyword = group_name_keyword  # type: str

    def validate(self):
        self.validate_required(self.project_id, 'project_id')
        self.validate_required(self.tenant_id, 'tenant_id')

    def to_map(self):
        result = {}
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        result['ProjectId'] = self.project_id
        result['TenantId'] = self.tenant_id
        result['GroupNameKeyword'] = self.group_name_keyword
        return result

    def from_map(self, map={}):
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        self.project_id = map.get('ProjectId')
        self.tenant_id = map.get('TenantId')
        self.group_name_keyword = map.get('GroupNameKeyword')
        return self


class ListDataServiceGroupsResponse(TeaModel):
    def __init__(self, request_id=None, group_paging_result=None):
        self.request_id = request_id    # type: str
        self.group_paging_result = group_paging_result  # type: ListDataServiceGroupsResponseGroupPagingResult

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.group_paging_result, 'group_paging_result')
        if self.group_paging_result:
            self.group_paging_result.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        if self.group_paging_result is not None:
            result['GroupPagingResult'] = self.group_paging_result.to_map()
        else:
            result['GroupPagingResult'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('GroupPagingResult') is not None:
            temp_model = ListDataServiceGroupsResponseGroupPagingResult()
            self.group_paging_result = temp_model.from_map(map['GroupPagingResult'])
        else:
            self.group_paging_result = None
        return self


class ListDataServiceGroupsResponseGroupPagingResultGroups(TeaModel):
    def __init__(self, tenant_id=None, group_id=None, api_gateway_group_id=None, group_name=None, description=None,
                 created_time=None, modified_time=None, creator_id=None, project_id=None):
        self.tenant_id = tenant_id      # type: int
        self.group_id = group_id        # type: str
        self.api_gateway_group_id = api_gateway_group_id  # type: str
        self.group_name = group_name    # type: str
        self.description = description  # type: str
        self.created_time = created_time  # type: str
        self.modified_time = modified_time  # type: str
        self.creator_id = creator_id    # type: str
        self.project_id = project_id    # type: int

    def validate(self):
        self.validate_required(self.tenant_id, 'tenant_id')
        self.validate_required(self.group_id, 'group_id')
        self.validate_required(self.api_gateway_group_id, 'api_gateway_group_id')
        self.validate_required(self.group_name, 'group_name')
        self.validate_required(self.description, 'description')
        self.validate_required(self.created_time, 'created_time')
        self.validate_required(self.modified_time, 'modified_time')
        self.validate_required(self.creator_id, 'creator_id')
        self.validate_required(self.project_id, 'project_id')

    def to_map(self):
        result = {}
        result['TenantId'] = self.tenant_id
        result['GroupId'] = self.group_id
        result['ApiGatewayGroupId'] = self.api_gateway_group_id
        result['GroupName'] = self.group_name
        result['Description'] = self.description
        result['CreatedTime'] = self.created_time
        result['ModifiedTime'] = self.modified_time
        result['CreatorId'] = self.creator_id
        result['ProjectId'] = self.project_id
        return result

    def from_map(self, map={}):
        self.tenant_id = map.get('TenantId')
        self.group_id = map.get('GroupId')
        self.api_gateway_group_id = map.get('ApiGatewayGroupId')
        self.group_name = map.get('GroupName')
        self.description = map.get('Description')
        self.created_time = map.get('CreatedTime')
        self.modified_time = map.get('ModifiedTime')
        self.creator_id = map.get('CreatorId')
        self.project_id = map.get('ProjectId')
        return self


class ListDataServiceGroupsResponseGroupPagingResult(TeaModel):
    def __init__(self, page_number=None, page_size=None, total_count=None, groups=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size      # type: int
        self.total_count = total_count  # type: int
        self.groups = groups            # type: List[ListDataServiceGroupsResponseGroupPagingResultGroups]

    def validate(self):
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.groups, 'groups')
        if self.groups:
            for k in self.groups:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        result['TotalCount'] = self.total_count
        result['Groups'] = []
        if self.groups is not None:
            for k in self.groups:
                result['Groups'].append(k.to_map() if k else None)
        else:
            result['Groups'] = None
        return result

    def from_map(self, map={}):
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        self.total_count = map.get('TotalCount')
        self.groups = []
        if map.get('Groups') is not None:
            for k in map.get('Groups'):
                temp_model = ListDataServiceGroupsResponseGroupPagingResultGroups()
                self.groups.append(temp_model.from_map(k))
        else:
            self.groups = None
        return self


class UpdateTableThemeRequest(TeaModel):
    def __init__(self, project_id=None, name=None, theme_id=None):
        self.project_id = project_id    # type: int
        self.name = name                # type: str
        self.theme_id = theme_id        # type: int

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.theme_id, 'theme_id')

    def to_map(self):
        result = {}
        result['ProjectId'] = self.project_id
        result['Name'] = self.name
        result['ThemeId'] = self.theme_id
        return result

    def from_map(self, map={}):
        self.project_id = map.get('ProjectId')
        self.name = map.get('Name')
        self.theme_id = map.get('ThemeId')
        return self


class UpdateTableThemeResponse(TeaModel):
    def __init__(self, request_id=None, error_code=None, error_message=None, http_status_code=None, success=None,
                 update_result=None):
        self.request_id = request_id    # type: str
        self.error_code = error_code    # type: str
        self.error_message = error_message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.success = success          # type: bool
        self.update_result = update_result  # type: bool

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.error_code, 'error_code')
        self.validate_required(self.error_message, 'error_message')
        self.validate_required(self.http_status_code, 'http_status_code')
        self.validate_required(self.success, 'success')
        self.validate_required(self.update_result, 'update_result')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['ErrorCode'] = self.error_code
        result['ErrorMessage'] = self.error_message
        result['HttpStatusCode'] = self.http_status_code
        result['Success'] = self.success
        result['UpdateResult'] = self.update_result
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.error_code = map.get('ErrorCode')
        self.error_message = map.get('ErrorMessage')
        self.http_status_code = map.get('HttpStatusCode')
        self.success = map.get('Success')
        self.update_result = map.get('UpdateResult')
        return self


class CreateDataServiceFolderRequest(TeaModel):
    def __init__(self, tenant_id=None, project_id=None, folder_name=None, parent_id=None, group_id=None):
        self.tenant_id = tenant_id      # type: int
        self.project_id = project_id    # type: int
        self.folder_name = folder_name  # type: str
        self.parent_id = parent_id      # type: int
        self.group_id = group_id        # type: str

    def validate(self):
        self.validate_required(self.tenant_id, 'tenant_id')
        self.validate_required(self.project_id, 'project_id')
        self.validate_required(self.folder_name, 'folder_name')
        self.validate_required(self.parent_id, 'parent_id')
        self.validate_required(self.group_id, 'group_id')

    def to_map(self):
        result = {}
        result['TenantId'] = self.tenant_id
        result['ProjectId'] = self.project_id
        result['FolderName'] = self.folder_name
        result['ParentId'] = self.parent_id
        result['GroupId'] = self.group_id
        return result

    def from_map(self, map={}):
        self.tenant_id = map.get('TenantId')
        self.project_id = map.get('ProjectId')
        self.folder_name = map.get('FolderName')
        self.parent_id = map.get('ParentId')
        self.group_id = map.get('GroupId')
        return self


class CreateDataServiceFolderResponse(TeaModel):
    def __init__(self, folder_id=None, request_id=None):
        self.folder_id = folder_id      # type: int
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.folder_id, 'folder_id')
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['FolderId'] = self.folder_id
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.folder_id = map.get('FolderId')
        self.request_id = map.get('RequestId')
        return self


class GetDataServiceGroupRequest(TeaModel):
    def __init__(self, tenant_id=None, project_id=None, group_id=None):
        self.tenant_id = tenant_id      # type: int
        self.project_id = project_id    # type: int
        self.group_id = group_id        # type: str

    def validate(self):
        self.validate_required(self.tenant_id, 'tenant_id')
        self.validate_required(self.project_id, 'project_id')
        self.validate_required(self.group_id, 'group_id')

    def to_map(self):
        result = {}
        result['TenantId'] = self.tenant_id
        result['ProjectId'] = self.project_id
        result['GroupId'] = self.group_id
        return result

    def from_map(self, map={}):
        self.tenant_id = map.get('TenantId')
        self.project_id = map.get('ProjectId')
        self.group_id = map.get('GroupId')
        return self


class GetDataServiceGroupResponse(TeaModel):
    def __init__(self, request_id=None, group=None):
        self.request_id = request_id    # type: str
        self.group = group              # type: GetDataServiceGroupResponseGroup

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.group, 'group')
        if self.group:
            self.group.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        if self.group is not None:
            result['Group'] = self.group.to_map()
        else:
            result['Group'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('Group') is not None:
            temp_model = GetDataServiceGroupResponseGroup()
            self.group = temp_model.from_map(map['Group'])
        else:
            self.group = None
        return self


class GetDataServiceGroupResponseGroup(TeaModel):
    def __init__(self, tenant_id=None, project_id=None, group_id=None, api_gateway_group_id=None, group_name=None,
                 description=None, created_time=None, modified_time=None, creator_id=None):
        self.tenant_id = tenant_id      # type: int
        self.project_id = project_id    # type: int
        self.group_id = group_id        # type: str
        self.api_gateway_group_id = api_gateway_group_id  # type: str
        self.group_name = group_name    # type: str
        self.description = description  # type: str
        self.created_time = created_time  # type: str
        self.modified_time = modified_time  # type: str
        self.creator_id = creator_id    # type: str

    def validate(self):
        self.validate_required(self.tenant_id, 'tenant_id')
        self.validate_required(self.project_id, 'project_id')
        self.validate_required(self.group_id, 'group_id')
        self.validate_required(self.api_gateway_group_id, 'api_gateway_group_id')
        self.validate_required(self.group_name, 'group_name')
        self.validate_required(self.description, 'description')
        self.validate_required(self.created_time, 'created_time')
        self.validate_required(self.modified_time, 'modified_time')
        self.validate_required(self.creator_id, 'creator_id')

    def to_map(self):
        result = {}
        result['TenantId'] = self.tenant_id
        result['ProjectId'] = self.project_id
        result['GroupId'] = self.group_id
        result['ApiGatewayGroupId'] = self.api_gateway_group_id
        result['GroupName'] = self.group_name
        result['Description'] = self.description
        result['CreatedTime'] = self.created_time
        result['ModifiedTime'] = self.modified_time
        result['CreatorId'] = self.creator_id
        return result

    def from_map(self, map={}):
        self.tenant_id = map.get('TenantId')
        self.project_id = map.get('ProjectId')
        self.group_id = map.get('GroupId')
        self.api_gateway_group_id = map.get('ApiGatewayGroupId')
        self.group_name = map.get('GroupName')
        self.description = map.get('Description')
        self.created_time = map.get('CreatedTime')
        self.modified_time = map.get('ModifiedTime')
        self.creator_id = map.get('CreatorId')
        return self


class CreateTableLevelRequest(TeaModel):
    def __init__(self, project_id=None, level_type=None, name=None, description=None):
        self.project_id = project_id    # type: int
        self.level_type = level_type    # type: int
        self.name = name                # type: str
        self.description = description  # type: str

    def validate(self):
        self.validate_required(self.level_type, 'level_type')
        self.validate_required(self.name, 'name')

    def to_map(self):
        result = {}
        result['ProjectId'] = self.project_id
        result['LevelType'] = self.level_type
        result['Name'] = self.name
        result['Description'] = self.description
        return result

    def from_map(self, map={}):
        self.project_id = map.get('ProjectId')
        self.level_type = map.get('LevelType')
        self.name = map.get('Name')
        self.description = map.get('Description')
        return self


class CreateTableLevelResponse(TeaModel):
    def __init__(self, request_id=None, error_code=None, error_message=None, http_status_code=None, success=None,
                 level_id=None):
        self.request_id = request_id    # type: str
        self.error_code = error_code    # type: str
        self.error_message = error_message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.success = success          # type: bool
        self.level_id = level_id        # type: int

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.error_code, 'error_code')
        self.validate_required(self.error_message, 'error_message')
        self.validate_required(self.http_status_code, 'http_status_code')
        self.validate_required(self.success, 'success')
        self.validate_required(self.level_id, 'level_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['ErrorCode'] = self.error_code
        result['ErrorMessage'] = self.error_message
        result['HttpStatusCode'] = self.http_status_code
        result['Success'] = self.success
        result['LevelId'] = self.level_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.error_code = map.get('ErrorCode')
        self.error_message = map.get('ErrorMessage')
        self.http_status_code = map.get('HttpStatusCode')
        self.success = map.get('Success')
        self.level_id = map.get('LevelId')
        return self


class UpdateMetaTableIntroWikiRequest(TeaModel):
    def __init__(self, table_guid=None, content=None):
        self.table_guid = table_guid    # type: str
        self.content = content          # type: str

    def validate(self):
        self.validate_required(self.table_guid, 'table_guid')
        self.validate_required(self.content, 'content')

    def to_map(self):
        result = {}
        result['TableGuid'] = self.table_guid
        result['Content'] = self.content
        return result

    def from_map(self, map={}):
        self.table_guid = map.get('TableGuid')
        self.content = map.get('Content')
        return self


class UpdateMetaTableIntroWikiResponse(TeaModel):
    def __init__(self, request_id=None, update_result=None):
        self.request_id = request_id    # type: str
        self.update_result = update_result  # type: bool

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.update_result, 'update_result')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['UpdateResult'] = self.update_result
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.update_result = map.get('UpdateResult')
        return self


class DeleteTableLevelRequest(TeaModel):
    def __init__(self, level_id=None, project_id=None):
        self.level_id = level_id        # type: int
        self.project_id = project_id    # type: int

    def validate(self):
        self.validate_required(self.level_id, 'level_id')
        self.validate_required(self.project_id, 'project_id')

    def to_map(self):
        result = {}
        result['LevelId'] = self.level_id
        result['ProjectId'] = self.project_id
        return result

    def from_map(self, map={}):
        self.level_id = map.get('LevelId')
        self.project_id = map.get('ProjectId')
        return self


class DeleteTableLevelResponse(TeaModel):
    def __init__(self, request_id=None, delete_result=None):
        self.request_id = request_id    # type: str
        self.delete_result = delete_result  # type: bool

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.delete_result, 'delete_result')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['DeleteResult'] = self.delete_result
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.delete_result = map.get('DeleteResult')
        return self


class UpdateTableLevelRequest(TeaModel):
    def __init__(self, project_id=None, level_type=None, name=None, description=None, level_id=None):
        self.project_id = project_id    # type: int
        self.level_type = level_type    # type: int
        self.name = name                # type: str
        self.description = description  # type: str
        self.level_id = level_id        # type: int

    def validate(self):
        self.validate_required(self.project_id, 'project_id')
        self.validate_required(self.level_id, 'level_id')

    def to_map(self):
        result = {}
        result['ProjectId'] = self.project_id
        result['LevelType'] = self.level_type
        result['Name'] = self.name
        result['Description'] = self.description
        result['LevelId'] = self.level_id
        return result

    def from_map(self, map={}):
        self.project_id = map.get('ProjectId')
        self.level_type = map.get('LevelType')
        self.name = map.get('Name')
        self.description = map.get('Description')
        self.level_id = map.get('LevelId')
        return self


class UpdateTableLevelResponse(TeaModel):
    def __init__(self, request_id=None, error_code=None, error_message=None, http_status_code=None, success=None,
                 update_result=None):
        self.request_id = request_id    # type: str
        self.error_code = error_code    # type: str
        self.error_message = error_message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.success = success          # type: bool
        self.update_result = update_result  # type: bool

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.error_code, 'error_code')
        self.validate_required(self.error_message, 'error_message')
        self.validate_required(self.http_status_code, 'http_status_code')
        self.validate_required(self.success, 'success')
        self.validate_required(self.update_result, 'update_result')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['ErrorCode'] = self.error_code
        result['ErrorMessage'] = self.error_message
        result['HttpStatusCode'] = self.http_status_code
        result['Success'] = self.success
        result['UpdateResult'] = self.update_result
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.error_code = map.get('ErrorCode')
        self.error_message = map.get('ErrorMessage')
        self.http_status_code = map.get('HttpStatusCode')
        self.success = map.get('Success')
        self.update_result = map.get('UpdateResult')
        return self


class DeleteTableThemeRequest(TeaModel):
    def __init__(self, theme_id=None, project_id=None):
        self.theme_id = theme_id        # type: int
        self.project_id = project_id    # type: int

    def validate(self):
        self.validate_required(self.theme_id, 'theme_id')

    def to_map(self):
        result = {}
        result['ThemeId'] = self.theme_id
        result['ProjectId'] = self.project_id
        return result

    def from_map(self, map={}):
        self.theme_id = map.get('ThemeId')
        self.project_id = map.get('ProjectId')
        return self


class DeleteTableThemeResponse(TeaModel):
    def __init__(self, request_id=None, error_code=None, error_message=None, http_status_code=None, success=None,
                 delete_result=None):
        self.request_id = request_id    # type: str
        self.error_code = error_code    # type: str
        self.error_message = error_message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.success = success          # type: bool
        self.delete_result = delete_result  # type: bool

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.error_code, 'error_code')
        self.validate_required(self.error_message, 'error_message')
        self.validate_required(self.http_status_code, 'http_status_code')
        self.validate_required(self.success, 'success')
        self.validate_required(self.delete_result, 'delete_result')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['ErrorCode'] = self.error_code
        result['ErrorMessage'] = self.error_message
        result['HttpStatusCode'] = self.http_status_code
        result['Success'] = self.success
        result['DeleteResult'] = self.delete_result
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.error_code = map.get('ErrorCode')
        self.error_message = map.get('ErrorMessage')
        self.http_status_code = map.get('HttpStatusCode')
        self.success = map.get('Success')
        self.delete_result = map.get('DeleteResult')
        return self


class ListProgramTypeCountRequest(TeaModel):
    def __init__(self, project_id=None, project_env=None):
        self.project_id = project_id    # type: int
        self.project_env = project_env  # type: str

    def validate(self):
        self.validate_required(self.project_id, 'project_id')
        self.validate_required(self.project_env, 'project_env')

    def to_map(self):
        result = {}
        result['ProjectId'] = self.project_id
        result['ProjectEnv'] = self.project_env
        return result

    def from_map(self, map={}):
        self.project_id = map.get('ProjectId')
        self.project_env = map.get('ProjectEnv')
        return self


class ListProgramTypeCountResponse(TeaModel):
    def __init__(self, request_id=None, program_type_and_counts=None):
        self.request_id = request_id    # type: str
        self.program_type_and_counts = program_type_and_counts  # type: List[ListProgramTypeCountResponseProgramTypeAndCounts]

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.program_type_and_counts, 'program_type_and_counts')
        if self.program_type_and_counts:
            for k in self.program_type_and_counts:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['ProgramTypeAndCounts'] = []
        if self.program_type_and_counts is not None:
            for k in self.program_type_and_counts:
                result['ProgramTypeAndCounts'].append(k.to_map() if k else None)
        else:
            result['ProgramTypeAndCounts'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.program_type_and_counts = []
        if map.get('ProgramTypeAndCounts') is not None:
            for k in map.get('ProgramTypeAndCounts'):
                temp_model = ListProgramTypeCountResponseProgramTypeAndCounts()
                self.program_type_and_counts.append(temp_model.from_map(k))
        else:
            self.program_type_and_counts = None
        return self


class ListProgramTypeCountResponseProgramTypeAndCounts(TeaModel):
    def __init__(self, program_type=None, count=None):
        self.program_type = program_type  # type: str
        self.count = count              # type: int

    def validate(self):
        self.validate_required(self.program_type, 'program_type')
        self.validate_required(self.count, 'count')

    def to_map(self):
        result = {}
        result['ProgramType'] = self.program_type
        result['Count'] = self.count
        return result

    def from_map(self, map={}):
        self.program_type = map.get('ProgramType')
        self.count = map.get('Count')
        return self


class UpdateTableModelInfoRequest(TeaModel):
    def __init__(self, first_level_theme_id=None, second_level_theme_id=None, level_id=None, table_guid=None,
                 level_type=None):
        self.first_level_theme_id = first_level_theme_id  # type: int
        self.second_level_theme_id = second_level_theme_id  # type: int
        self.level_id = level_id        # type: int
        self.table_guid = table_guid    # type: str
        self.level_type = level_type    # type: int

    def validate(self):
        self.validate_required(self.table_guid, 'table_guid')

    def to_map(self):
        result = {}
        result['FirstLevelThemeId'] = self.first_level_theme_id
        result['SecondLevelThemeId'] = self.second_level_theme_id
        result['LevelId'] = self.level_id
        result['TableGuid'] = self.table_guid
        result['LevelType'] = self.level_type
        return result

    def from_map(self, map={}):
        self.first_level_theme_id = map.get('FirstLevelThemeId')
        self.second_level_theme_id = map.get('SecondLevelThemeId')
        self.level_id = map.get('LevelId')
        self.table_guid = map.get('TableGuid')
        self.level_type = map.get('LevelType')
        return self


class UpdateTableModelInfoResponse(TeaModel):
    def __init__(self, request_id=None, update_result=None):
        self.request_id = request_id    # type: str
        self.update_result = update_result  # type: bool

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.update_result, 'update_result')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['UpdateResult'] = self.update_result
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.update_result = map.get('UpdateResult')
        return self


class ListProjectsRequest(TeaModel):
    def __init__(self, page_number=None, page_size=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size      # type: int

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        return result

    def from_map(self, map={}):
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        return self


class ListProjectsResponse(TeaModel):
    def __init__(self, request_id=None, page_result=None):
        self.request_id = request_id    # type: str
        self.page_result = page_result  # type: ListProjectsResponsePageResult

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.page_result, 'page_result')
        if self.page_result:
            self.page_result.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        if self.page_result is not None:
            result['PageResult'] = self.page_result.to_map()
        else:
            result['PageResult'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('PageResult') is not None:
            temp_model = ListProjectsResponsePageResult()
            self.page_result = temp_model.from_map(map['PageResult'])
        else:
            self.page_result = None
        return self


class ListProjectsResponsePageResultProjectList(TeaModel):
    def __init__(self, project_name=None, project_identifier=None, project_description=None, project_status=None,
                 project_id=None, project_owner_base_id=None, project_status_code=None):
        self.project_name = project_name  # type: str
        self.project_identifier = project_identifier  # type: str
        self.project_description = project_description  # type: str
        self.project_status = project_status  # type: int
        self.project_id = project_id    # type: int
        self.project_owner_base_id = project_owner_base_id  # type: str
        self.project_status_code = project_status_code  # type: str

    def validate(self):
        self.validate_required(self.project_name, 'project_name')
        self.validate_required(self.project_identifier, 'project_identifier')
        self.validate_required(self.project_description, 'project_description')
        self.validate_required(self.project_status, 'project_status')
        self.validate_required(self.project_id, 'project_id')
        self.validate_required(self.project_owner_base_id, 'project_owner_base_id')
        self.validate_required(self.project_status_code, 'project_status_code')

    def to_map(self):
        result = {}
        result['ProjectName'] = self.project_name
        result['ProjectIdentifier'] = self.project_identifier
        result['ProjectDescription'] = self.project_description
        result['ProjectStatus'] = self.project_status
        result['ProjectId'] = self.project_id
        result['ProjectOwnerBaseId'] = self.project_owner_base_id
        result['ProjectStatusCode'] = self.project_status_code
        return result

    def from_map(self, map={}):
        self.project_name = map.get('ProjectName')
        self.project_identifier = map.get('ProjectIdentifier')
        self.project_description = map.get('ProjectDescription')
        self.project_status = map.get('ProjectStatus')
        self.project_id = map.get('ProjectId')
        self.project_owner_base_id = map.get('ProjectOwnerBaseId')
        self.project_status_code = map.get('ProjectStatusCode')
        return self


class ListProjectsResponsePageResult(TeaModel):
    def __init__(self, page_number=None, page_size=None, total_count=None, project_list=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size      # type: int
        self.total_count = total_count  # type: int
        self.project_list = project_list  # type: List[ListProjectsResponsePageResultProjectList]

    def validate(self):
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.project_list, 'project_list')
        if self.project_list:
            for k in self.project_list:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        result['TotalCount'] = self.total_count
        result['ProjectList'] = []
        if self.project_list is not None:
            for k in self.project_list:
                result['ProjectList'].append(k.to_map() if k else None)
        else:
            result['ProjectList'] = None
        return result

    def from_map(self, map={}):
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        self.total_count = map.get('TotalCount')
        self.project_list = []
        if map.get('ProjectList') is not None:
            for k in map.get('ProjectList'):
                temp_model = ListProjectsResponsePageResultProjectList()
                self.project_list.append(temp_model.from_map(k))
        else:
            self.project_list = None
        return self


class ListProjectMembersRequest(TeaModel):
    def __init__(self, project_id=None, page_number=None, page_size=None):
        self.project_id = project_id    # type: int
        self.page_number = page_number  # type: int
        self.page_size = page_size      # type: int

    def validate(self):
        self.validate_required(self.project_id, 'project_id')

    def to_map(self):
        result = {}
        result['ProjectId'] = self.project_id
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        return result

    def from_map(self, map={}):
        self.project_id = map.get('ProjectId')
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        return self


class ListProjectMembersResponse(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = request_id    # type: str
        self.data = data                # type: ListProjectMembersResponseData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('Data') is not None:
            temp_model = ListProjectMembersResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class ListProjectMembersResponseDataProjectMemberListProjectRoleList(TeaModel):
    def __init__(self, project_role_code=None, project_role_id=None, project_role_name=None,
                 project_role_type=None):
        self.project_role_code = project_role_code  # type: str
        self.project_role_id = project_role_id  # type: int
        self.project_role_name = project_role_name  # type: str
        self.project_role_type = project_role_type  # type: str

    def validate(self):
        self.validate_required(self.project_role_code, 'project_role_code')
        self.validate_required(self.project_role_id, 'project_role_id')
        self.validate_required(self.project_role_name, 'project_role_name')
        self.validate_required(self.project_role_type, 'project_role_type')

    def to_map(self):
        result = {}
        result['ProjectRoleCode'] = self.project_role_code
        result['ProjectRoleId'] = self.project_role_id
        result['ProjectRoleName'] = self.project_role_name
        result['ProjectRoleType'] = self.project_role_type
        return result

    def from_map(self, map={}):
        self.project_role_code = map.get('ProjectRoleCode')
        self.project_role_id = map.get('ProjectRoleId')
        self.project_role_name = map.get('ProjectRoleName')
        self.project_role_type = map.get('ProjectRoleType')
        return self


class ListProjectMembersResponseDataProjectMemberList(TeaModel):
    def __init__(self, nick=None, project_member_id=None, project_member_name=None, project_member_type=None,
                 status=None, project_role_list=None):
        self.nick = nick                # type: str
        self.project_member_id = project_member_id  # type: str
        self.project_member_name = project_member_name  # type: str
        self.project_member_type = project_member_type  # type: str
        self.status = status            # type: str
        self.project_role_list = project_role_list  # type: List[ListProjectMembersResponseDataProjectMemberListProjectRoleList]

    def validate(self):
        self.validate_required(self.nick, 'nick')
        self.validate_required(self.project_member_id, 'project_member_id')
        self.validate_required(self.project_member_name, 'project_member_name')
        self.validate_required(self.project_member_type, 'project_member_type')
        self.validate_required(self.status, 'status')
        self.validate_required(self.project_role_list, 'project_role_list')
        if self.project_role_list:
            for k in self.project_role_list:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['Nick'] = self.nick
        result['ProjectMemberId'] = self.project_member_id
        result['ProjectMemberName'] = self.project_member_name
        result['ProjectMemberType'] = self.project_member_type
        result['Status'] = self.status
        result['ProjectRoleList'] = []
        if self.project_role_list is not None:
            for k in self.project_role_list:
                result['ProjectRoleList'].append(k.to_map() if k else None)
        else:
            result['ProjectRoleList'] = None
        return result

    def from_map(self, map={}):
        self.nick = map.get('Nick')
        self.project_member_id = map.get('ProjectMemberId')
        self.project_member_name = map.get('ProjectMemberName')
        self.project_member_type = map.get('ProjectMemberType')
        self.status = map.get('Status')
        self.project_role_list = []
        if map.get('ProjectRoleList') is not None:
            for k in map.get('ProjectRoleList'):
                temp_model = ListProjectMembersResponseDataProjectMemberListProjectRoleList()
                self.project_role_list.append(temp_model.from_map(k))
        else:
            self.project_role_list = None
        return self


class ListProjectMembersResponseData(TeaModel):
    def __init__(self, page_number=None, page_size=None, total_count=None, project_member_list=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size      # type: int
        self.total_count = total_count  # type: int
        self.project_member_list = project_member_list  # type: List[ListProjectMembersResponseDataProjectMemberList]

    def validate(self):
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.project_member_list, 'project_member_list')
        if self.project_member_list:
            for k in self.project_member_list:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        result['TotalCount'] = self.total_count
        result['ProjectMemberList'] = []
        if self.project_member_list is not None:
            for k in self.project_member_list:
                result['ProjectMemberList'].append(k.to_map() if k else None)
        else:
            result['ProjectMemberList'] = None
        return result

    def from_map(self, map={}):
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        self.total_count = map.get('TotalCount')
        self.project_member_list = []
        if map.get('ProjectMemberList') is not None:
            for k in map.get('ProjectMemberList'):
                temp_model = ListProjectMembersResponseDataProjectMemberList()
                self.project_member_list.append(temp_model.from_map(k))
        else:
            self.project_member_list = None
        return self


class CreateProjectMemberRequest(TeaModel):
    def __init__(self, project_id=None, user_id=None, client_token=None, role_code=None):
        self.project_id = project_id    # type: int
        self.user_id = user_id          # type: str
        self.client_token = client_token  # type: str
        self.role_code = role_code      # type: str

    def validate(self):
        self.validate_required(self.project_id, 'project_id')
        self.validate_required(self.user_id, 'user_id')

    def to_map(self):
        result = {}
        result['ProjectId'] = self.project_id
        result['UserId'] = self.user_id
        result['ClientToken'] = self.client_token
        result['RoleCode'] = self.role_code
        return result

    def from_map(self, map={}):
        self.project_id = map.get('ProjectId')
        self.user_id = map.get('UserId')
        self.client_token = map.get('ClientToken')
        self.role_code = map.get('RoleCode')
        return self


class CreateProjectMemberResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class ListProjectRolesRequest(TeaModel):
    def __init__(self, project_id=None):
        self.project_id = project_id    # type: int

    def validate(self):
        self.validate_required(self.project_id, 'project_id')

    def to_map(self):
        result = {}
        result['ProjectId'] = self.project_id
        return result

    def from_map(self, map={}):
        self.project_id = map.get('ProjectId')
        return self


class ListProjectRolesResponse(TeaModel):
    def __init__(self, request_id=None, project_role_list=None):
        self.request_id = request_id    # type: str
        self.project_role_list = project_role_list  # type: List[ListProjectRolesResponseProjectRoleList]

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.project_role_list, 'project_role_list')
        if self.project_role_list:
            for k in self.project_role_list:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['ProjectRoleList'] = []
        if self.project_role_list is not None:
            for k in self.project_role_list:
                result['ProjectRoleList'].append(k.to_map() if k else None)
        else:
            result['ProjectRoleList'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.project_role_list = []
        if map.get('ProjectRoleList') is not None:
            for k in map.get('ProjectRoleList'):
                temp_model = ListProjectRolesResponseProjectRoleList()
                self.project_role_list.append(temp_model.from_map(k))
        else:
            self.project_role_list = None
        return self


class ListProjectRolesResponseProjectRoleList(TeaModel):
    def __init__(self, project_role_code=None, project_role_id=None, project_role_name=None,
                 project_role_type=None):
        self.project_role_code = project_role_code  # type: str
        self.project_role_id = project_role_id  # type: int
        self.project_role_name = project_role_name  # type: str
        self.project_role_type = project_role_type  # type: str

    def validate(self):
        self.validate_required(self.project_role_code, 'project_role_code')
        self.validate_required(self.project_role_id, 'project_role_id')
        self.validate_required(self.project_role_name, 'project_role_name')
        self.validate_required(self.project_role_type, 'project_role_type')

    def to_map(self):
        result = {}
        result['ProjectRoleCode'] = self.project_role_code
        result['ProjectRoleId'] = self.project_role_id
        result['ProjectRoleName'] = self.project_role_name
        result['ProjectRoleType'] = self.project_role_type
        return result

    def from_map(self, map={}):
        self.project_role_code = map.get('ProjectRoleCode')
        self.project_role_id = map.get('ProjectRoleId')
        self.project_role_name = map.get('ProjectRoleName')
        self.project_role_type = map.get('ProjectRoleType')
        return self


class AddProjectMemberToRoleRequest(TeaModel):
    def __init__(self, project_id=None, user_id=None, role_code=None, client_token=None):
        self.project_id = project_id    # type: int
        self.user_id = user_id          # type: str
        self.role_code = role_code      # type: str
        self.client_token = client_token  # type: str

    def validate(self):
        self.validate_required(self.project_id, 'project_id')
        self.validate_required(self.user_id, 'user_id')
        self.validate_required(self.role_code, 'role_code')

    def to_map(self):
        result = {}
        result['ProjectId'] = self.project_id
        result['UserId'] = self.user_id
        result['RoleCode'] = self.role_code
        result['ClientToken'] = self.client_token
        return result

    def from_map(self, map={}):
        self.project_id = map.get('ProjectId')
        self.user_id = map.get('UserId')
        self.role_code = map.get('RoleCode')
        self.client_token = map.get('ClientToken')
        return self


class AddProjectMemberToRoleResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class RemoveProjectMemberFromRoleRequest(TeaModel):
    def __init__(self, project_id=None, user_id=None, role_code=None):
        self.project_id = project_id    # type: int
        self.user_id = user_id          # type: str
        self.role_code = role_code      # type: str

    def validate(self):
        self.validate_required(self.project_id, 'project_id')
        self.validate_required(self.user_id, 'user_id')
        self.validate_required(self.role_code, 'role_code')

    def to_map(self):
        result = {}
        result['ProjectId'] = self.project_id
        result['UserId'] = self.user_id
        result['RoleCode'] = self.role_code
        return result

    def from_map(self, map={}):
        self.project_id = map.get('ProjectId')
        self.user_id = map.get('UserId')
        self.role_code = map.get('RoleCode')
        return self


class RemoveProjectMemberFromRoleResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class DeleteProjectMemberRequest(TeaModel):
    def __init__(self, project_id=None, user_id=None):
        self.project_id = project_id    # type: int
        self.user_id = user_id          # type: str

    def validate(self):
        self.validate_required(self.project_id, 'project_id')
        self.validate_required(self.user_id, 'user_id')

    def to_map(self):
        result = {}
        result['ProjectId'] = self.project_id
        result['UserId'] = self.user_id
        return result

    def from_map(self, map={}):
        self.project_id = map.get('ProjectId')
        self.user_id = map.get('UserId')
        return self


class DeleteProjectMemberResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class CreateDagComplementRequest(TeaModel):
    def __init__(self, project_env=None, start_biz_date=None, name=None, root_node_id=None, include_node_ids=None,
                 exclude_node_ids=None, biz_begin_time=None, biz_end_time=None, parallelism=None, end_biz_date=None,
                 node_params=None):
        self.project_env = project_env  # type: str
        self.start_biz_date = start_biz_date  # type: str
        self.name = name                # type: str
        self.root_node_id = root_node_id  # type: int
        self.include_node_ids = include_node_ids  # type: str
        self.exclude_node_ids = exclude_node_ids  # type: str
        self.biz_begin_time = biz_begin_time  # type: str
        self.biz_end_time = biz_end_time  # type: str
        self.parallelism = parallelism  # type: bool
        self.end_biz_date = end_biz_date  # type: str
        self.node_params = node_params  # type: str

    def validate(self):
        self.validate_required(self.project_env, 'project_env')
        self.validate_required(self.start_biz_date, 'start_biz_date')
        self.validate_required(self.name, 'name')
        self.validate_required(self.root_node_id, 'root_node_id')
        self.validate_required(self.include_node_ids, 'include_node_ids')
        self.validate_required(self.parallelism, 'parallelism')
        self.validate_required(self.end_biz_date, 'end_biz_date')

    def to_map(self):
        result = {}
        result['ProjectEnv'] = self.project_env
        result['StartBizDate'] = self.start_biz_date
        result['Name'] = self.name
        result['RootNodeId'] = self.root_node_id
        result['IncludeNodeIds'] = self.include_node_ids
        result['ExcludeNodeIds'] = self.exclude_node_ids
        result['BizBeginTime'] = self.biz_begin_time
        result['BizEndTime'] = self.biz_end_time
        result['Parallelism'] = self.parallelism
        result['EndBizDate'] = self.end_biz_date
        result['NodeParams'] = self.node_params
        return result

    def from_map(self, map={}):
        self.project_env = map.get('ProjectEnv')
        self.start_biz_date = map.get('StartBizDate')
        self.name = map.get('Name')
        self.root_node_id = map.get('RootNodeId')
        self.include_node_ids = map.get('IncludeNodeIds')
        self.exclude_node_ids = map.get('ExcludeNodeIds')
        self.biz_begin_time = map.get('BizBeginTime')
        self.biz_end_time = map.get('BizEndTime')
        self.parallelism = map.get('Parallelism')
        self.end_biz_date = map.get('EndBizDate')
        self.node_params = map.get('NodeParams')
        return self


class CreateDagComplementResponse(TeaModel):
    def __init__(self, error_code=None, error_message=None, http_status_code=None, request_id=None, success=None,
                 data=None):
        self.error_code = error_code    # type: str
        self.error_message = error_message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.request_id = request_id    # type: str
        self.success = success          # type: bool
        self.data = data                # type: List[int]

    def validate(self):
        self.validate_required(self.error_code, 'error_code')
        self.validate_required(self.error_message, 'error_message')
        self.validate_required(self.http_status_code, 'http_status_code')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.success, 'success')
        self.validate_required(self.data, 'data')

    def to_map(self):
        result = {}
        result['ErrorCode'] = self.error_code
        result['ErrorMessage'] = self.error_message
        result['HttpStatusCode'] = self.http_status_code
        result['RequestId'] = self.request_id
        result['Success'] = self.success
        result['Data'] = self.data
        return result

    def from_map(self, map={}):
        self.error_code = map.get('ErrorCode')
        self.error_message = map.get('ErrorMessage')
        self.http_status_code = map.get('HttpStatusCode')
        self.request_id = map.get('RequestId')
        self.success = map.get('Success')
        self.data = map.get('Data')
        return self


class CreateDagTestRequest(TeaModel):
    def __init__(self, project_env=None, bizdate=None, name=None, node_id=None, node_params=None):
        self.project_env = project_env  # type: str
        self.bizdate = bizdate          # type: str
        self.name = name                # type: str
        self.node_id = node_id          # type: int
        self.node_params = node_params  # type: str

    def validate(self):
        self.validate_required(self.project_env, 'project_env')
        self.validate_required(self.bizdate, 'bizdate')
        self.validate_required(self.name, 'name')
        self.validate_required(self.node_id, 'node_id')

    def to_map(self):
        result = {}
        result['ProjectEnv'] = self.project_env
        result['Bizdate'] = self.bizdate
        result['Name'] = self.name
        result['NodeId'] = self.node_id
        result['NodeParams'] = self.node_params
        return result

    def from_map(self, map={}):
        self.project_env = map.get('ProjectEnv')
        self.bizdate = map.get('Bizdate')
        self.name = map.get('Name')
        self.node_id = map.get('NodeId')
        self.node_params = map.get('NodeParams')
        return self


class CreateDagTestResponse(TeaModel):
    def __init__(self, error_code=None, error_message=None, http_status_code=None, request_id=None, success=None,
                 data=None):
        self.error_code = error_code    # type: str
        self.error_message = error_message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.request_id = request_id    # type: str
        self.success = success          # type: bool
        self.data = data                # type: int

    def validate(self):
        self.validate_required(self.error_code, 'error_code')
        self.validate_required(self.error_message, 'error_message')
        self.validate_required(self.http_status_code, 'http_status_code')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.success, 'success')
        self.validate_required(self.data, 'data')

    def to_map(self):
        result = {}
        result['ErrorCode'] = self.error_code
        result['ErrorMessage'] = self.error_message
        result['HttpStatusCode'] = self.http_status_code
        result['RequestId'] = self.request_id
        result['Success'] = self.success
        result['Data'] = self.data
        return result

    def from_map(self, map={}):
        self.error_code = map.get('ErrorCode')
        self.error_message = map.get('ErrorMessage')
        self.http_status_code = map.get('HttpStatusCode')
        self.request_id = map.get('RequestId')
        self.success = map.get('Success')
        self.data = map.get('Data')
        return self


class ListCalcEnginesRequest(TeaModel):
    def __init__(self, project_id=None, name=None, calc_engine_type=None, env_type=None, page_size=None,
                 page_number=None):
        self.project_id = project_id    # type: int
        self.name = name                # type: str
        self.calc_engine_type = calc_engine_type  # type: str
        self.env_type = env_type        # type: str
        self.page_size = page_size      # type: int
        self.page_number = page_number  # type: int

    def validate(self):
        self.validate_required(self.project_id, 'project_id')
        self.validate_required(self.calc_engine_type, 'calc_engine_type')

    def to_map(self):
        result = {}
        result['ProjectId'] = self.project_id
        result['Name'] = self.name
        result['CalcEngineType'] = self.calc_engine_type
        result['EnvType'] = self.env_type
        result['PageSize'] = self.page_size
        result['PageNumber'] = self.page_number
        return result

    def from_map(self, map={}):
        self.project_id = map.get('ProjectId')
        self.name = map.get('Name')
        self.calc_engine_type = map.get('CalcEngineType')
        self.env_type = map.get('EnvType')
        self.page_size = map.get('PageSize')
        self.page_number = map.get('PageNumber')
        return self


class ListCalcEnginesResponse(TeaModel):
    def __init__(self, http_status_code=None, success=None, request_id=None, data=None):
        self.http_status_code = http_status_code  # type: int
        self.success = success          # type: bool
        self.request_id = request_id    # type: str
        self.data = data                # type: ListCalcEnginesResponseData

    def validate(self):
        self.validate_required(self.http_status_code, 'http_status_code')
        self.validate_required(self.success, 'success')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['HttpStatusCode'] = self.http_status_code
        result['Success'] = self.success
        result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.http_status_code = map.get('HttpStatusCode')
        self.success = map.get('Success')
        self.request_id = map.get('RequestId')
        if map.get('Data') is not None:
            temp_model = ListCalcEnginesResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class ListCalcEnginesResponseDataCalcEngines(TeaModel):
    def __init__(self, calc_engine_type=None, gmt_create=None, dw_region=None, is_default=None,
                 binding_project_id=None, env_type=None, tenant_id=None, name=None, binding_project_name=None, region=None,
                 engine_id=None, engine_info=None, task_auth_type=None):
        self.calc_engine_type = calc_engine_type  # type: str
        self.gmt_create = gmt_create    # type: str
        self.dw_region = dw_region      # type: str
        self.is_default = is_default    # type: bool
        self.binding_project_id = binding_project_id  # type: int
        self.env_type = env_type        # type: str
        self.tenant_id = tenant_id      # type: int
        self.name = name                # type: str
        self.binding_project_name = binding_project_name  # type: str
        self.region = region            # type: str
        self.engine_id = engine_id      # type: int
        self.engine_info = engine_info  # type: Dict[str, Any]
        self.task_auth_type = task_auth_type  # type: str

    def validate(self):
        self.validate_required(self.calc_engine_type, 'calc_engine_type')
        self.validate_required(self.gmt_create, 'gmt_create')
        self.validate_required(self.dw_region, 'dw_region')
        self.validate_required(self.is_default, 'is_default')
        self.validate_required(self.binding_project_id, 'binding_project_id')
        self.validate_required(self.env_type, 'env_type')
        self.validate_required(self.tenant_id, 'tenant_id')
        self.validate_required(self.name, 'name')
        self.validate_required(self.binding_project_name, 'binding_project_name')
        self.validate_required(self.region, 'region')
        self.validate_required(self.engine_id, 'engine_id')
        self.validate_required(self.engine_info, 'engine_info')
        self.validate_required(self.task_auth_type, 'task_auth_type')

    def to_map(self):
        result = {}
        result['CalcEngineType'] = self.calc_engine_type
        result['GmtCreate'] = self.gmt_create
        result['DwRegion'] = self.dw_region
        result['IsDefault'] = self.is_default
        result['BindingProjectId'] = self.binding_project_id
        result['EnvType'] = self.env_type
        result['TenantId'] = self.tenant_id
        result['Name'] = self.name
        result['BindingProjectName'] = self.binding_project_name
        result['Region'] = self.region
        result['EngineId'] = self.engine_id
        result['EngineInfo'] = self.engine_info
        result['TaskAuthType'] = self.task_auth_type
        return result

    def from_map(self, map={}):
        self.calc_engine_type = map.get('CalcEngineType')
        self.gmt_create = map.get('GmtCreate')
        self.dw_region = map.get('DwRegion')
        self.is_default = map.get('IsDefault')
        self.binding_project_id = map.get('BindingProjectId')
        self.env_type = map.get('EnvType')
        self.tenant_id = map.get('TenantId')
        self.name = map.get('Name')
        self.binding_project_name = map.get('BindingProjectName')
        self.region = map.get('Region')
        self.engine_id = map.get('EngineId')
        self.engine_info = map.get('EngineInfo')
        self.task_auth_type = map.get('TaskAuthType')
        return self


class ListCalcEnginesResponseData(TeaModel):
    def __init__(self, page_number=None, page_size=None, total_count=None, calc_engines=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size      # type: int
        self.total_count = total_count  # type: int
        self.calc_engines = calc_engines  # type: List[ListCalcEnginesResponseDataCalcEngines]

    def validate(self):
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.calc_engines, 'calc_engines')
        if self.calc_engines:
            for k in self.calc_engines:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        result['TotalCount'] = self.total_count
        result['CalcEngines'] = []
        if self.calc_engines is not None:
            for k in self.calc_engines:
                result['CalcEngines'].append(k.to_map() if k else None)
        else:
            result['CalcEngines'] = None
        return result

    def from_map(self, map={}):
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        self.total_count = map.get('TotalCount')
        self.calc_engines = []
        if map.get('CalcEngines') is not None:
            for k in map.get('CalcEngines'):
                temp_model = ListCalcEnginesResponseDataCalcEngines()
                self.calc_engines.append(temp_model.from_map(k))
        else:
            self.calc_engines = None
        return self


class ListConnectionsRequest(TeaModel):
    def __init__(self, project_id=None, name=None, connection_type=None, sub_type=None, status=None, env_type=None,
                 page_size=None, page_number=None):
        self.project_id = project_id    # type: int
        self.name = name                # type: str
        self.connection_type = connection_type  # type: str
        self.sub_type = sub_type        # type: str
        self.status = status            # type: str
        self.env_type = env_type        # type: int
        self.page_size = page_size      # type: int
        self.page_number = page_number  # type: int

    def validate(self):
        self.validate_required(self.project_id, 'project_id')

    def to_map(self):
        result = {}
        result['ProjectId'] = self.project_id
        result['Name'] = self.name
        result['ConnectionType'] = self.connection_type
        result['SubType'] = self.sub_type
        result['Status'] = self.status
        result['EnvType'] = self.env_type
        result['PageSize'] = self.page_size
        result['PageNumber'] = self.page_number
        return result

    def from_map(self, map={}):
        self.project_id = map.get('ProjectId')
        self.name = map.get('Name')
        self.connection_type = map.get('ConnectionType')
        self.sub_type = map.get('SubType')
        self.status = map.get('Status')
        self.env_type = map.get('EnvType')
        self.page_size = map.get('PageSize')
        self.page_number = map.get('PageNumber')
        return self


class ListConnectionsResponse(TeaModel):
    def __init__(self, http_status_code=None, success=None, request_id=None, data=None):
        self.http_status_code = http_status_code  # type: int
        self.success = success          # type: bool
        self.request_id = request_id    # type: str
        self.data = data                # type: ListConnectionsResponseData

    def validate(self):
        self.validate_required(self.http_status_code, 'http_status_code')
        self.validate_required(self.success, 'success')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['HttpStatusCode'] = self.http_status_code
        result['Success'] = self.success
        result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.http_status_code = map.get('HttpStatusCode')
        self.success = map.get('Success')
        self.request_id = map.get('RequestId')
        if map.get('Data') is not None:
            temp_model = ListConnectionsResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class ListConnectionsResponseDataConnections(TeaModel):
    def __init__(self, shared=None, gmt_modified=None, connect_status=None, binding_calc_engine_id=None,
                 description=None, connection_type=None, gmt_create=None, default_engine=None, operator=None, sequence=None,
                 env_type=None, tenant_id=None, name=None, sub_type=None, id=None, project_id=None, status=None, content=None):
        self.shared = shared            # type: bool
        self.gmt_modified = gmt_modified  # type: str
        self.connect_status = connect_status  # type: int
        self.binding_calc_engine_id = binding_calc_engine_id  # type: int
        self.description = description  # type: str
        self.connection_type = connection_type  # type: str
        self.gmt_create = gmt_create    # type: str
        self.default_engine = default_engine  # type: bool
        self.operator = operator        # type: str
        self.sequence = sequence        # type: int
        self.env_type = env_type        # type: int
        self.tenant_id = tenant_id      # type: int
        self.name = name                # type: str
        self.sub_type = sub_type        # type: str
        self.id = id                    # type: int
        self.project_id = project_id    # type: int
        self.status = status            # type: int
        self.content = content          # type: str

    def validate(self):
        self.validate_required(self.shared, 'shared')
        self.validate_required(self.gmt_modified, 'gmt_modified')
        self.validate_required(self.connect_status, 'connect_status')
        self.validate_required(self.binding_calc_engine_id, 'binding_calc_engine_id')
        self.validate_required(self.description, 'description')
        self.validate_required(self.connection_type, 'connection_type')
        self.validate_required(self.gmt_create, 'gmt_create')
        self.validate_required(self.default_engine, 'default_engine')
        self.validate_required(self.operator, 'operator')
        self.validate_required(self.sequence, 'sequence')
        self.validate_required(self.env_type, 'env_type')
        self.validate_required(self.tenant_id, 'tenant_id')
        self.validate_required(self.name, 'name')
        self.validate_required(self.sub_type, 'sub_type')
        self.validate_required(self.id, 'id')
        self.validate_required(self.project_id, 'project_id')
        self.validate_required(self.status, 'status')
        self.validate_required(self.content, 'content')

    def to_map(self):
        result = {}
        result['Shared'] = self.shared
        result['GmtModified'] = self.gmt_modified
        result['ConnectStatus'] = self.connect_status
        result['BindingCalcEngineId'] = self.binding_calc_engine_id
        result['Description'] = self.description
        result['ConnectionType'] = self.connection_type
        result['GmtCreate'] = self.gmt_create
        result['DefaultEngine'] = self.default_engine
        result['Operator'] = self.operator
        result['Sequence'] = self.sequence
        result['EnvType'] = self.env_type
        result['TenantId'] = self.tenant_id
        result['Name'] = self.name
        result['SubType'] = self.sub_type
        result['Id'] = self.id
        result['ProjectId'] = self.project_id
        result['Status'] = self.status
        result['Content'] = self.content
        return result

    def from_map(self, map={}):
        self.shared = map.get('Shared')
        self.gmt_modified = map.get('GmtModified')
        self.connect_status = map.get('ConnectStatus')
        self.binding_calc_engine_id = map.get('BindingCalcEngineId')
        self.description = map.get('Description')
        self.connection_type = map.get('ConnectionType')
        self.gmt_create = map.get('GmtCreate')
        self.default_engine = map.get('DefaultEngine')
        self.operator = map.get('Operator')
        self.sequence = map.get('Sequence')
        self.env_type = map.get('EnvType')
        self.tenant_id = map.get('TenantId')
        self.name = map.get('Name')
        self.sub_type = map.get('SubType')
        self.id = map.get('Id')
        self.project_id = map.get('ProjectId')
        self.status = map.get('Status')
        self.content = map.get('Content')
        return self


class ListConnectionsResponseData(TeaModel):
    def __init__(self, page_number=None, page_size=None, total_count=None, connections=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size      # type: int
        self.total_count = total_count  # type: int
        self.connections = connections  # type: List[ListConnectionsResponseDataConnections]

    def validate(self):
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.connections, 'connections')
        if self.connections:
            for k in self.connections:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        result['TotalCount'] = self.total_count
        result['Connections'] = []
        if self.connections is not None:
            for k in self.connections:
                result['Connections'].append(k.to_map() if k else None)
        else:
            result['Connections'] = None
        return result

    def from_map(self, map={}):
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        self.total_count = map.get('TotalCount')
        self.connections = []
        if map.get('Connections') is not None:
            for k in map.get('Connections'):
                temp_model = ListConnectionsResponseDataConnections()
                self.connections.append(temp_model.from_map(k))
        else:
            self.connections = None
        return self


class UpdateConnectionRequest(TeaModel):
    def __init__(self, description=None, env_type=None, content=None, status=None, connection_id=None):
        self.description = description  # type: str
        self.env_type = env_type        # type: int
        self.content = content          # type: str
        self.status = status            # type: str
        self.connection_id = connection_id  # type: int

    def validate(self):
        self.validate_required(self.connection_id, 'connection_id')

    def to_map(self):
        result = {}
        result['Description'] = self.description
        result['EnvType'] = self.env_type
        result['Content'] = self.content
        result['Status'] = self.status
        result['ConnectionId'] = self.connection_id
        return result

    def from_map(self, map={}):
        self.description = map.get('Description')
        self.env_type = map.get('EnvType')
        self.content = map.get('Content')
        self.status = map.get('Status')
        self.connection_id = map.get('ConnectionId')
        return self


class UpdateConnectionResponse(TeaModel):
    def __init__(self, success=None, http_status_code=None, data=None, request_id=None):
        self.success = success          # type: bool
        self.http_status_code = http_status_code  # type: str
        self.data = data                # type: bool
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.success, 'success')
        self.validate_required(self.http_status_code, 'http_status_code')
        self.validate_required(self.data, 'data')
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['Success'] = self.success
        result['HttpStatusCode'] = self.http_status_code
        result['Data'] = self.data
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.success = map.get('Success')
        self.http_status_code = map.get('HttpStatusCode')
        self.data = map.get('Data')
        self.request_id = map.get('RequestId')
        return self


class DeleteConnectionRequest(TeaModel):
    def __init__(self, connection_id=None):
        self.connection_id = connection_id  # type: int

    def validate(self):
        self.validate_required(self.connection_id, 'connection_id')

    def to_map(self):
        result = {}
        result['ConnectionId'] = self.connection_id
        return result

    def from_map(self, map={}):
        self.connection_id = map.get('ConnectionId')
        return self


class DeleteConnectionResponse(TeaModel):
    def __init__(self, success=None, http_status_code=None, data=None, request_id=None):
        self.success = success          # type: bool
        self.http_status_code = http_status_code  # type: str
        self.data = data                # type: bool
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.success, 'success')
        self.validate_required(self.http_status_code, 'http_status_code')
        self.validate_required(self.data, 'data')
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['Success'] = self.success
        result['HttpStatusCode'] = self.http_status_code
        result['Data'] = self.data
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.success = map.get('Success')
        self.http_status_code = map.get('HttpStatusCode')
        self.data = map.get('Data')
        self.request_id = map.get('RequestId')
        return self


class GetProjectDetailRequest(TeaModel):
    def __init__(self, project_id=None):
        self.project_id = project_id    # type: int

    def validate(self):
        self.validate_required(self.project_id, 'project_id')

    def to_map(self):
        result = {}
        result['ProjectId'] = self.project_id
        return result

    def from_map(self, map={}):
        self.project_id = map.get('ProjectId')
        return self


class GetProjectDetailResponse(TeaModel):
    def __init__(self, http_status_code=None, success=None, request_id=None, data=None):
        self.http_status_code = http_status_code  # type: int
        self.success = success          # type: bool
        self.request_id = request_id    # type: str
        self.data = data                # type: GetProjectDetailResponseData

    def validate(self):
        self.validate_required(self.http_status_code, 'http_status_code')
        self.validate_required(self.success, 'success')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['HttpStatusCode'] = self.http_status_code
        result['Success'] = self.success
        result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.http_status_code = map.get('HttpStatusCode')
        self.success = map.get('Success')
        self.request_id = map.get('RequestId')
        if map.get('Data') is not None:
            temp_model = GetProjectDetailResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class GetProjectDetailResponseData(TeaModel):
    def __init__(self, gmt_modified=None, default_di_resource_group_identifier=None, is_allow_download=None,
                 scheduler_retry_interval=None, resident_area=None, project_owner_base_id=None, project_mode=None, gmt_create=None,
                 protected_mode=None, tenant_id=None, project_description=None, scheduler_max_retry_times=None, project_name=None,
                 project_identifier=None, project_id=None, status=None, development_type=None, env_types=None):
        self.gmt_modified = gmt_modified  # type: str
        self.default_di_resource_group_identifier = default_di_resource_group_identifier  # type: str
        self.is_allow_download = is_allow_download  # type: int
        self.scheduler_retry_interval = scheduler_retry_interval  # type: int
        self.resident_area = resident_area  # type: str
        self.project_owner_base_id = project_owner_base_id  # type: str
        self.project_mode = project_mode  # type: int
        self.gmt_create = gmt_create    # type: str
        self.protected_mode = protected_mode  # type: int
        self.tenant_id = tenant_id      # type: int
        self.project_description = project_description  # type: str
        self.scheduler_max_retry_times = scheduler_max_retry_times  # type: int
        self.project_name = project_name  # type: str
        self.project_identifier = project_identifier  # type: str
        self.project_id = project_id    # type: int
        self.status = status            # type: int
        self.development_type = development_type  # type: int
        self.env_types = env_types      # type: List[str]

    def validate(self):
        self.validate_required(self.gmt_modified, 'gmt_modified')
        self.validate_required(self.default_di_resource_group_identifier, 'default_di_resource_group_identifier')
        self.validate_required(self.is_allow_download, 'is_allow_download')
        self.validate_required(self.scheduler_retry_interval, 'scheduler_retry_interval')
        self.validate_required(self.resident_area, 'resident_area')
        self.validate_required(self.project_owner_base_id, 'project_owner_base_id')
        self.validate_required(self.project_mode, 'project_mode')
        self.validate_required(self.gmt_create, 'gmt_create')
        self.validate_required(self.protected_mode, 'protected_mode')
        self.validate_required(self.tenant_id, 'tenant_id')
        self.validate_required(self.project_description, 'project_description')
        self.validate_required(self.scheduler_max_retry_times, 'scheduler_max_retry_times')
        self.validate_required(self.project_name, 'project_name')
        self.validate_required(self.project_identifier, 'project_identifier')
        self.validate_required(self.project_id, 'project_id')
        self.validate_required(self.status, 'status')
        self.validate_required(self.development_type, 'development_type')
        self.validate_required(self.env_types, 'env_types')

    def to_map(self):
        result = {}
        result['GmtModified'] = self.gmt_modified
        result['DefaultDiResourceGroupIdentifier'] = self.default_di_resource_group_identifier
        result['IsAllowDownload'] = self.is_allow_download
        result['SchedulerRetryInterval'] = self.scheduler_retry_interval
        result['ResidentArea'] = self.resident_area
        result['ProjectOwnerBaseId'] = self.project_owner_base_id
        result['ProjectMode'] = self.project_mode
        result['GmtCreate'] = self.gmt_create
        result['ProtectedMode'] = self.protected_mode
        result['TenantId'] = self.tenant_id
        result['ProjectDescription'] = self.project_description
        result['SchedulerMaxRetryTimes'] = self.scheduler_max_retry_times
        result['ProjectName'] = self.project_name
        result['ProjectIdentifier'] = self.project_identifier
        result['ProjectId'] = self.project_id
        result['Status'] = self.status
        result['DevelopmentType'] = self.development_type
        result['EnvTypes'] = self.env_types
        return result

    def from_map(self, map={}):
        self.gmt_modified = map.get('GmtModified')
        self.default_di_resource_group_identifier = map.get('DefaultDiResourceGroupIdentifier')
        self.is_allow_download = map.get('IsAllowDownload')
        self.scheduler_retry_interval = map.get('SchedulerRetryInterval')
        self.resident_area = map.get('ResidentArea')
        self.project_owner_base_id = map.get('ProjectOwnerBaseId')
        self.project_mode = map.get('ProjectMode')
        self.gmt_create = map.get('GmtCreate')
        self.protected_mode = map.get('ProtectedMode')
        self.tenant_id = map.get('TenantId')
        self.project_description = map.get('ProjectDescription')
        self.scheduler_max_retry_times = map.get('SchedulerMaxRetryTimes')
        self.project_name = map.get('ProjectName')
        self.project_identifier = map.get('ProjectIdentifier')
        self.project_id = map.get('ProjectId')
        self.status = map.get('Status')
        self.development_type = map.get('DevelopmentType')
        self.env_types = map.get('EnvTypes')
        return self


class ListResourceGroupsRequest(TeaModel):
    def __init__(self, resource_group_type=None, keyword=None):
        self.resource_group_type = resource_group_type  # type: int
        self.keyword = keyword          # type: str

    def validate(self):
        self.validate_required(self.resource_group_type, 'resource_group_type')

    def to_map(self):
        result = {}
        result['ResourceGroupType'] = self.resource_group_type
        result['Keyword'] = self.keyword
        return result

    def from_map(self, map={}):
        self.resource_group_type = map.get('ResourceGroupType')
        self.keyword = map.get('Keyword')
        return self


class ListResourceGroupsResponse(TeaModel):
    def __init__(self, http_status_code=None, success=None, request_id=None, data=None):
        self.http_status_code = http_status_code  # type: int
        self.success = success          # type: bool
        self.request_id = request_id    # type: str
        self.data = data                # type: List[ListResourceGroupsResponseData]

    def validate(self):
        self.validate_required(self.http_status_code, 'http_status_code')
        self.validate_required(self.success, 'success')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['HttpStatusCode'] = self.http_status_code
        result['Success'] = self.success
        result['RequestId'] = self.request_id
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.http_status_code = map.get('HttpStatusCode')
        self.success = map.get('Success')
        self.request_id = map.get('RequestId')
        self.data = []
        if map.get('Data') is not None:
            for k in map.get('Data'):
                temp_model = ListResourceGroupsResponseData()
                self.data.append(temp_model.from_map(k))
        else:
            self.data = None
        return self


class ListResourceGroupsResponseData(TeaModel):
    def __init__(self, identifier=None, cluster=None, biz_ext_key=None, enable_kp=None, update_time=None,
                 resource_group_type=None, mode=None, sequence=None, is_default=None, create_time=None, name=None, tenant_id=None,
                 id=None, status=None, specs=None):
        self.identifier = identifier    # type: str
        self.cluster = cluster          # type: str
        self.biz_ext_key = biz_ext_key  # type: str
        self.enable_kp = enable_kp      # type: bool
        self.update_time = update_time  # type: str
        self.resource_group_type = resource_group_type  # type: str
        self.mode = mode                # type: str
        self.sequence = sequence        # type: int
        self.is_default = is_default    # type: bool
        self.create_time = create_time  # type: str
        self.name = name                # type: str
        self.tenant_id = tenant_id      # type: int
        self.id = id                    # type: int
        self.status = status            # type: int
        self.specs = specs              # type: Dict[str, Any]

    def validate(self):
        self.validate_required(self.identifier, 'identifier')
        self.validate_required(self.cluster, 'cluster')
        self.validate_required(self.biz_ext_key, 'biz_ext_key')
        self.validate_required(self.enable_kp, 'enable_kp')
        self.validate_required(self.update_time, 'update_time')
        self.validate_required(self.resource_group_type, 'resource_group_type')
        self.validate_required(self.mode, 'mode')
        self.validate_required(self.sequence, 'sequence')
        self.validate_required(self.is_default, 'is_default')
        self.validate_required(self.create_time, 'create_time')
        self.validate_required(self.name, 'name')
        self.validate_required(self.tenant_id, 'tenant_id')
        self.validate_required(self.id, 'id')
        self.validate_required(self.status, 'status')
        self.validate_required(self.specs, 'specs')

    def to_map(self):
        result = {}
        result['Identifier'] = self.identifier
        result['Cluster'] = self.cluster
        result['BizExtKey'] = self.biz_ext_key
        result['EnableKp'] = self.enable_kp
        result['UpdateTime'] = self.update_time
        result['ResourceGroupType'] = self.resource_group_type
        result['Mode'] = self.mode
        result['Sequence'] = self.sequence
        result['IsDefault'] = self.is_default
        result['CreateTime'] = self.create_time
        result['Name'] = self.name
        result['TenantId'] = self.tenant_id
        result['Id'] = self.id
        result['Status'] = self.status
        result['Specs'] = self.specs
        return result

    def from_map(self, map={}):
        self.identifier = map.get('Identifier')
        self.cluster = map.get('Cluster')
        self.biz_ext_key = map.get('BizExtKey')
        self.enable_kp = map.get('EnableKp')
        self.update_time = map.get('UpdateTime')
        self.resource_group_type = map.get('ResourceGroupType')
        self.mode = map.get('Mode')
        self.sequence = map.get('Sequence')
        self.is_default = map.get('IsDefault')
        self.create_time = map.get('CreateTime')
        self.name = map.get('Name')
        self.tenant_id = map.get('TenantId')
        self.id = map.get('Id')
        self.status = map.get('Status')
        self.specs = map.get('Specs')
        return self


class CreateConnectionRequest(TeaModel):
    def __init__(self, project_id=None, name=None, description=None, connection_type=None, sub_type=None,
                 env_type=None, content=None):
        self.project_id = project_id    # type: int
        self.name = name                # type: str
        self.description = description  # type: str
        self.connection_type = connection_type  # type: str
        self.sub_type = sub_type        # type: str
        self.env_type = env_type        # type: int
        self.content = content          # type: str

    def validate(self):
        self.validate_required(self.project_id, 'project_id')
        self.validate_required(self.name, 'name')
        self.validate_required(self.connection_type, 'connection_type')
        self.validate_required(self.env_type, 'env_type')
        self.validate_required(self.content, 'content')

    def to_map(self):
        result = {}
        result['ProjectId'] = self.project_id
        result['Name'] = self.name
        result['Description'] = self.description
        result['ConnectionType'] = self.connection_type
        result['SubType'] = self.sub_type
        result['EnvType'] = self.env_type
        result['Content'] = self.content
        return result

    def from_map(self, map={}):
        self.project_id = map.get('ProjectId')
        self.name = map.get('Name')
        self.description = map.get('Description')
        self.connection_type = map.get('ConnectionType')
        self.sub_type = map.get('SubType')
        self.env_type = map.get('EnvType')
        self.content = map.get('Content')
        return self


class CreateConnectionResponse(TeaModel):
    def __init__(self, success=None, http_status_code=None, data=None, request_id=None):
        self.success = success          # type: bool
        self.http_status_code = http_status_code  # type: str
        self.data = data                # type: int
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.success, 'success')
        self.validate_required(self.http_status_code, 'http_status_code')
        self.validate_required(self.data, 'data')
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['Success'] = self.success
        result['HttpStatusCode'] = self.http_status_code
        result['Data'] = self.data
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.success = map.get('Success')
        self.http_status_code = map.get('HttpStatusCode')
        self.data = map.get('Data')
        self.request_id = map.get('RequestId')
        return self


class GetDataServiceApplicationRequest(TeaModel):
    def __init__(self, tenant_id=None, project_id=None, application_id=None):
        self.tenant_id = tenant_id      # type: int
        self.project_id = project_id    # type: int
        self.application_id = application_id  # type: int

    def validate(self):
        self.validate_required(self.tenant_id, 'tenant_id')
        self.validate_required(self.project_id, 'project_id')
        self.validate_required(self.application_id, 'application_id')

    def to_map(self):
        result = {}
        result['TenantId'] = self.tenant_id
        result['ProjectId'] = self.project_id
        result['ApplicationId'] = self.application_id
        return result

    def from_map(self, map={}):
        self.tenant_id = map.get('TenantId')
        self.project_id = map.get('ProjectId')
        self.application_id = map.get('ApplicationId')
        return self


class GetDataServiceApplicationResponse(TeaModel):
    def __init__(self, error_code=None, error_message=None, http_status_code=None, request_id=None, success=None,
                 data=None):
        self.error_code = error_code    # type: str
        self.error_message = error_message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.request_id = request_id    # type: str
        self.success = success          # type: bool
        self.data = data                # type: GetDataServiceApplicationResponseData

    def validate(self):
        self.validate_required(self.error_code, 'error_code')
        self.validate_required(self.error_message, 'error_message')
        self.validate_required(self.http_status_code, 'http_status_code')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.success, 'success')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['ErrorCode'] = self.error_code
        result['ErrorMessage'] = self.error_message
        result['HttpStatusCode'] = self.http_status_code
        result['RequestId'] = self.request_id
        result['Success'] = self.success
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.error_code = map.get('ErrorCode')
        self.error_message = map.get('ErrorMessage')
        self.http_status_code = map.get('HttpStatusCode')
        self.request_id = map.get('RequestId')
        self.success = map.get('Success')
        if map.get('Data') is not None:
            temp_model = GetDataServiceApplicationResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class GetDataServiceApplicationResponseData(TeaModel):
    def __init__(self, application_code=None, application_id=None, application_key=None, application_name=None,
                 application_secret=None, project_id=None):
        self.application_code = application_code  # type: str
        self.application_id = application_id  # type: int
        self.application_key = application_key  # type: str
        self.application_name = application_name  # type: str
        self.application_secret = application_secret  # type: str
        self.project_id = project_id    # type: int

    def validate(self):
        self.validate_required(self.application_code, 'application_code')
        self.validate_required(self.application_id, 'application_id')
        self.validate_required(self.application_key, 'application_key')
        self.validate_required(self.application_name, 'application_name')
        self.validate_required(self.application_secret, 'application_secret')
        self.validate_required(self.project_id, 'project_id')

    def to_map(self):
        result = {}
        result['ApplicationCode'] = self.application_code
        result['ApplicationId'] = self.application_id
        result['ApplicationKey'] = self.application_key
        result['ApplicationName'] = self.application_name
        result['ApplicationSecret'] = self.application_secret
        result['ProjectId'] = self.project_id
        return result

    def from_map(self, map={}):
        self.application_code = map.get('ApplicationCode')
        self.application_id = map.get('ApplicationId')
        self.application_key = map.get('ApplicationKey')
        self.application_name = map.get('ApplicationName')
        self.application_secret = map.get('ApplicationSecret')
        self.project_id = map.get('ProjectId')
        return self


class ListDataServiceApplicationsRequest(TeaModel):
    def __init__(self, page_number=None, page_size=None, project_id_list=None, tenant_id=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size      # type: int
        self.project_id_list = project_id_list  # type: str
        self.tenant_id = tenant_id      # type: int

    def validate(self):
        self.validate_required(self.project_id_list, 'project_id_list')
        self.validate_required(self.tenant_id, 'tenant_id')

    def to_map(self):
        result = {}
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        result['ProjectIdList'] = self.project_id_list
        result['TenantId'] = self.tenant_id
        return result

    def from_map(self, map={}):
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        self.project_id_list = map.get('ProjectIdList')
        self.tenant_id = map.get('TenantId')
        return self


class ListDataServiceApplicationsResponse(TeaModel):
    def __init__(self, error_code=None, error_message=None, http_status_code=None, request_id=None, success=None,
                 data=None):
        self.error_code = error_code    # type: str
        self.error_message = error_message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.request_id = request_id    # type: str
        self.success = success          # type: bool
        self.data = data                # type: ListDataServiceApplicationsResponseData

    def validate(self):
        self.validate_required(self.error_code, 'error_code')
        self.validate_required(self.error_message, 'error_message')
        self.validate_required(self.http_status_code, 'http_status_code')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.success, 'success')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['ErrorCode'] = self.error_code
        result['ErrorMessage'] = self.error_message
        result['HttpStatusCode'] = self.http_status_code
        result['RequestId'] = self.request_id
        result['Success'] = self.success
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.error_code = map.get('ErrorCode')
        self.error_message = map.get('ErrorMessage')
        self.http_status_code = map.get('HttpStatusCode')
        self.request_id = map.get('RequestId')
        self.success = map.get('Success')
        if map.get('Data') is not None:
            temp_model = ListDataServiceApplicationsResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class ListDataServiceApplicationsResponseDataApplications(TeaModel):
    def __init__(self, application_id=None, application_name=None, project_id=None):
        self.application_id = application_id  # type: int
        self.application_name = application_name  # type: str
        self.project_id = project_id    # type: int

    def validate(self):
        self.validate_required(self.application_id, 'application_id')
        self.validate_required(self.application_name, 'application_name')
        self.validate_required(self.project_id, 'project_id')

    def to_map(self):
        result = {}
        result['ApplicationId'] = self.application_id
        result['ApplicationName'] = self.application_name
        result['ProjectId'] = self.project_id
        return result

    def from_map(self, map={}):
        self.application_id = map.get('ApplicationId')
        self.application_name = map.get('ApplicationName')
        self.project_id = map.get('ProjectId')
        return self


class ListDataServiceApplicationsResponseData(TeaModel):
    def __init__(self, page_number=None, page_size=None, total_count=None, applications=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size      # type: int
        self.total_count = total_count  # type: int
        self.applications = applications  # type: List[ListDataServiceApplicationsResponseDataApplications]

    def validate(self):
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.applications, 'applications')
        if self.applications:
            for k in self.applications:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        result['TotalCount'] = self.total_count
        result['Applications'] = []
        if self.applications is not None:
            for k in self.applications:
                result['Applications'].append(k.to_map() if k else None)
        else:
            result['Applications'] = None
        return result

    def from_map(self, map={}):
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        self.total_count = map.get('TotalCount')
        self.applications = []
        if map.get('Applications') is not None:
            for k in map.get('Applications'):
                temp_model = ListDataServiceApplicationsResponseDataApplications()
                self.applications.append(temp_model.from_map(k))
        else:
            self.applications = None
        return self


class GetNodeOnBaselineRequest(TeaModel):
    def __init__(self, baseline_id=None):
        self.baseline_id = baseline_id  # type: int

    def validate(self):
        self.validate_required(self.baseline_id, 'baseline_id')

    def to_map(self):
        result = {}
        result['BaselineId'] = self.baseline_id
        return result

    def from_map(self, map={}):
        self.baseline_id = map.get('BaselineId')
        return self


class GetNodeOnBaselineResponse(TeaModel):
    def __init__(self, success=None, error_code=None, error_message=None, http_status_code=None, request_id=None,
                 data=None):
        self.success = success          # type: str
        self.error_code = error_code    # type: str
        self.error_message = error_message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.request_id = request_id    # type: str
        self.data = data                # type: List[GetNodeOnBaselineResponseData]

    def validate(self):
        self.validate_required(self.success, 'success')
        self.validate_required(self.error_code, 'error_code')
        self.validate_required(self.error_message, 'error_message')
        self.validate_required(self.http_status_code, 'http_status_code')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['Success'] = self.success
        result['ErrorCode'] = self.error_code
        result['ErrorMessage'] = self.error_message
        result['HttpStatusCode'] = self.http_status_code
        result['RequestId'] = self.request_id
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.success = map.get('Success')
        self.error_code = map.get('ErrorCode')
        self.error_message = map.get('ErrorMessage')
        self.http_status_code = map.get('HttpStatusCode')
        self.request_id = map.get('RequestId')
        self.data = []
        if map.get('Data') is not None:
            for k in map.get('Data'):
                temp_model = GetNodeOnBaselineResponseData()
                self.data.append(temp_model.from_map(k))
        else:
            self.data = None
        return self


class GetNodeOnBaselineResponseData(TeaModel):
    def __init__(self, node_id=None, node_name=None, owner=None, project_id=None):
        self.node_id = node_id          # type: int
        self.node_name = node_name      # type: str
        self.owner = owner              # type: str
        self.project_id = project_id    # type: int

    def validate(self):
        self.validate_required(self.node_id, 'node_id')
        self.validate_required(self.node_name, 'node_name')
        self.validate_required(self.owner, 'owner')
        self.validate_required(self.project_id, 'project_id')

    def to_map(self):
        result = {}
        result['NodeId'] = self.node_id
        result['NodeName'] = self.node_name
        result['Owner'] = self.owner
        result['ProjectId'] = self.project_id
        return result

    def from_map(self, map={}):
        self.node_id = map.get('NodeId')
        self.node_name = map.get('NodeName')
        self.owner = map.get('Owner')
        self.project_id = map.get('ProjectId')
        return self


class ListBaselineConfigsRequest(TeaModel):
    def __init__(self, page_number=None, page_size=None, owner=None, project_id=None, priority=None, useflag=None,
                 baseline_types=None, search_text=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size      # type: int
        self.owner = owner              # type: str
        self.project_id = project_id    # type: int
        self.priority = priority        # type: str
        self.useflag = useflag          # type: bool
        self.baseline_types = baseline_types  # type: str
        self.search_text = search_text  # type: str

    def validate(self):
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.project_id, 'project_id')

    def to_map(self):
        result = {}
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        result['Owner'] = self.owner
        result['ProjectId'] = self.project_id
        result['Priority'] = self.priority
        result['Useflag'] = self.useflag
        result['BaselineTypes'] = self.baseline_types
        result['SearchText'] = self.search_text
        return result

    def from_map(self, map={}):
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        self.owner = map.get('Owner')
        self.project_id = map.get('ProjectId')
        self.priority = map.get('Priority')
        self.useflag = map.get('Useflag')
        self.baseline_types = map.get('BaselineTypes')
        self.search_text = map.get('SearchText')
        return self


class ListBaselineConfigsResponse(TeaModel):
    def __init__(self, success=None, error_code=None, error_message=None, http_status_code=None, request_id=None,
                 data=None):
        self.success = success          # type: bool
        self.error_code = error_code    # type: str
        self.error_message = error_message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.request_id = request_id    # type: str
        self.data = data                # type: ListBaselineConfigsResponseData

    def validate(self):
        self.validate_required(self.success, 'success')
        self.validate_required(self.error_code, 'error_code')
        self.validate_required(self.error_message, 'error_message')
        self.validate_required(self.http_status_code, 'http_status_code')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['Success'] = self.success
        result['ErrorCode'] = self.error_code
        result['ErrorMessage'] = self.error_message
        result['HttpStatusCode'] = self.http_status_code
        result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.success = map.get('Success')
        self.error_code = map.get('ErrorCode')
        self.error_message = map.get('ErrorMessage')
        self.http_status_code = map.get('HttpStatusCode')
        self.request_id = map.get('RequestId')
        if map.get('Data') is not None:
            temp_model = ListBaselineConfigsResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class ListBaselineConfigsResponseDataBaselines(TeaModel):
    def __init__(self, baseline_id=None, priority=None, baseline_name=None, owner=None, project_id=None,
                 use_flag=None, baseline_type=None, exp_hour=None, exp_minu=None, sla_hour=None, sla_minu=None,
                 hour_exp_detail=None, hour_sla_detail=None, is_default=None):
        self.baseline_id = baseline_id  # type: int
        self.priority = priority        # type: int
        self.baseline_name = baseline_name  # type: str
        self.owner = owner              # type: str
        self.project_id = project_id    # type: int
        self.use_flag = use_flag        # type: bool
        self.baseline_type = baseline_type  # type: str
        self.exp_hour = exp_hour        # type: int
        self.exp_minu = exp_minu        # type: int
        self.sla_hour = sla_hour        # type: int
        self.sla_minu = sla_minu        # type: int
        self.hour_exp_detail = hour_exp_detail  # type: str
        self.hour_sla_detail = hour_sla_detail  # type: str
        self.is_default = is_default    # type: bool

    def validate(self):
        self.validate_required(self.baseline_id, 'baseline_id')
        self.validate_required(self.priority, 'priority')
        self.validate_required(self.baseline_name, 'baseline_name')
        self.validate_required(self.owner, 'owner')
        self.validate_required(self.project_id, 'project_id')
        self.validate_required(self.use_flag, 'use_flag')
        self.validate_required(self.baseline_type, 'baseline_type')
        self.validate_required(self.exp_hour, 'exp_hour')
        self.validate_required(self.exp_minu, 'exp_minu')
        self.validate_required(self.sla_hour, 'sla_hour')
        self.validate_required(self.sla_minu, 'sla_minu')
        self.validate_required(self.hour_exp_detail, 'hour_exp_detail')
        self.validate_required(self.hour_sla_detail, 'hour_sla_detail')
        self.validate_required(self.is_default, 'is_default')

    def to_map(self):
        result = {}
        result['BaselineId'] = self.baseline_id
        result['Priority'] = self.priority
        result['BaselineName'] = self.baseline_name
        result['Owner'] = self.owner
        result['ProjectId'] = self.project_id
        result['UseFlag'] = self.use_flag
        result['BaselineType'] = self.baseline_type
        result['ExpHour'] = self.exp_hour
        result['ExpMinu'] = self.exp_minu
        result['SlaHour'] = self.sla_hour
        result['SlaMinu'] = self.sla_minu
        result['HourExpDetail'] = self.hour_exp_detail
        result['HourSlaDetail'] = self.hour_sla_detail
        result['IsDefault'] = self.is_default
        return result

    def from_map(self, map={}):
        self.baseline_id = map.get('BaselineId')
        self.priority = map.get('Priority')
        self.baseline_name = map.get('BaselineName')
        self.owner = map.get('Owner')
        self.project_id = map.get('ProjectId')
        self.use_flag = map.get('UseFlag')
        self.baseline_type = map.get('BaselineType')
        self.exp_hour = map.get('ExpHour')
        self.exp_minu = map.get('ExpMinu')
        self.sla_hour = map.get('SlaHour')
        self.sla_minu = map.get('SlaMinu')
        self.hour_exp_detail = map.get('HourExpDetail')
        self.hour_sla_detail = map.get('HourSlaDetail')
        self.is_default = map.get('IsDefault')
        return self


class ListBaselineConfigsResponseData(TeaModel):
    def __init__(self, page_number=None, page_size=None, total_count=None, baselines=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size      # type: int
        self.total_count = total_count  # type: int
        self.baselines = baselines      # type: List[ListBaselineConfigsResponseDataBaselines]

    def validate(self):
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.baselines, 'baselines')
        if self.baselines:
            for k in self.baselines:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        result['TotalCount'] = self.total_count
        result['Baselines'] = []
        if self.baselines is not None:
            for k in self.baselines:
                result['Baselines'].append(k.to_map() if k else None)
        else:
            result['Baselines'] = None
        return result

    def from_map(self, map={}):
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        self.total_count = map.get('TotalCount')
        self.baselines = []
        if map.get('Baselines') is not None:
            for k in map.get('Baselines'):
                temp_model = ListBaselineConfigsResponseDataBaselines()
                self.baselines.append(temp_model.from_map(k))
        else:
            self.baselines = None
        return self


class GetMetaTableChangeLogRequest(TeaModel):
    def __init__(self, page_number=None, page_size=None, table_guid=None, change_type=None, object_type=None,
                 start_date=None, end_date=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size      # type: int
        self.table_guid = table_guid    # type: str
        self.change_type = change_type  # type: str
        self.object_type = object_type  # type: str
        self.start_date = start_date    # type: str
        self.end_date = end_date        # type: str

    def validate(self):
        self.validate_required(self.table_guid, 'table_guid')

    def to_map(self):
        result = {}
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        result['TableGuid'] = self.table_guid
        result['ChangeType'] = self.change_type
        result['ObjectType'] = self.object_type
        result['StartDate'] = self.start_date
        result['EndDate'] = self.end_date
        return result

    def from_map(self, map={}):
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        self.table_guid = map.get('TableGuid')
        self.change_type = map.get('ChangeType')
        self.object_type = map.get('ObjectType')
        self.start_date = map.get('StartDate')
        self.end_date = map.get('EndDate')
        return self


class GetMetaTableChangeLogResponse(TeaModel):
    def __init__(self, request_id=None, error_code=None, error_message=None, http_status_code=None, success=None,
                 data=None):
        self.request_id = request_id    # type: str
        self.error_code = error_code    # type: str
        self.error_message = error_message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.success = success          # type: bool
        self.data = data                # type: GetMetaTableChangeLogResponseData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.error_code, 'error_code')
        self.validate_required(self.error_message, 'error_message')
        self.validate_required(self.http_status_code, 'http_status_code')
        self.validate_required(self.success, 'success')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['ErrorCode'] = self.error_code
        result['ErrorMessage'] = self.error_message
        result['HttpStatusCode'] = self.http_status_code
        result['Success'] = self.success
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.error_code = map.get('ErrorCode')
        self.error_message = map.get('ErrorMessage')
        self.http_status_code = map.get('HttpStatusCode')
        self.success = map.get('Success')
        if map.get('Data') is not None:
            temp_model = GetMetaTableChangeLogResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class GetMetaTableChangeLogResponseDataDataEntityList(TeaModel):
    def __init__(self, create_time=None, modified_time=None, change_type=None, operator=None, object_type=None,
                 change_content=None):
        self.create_time = create_time  # type: int
        self.modified_time = modified_time  # type: int
        self.change_type = change_type  # type: str
        self.operator = operator        # type: str
        self.object_type = object_type  # type: str
        self.change_content = change_content  # type: str

    def validate(self):
        self.validate_required(self.create_time, 'create_time')
        self.validate_required(self.modified_time, 'modified_time')
        self.validate_required(self.change_type, 'change_type')
        self.validate_required(self.operator, 'operator')
        self.validate_required(self.object_type, 'object_type')
        self.validate_required(self.change_content, 'change_content')

    def to_map(self):
        result = {}
        result['CreateTime'] = self.create_time
        result['ModifiedTime'] = self.modified_time
        result['ChangeType'] = self.change_type
        result['Operator'] = self.operator
        result['ObjectType'] = self.object_type
        result['ChangeContent'] = self.change_content
        return result

    def from_map(self, map={}):
        self.create_time = map.get('CreateTime')
        self.modified_time = map.get('ModifiedTime')
        self.change_type = map.get('ChangeType')
        self.operator = map.get('Operator')
        self.object_type = map.get('ObjectType')
        self.change_content = map.get('ChangeContent')
        return self


class GetMetaTableChangeLogResponseData(TeaModel):
    def __init__(self, page_number=None, page_size=None, total_count=None, data_entity_list=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size      # type: int
        self.total_count = total_count  # type: int
        self.data_entity_list = data_entity_list  # type: List[GetMetaTableChangeLogResponseDataDataEntityList]

    def validate(self):
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.data_entity_list, 'data_entity_list')
        if self.data_entity_list:
            for k in self.data_entity_list:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        result['TotalCount'] = self.total_count
        result['DataEntityList'] = []
        if self.data_entity_list is not None:
            for k in self.data_entity_list:
                result['DataEntityList'].append(k.to_map() if k else None)
        else:
            result['DataEntityList'] = None
        return result

    def from_map(self, map={}):
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        self.total_count = map.get('TotalCount')
        self.data_entity_list = []
        if map.get('DataEntityList') is not None:
            for k in map.get('DataEntityList'):
                temp_model = GetMetaTableChangeLogResponseDataDataEntityList()
                self.data_entity_list.append(temp_model.from_map(k))
        else:
            self.data_entity_list = None
        return self


class GetMetaTableOutputRequest(TeaModel):
    def __init__(self, page_number=None, page_size=None, table_guid=None, start_date=None, end_date=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size      # type: int
        self.table_guid = table_guid    # type: str
        self.start_date = start_date    # type: str
        self.end_date = end_date        # type: str

    def validate(self):
        self.validate_required(self.table_guid, 'table_guid')
        self.validate_required(self.start_date, 'start_date')
        self.validate_required(self.end_date, 'end_date')

    def to_map(self):
        result = {}
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        result['TableGuid'] = self.table_guid
        result['StartDate'] = self.start_date
        result['EndDate'] = self.end_date
        return result

    def from_map(self, map={}):
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        self.table_guid = map.get('TableGuid')
        self.start_date = map.get('StartDate')
        self.end_date = map.get('EndDate')
        return self


class GetMetaTableOutputResponse(TeaModel):
    def __init__(self, request_id=None, error_code=None, error_message=None, http_status_code=None, success=None,
                 data=None):
        self.request_id = request_id    # type: str
        self.error_code = error_code    # type: str
        self.error_message = error_message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.success = success          # type: bool
        self.data = data                # type: GetMetaTableOutputResponseData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.error_code, 'error_code')
        self.validate_required(self.error_message, 'error_message')
        self.validate_required(self.http_status_code, 'http_status_code')
        self.validate_required(self.success, 'success')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['ErrorCode'] = self.error_code
        result['ErrorMessage'] = self.error_message
        result['HttpStatusCode'] = self.http_status_code
        result['Success'] = self.success
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.error_code = map.get('ErrorCode')
        self.error_message = map.get('ErrorMessage')
        self.http_status_code = map.get('HttpStatusCode')
        self.success = map.get('Success')
        if map.get('Data') is not None:
            temp_model = GetMetaTableOutputResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class GetMetaTableOutputResponseDataDataEntityList(TeaModel):
    def __init__(self, table_guid=None, task_id=None, start_time=None, end_time=None, wait_time=None,
                 project_id=None, task_instance_id=None):
        self.table_guid = table_guid    # type: str
        self.task_id = task_id          # type: str
        self.start_time = start_time    # type: str
        self.end_time = end_time        # type: str
        self.wait_time = wait_time      # type: str
        self.project_id = project_id    # type: int
        self.task_instance_id = task_instance_id  # type: int

    def validate(self):
        self.validate_required(self.table_guid, 'table_guid')
        self.validate_required(self.task_id, 'task_id')
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')
        self.validate_required(self.wait_time, 'wait_time')
        self.validate_required(self.project_id, 'project_id')
        self.validate_required(self.task_instance_id, 'task_instance_id')

    def to_map(self):
        result = {}
        result['TableGuid'] = self.table_guid
        result['TaskId'] = self.task_id
        result['StartTime'] = self.start_time
        result['EndTime'] = self.end_time
        result['WaitTime'] = self.wait_time
        result['ProjectId'] = self.project_id
        result['TaskInstanceId'] = self.task_instance_id
        return result

    def from_map(self, map={}):
        self.table_guid = map.get('TableGuid')
        self.task_id = map.get('TaskId')
        self.start_time = map.get('StartTime')
        self.end_time = map.get('EndTime')
        self.wait_time = map.get('WaitTime')
        self.project_id = map.get('ProjectId')
        self.task_instance_id = map.get('TaskInstanceId')
        return self


class GetMetaTableOutputResponseData(TeaModel):
    def __init__(self, page_number=None, page_size=None, total_count=None, data_entity_list=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size      # type: int
        self.total_count = total_count  # type: int
        self.data_entity_list = data_entity_list  # type: List[GetMetaTableOutputResponseDataDataEntityList]

    def validate(self):
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.data_entity_list, 'data_entity_list')
        if self.data_entity_list:
            for k in self.data_entity_list:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        result['TotalCount'] = self.total_count
        result['DataEntityList'] = []
        if self.data_entity_list is not None:
            for k in self.data_entity_list:
                result['DataEntityList'].append(k.to_map() if k else None)
        else:
            result['DataEntityList'] = None
        return result

    def from_map(self, map={}):
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        self.total_count = map.get('TotalCount')
        self.data_entity_list = []
        if map.get('DataEntityList') is not None:
            for k in map.get('DataEntityList'):
                temp_model = GetMetaTableOutputResponseDataDataEntityList()
                self.data_entity_list.append(temp_model.from_map(k))
        else:
            self.data_entity_list = None
        return self


class GetMetaTablePartitionRequest(TeaModel):
    def __init__(self, page_number=None, page_size=None, table_guid=None, cluster_id=None, database_name=None,
                 table_name=None, data_source_type=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size      # type: int
        self.table_guid = table_guid    # type: str
        self.cluster_id = cluster_id    # type: str
        self.database_name = database_name  # type: str
        self.table_name = table_name    # type: str
        self.data_source_type = data_source_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        result['TableGuid'] = self.table_guid
        result['ClusterId'] = self.cluster_id
        result['DatabaseName'] = self.database_name
        result['TableName'] = self.table_name
        result['DataSourceType'] = self.data_source_type
        return result

    def from_map(self, map={}):
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        self.table_guid = map.get('TableGuid')
        self.cluster_id = map.get('ClusterId')
        self.database_name = map.get('DatabaseName')
        self.table_name = map.get('TableName')
        self.data_source_type = map.get('DataSourceType')
        return self


class GetMetaTablePartitionResponse(TeaModel):
    def __init__(self, request_id=None, error_code=None, error_message=None, http_status_code=None, success=None,
                 data=None):
        self.request_id = request_id    # type: str
        self.error_code = error_code    # type: str
        self.error_message = error_message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.success = success          # type: bool
        self.data = data                # type: GetMetaTablePartitionResponseData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.error_code, 'error_code')
        self.validate_required(self.error_message, 'error_message')
        self.validate_required(self.http_status_code, 'http_status_code')
        self.validate_required(self.success, 'success')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['ErrorCode'] = self.error_code
        result['ErrorMessage'] = self.error_message
        result['HttpStatusCode'] = self.http_status_code
        result['Success'] = self.success
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.error_code = map.get('ErrorCode')
        self.error_message = map.get('ErrorMessage')
        self.http_status_code = map.get('HttpStatusCode')
        self.success = map.get('Success')
        if map.get('Data') is not None:
            temp_model = GetMetaTablePartitionResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class GetMetaTablePartitionResponseDataDataEntityList(TeaModel):
    def __init__(self, partition_guid=None, partition_name=None, create_time=None, data_size=None,
                 record_count=None, modified_time=None, table_guid=None, comment=None, partition_type=None, partition_path=None,
                 partition_location=None):
        self.partition_guid = partition_guid  # type: str
        self.partition_name = partition_name  # type: str
        self.create_time = create_time  # type: int
        self.data_size = data_size      # type: int
        self.record_count = record_count  # type: int
        self.modified_time = modified_time  # type: int
        self.table_guid = table_guid    # type: str
        self.comment = comment          # type: str
        self.partition_type = partition_type  # type: str
        self.partition_path = partition_path  # type: str
        self.partition_location = partition_location  # type: str

    def validate(self):
        self.validate_required(self.partition_guid, 'partition_guid')
        self.validate_required(self.partition_name, 'partition_name')
        self.validate_required(self.create_time, 'create_time')
        self.validate_required(self.data_size, 'data_size')
        self.validate_required(self.record_count, 'record_count')
        self.validate_required(self.modified_time, 'modified_time')
        self.validate_required(self.table_guid, 'table_guid')
        self.validate_required(self.comment, 'comment')
        self.validate_required(self.partition_type, 'partition_type')
        self.validate_required(self.partition_path, 'partition_path')
        self.validate_required(self.partition_location, 'partition_location')

    def to_map(self):
        result = {}
        result['PartitionGuid'] = self.partition_guid
        result['PartitionName'] = self.partition_name
        result['CreateTime'] = self.create_time
        result['DataSize'] = self.data_size
        result['RecordCount'] = self.record_count
        result['ModifiedTime'] = self.modified_time
        result['TableGuid'] = self.table_guid
        result['Comment'] = self.comment
        result['PartitionType'] = self.partition_type
        result['PartitionPath'] = self.partition_path
        result['PartitionLocation'] = self.partition_location
        return result

    def from_map(self, map={}):
        self.partition_guid = map.get('PartitionGuid')
        self.partition_name = map.get('PartitionName')
        self.create_time = map.get('CreateTime')
        self.data_size = map.get('DataSize')
        self.record_count = map.get('RecordCount')
        self.modified_time = map.get('ModifiedTime')
        self.table_guid = map.get('TableGuid')
        self.comment = map.get('Comment')
        self.partition_type = map.get('PartitionType')
        self.partition_path = map.get('PartitionPath')
        self.partition_location = map.get('PartitionLocation')
        return self


class GetMetaTablePartitionResponseData(TeaModel):
    def __init__(self, page_number=None, page_size=None, total_count=None, data_entity_list=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size      # type: int
        self.total_count = total_count  # type: int
        self.data_entity_list = data_entity_list  # type: List[GetMetaTablePartitionResponseDataDataEntityList]

    def validate(self):
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.data_entity_list, 'data_entity_list')
        if self.data_entity_list:
            for k in self.data_entity_list:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        result['TotalCount'] = self.total_count
        result['DataEntityList'] = []
        if self.data_entity_list is not None:
            for k in self.data_entity_list:
                result['DataEntityList'].append(k.to_map() if k else None)
        else:
            result['DataEntityList'] = None
        return result

    def from_map(self, map={}):
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        self.total_count = map.get('TotalCount')
        self.data_entity_list = []
        if map.get('DataEntityList') is not None:
            for k in map.get('DataEntityList'):
                temp_model = GetMetaTablePartitionResponseDataDataEntityList()
                self.data_entity_list.append(temp_model.from_map(k))
        else:
            self.data_entity_list = None
        return self


class GetMetaTableFullInfoRequest(TeaModel):
    def __init__(self, table_guid=None, page_num=None, page_size=None, cluster_id=None, database_name=None,
                 table_name=None, data_source_type=None):
        self.table_guid = table_guid    # type: str
        self.page_num = page_num        # type: int
        self.page_size = page_size      # type: int
        self.cluster_id = cluster_id    # type: str
        self.database_name = database_name  # type: str
        self.table_name = table_name    # type: str
        self.data_source_type = data_source_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['TableGuid'] = self.table_guid
        result['PageNum'] = self.page_num
        result['PageSize'] = self.page_size
        result['ClusterId'] = self.cluster_id
        result['DatabaseName'] = self.database_name
        result['TableName'] = self.table_name
        result['DataSourceType'] = self.data_source_type
        return result

    def from_map(self, map={}):
        self.table_guid = map.get('TableGuid')
        self.page_num = map.get('PageNum')
        self.page_size = map.get('PageSize')
        self.cluster_id = map.get('ClusterId')
        self.database_name = map.get('DatabaseName')
        self.table_name = map.get('TableName')
        self.data_source_type = map.get('DataSourceType')
        return self


class GetMetaTableFullInfoResponse(TeaModel):
    def __init__(self, request_id=None, error_code=None, error_message=None, http_status_code=None, success=None,
                 data=None):
        self.request_id = request_id    # type: str
        self.error_code = error_code    # type: str
        self.error_message = error_message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.success = success          # type: bool
        self.data = data                # type: GetMetaTableFullInfoResponseData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.error_code, 'error_code')
        self.validate_required(self.error_message, 'error_message')
        self.validate_required(self.http_status_code, 'http_status_code')
        self.validate_required(self.success, 'success')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['ErrorCode'] = self.error_code
        result['ErrorMessage'] = self.error_message
        result['HttpStatusCode'] = self.http_status_code
        result['Success'] = self.success
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.error_code = map.get('ErrorCode')
        self.error_message = map.get('ErrorMessage')
        self.http_status_code = map.get('HttpStatusCode')
        self.success = map.get('Success')
        if map.get('Data') is not None:
            temp_model = GetMetaTableFullInfoResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class GetMetaTableFullInfoResponseDataColumnList(TeaModel):
    def __init__(self, column_guid=None, column_name=None, column_type=None, is_primary_key=None, comment=None,
                 is_partition_column=None, is_foreign_key=None, caption=None):
        self.column_guid = column_guid  # type: str
        self.column_name = column_name  # type: str
        self.column_type = column_type  # type: str
        self.is_primary_key = is_primary_key  # type: bool
        self.comment = comment          # type: str
        self.is_partition_column = is_partition_column  # type: bool
        self.is_foreign_key = is_foreign_key  # type: bool
        self.caption = caption          # type: str

    def validate(self):
        self.validate_required(self.column_guid, 'column_guid')
        self.validate_required(self.column_name, 'column_name')
        self.validate_required(self.column_type, 'column_type')
        self.validate_required(self.is_primary_key, 'is_primary_key')
        self.validate_required(self.comment, 'comment')
        self.validate_required(self.is_partition_column, 'is_partition_column')
        self.validate_required(self.is_foreign_key, 'is_foreign_key')
        self.validate_required(self.caption, 'caption')

    def to_map(self):
        result = {}
        result['ColumnGuid'] = self.column_guid
        result['ColumnName'] = self.column_name
        result['ColumnType'] = self.column_type
        result['IsPrimaryKey'] = self.is_primary_key
        result['Comment'] = self.comment
        result['IsPartitionColumn'] = self.is_partition_column
        result['IsForeignKey'] = self.is_foreign_key
        result['Caption'] = self.caption
        return result

    def from_map(self, map={}):
        self.column_guid = map.get('ColumnGuid')
        self.column_name = map.get('ColumnName')
        self.column_type = map.get('ColumnType')
        self.is_primary_key = map.get('IsPrimaryKey')
        self.comment = map.get('Comment')
        self.is_partition_column = map.get('IsPartitionColumn')
        self.is_foreign_key = map.get('IsForeignKey')
        self.caption = map.get('Caption')
        return self


class GetMetaTableFullInfoResponseData(TeaModel):
    def __init__(self, table_name=None, table_guid=None, owner_id=None, tenant_id=None, project_id=None,
                 create_time=None, last_modify_time=None, life_cycle=None, is_visible=None, project_name=None, data_size=None,
                 env_type=None, comment=None, total_column_count=None, last_ddl_time=None, last_access_time=None,
                 database_name=None, partition_keys=None, location=None, cluster_id=None, column_list=None):
        self.table_name = table_name    # type: str
        self.table_guid = table_guid    # type: str
        self.owner_id = owner_id        # type: str
        self.tenant_id = tenant_id      # type: int
        self.project_id = project_id    # type: int
        self.create_time = create_time  # type: int
        self.last_modify_time = last_modify_time  # type: int
        self.life_cycle = life_cycle    # type: int
        self.is_visible = is_visible    # type: int
        self.project_name = project_name  # type: str
        self.data_size = data_size      # type: int
        self.env_type = env_type        # type: int
        self.comment = comment          # type: str
        self.total_column_count = total_column_count  # type: int
        self.last_ddl_time = last_ddl_time  # type: int
        self.last_access_time = last_access_time  # type: int
        self.database_name = database_name  # type: str
        self.partition_keys = partition_keys  # type: str
        self.location = location        # type: str
        self.cluster_id = cluster_id    # type: str
        self.column_list = column_list  # type: List[GetMetaTableFullInfoResponseDataColumnList]

    def validate(self):
        self.validate_required(self.table_name, 'table_name')
        self.validate_required(self.table_guid, 'table_guid')
        self.validate_required(self.owner_id, 'owner_id')
        self.validate_required(self.tenant_id, 'tenant_id')
        self.validate_required(self.project_id, 'project_id')
        self.validate_required(self.create_time, 'create_time')
        self.validate_required(self.last_modify_time, 'last_modify_time')
        self.validate_required(self.life_cycle, 'life_cycle')
        self.validate_required(self.is_visible, 'is_visible')
        self.validate_required(self.project_name, 'project_name')
        self.validate_required(self.data_size, 'data_size')
        self.validate_required(self.env_type, 'env_type')
        self.validate_required(self.comment, 'comment')
        self.validate_required(self.total_column_count, 'total_column_count')
        self.validate_required(self.last_ddl_time, 'last_ddl_time')
        self.validate_required(self.last_access_time, 'last_access_time')
        self.validate_required(self.database_name, 'database_name')
        self.validate_required(self.partition_keys, 'partition_keys')
        self.validate_required(self.location, 'location')
        self.validate_required(self.cluster_id, 'cluster_id')
        self.validate_required(self.column_list, 'column_list')
        if self.column_list:
            for k in self.column_list:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['TableName'] = self.table_name
        result['TableGuid'] = self.table_guid
        result['OwnerId'] = self.owner_id
        result['TenantId'] = self.tenant_id
        result['ProjectId'] = self.project_id
        result['CreateTime'] = self.create_time
        result['LastModifyTime'] = self.last_modify_time
        result['LifeCycle'] = self.life_cycle
        result['IsVisible'] = self.is_visible
        result['ProjectName'] = self.project_name
        result['DataSize'] = self.data_size
        result['EnvType'] = self.env_type
        result['Comment'] = self.comment
        result['TotalColumnCount'] = self.total_column_count
        result['LastDdlTime'] = self.last_ddl_time
        result['LastAccessTime'] = self.last_access_time
        result['DatabaseName'] = self.database_name
        result['PartitionKeys'] = self.partition_keys
        result['Location'] = self.location
        result['ClusterId'] = self.cluster_id
        result['ColumnList'] = []
        if self.column_list is not None:
            for k in self.column_list:
                result['ColumnList'].append(k.to_map() if k else None)
        else:
            result['ColumnList'] = None
        return result

    def from_map(self, map={}):
        self.table_name = map.get('TableName')
        self.table_guid = map.get('TableGuid')
        self.owner_id = map.get('OwnerId')
        self.tenant_id = map.get('TenantId')
        self.project_id = map.get('ProjectId')
        self.create_time = map.get('CreateTime')
        self.last_modify_time = map.get('LastModifyTime')
        self.life_cycle = map.get('LifeCycle')
        self.is_visible = map.get('IsVisible')
        self.project_name = map.get('ProjectName')
        self.data_size = map.get('DataSize')
        self.env_type = map.get('EnvType')
        self.comment = map.get('Comment')
        self.total_column_count = map.get('TotalColumnCount')
        self.last_ddl_time = map.get('LastDdlTime')
        self.last_access_time = map.get('LastAccessTime')
        self.database_name = map.get('DatabaseName')
        self.partition_keys = map.get('PartitionKeys')
        self.location = map.get('Location')
        self.cluster_id = map.get('ClusterId')
        self.column_list = []
        if map.get('ColumnList') is not None:
            for k in map.get('ColumnList'):
                temp_model = GetMetaTableFullInfoResponseDataColumnList()
                self.column_list.append(temp_model.from_map(k))
        else:
            self.column_list = None
        return self


class GetFileVersionRequest(TeaModel):
    def __init__(self, file_id=None, project_id=None, project_identifier=None, file_version=None):
        self.file_id = file_id          # type: int
        self.project_id = project_id    # type: int
        self.project_identifier = project_identifier  # type: str
        self.file_version = file_version  # type: int

    def validate(self):
        self.validate_required(self.file_id, 'file_id')
        self.validate_required(self.file_version, 'file_version')

    def to_map(self):
        result = {}
        result['FileId'] = self.file_id
        result['ProjectId'] = self.project_id
        result['ProjectIdentifier'] = self.project_identifier
        result['FileVersion'] = self.file_version
        return result

    def from_map(self, map={}):
        self.file_id = map.get('FileId')
        self.project_id = map.get('ProjectId')
        self.project_identifier = map.get('ProjectIdentifier')
        self.file_version = map.get('FileVersion')
        return self


class GetFileVersionResponse(TeaModel):
    def __init__(self, request_id=None, success=None, error_code=None, error_message=None, http_status_code=None,
                 data=None):
        self.request_id = request_id    # type: str
        self.success = success          # type: bool
        self.error_code = error_code    # type: str
        self.error_message = error_message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.data = data                # type: GetFileVersionResponseData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.success, 'success')
        self.validate_required(self.error_code, 'error_code')
        self.validate_required(self.error_message, 'error_message')
        self.validate_required(self.http_status_code, 'http_status_code')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Success'] = self.success
        result['ErrorCode'] = self.error_code
        result['ErrorMessage'] = self.error_message
        result['HttpStatusCode'] = self.http_status_code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.success = map.get('Success')
        self.error_code = map.get('ErrorCode')
        self.error_message = map.get('ErrorMessage')
        self.http_status_code = map.get('HttpStatusCode')
        if map.get('Data') is not None:
            temp_model = GetFileVersionResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class GetFileVersionResponseData(TeaModel):
    def __init__(self, file_version=None, file_content=None, file_property_content=None, node_content=None,
                 comment=None, node_id=None, is_current_prod=None, change_type=None, status=None, file_name=None,
                 commit_user=None, commit_time=None, use_type=None):
        self.file_version = file_version  # type: int
        self.file_content = file_content  # type: str
        self.file_property_content = file_property_content  # type: str
        self.node_content = node_content  # type: str
        self.comment = comment          # type: str
        self.node_id = node_id          # type: int
        self.is_current_prod = is_current_prod  # type: bool
        self.change_type = change_type  # type: str
        self.status = status            # type: str
        self.file_name = file_name      # type: str
        self.commit_user = commit_user  # type: str
        self.commit_time = commit_time  # type: int
        self.use_type = use_type        # type: str

    def validate(self):
        self.validate_required(self.file_version, 'file_version')
        self.validate_required(self.file_content, 'file_content')
        self.validate_required(self.file_property_content, 'file_property_content')
        self.validate_required(self.node_content, 'node_content')
        self.validate_required(self.comment, 'comment')
        self.validate_required(self.node_id, 'node_id')
        self.validate_required(self.is_current_prod, 'is_current_prod')
        self.validate_required(self.change_type, 'change_type')
        self.validate_required(self.status, 'status')
        self.validate_required(self.file_name, 'file_name')
        self.validate_required(self.commit_user, 'commit_user')
        self.validate_required(self.commit_time, 'commit_time')
        self.validate_required(self.use_type, 'use_type')

    def to_map(self):
        result = {}
        result['FileVersion'] = self.file_version
        result['FileContent'] = self.file_content
        result['FilePropertyContent'] = self.file_property_content
        result['NodeContent'] = self.node_content
        result['Comment'] = self.comment
        result['NodeId'] = self.node_id
        result['IsCurrentProd'] = self.is_current_prod
        result['ChangeType'] = self.change_type
        result['Status'] = self.status
        result['FileName'] = self.file_name
        result['CommitUser'] = self.commit_user
        result['CommitTime'] = self.commit_time
        result['UseType'] = self.use_type
        return result

    def from_map(self, map={}):
        self.file_version = map.get('FileVersion')
        self.file_content = map.get('FileContent')
        self.file_property_content = map.get('FilePropertyContent')
        self.node_content = map.get('NodeContent')
        self.comment = map.get('Comment')
        self.node_id = map.get('NodeId')
        self.is_current_prod = map.get('IsCurrentProd')
        self.change_type = map.get('ChangeType')
        self.status = map.get('Status')
        self.file_name = map.get('FileName')
        self.commit_user = map.get('CommitUser')
        self.commit_time = map.get('CommitTime')
        self.use_type = map.get('UseType')
        return self


class GetMetaTableBasicInfoRequest(TeaModel):
    def __init__(self, table_guid=None, cluster_id=None, database_name=None, table_name=None, data_source_type=None):
        self.table_guid = table_guid    # type: str
        self.cluster_id = cluster_id    # type: str
        self.database_name = database_name  # type: str
        self.table_name = table_name    # type: str
        self.data_source_type = data_source_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['TableGuid'] = self.table_guid
        result['ClusterId'] = self.cluster_id
        result['DatabaseName'] = self.database_name
        result['TableName'] = self.table_name
        result['DataSourceType'] = self.data_source_type
        return result

    def from_map(self, map={}):
        self.table_guid = map.get('TableGuid')
        self.cluster_id = map.get('ClusterId')
        self.database_name = map.get('DatabaseName')
        self.table_name = map.get('TableName')
        self.data_source_type = map.get('DataSourceType')
        return self


class GetMetaTableBasicInfoResponse(TeaModel):
    def __init__(self, request_id=None, error_code=None, error_message=None, http_status_code=None, success=None,
                 data=None):
        self.request_id = request_id    # type: str
        self.error_code = error_code    # type: str
        self.error_message = error_message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.success = success          # type: bool
        self.data = data                # type: GetMetaTableBasicInfoResponseData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.error_code, 'error_code')
        self.validate_required(self.error_message, 'error_message')
        self.validate_required(self.http_status_code, 'http_status_code')
        self.validate_required(self.success, 'success')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['ErrorCode'] = self.error_code
        result['ErrorMessage'] = self.error_message
        result['HttpStatusCode'] = self.http_status_code
        result['Success'] = self.success
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.error_code = map.get('ErrorCode')
        self.error_message = map.get('ErrorMessage')
        self.http_status_code = map.get('HttpStatusCode')
        self.success = map.get('Success')
        if map.get('Data') is not None:
            temp_model = GetMetaTableBasicInfoResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class GetMetaTableBasicInfoResponseData(TeaModel):
    def __init__(self, table_name=None, table_guid=None, owner_id=None, tenant_id=None, project_id=None,
                 create_time=None, last_modify_time=None, life_cycle=None, is_visible=None, last_ddl_time=None,
                 last_access_time=None, env_type=None, data_size=None, comment=None, project_name=None, database_name=None,
                 partition_keys=None, location=None, cluster_id=None, caption=None):
        self.table_name = table_name    # type: str
        self.table_guid = table_guid    # type: str
        self.owner_id = owner_id        # type: str
        self.tenant_id = tenant_id      # type: int
        self.project_id = project_id    # type: int
        self.create_time = create_time  # type: int
        self.last_modify_time = last_modify_time  # type: int
        self.life_cycle = life_cycle    # type: int
        self.is_visible = is_visible    # type: int
        self.last_ddl_time = last_ddl_time  # type: int
        self.last_access_time = last_access_time  # type: int
        self.env_type = env_type        # type: int
        self.data_size = data_size      # type: int
        self.comment = comment          # type: str
        self.project_name = project_name  # type: str
        self.database_name = database_name  # type: str
        self.partition_keys = partition_keys  # type: str
        self.location = location        # type: str
        self.cluster_id = cluster_id    # type: str
        self.caption = caption          # type: str

    def validate(self):
        self.validate_required(self.table_name, 'table_name')
        self.validate_required(self.table_guid, 'table_guid')
        self.validate_required(self.owner_id, 'owner_id')
        self.validate_required(self.tenant_id, 'tenant_id')
        self.validate_required(self.project_id, 'project_id')
        self.validate_required(self.create_time, 'create_time')
        self.validate_required(self.last_modify_time, 'last_modify_time')
        self.validate_required(self.life_cycle, 'life_cycle')
        self.validate_required(self.is_visible, 'is_visible')
        self.validate_required(self.last_ddl_time, 'last_ddl_time')
        self.validate_required(self.last_access_time, 'last_access_time')
        self.validate_required(self.env_type, 'env_type')
        self.validate_required(self.data_size, 'data_size')
        self.validate_required(self.comment, 'comment')
        self.validate_required(self.project_name, 'project_name')
        self.validate_required(self.database_name, 'database_name')
        self.validate_required(self.partition_keys, 'partition_keys')
        self.validate_required(self.location, 'location')
        self.validate_required(self.cluster_id, 'cluster_id')
        self.validate_required(self.caption, 'caption')

    def to_map(self):
        result = {}
        result['TableName'] = self.table_name
        result['TableGuid'] = self.table_guid
        result['OwnerId'] = self.owner_id
        result['TenantId'] = self.tenant_id
        result['ProjectId'] = self.project_id
        result['CreateTime'] = self.create_time
        result['LastModifyTime'] = self.last_modify_time
        result['LifeCycle'] = self.life_cycle
        result['IsVisible'] = self.is_visible
        result['LastDdlTime'] = self.last_ddl_time
        result['LastAccessTime'] = self.last_access_time
        result['EnvType'] = self.env_type
        result['DataSize'] = self.data_size
        result['Comment'] = self.comment
        result['ProjectName'] = self.project_name
        result['DatabaseName'] = self.database_name
        result['PartitionKeys'] = self.partition_keys
        result['Location'] = self.location
        result['ClusterId'] = self.cluster_id
        result['Caption'] = self.caption
        return result

    def from_map(self, map={}):
        self.table_name = map.get('TableName')
        self.table_guid = map.get('TableGuid')
        self.owner_id = map.get('OwnerId')
        self.tenant_id = map.get('TenantId')
        self.project_id = map.get('ProjectId')
        self.create_time = map.get('CreateTime')
        self.last_modify_time = map.get('LastModifyTime')
        self.life_cycle = map.get('LifeCycle')
        self.is_visible = map.get('IsVisible')
        self.last_ddl_time = map.get('LastDdlTime')
        self.last_access_time = map.get('LastAccessTime')
        self.env_type = map.get('EnvType')
        self.data_size = map.get('DataSize')
        self.comment = map.get('Comment')
        self.project_name = map.get('ProjectName')
        self.database_name = map.get('DatabaseName')
        self.partition_keys = map.get('PartitionKeys')
        self.location = map.get('Location')
        self.cluster_id = map.get('ClusterId')
        self.caption = map.get('Caption')
        return self


class GetMetaTableColumnRequest(TeaModel):
    def __init__(self, table_guid=None, page_num=None, page_size=None, cluster_id=None, database_name=None,
                 table_name=None, data_source_type=None):
        self.table_guid = table_guid    # type: str
        self.page_num = page_num        # type: int
        self.page_size = page_size      # type: int
        self.cluster_id = cluster_id    # type: str
        self.database_name = database_name  # type: str
        self.table_name = table_name    # type: str
        self.data_source_type = data_source_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['TableGuid'] = self.table_guid
        result['PageNum'] = self.page_num
        result['PageSize'] = self.page_size
        result['ClusterId'] = self.cluster_id
        result['DatabaseName'] = self.database_name
        result['TableName'] = self.table_name
        result['DataSourceType'] = self.data_source_type
        return result

    def from_map(self, map={}):
        self.table_guid = map.get('TableGuid')
        self.page_num = map.get('PageNum')
        self.page_size = map.get('PageSize')
        self.cluster_id = map.get('ClusterId')
        self.database_name = map.get('DatabaseName')
        self.table_name = map.get('TableName')
        self.data_source_type = map.get('DataSourceType')
        return self


class GetMetaTableColumnResponse(TeaModel):
    def __init__(self, request_id=None, error_code=None, error_message=None, http_status_code=None, success=None,
                 data=None):
        self.request_id = request_id    # type: str
        self.error_code = error_code    # type: str
        self.error_message = error_message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.success = success          # type: bool
        self.data = data                # type: GetMetaTableColumnResponseData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.error_code, 'error_code')
        self.validate_required(self.error_message, 'error_message')
        self.validate_required(self.http_status_code, 'http_status_code')
        self.validate_required(self.success, 'success')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['ErrorCode'] = self.error_code
        result['ErrorMessage'] = self.error_message
        result['HttpStatusCode'] = self.http_status_code
        result['Success'] = self.success
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.error_code = map.get('ErrorCode')
        self.error_message = map.get('ErrorMessage')
        self.http_status_code = map.get('HttpStatusCode')
        self.success = map.get('Success')
        if map.get('Data') is not None:
            temp_model = GetMetaTableColumnResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class GetMetaTableColumnResponseDataColumnList(TeaModel):
    def __init__(self, column_name=None, column_guid=None, comment=None, is_primary_key=None, column_type=None,
                 is_partition_column=None, is_foreign_key=None, caption=None):
        self.column_name = column_name  # type: str
        self.column_guid = column_guid  # type: str
        self.comment = comment          # type: str
        self.is_primary_key = is_primary_key  # type: bool
        self.column_type = column_type  # type: str
        self.is_partition_column = is_partition_column  # type: bool
        self.is_foreign_key = is_foreign_key  # type: bool
        self.caption = caption          # type: str

    def validate(self):
        self.validate_required(self.column_name, 'column_name')
        self.validate_required(self.column_guid, 'column_guid')
        self.validate_required(self.comment, 'comment')
        self.validate_required(self.is_primary_key, 'is_primary_key')
        self.validate_required(self.column_type, 'column_type')
        self.validate_required(self.is_partition_column, 'is_partition_column')
        self.validate_required(self.is_foreign_key, 'is_foreign_key')
        self.validate_required(self.caption, 'caption')

    def to_map(self):
        result = {}
        result['ColumnName'] = self.column_name
        result['ColumnGuid'] = self.column_guid
        result['Comment'] = self.comment
        result['IsPrimaryKey'] = self.is_primary_key
        result['ColumnType'] = self.column_type
        result['IsPartitionColumn'] = self.is_partition_column
        result['IsForeignKey'] = self.is_foreign_key
        result['Caption'] = self.caption
        return result

    def from_map(self, map={}):
        self.column_name = map.get('ColumnName')
        self.column_guid = map.get('ColumnGuid')
        self.comment = map.get('Comment')
        self.is_primary_key = map.get('IsPrimaryKey')
        self.column_type = map.get('ColumnType')
        self.is_partition_column = map.get('IsPartitionColumn')
        self.is_foreign_key = map.get('IsForeignKey')
        self.caption = map.get('Caption')
        return self


class GetMetaTableColumnResponseData(TeaModel):
    def __init__(self, total_count=None, page_num=None, page_size=None, column_list=None):
        self.total_count = total_count  # type: int
        self.page_num = page_num        # type: int
        self.page_size = page_size      # type: int
        self.column_list = column_list  # type: List[GetMetaTableColumnResponseDataColumnList]

    def validate(self):
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.page_num, 'page_num')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.column_list, 'column_list')
        if self.column_list:
            for k in self.column_list:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['TotalCount'] = self.total_count
        result['PageNum'] = self.page_num
        result['PageSize'] = self.page_size
        result['ColumnList'] = []
        if self.column_list is not None:
            for k in self.column_list:
                result['ColumnList'].append(k.to_map() if k else None)
        else:
            result['ColumnList'] = None
        return result

    def from_map(self, map={}):
        self.total_count = map.get('TotalCount')
        self.page_num = map.get('PageNum')
        self.page_size = map.get('PageSize')
        self.column_list = []
        if map.get('ColumnList') is not None:
            for k in map.get('ColumnList'):
                temp_model = GetMetaTableColumnResponseDataColumnList()
                self.column_list.append(temp_model.from_map(k))
        else:
            self.column_list = None
        return self


class GetMetaDBInfoRequest(TeaModel):
    def __init__(self, app_guid=None, cluster_id=None, database_name=None, data_source_type=None):
        self.app_guid = app_guid        # type: str
        self.cluster_id = cluster_id    # type: str
        self.database_name = database_name  # type: str
        self.data_source_type = data_source_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['AppGuid'] = self.app_guid
        result['ClusterId'] = self.cluster_id
        result['DatabaseName'] = self.database_name
        result['DataSourceType'] = self.data_source_type
        return result

    def from_map(self, map={}):
        self.app_guid = map.get('AppGuid')
        self.cluster_id = map.get('ClusterId')
        self.database_name = map.get('DatabaseName')
        self.data_source_type = map.get('DataSourceType')
        return self


class GetMetaDBInfoResponse(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = request_id    # type: str
        self.data = data                # type: GetMetaDBInfoResponseData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('Data') is not None:
            temp_model = GetMetaDBInfoResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class GetMetaDBInfoResponseData(TeaModel):
    def __init__(self, app_guid=None, tenant_id=None, endpoint=None, project_id=None, env_type=None,
                 project_name=None, project_name_cn=None, create_time=None, modify_time=None, owner_id=None, owner_name=None,
                 name=None, type=None, comment=None, location=None, cluster_biz_id=None):
        self.app_guid = app_guid        # type: str
        self.tenant_id = tenant_id      # type: int
        self.endpoint = endpoint        # type: str
        self.project_id = project_id    # type: int
        self.env_type = env_type        # type: int
        self.project_name = project_name  # type: str
        self.project_name_cn = project_name_cn  # type: str
        self.create_time = create_time  # type: int
        self.modify_time = modify_time  # type: int
        self.owner_id = owner_id        # type: str
        self.owner_name = owner_name    # type: str
        self.name = name                # type: str
        self.type = type                # type: str
        self.comment = comment          # type: str
        self.location = location        # type: str
        self.cluster_biz_id = cluster_biz_id  # type: str

    def validate(self):
        self.validate_required(self.app_guid, 'app_guid')
        self.validate_required(self.tenant_id, 'tenant_id')
        self.validate_required(self.endpoint, 'endpoint')
        self.validate_required(self.project_id, 'project_id')
        self.validate_required(self.env_type, 'env_type')
        self.validate_required(self.project_name, 'project_name')
        self.validate_required(self.project_name_cn, 'project_name_cn')
        self.validate_required(self.create_time, 'create_time')
        self.validate_required(self.modify_time, 'modify_time')
        self.validate_required(self.owner_id, 'owner_id')
        self.validate_required(self.owner_name, 'owner_name')
        self.validate_required(self.name, 'name')
        self.validate_required(self.type, 'type')
        self.validate_required(self.comment, 'comment')
        self.validate_required(self.location, 'location')
        self.validate_required(self.cluster_biz_id, 'cluster_biz_id')

    def to_map(self):
        result = {}
        result['AppGuid'] = self.app_guid
        result['TenantId'] = self.tenant_id
        result['Endpoint'] = self.endpoint
        result['ProjectId'] = self.project_id
        result['EnvType'] = self.env_type
        result['ProjectName'] = self.project_name
        result['ProjectNameCn'] = self.project_name_cn
        result['CreateTime'] = self.create_time
        result['ModifyTime'] = self.modify_time
        result['OwnerId'] = self.owner_id
        result['OwnerName'] = self.owner_name
        result['Name'] = self.name
        result['Type'] = self.type
        result['Comment'] = self.comment
        result['Location'] = self.location
        result['ClusterBizId'] = self.cluster_biz_id
        return result

    def from_map(self, map={}):
        self.app_guid = map.get('AppGuid')
        self.tenant_id = map.get('TenantId')
        self.endpoint = map.get('Endpoint')
        self.project_id = map.get('ProjectId')
        self.env_type = map.get('EnvType')
        self.project_name = map.get('ProjectName')
        self.project_name_cn = map.get('ProjectNameCn')
        self.create_time = map.get('CreateTime')
        self.modify_time = map.get('ModifyTime')
        self.owner_id = map.get('OwnerId')
        self.owner_name = map.get('OwnerName')
        self.name = map.get('Name')
        self.type = map.get('Type')
        self.comment = map.get('Comment')
        self.location = map.get('Location')
        self.cluster_biz_id = map.get('ClusterBizId')
        return self


class GetMetaCategoryRequest(TeaModel):
    def __init__(self, parent_category_id=None, page_num=None, page_size=None):
        self.parent_category_id = parent_category_id  # type: int
        self.page_num = page_num        # type: int
        self.page_size = page_size      # type: int

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['ParentCategoryId'] = self.parent_category_id
        result['PageNum'] = self.page_num
        result['PageSize'] = self.page_size
        return result

    def from_map(self, map={}):
        self.parent_category_id = map.get('ParentCategoryId')
        self.page_num = map.get('PageNum')
        self.page_size = map.get('PageSize')
        return self


class GetMetaCategoryResponse(TeaModel):
    def __init__(self, request_id=None, error_code=None, error_message=None, http_status_code=None, success=None,
                 data=None):
        self.request_id = request_id    # type: str
        self.error_code = error_code    # type: str
        self.error_message = error_message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.success = success          # type: bool
        self.data = data                # type: GetMetaCategoryResponseData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.error_code, 'error_code')
        self.validate_required(self.error_message, 'error_message')
        self.validate_required(self.http_status_code, 'http_status_code')
        self.validate_required(self.success, 'success')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['ErrorCode'] = self.error_code
        result['ErrorMessage'] = self.error_message
        result['HttpStatusCode'] = self.http_status_code
        result['Success'] = self.success
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.error_code = map.get('ErrorCode')
        self.error_message = map.get('ErrorMessage')
        self.http_status_code = map.get('HttpStatusCode')
        self.success = map.get('Success')
        if map.get('Data') is not None:
            temp_model = GetMetaCategoryResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class GetMetaCategoryResponseDataDataEntityList(TeaModel):
    def __init__(self, category_id=None, name=None, create_time=None, modified_time=None, comment=None,
                 owner_id=None, last_operator_id=None, parent_category_id=None, depth=None):
        self.category_id = category_id  # type: int
        self.name = name                # type: str
        self.create_time = create_time  # type: int
        self.modified_time = modified_time  # type: int
        self.comment = comment          # type: str
        self.owner_id = owner_id        # type: str
        self.last_operator_id = last_operator_id  # type: str
        self.parent_category_id = parent_category_id  # type: int
        self.depth = depth              # type: int

    def validate(self):
        self.validate_required(self.category_id, 'category_id')
        self.validate_required(self.name, 'name')
        self.validate_required(self.create_time, 'create_time')
        self.validate_required(self.modified_time, 'modified_time')
        self.validate_required(self.comment, 'comment')
        self.validate_required(self.owner_id, 'owner_id')
        self.validate_required(self.last_operator_id, 'last_operator_id')
        self.validate_required(self.parent_category_id, 'parent_category_id')
        self.validate_required(self.depth, 'depth')

    def to_map(self):
        result = {}
        result['CategoryId'] = self.category_id
        result['Name'] = self.name
        result['CreateTime'] = self.create_time
        result['ModifiedTime'] = self.modified_time
        result['Comment'] = self.comment
        result['OwnerId'] = self.owner_id
        result['LastOperatorId'] = self.last_operator_id
        result['ParentCategoryId'] = self.parent_category_id
        result['Depth'] = self.depth
        return result

    def from_map(self, map={}):
        self.category_id = map.get('CategoryId')
        self.name = map.get('Name')
        self.create_time = map.get('CreateTime')
        self.modified_time = map.get('ModifiedTime')
        self.comment = map.get('Comment')
        self.owner_id = map.get('OwnerId')
        self.last_operator_id = map.get('LastOperatorId')
        self.parent_category_id = map.get('ParentCategoryId')
        self.depth = map.get('Depth')
        return self


class GetMetaCategoryResponseData(TeaModel):
    def __init__(self, page_num=None, page_size=None, total_count=None, data_entity_list=None):
        self.page_num = page_num        # type: int
        self.page_size = page_size      # type: int
        self.total_count = total_count  # type: int
        self.data_entity_list = data_entity_list  # type: List[GetMetaCategoryResponseDataDataEntityList]

    def validate(self):
        self.validate_required(self.page_num, 'page_num')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.data_entity_list, 'data_entity_list')
        if self.data_entity_list:
            for k in self.data_entity_list:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['PageNum'] = self.page_num
        result['PageSize'] = self.page_size
        result['TotalCount'] = self.total_count
        result['DataEntityList'] = []
        if self.data_entity_list is not None:
            for k in self.data_entity_list:
                result['DataEntityList'].append(k.to_map() if k else None)
        else:
            result['DataEntityList'] = None
        return result

    def from_map(self, map={}):
        self.page_num = map.get('PageNum')
        self.page_size = map.get('PageSize')
        self.total_count = map.get('TotalCount')
        self.data_entity_list = []
        if map.get('DataEntityList') is not None:
            for k in map.get('DataEntityList'):
                temp_model = GetMetaCategoryResponseDataDataEntityList()
                self.data_entity_list.append(temp_model.from_map(k))
        else:
            self.data_entity_list = None
        return self


class ListAlertMessagesRequest(TeaModel):
    def __init__(self, page_number=None, page_size=None, begin_time=None, end_time=None, remind_id=None,
                 alert_methods=None, alert_user=None, alert_rule_types=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size      # type: int
        self.begin_time = begin_time    # type: str
        self.end_time = end_time        # type: str
        self.remind_id = remind_id      # type: int
        self.alert_methods = alert_methods  # type: str
        self.alert_user = alert_user    # type: str
        self.alert_rule_types = alert_rule_types  # type: str

    def validate(self):
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.begin_time, 'begin_time')
        self.validate_required(self.end_time, 'end_time')

    def to_map(self):
        result = {}
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        result['BeginTime'] = self.begin_time
        result['EndTime'] = self.end_time
        result['RemindId'] = self.remind_id
        result['AlertMethods'] = self.alert_methods
        result['AlertUser'] = self.alert_user
        result['AlertRuleTypes'] = self.alert_rule_types
        return result

    def from_map(self, map={}):
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        self.begin_time = map.get('BeginTime')
        self.end_time = map.get('EndTime')
        self.remind_id = map.get('RemindId')
        self.alert_methods = map.get('AlertMethods')
        self.alert_user = map.get('AlertUser')
        self.alert_rule_types = map.get('AlertRuleTypes')
        return self


class ListAlertMessagesResponse(TeaModel):
    def __init__(self, success=None, error_code=None, error_message=None, http_status_code=None, request_id=None,
                 data=None):
        self.success = success          # type: bool
        self.error_code = error_code    # type: str
        self.error_message = error_message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.request_id = request_id    # type: str
        self.data = data                # type: ListAlertMessagesResponseData

    def validate(self):
        self.validate_required(self.success, 'success')
        self.validate_required(self.error_code, 'error_code')
        self.validate_required(self.error_message, 'error_message')
        self.validate_required(self.http_status_code, 'http_status_code')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['Success'] = self.success
        result['ErrorCode'] = self.error_code
        result['ErrorMessage'] = self.error_message
        result['HttpStatusCode'] = self.http_status_code
        result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.success = map.get('Success')
        self.error_code = map.get('ErrorCode')
        self.error_message = map.get('ErrorMessage')
        self.http_status_code = map.get('HttpStatusCode')
        self.request_id = map.get('RequestId')
        if map.get('Data') is not None:
            temp_model = ListAlertMessagesResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class ListAlertMessagesResponseDataAlertMessagesInstances(TeaModel):
    def __init__(self, node_id=None, node_name=None, project_id=None, status=None, instance_id=None):
        self.node_id = node_id          # type: int
        self.node_name = node_name      # type: str
        self.project_id = project_id    # type: int
        self.status = status            # type: str
        self.instance_id = instance_id  # type: int

    def validate(self):
        self.validate_required(self.node_id, 'node_id')
        self.validate_required(self.node_name, 'node_name')
        self.validate_required(self.project_id, 'project_id')
        self.validate_required(self.status, 'status')
        self.validate_required(self.instance_id, 'instance_id')

    def to_map(self):
        result = {}
        result['NodeId'] = self.node_id
        result['NodeName'] = self.node_name
        result['ProjectId'] = self.project_id
        result['Status'] = self.status
        result['InstanceId'] = self.instance_id
        return result

    def from_map(self, map={}):
        self.node_id = map.get('NodeId')
        self.node_name = map.get('NodeName')
        self.project_id = map.get('ProjectId')
        self.status = map.get('Status')
        self.instance_id = map.get('InstanceId')
        return self


class ListAlertMessagesResponseDataAlertMessagesTopics(TeaModel):
    def __init__(self, node_id=None, instance_id=None, topic_id=None, topic_name=None, topic_owner=None,
                 topic_status=None):
        self.node_id = node_id          # type: int
        self.instance_id = instance_id  # type: int
        self.topic_id = topic_id        # type: int
        self.topic_name = topic_name    # type: str
        self.topic_owner = topic_owner  # type: str
        self.topic_status = topic_status  # type: str

    def validate(self):
        self.validate_required(self.node_id, 'node_id')
        self.validate_required(self.instance_id, 'instance_id')
        self.validate_required(self.topic_id, 'topic_id')
        self.validate_required(self.topic_name, 'topic_name')
        self.validate_required(self.topic_owner, 'topic_owner')
        self.validate_required(self.topic_status, 'topic_status')

    def to_map(self):
        result = {}
        result['NodeId'] = self.node_id
        result['InstanceId'] = self.instance_id
        result['TopicId'] = self.topic_id
        result['TopicName'] = self.topic_name
        result['TopicOwner'] = self.topic_owner
        result['TopicStatus'] = self.topic_status
        return result

    def from_map(self, map={}):
        self.node_id = map.get('NodeId')
        self.instance_id = map.get('InstanceId')
        self.topic_id = map.get('TopicId')
        self.topic_name = map.get('TopicName')
        self.topic_owner = map.get('TopicOwner')
        self.topic_status = map.get('TopicStatus')
        return self


class ListAlertMessagesResponseDataAlertMessagesNodes(TeaModel):
    def __init__(self, node_id=None, node_name=None, owner=None, project_id=None):
        self.node_id = node_id          # type: int
        self.node_name = node_name      # type: str
        self.owner = owner              # type: str
        self.project_id = project_id    # type: int

    def validate(self):
        self.validate_required(self.node_id, 'node_id')
        self.validate_required(self.node_name, 'node_name')
        self.validate_required(self.owner, 'owner')
        self.validate_required(self.project_id, 'project_id')

    def to_map(self):
        result = {}
        result['NodeId'] = self.node_id
        result['NodeName'] = self.node_name
        result['Owner'] = self.owner
        result['ProjectId'] = self.project_id
        return result

    def from_map(self, map={}):
        self.node_id = map.get('NodeId')
        self.node_name = map.get('NodeName')
        self.owner = map.get('Owner')
        self.project_id = map.get('ProjectId')
        return self


class ListAlertMessagesResponseDataAlertMessagesSlaAlert(TeaModel):
    def __init__(self, baseline_id=None, baseline_name=None, baseline_owner=None, bizdate=None, in_group_id=None,
                 project_id=None, status=None):
        self.baseline_id = baseline_id  # type: int
        self.baseline_name = baseline_name  # type: str
        self.baseline_owner = baseline_owner  # type: str
        self.bizdate = bizdate          # type: int
        self.in_group_id = in_group_id  # type: int
        self.project_id = project_id    # type: int
        self.status = status            # type: str

    def validate(self):
        self.validate_required(self.baseline_id, 'baseline_id')
        self.validate_required(self.baseline_name, 'baseline_name')
        self.validate_required(self.baseline_owner, 'baseline_owner')
        self.validate_required(self.bizdate, 'bizdate')
        self.validate_required(self.in_group_id, 'in_group_id')
        self.validate_required(self.project_id, 'project_id')
        self.validate_required(self.status, 'status')

    def to_map(self):
        result = {}
        result['BaselineId'] = self.baseline_id
        result['BaselineName'] = self.baseline_name
        result['BaselineOwner'] = self.baseline_owner
        result['Bizdate'] = self.bizdate
        result['InGroupId'] = self.in_group_id
        result['ProjectId'] = self.project_id
        result['Status'] = self.status
        return result

    def from_map(self, map={}):
        self.baseline_id = map.get('BaselineId')
        self.baseline_name = map.get('BaselineName')
        self.baseline_owner = map.get('BaselineOwner')
        self.bizdate = map.get('Bizdate')
        self.in_group_id = map.get('InGroupId')
        self.project_id = map.get('ProjectId')
        self.status = map.get('Status')
        return self


class ListAlertMessagesResponseDataAlertMessages(TeaModel):
    def __init__(self, alert_id=None, alert_time=None, source=None, remind_id=None, remind_name=None,
                 alert_user=None, alert_method=None, alert_message_status=None, content=None, instances=None, topics=None,
                 nodes=None, sla_alert=None):
        self.alert_id = alert_id        # type: int
        self.alert_time = alert_time    # type: int
        self.source = source            # type: str
        self.remind_id = remind_id      # type: int
        self.remind_name = remind_name  # type: str
        self.alert_user = alert_user    # type: str
        self.alert_method = alert_method  # type: str
        self.alert_message_status = alert_message_status  # type: str
        self.content = content          # type: str
        self.instances = instances      # type: List[ListAlertMessagesResponseDataAlertMessagesInstances]
        self.topics = topics            # type: List[ListAlertMessagesResponseDataAlertMessagesTopics]
        self.nodes = nodes              # type: List[ListAlertMessagesResponseDataAlertMessagesNodes]
        self.sla_alert = sla_alert      # type: ListAlertMessagesResponseDataAlertMessagesSlaAlert

    def validate(self):
        self.validate_required(self.alert_id, 'alert_id')
        self.validate_required(self.alert_time, 'alert_time')
        self.validate_required(self.source, 'source')
        self.validate_required(self.remind_id, 'remind_id')
        self.validate_required(self.remind_name, 'remind_name')
        self.validate_required(self.alert_user, 'alert_user')
        self.validate_required(self.alert_method, 'alert_method')
        self.validate_required(self.alert_message_status, 'alert_message_status')
        self.validate_required(self.content, 'content')
        self.validate_required(self.instances, 'instances')
        if self.instances:
            for k in self.instances:
                if k:
                    k.validate()
        self.validate_required(self.topics, 'topics')
        if self.topics:
            for k in self.topics:
                if k:
                    k.validate()
        self.validate_required(self.nodes, 'nodes')
        if self.nodes:
            for k in self.nodes:
                if k:
                    k.validate()
        self.validate_required(self.sla_alert, 'sla_alert')
        if self.sla_alert:
            self.sla_alert.validate()

    def to_map(self):
        result = {}
        result['AlertId'] = self.alert_id
        result['AlertTime'] = self.alert_time
        result['Source'] = self.source
        result['RemindId'] = self.remind_id
        result['RemindName'] = self.remind_name
        result['AlertUser'] = self.alert_user
        result['AlertMethod'] = self.alert_method
        result['AlertMessageStatus'] = self.alert_message_status
        result['Content'] = self.content
        result['Instances'] = []
        if self.instances is not None:
            for k in self.instances:
                result['Instances'].append(k.to_map() if k else None)
        else:
            result['Instances'] = None
        result['Topics'] = []
        if self.topics is not None:
            for k in self.topics:
                result['Topics'].append(k.to_map() if k else None)
        else:
            result['Topics'] = None
        result['Nodes'] = []
        if self.nodes is not None:
            for k in self.nodes:
                result['Nodes'].append(k.to_map() if k else None)
        else:
            result['Nodes'] = None
        if self.sla_alert is not None:
            result['SlaAlert'] = self.sla_alert.to_map()
        else:
            result['SlaAlert'] = None
        return result

    def from_map(self, map={}):
        self.alert_id = map.get('AlertId')
        self.alert_time = map.get('AlertTime')
        self.source = map.get('Source')
        self.remind_id = map.get('RemindId')
        self.remind_name = map.get('RemindName')
        self.alert_user = map.get('AlertUser')
        self.alert_method = map.get('AlertMethod')
        self.alert_message_status = map.get('AlertMessageStatus')
        self.content = map.get('Content')
        self.instances = []
        if map.get('Instances') is not None:
            for k in map.get('Instances'):
                temp_model = ListAlertMessagesResponseDataAlertMessagesInstances()
                self.instances.append(temp_model.from_map(k))
        else:
            self.instances = None
        self.topics = []
        if map.get('Topics') is not None:
            for k in map.get('Topics'):
                temp_model = ListAlertMessagesResponseDataAlertMessagesTopics()
                self.topics.append(temp_model.from_map(k))
        else:
            self.topics = None
        self.nodes = []
        if map.get('Nodes') is not None:
            for k in map.get('Nodes'):
                temp_model = ListAlertMessagesResponseDataAlertMessagesNodes()
                self.nodes.append(temp_model.from_map(k))
        else:
            self.nodes = None
        if map.get('SlaAlert') is not None:
            temp_model = ListAlertMessagesResponseDataAlertMessagesSlaAlert()
            self.sla_alert = temp_model.from_map(map['SlaAlert'])
        else:
            self.sla_alert = None
        return self


class ListAlertMessagesResponseData(TeaModel):
    def __init__(self, page_number=None, page_size=None, total_count=None, alert_messages=None):
        self.page_number = page_number  # type: str
        self.page_size = page_size      # type: str
        self.total_count = total_count  # type: str
        self.alert_messages = alert_messages  # type: List[ListAlertMessagesResponseDataAlertMessages]

    def validate(self):
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.alert_messages, 'alert_messages')
        if self.alert_messages:
            for k in self.alert_messages:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        result['TotalCount'] = self.total_count
        result['AlertMessages'] = []
        if self.alert_messages is not None:
            for k in self.alert_messages:
                result['AlertMessages'].append(k.to_map() if k else None)
        else:
            result['AlertMessages'] = None
        return result

    def from_map(self, map={}):
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        self.total_count = map.get('TotalCount')
        self.alert_messages = []
        if map.get('AlertMessages') is not None:
            for k in map.get('AlertMessages'):
                temp_model = ListAlertMessagesResponseDataAlertMessages()
                self.alert_messages.append(temp_model.from_map(k))
        else:
            self.alert_messages = None
        return self


class GetBaselineConfigRequest(TeaModel):
    def __init__(self, baseline_id=None):
        self.baseline_id = baseline_id  # type: int

    def validate(self):
        self.validate_required(self.baseline_id, 'baseline_id')

    def to_map(self):
        result = {}
        result['BaselineId'] = self.baseline_id
        return result

    def from_map(self, map={}):
        self.baseline_id = map.get('BaselineId')
        return self


class GetBaselineConfigResponse(TeaModel):
    def __init__(self, success=None, error_code=None, error_message=None, http_status_code=None, request_id=None,
                 data=None):
        self.success = success          # type: bool
        self.error_code = error_code    # type: str
        self.error_message = error_message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.request_id = request_id    # type: str
        self.data = data                # type: GetBaselineConfigResponseData

    def validate(self):
        self.validate_required(self.success, 'success')
        self.validate_required(self.error_code, 'error_code')
        self.validate_required(self.error_message, 'error_message')
        self.validate_required(self.http_status_code, 'http_status_code')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['Success'] = self.success
        result['ErrorCode'] = self.error_code
        result['ErrorMessage'] = self.error_message
        result['HttpStatusCode'] = self.http_status_code
        result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.success = map.get('Success')
        self.error_code = map.get('ErrorCode')
        self.error_message = map.get('ErrorMessage')
        self.http_status_code = map.get('HttpStatusCode')
        self.request_id = map.get('RequestId')
        if map.get('Data') is not None:
            temp_model = GetBaselineConfigResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class GetBaselineConfigResponseData(TeaModel):
    def __init__(self, baseline_id=None, priority=None, baseline_name=None, owner=None, project_id=None,
                 use_flag=None, baseline_type=None, exp_hour=None, exp_minu=None, sla_hour=None, sla_minu=None,
                 hour_exp_detail=None, hour_sla_detail=None, is_default=None):
        self.baseline_id = baseline_id  # type: int
        self.priority = priority        # type: int
        self.baseline_name = baseline_name  # type: str
        self.owner = owner              # type: str
        self.project_id = project_id    # type: int
        self.use_flag = use_flag        # type: bool
        self.baseline_type = baseline_type  # type: str
        self.exp_hour = exp_hour        # type: int
        self.exp_minu = exp_minu        # type: int
        self.sla_hour = sla_hour        # type: int
        self.sla_minu = sla_minu        # type: int
        self.hour_exp_detail = hour_exp_detail  # type: str
        self.hour_sla_detail = hour_sla_detail  # type: str
        self.is_default = is_default    # type: bool

    def validate(self):
        self.validate_required(self.baseline_id, 'baseline_id')
        self.validate_required(self.priority, 'priority')
        self.validate_required(self.baseline_name, 'baseline_name')
        self.validate_required(self.owner, 'owner')
        self.validate_required(self.project_id, 'project_id')
        self.validate_required(self.use_flag, 'use_flag')
        self.validate_required(self.baseline_type, 'baseline_type')
        self.validate_required(self.exp_hour, 'exp_hour')
        self.validate_required(self.exp_minu, 'exp_minu')
        self.validate_required(self.sla_hour, 'sla_hour')
        self.validate_required(self.sla_minu, 'sla_minu')
        self.validate_required(self.hour_exp_detail, 'hour_exp_detail')
        self.validate_required(self.hour_sla_detail, 'hour_sla_detail')
        self.validate_required(self.is_default, 'is_default')

    def to_map(self):
        result = {}
        result['BaselineId'] = self.baseline_id
        result['Priority'] = self.priority
        result['BaselineName'] = self.baseline_name
        result['Owner'] = self.owner
        result['ProjectId'] = self.project_id
        result['UseFlag'] = self.use_flag
        result['BaselineType'] = self.baseline_type
        result['ExpHour'] = self.exp_hour
        result['ExpMinu'] = self.exp_minu
        result['SlaHour'] = self.sla_hour
        result['SlaMinu'] = self.sla_minu
        result['HourExpDetail'] = self.hour_exp_detail
        result['HourSlaDetail'] = self.hour_sla_detail
        result['IsDefault'] = self.is_default
        return result

    def from_map(self, map={}):
        self.baseline_id = map.get('BaselineId')
        self.priority = map.get('Priority')
        self.baseline_name = map.get('BaselineName')
        self.owner = map.get('Owner')
        self.project_id = map.get('ProjectId')
        self.use_flag = map.get('UseFlag')
        self.baseline_type = map.get('BaselineType')
        self.exp_hour = map.get('ExpHour')
        self.exp_minu = map.get('ExpMinu')
        self.sla_hour = map.get('SlaHour')
        self.sla_minu = map.get('SlaMinu')
        self.hour_exp_detail = map.get('HourExpDetail')
        self.hour_sla_detail = map.get('HourSlaDetail')
        self.is_default = map.get('IsDefault')
        return self


class SearchMetaTablesRequest(TeaModel):
    def __init__(self, page_number=None, page_size=None, app_guid=None, keyword=None, entity_type=None,
                 cluster_id=None, data_source_type=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size      # type: int
        self.app_guid = app_guid        # type: str
        self.keyword = keyword          # type: str
        self.entity_type = entity_type  # type: int
        self.cluster_id = cluster_id    # type: str
        self.data_source_type = data_source_type  # type: str

    def validate(self):
        self.validate_required(self.keyword, 'keyword')

    def to_map(self):
        result = {}
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        result['AppGuid'] = self.app_guid
        result['Keyword'] = self.keyword
        result['EntityType'] = self.entity_type
        result['ClusterId'] = self.cluster_id
        result['DataSourceType'] = self.data_source_type
        return result

    def from_map(self, map={}):
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        self.app_guid = map.get('AppGuid')
        self.keyword = map.get('Keyword')
        self.entity_type = map.get('EntityType')
        self.cluster_id = map.get('ClusterId')
        self.data_source_type = map.get('DataSourceType')
        return self


class SearchMetaTablesResponse(TeaModel):
    def __init__(self, request_id=None, error_code=None, error_message=None, http_status_code=None, success=None,
                 data=None):
        self.request_id = request_id    # type: str
        self.error_code = error_code    # type: str
        self.error_message = error_message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.success = success          # type: bool
        self.data = data                # type: SearchMetaTablesResponseData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.error_code, 'error_code')
        self.validate_required(self.error_message, 'error_message')
        self.validate_required(self.http_status_code, 'http_status_code')
        self.validate_required(self.success, 'success')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['ErrorCode'] = self.error_code
        result['ErrorMessage'] = self.error_message
        result['HttpStatusCode'] = self.http_status_code
        result['Success'] = self.success
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.error_code = map.get('ErrorCode')
        self.error_message = map.get('ErrorMessage')
        self.http_status_code = map.get('HttpStatusCode')
        self.success = map.get('Success')
        if map.get('Data') is not None:
            temp_model = SearchMetaTablesResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class SearchMetaTablesResponseDataDataEntityList(TeaModel):
    def __init__(self, table_name=None, table_guid=None, owner_id=None, tenant_id=None, env_type=None,
                 entity_type=None, project_id=None, project_name=None, cluster_id=None, database_name=None):
        self.table_name = table_name    # type: str
        self.table_guid = table_guid    # type: str
        self.owner_id = owner_id        # type: str
        self.tenant_id = tenant_id      # type: int
        self.env_type = env_type        # type: int
        self.entity_type = entity_type  # type: int
        self.project_id = project_id    # type: int
        self.project_name = project_name  # type: str
        self.cluster_id = cluster_id    # type: str
        self.database_name = database_name  # type: str

    def validate(self):
        self.validate_required(self.table_name, 'table_name')
        self.validate_required(self.table_guid, 'table_guid')
        self.validate_required(self.owner_id, 'owner_id')
        self.validate_required(self.tenant_id, 'tenant_id')
        self.validate_required(self.env_type, 'env_type')
        self.validate_required(self.entity_type, 'entity_type')
        self.validate_required(self.project_id, 'project_id')
        self.validate_required(self.project_name, 'project_name')
        self.validate_required(self.cluster_id, 'cluster_id')
        self.validate_required(self.database_name, 'database_name')

    def to_map(self):
        result = {}
        result['TableName'] = self.table_name
        result['TableGuid'] = self.table_guid
        result['OwnerId'] = self.owner_id
        result['TenantId'] = self.tenant_id
        result['EnvType'] = self.env_type
        result['EntityType'] = self.entity_type
        result['ProjectId'] = self.project_id
        result['ProjectName'] = self.project_name
        result['ClusterId'] = self.cluster_id
        result['DatabaseName'] = self.database_name
        return result

    def from_map(self, map={}):
        self.table_name = map.get('TableName')
        self.table_guid = map.get('TableGuid')
        self.owner_id = map.get('OwnerId')
        self.tenant_id = map.get('TenantId')
        self.env_type = map.get('EnvType')
        self.entity_type = map.get('EntityType')
        self.project_id = map.get('ProjectId')
        self.project_name = map.get('ProjectName')
        self.cluster_id = map.get('ClusterId')
        self.database_name = map.get('DatabaseName')
        return self


class SearchMetaTablesResponseData(TeaModel):
    def __init__(self, page_number=None, page_size=None, total_count=None, data_entity_list=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size      # type: int
        self.total_count = total_count  # type: int
        self.data_entity_list = data_entity_list  # type: List[SearchMetaTablesResponseDataDataEntityList]

    def validate(self):
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.data_entity_list, 'data_entity_list')
        if self.data_entity_list:
            for k in self.data_entity_list:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        result['TotalCount'] = self.total_count
        result['DataEntityList'] = []
        if self.data_entity_list is not None:
            for k in self.data_entity_list:
                result['DataEntityList'].append(k.to_map() if k else None)
        else:
            result['DataEntityList'] = None
        return result

    def from_map(self, map={}):
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        self.total_count = map.get('TotalCount')
        self.data_entity_list = []
        if map.get('DataEntityList') is not None:
            for k in map.get('DataEntityList'):
                temp_model = SearchMetaTablesResponseDataDataEntityList()
                self.data_entity_list.append(temp_model.from_map(k))
        else:
            self.data_entity_list = None
        return self


class GetMetaTableListByCategoryRequest(TeaModel):
    def __init__(self, page_number=None, page_size=None, category_id=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size      # type: int
        self.category_id = category_id  # type: int

    def validate(self):
        self.validate_required(self.category_id, 'category_id')

    def to_map(self):
        result = {}
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        result['CategoryId'] = self.category_id
        return result

    def from_map(self, map={}):
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        self.category_id = map.get('CategoryId')
        return self


class GetMetaTableListByCategoryResponse(TeaModel):
    def __init__(self, request_id=None, error_code=None, error_message=None, http_status_code=None, success=None,
                 data=None):
        self.request_id = request_id    # type: str
        self.error_code = error_code    # type: str
        self.error_message = error_message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.success = success          # type: bool
        self.data = data                # type: GetMetaTableListByCategoryResponseData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.error_code, 'error_code')
        self.validate_required(self.error_message, 'error_message')
        self.validate_required(self.http_status_code, 'http_status_code')
        self.validate_required(self.success, 'success')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['ErrorCode'] = self.error_code
        result['ErrorMessage'] = self.error_message
        result['HttpStatusCode'] = self.http_status_code
        result['Success'] = self.success
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.error_code = map.get('ErrorCode')
        self.error_message = map.get('ErrorMessage')
        self.http_status_code = map.get('HttpStatusCode')
        self.success = map.get('Success')
        if map.get('Data') is not None:
            temp_model = GetMetaTableListByCategoryResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class GetMetaTableListByCategoryResponseData(TeaModel):
    def __init__(self, page_number=None, page_size=None, total_count=None, table_guid_list=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size      # type: int
        self.total_count = total_count  # type: int
        self.table_guid_list = table_guid_list  # type: List[str]

    def validate(self):
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.table_guid_list, 'table_guid_list')

    def to_map(self):
        result = {}
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        result['TotalCount'] = self.total_count
        result['TableGuidList'] = self.table_guid_list
        return result

    def from_map(self, map={}):
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        self.total_count = map.get('TotalCount')
        self.table_guid_list = map.get('TableGuidList')
        return self


class DeleteMetaCategoryRequest(TeaModel):
    def __init__(self, category_id=None):
        self.category_id = category_id  # type: int

    def validate(self):
        self.validate_required(self.category_id, 'category_id')

    def to_map(self):
        result = {}
        result['CategoryId'] = self.category_id
        return result

    def from_map(self, map={}):
        self.category_id = map.get('CategoryId')
        return self


class DeleteMetaCategoryResponse(TeaModel):
    def __init__(self, request_id=None, error_code=None, error_message=None, http_status_code=None, success=None,
                 data=None):
        self.request_id = request_id    # type: str
        self.error_code = error_code    # type: str
        self.error_message = error_message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.success = success          # type: bool
        self.data = data                # type: bool

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.error_code, 'error_code')
        self.validate_required(self.error_message, 'error_message')
        self.validate_required(self.http_status_code, 'http_status_code')
        self.validate_required(self.success, 'success')
        self.validate_required(self.data, 'data')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['ErrorCode'] = self.error_code
        result['ErrorMessage'] = self.error_message
        result['HttpStatusCode'] = self.http_status_code
        result['Success'] = self.success
        result['Data'] = self.data
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.error_code = map.get('ErrorCode')
        self.error_message = map.get('ErrorMessage')
        self.http_status_code = map.get('HttpStatusCode')
        self.success = map.get('Success')
        self.data = map.get('Data')
        return self


class UpdateMetaCategoryRequest(TeaModel):
    def __init__(self, name=None, comment=None, category_id=None):
        self.name = name                # type: str
        self.comment = comment          # type: str
        self.category_id = category_id  # type: int

    def validate(self):
        self.validate_required(self.category_id, 'category_id')

    def to_map(self):
        result = {}
        result['Name'] = self.name
        result['Comment'] = self.comment
        result['CategoryId'] = self.category_id
        return result

    def from_map(self, map={}):
        self.name = map.get('Name')
        self.comment = map.get('Comment')
        self.category_id = map.get('CategoryId')
        return self


class UpdateMetaCategoryResponse(TeaModel):
    def __init__(self, request_id=None, error_code=None, error_message=None, http_status_code=None, success=None,
                 data=None):
        self.request_id = request_id    # type: str
        self.error_code = error_code    # type: str
        self.error_message = error_message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.success = success          # type: bool
        self.data = data                # type: bool

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.error_code, 'error_code')
        self.validate_required(self.error_message, 'error_message')
        self.validate_required(self.http_status_code, 'http_status_code')
        self.validate_required(self.success, 'success')
        self.validate_required(self.data, 'data')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['ErrorCode'] = self.error_code
        result['ErrorMessage'] = self.error_message
        result['HttpStatusCode'] = self.http_status_code
        result['Success'] = self.success
        result['Data'] = self.data
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.error_code = map.get('ErrorCode')
        self.error_message = map.get('ErrorMessage')
        self.http_status_code = map.get('HttpStatusCode')
        self.success = map.get('Success')
        self.data = map.get('Data')
        return self


class ListTopicsRequest(TeaModel):
    def __init__(self, begin_time=None, end_time=None, topic_types=None, topic_statuses=None, node_id=None,
                 instance_id=None, owner=None, page_number=None, page_size=None):
        self.begin_time = begin_time    # type: str
        self.end_time = end_time        # type: str
        self.topic_types = topic_types  # type: str
        self.topic_statuses = topic_statuses  # type: str
        self.node_id = node_id          # type: int
        self.instance_id = instance_id  # type: int
        self.owner = owner              # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size      # type: int

    def validate(self):
        self.validate_required(self.begin_time, 'begin_time')
        self.validate_required(self.end_time, 'end_time')
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_size, 'page_size')

    def to_map(self):
        result = {}
        result['BeginTime'] = self.begin_time
        result['EndTime'] = self.end_time
        result['TopicTypes'] = self.topic_types
        result['TopicStatuses'] = self.topic_statuses
        result['NodeId'] = self.node_id
        result['InstanceId'] = self.instance_id
        result['Owner'] = self.owner
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        return result

    def from_map(self, map={}):
        self.begin_time = map.get('BeginTime')
        self.end_time = map.get('EndTime')
        self.topic_types = map.get('TopicTypes')
        self.topic_statuses = map.get('TopicStatuses')
        self.node_id = map.get('NodeId')
        self.instance_id = map.get('InstanceId')
        self.owner = map.get('Owner')
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        return self


class ListTopicsResponse(TeaModel):
    def __init__(self, success=None, error_code=None, error_message=None, http_status_code=None, request_id=None,
                 data=None):
        self.success = success          # type: bool
        self.error_code = error_code    # type: str
        self.error_message = error_message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.request_id = request_id    # type: str
        self.data = data                # type: ListTopicsResponseData

    def validate(self):
        self.validate_required(self.success, 'success')
        self.validate_required(self.error_code, 'error_code')
        self.validate_required(self.error_message, 'error_message')
        self.validate_required(self.http_status_code, 'http_status_code')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['Success'] = self.success
        result['ErrorCode'] = self.error_code
        result['ErrorMessage'] = self.error_message
        result['HttpStatusCode'] = self.http_status_code
        result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.success = map.get('Success')
        self.error_code = map.get('ErrorCode')
        self.error_message = map.get('ErrorMessage')
        self.http_status_code = map.get('HttpStatusCode')
        self.request_id = map.get('RequestId')
        if map.get('Data') is not None:
            temp_model = ListTopicsResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class ListTopicsResponseDataTopics(TeaModel):
    def __init__(self, topic_id=None, topic_name=None, topic_status=None, topic_type=None, add_time=None,
                 happen_time=None, fix_time=None, instance_id=None, node_id=None, node_name=None, node_owner=None,
                 project_id=None):
        self.topic_id = topic_id        # type: int
        self.topic_name = topic_name    # type: str
        self.topic_status = topic_status  # type: str
        self.topic_type = topic_type    # type: str
        self.add_time = add_time        # type: int
        self.happen_time = happen_time  # type: int
        self.fix_time = fix_time        # type: int
        self.instance_id = instance_id  # type: int
        self.node_id = node_id          # type: int
        self.node_name = node_name      # type: str
        self.node_owner = node_owner    # type: str
        self.project_id = project_id    # type: int

    def validate(self):
        self.validate_required(self.topic_id, 'topic_id')
        self.validate_required(self.topic_name, 'topic_name')
        self.validate_required(self.topic_status, 'topic_status')
        self.validate_required(self.topic_type, 'topic_type')
        self.validate_required(self.add_time, 'add_time')
        self.validate_required(self.happen_time, 'happen_time')
        self.validate_required(self.fix_time, 'fix_time')
        self.validate_required(self.instance_id, 'instance_id')
        self.validate_required(self.node_id, 'node_id')
        self.validate_required(self.node_name, 'node_name')
        self.validate_required(self.node_owner, 'node_owner')
        self.validate_required(self.project_id, 'project_id')

    def to_map(self):
        result = {}
        result['TopicId'] = self.topic_id
        result['TopicName'] = self.topic_name
        result['TopicStatus'] = self.topic_status
        result['TopicType'] = self.topic_type
        result['AddTime'] = self.add_time
        result['HappenTime'] = self.happen_time
        result['FixTime'] = self.fix_time
        result['InstanceId'] = self.instance_id
        result['NodeId'] = self.node_id
        result['NodeName'] = self.node_name
        result['NodeOwner'] = self.node_owner
        result['ProjectId'] = self.project_id
        return result

    def from_map(self, map={}):
        self.topic_id = map.get('TopicId')
        self.topic_name = map.get('TopicName')
        self.topic_status = map.get('TopicStatus')
        self.topic_type = map.get('TopicType')
        self.add_time = map.get('AddTime')
        self.happen_time = map.get('HappenTime')
        self.fix_time = map.get('FixTime')
        self.instance_id = map.get('InstanceId')
        self.node_id = map.get('NodeId')
        self.node_name = map.get('NodeName')
        self.node_owner = map.get('NodeOwner')
        self.project_id = map.get('ProjectId')
        return self


class ListTopicsResponseData(TeaModel):
    def __init__(self, page_number=None, page_size=None, total_count=None, topics=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size      # type: int
        self.total_count = total_count  # type: int
        self.topics = topics            # type: List[ListTopicsResponseDataTopics]

    def validate(self):
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.topics, 'topics')
        if self.topics:
            for k in self.topics:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        result['TotalCount'] = self.total_count
        result['Topics'] = []
        if self.topics is not None:
            for k in self.topics:
                result['Topics'].append(k.to_map() if k else None)
        else:
            result['Topics'] = None
        return result

    def from_map(self, map={}):
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        self.total_count = map.get('TotalCount')
        self.topics = []
        if map.get('Topics') is not None:
            for k in map.get('Topics'):
                temp_model = ListTopicsResponseDataTopics()
                self.topics.append(temp_model.from_map(k))
        else:
            self.topics = None
        return self


class ListFileVersionsRequest(TeaModel):
    def __init__(self, file_id=None, project_id=None, project_identifier=None, page_number=None, page_size=None):
        self.file_id = file_id          # type: int
        self.project_id = project_id    # type: int
        self.project_identifier = project_identifier  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size      # type: int

    def validate(self):
        self.validate_required(self.file_id, 'file_id')

    def to_map(self):
        result = {}
        result['FileId'] = self.file_id
        result['ProjectId'] = self.project_id
        result['ProjectIdentifier'] = self.project_identifier
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        return result

    def from_map(self, map={}):
        self.file_id = map.get('FileId')
        self.project_id = map.get('ProjectId')
        self.project_identifier = map.get('ProjectIdentifier')
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        return self


class ListFileVersionsResponse(TeaModel):
    def __init__(self, request_id=None, success=None, error_code=None, error_message=None, http_status_code=None,
                 data=None):
        self.request_id = request_id    # type: str
        self.success = success          # type: bool
        self.error_code = error_code    # type: str
        self.error_message = error_message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.data = data                # type: ListFileVersionsResponseData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.success, 'success')
        self.validate_required(self.error_code, 'error_code')
        self.validate_required(self.error_message, 'error_message')
        self.validate_required(self.http_status_code, 'http_status_code')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Success'] = self.success
        result['ErrorCode'] = self.error_code
        result['ErrorMessage'] = self.error_message
        result['HttpStatusCode'] = self.http_status_code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.success = map.get('Success')
        self.error_code = map.get('ErrorCode')
        self.error_message = map.get('ErrorMessage')
        self.http_status_code = map.get('HttpStatusCode')
        if map.get('Data') is not None:
            temp_model = ListFileVersionsResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class ListFileVersionsResponseDataFileVersions(TeaModel):
    def __init__(self, file_version=None, file_content=None, commit_time=None, commit_user=None, file_name=None,
                 status=None, change_type=None, is_current_prod=None, node_id=None, comment=None, node_content=None,
                 file_property_content=None, use_type=None):
        self.file_version = file_version  # type: int
        self.file_content = file_content  # type: str
        self.commit_time = commit_time  # type: int
        self.commit_user = commit_user  # type: str
        self.file_name = file_name      # type: str
        self.status = status            # type: str
        self.change_type = change_type  # type: str
        self.is_current_prod = is_current_prod  # type: bool
        self.node_id = node_id          # type: int
        self.comment = comment          # type: str
        self.node_content = node_content  # type: str
        self.file_property_content = file_property_content  # type: str
        self.use_type = use_type        # type: str

    def validate(self):
        self.validate_required(self.file_version, 'file_version')
        self.validate_required(self.file_content, 'file_content')
        self.validate_required(self.commit_time, 'commit_time')
        self.validate_required(self.commit_user, 'commit_user')
        self.validate_required(self.file_name, 'file_name')
        self.validate_required(self.status, 'status')
        self.validate_required(self.change_type, 'change_type')
        self.validate_required(self.is_current_prod, 'is_current_prod')
        self.validate_required(self.node_id, 'node_id')
        self.validate_required(self.comment, 'comment')
        self.validate_required(self.node_content, 'node_content')
        self.validate_required(self.file_property_content, 'file_property_content')
        self.validate_required(self.use_type, 'use_type')

    def to_map(self):
        result = {}
        result['FileVersion'] = self.file_version
        result['FileContent'] = self.file_content
        result['CommitTime'] = self.commit_time
        result['CommitUser'] = self.commit_user
        result['FileName'] = self.file_name
        result['Status'] = self.status
        result['ChangeType'] = self.change_type
        result['IsCurrentProd'] = self.is_current_prod
        result['NodeId'] = self.node_id
        result['Comment'] = self.comment
        result['NodeContent'] = self.node_content
        result['FilePropertyContent'] = self.file_property_content
        result['UseType'] = self.use_type
        return result

    def from_map(self, map={}):
        self.file_version = map.get('FileVersion')
        self.file_content = map.get('FileContent')
        self.commit_time = map.get('CommitTime')
        self.commit_user = map.get('CommitUser')
        self.file_name = map.get('FileName')
        self.status = map.get('Status')
        self.change_type = map.get('ChangeType')
        self.is_current_prod = map.get('IsCurrentProd')
        self.node_id = map.get('NodeId')
        self.comment = map.get('Comment')
        self.node_content = map.get('NodeContent')
        self.file_property_content = map.get('FilePropertyContent')
        self.use_type = map.get('UseType')
        return self


class ListFileVersionsResponseData(TeaModel):
    def __init__(self, page_number=None, page_size=None, total_count=None, file_versions=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size      # type: int
        self.total_count = total_count  # type: int
        self.file_versions = file_versions  # type: List[ListFileVersionsResponseDataFileVersions]

    def validate(self):
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.file_versions, 'file_versions')
        if self.file_versions:
            for k in self.file_versions:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        result['TotalCount'] = self.total_count
        result['FileVersions'] = []
        if self.file_versions is not None:
            for k in self.file_versions:
                result['FileVersions'].append(k.to_map() if k else None)
        else:
            result['FileVersions'] = None
        return result

    def from_map(self, map={}):
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        self.total_count = map.get('TotalCount')
        self.file_versions = []
        if map.get('FileVersions') is not None:
            for k in map.get('FileVersions'):
                temp_model = ListFileVersionsResponseDataFileVersions()
                self.file_versions.append(temp_model.from_map(k))
        else:
            self.file_versions = None
        return self


class CreateMetaCategoryRequest(TeaModel):
    def __init__(self, name=None, comment=None, parent_id=None):
        self.name = name                # type: str
        self.comment = comment          # type: str
        self.parent_id = parent_id      # type: int

    def validate(self):
        self.validate_required(self.name, 'name')

    def to_map(self):
        result = {}
        result['Name'] = self.name
        result['Comment'] = self.comment
        result['ParentId'] = self.parent_id
        return result

    def from_map(self, map={}):
        self.name = map.get('Name')
        self.comment = map.get('Comment')
        self.parent_id = map.get('ParentId')
        return self


class CreateMetaCategoryResponse(TeaModel):
    def __init__(self, request_id=None, error_code=None, error_message=None, http_status_code=None, success=None,
                 data=None):
        self.request_id = request_id    # type: str
        self.error_code = error_code    # type: str
        self.error_message = error_message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.success = success          # type: bool
        self.data = data                # type: CreateMetaCategoryResponseData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.error_code, 'error_code')
        self.validate_required(self.error_message, 'error_message')
        self.validate_required(self.http_status_code, 'http_status_code')
        self.validate_required(self.success, 'success')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['ErrorCode'] = self.error_code
        result['ErrorMessage'] = self.error_message
        result['HttpStatusCode'] = self.http_status_code
        result['Success'] = self.success
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.error_code = map.get('ErrorCode')
        self.error_message = map.get('ErrorMessage')
        self.http_status_code = map.get('HttpStatusCode')
        self.success = map.get('Success')
        if map.get('Data') is not None:
            temp_model = CreateMetaCategoryResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class CreateMetaCategoryResponseData(TeaModel):
    def __init__(self, category_id=None):
        self.category_id = category_id  # type: int

    def validate(self):
        self.validate_required(self.category_id, 'category_id')

    def to_map(self):
        result = {}
        result['CategoryId'] = self.category_id
        return result

    def from_map(self, map={}):
        self.category_id = map.get('CategoryId')
        return self


class ListNodeIORequest(TeaModel):
    def __init__(self, node_id=None, project_env=None, io_type=None):
        self.node_id = node_id          # type: int
        self.project_env = project_env  # type: str
        self.io_type = io_type          # type: str

    def validate(self):
        self.validate_required(self.node_id, 'node_id')
        self.validate_required(self.project_env, 'project_env')
        self.validate_required(self.io_type, 'io_type')

    def to_map(self):
        result = {}
        result['NodeId'] = self.node_id
        result['ProjectEnv'] = self.project_env
        result['IoType'] = self.io_type
        return result

    def from_map(self, map={}):
        self.node_id = map.get('NodeId')
        self.project_env = map.get('ProjectEnv')
        self.io_type = map.get('IoType')
        return self


class ListNodeIOResponse(TeaModel):
    def __init__(self, success=None, error_code=None, error_message=None, http_status_code=None, request_id=None,
                 data=None):
        self.success = success          # type: bool
        self.error_code = error_code    # type: str
        self.error_message = error_message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.request_id = request_id    # type: str
        self.data = data                # type: List[ListNodeIOResponseData]

    def validate(self):
        self.validate_required(self.success, 'success')
        self.validate_required(self.error_code, 'error_code')
        self.validate_required(self.error_message, 'error_message')
        self.validate_required(self.http_status_code, 'http_status_code')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['Success'] = self.success
        result['ErrorCode'] = self.error_code
        result['ErrorMessage'] = self.error_message
        result['HttpStatusCode'] = self.http_status_code
        result['RequestId'] = self.request_id
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.success = map.get('Success')
        self.error_code = map.get('ErrorCode')
        self.error_message = map.get('ErrorMessage')
        self.http_status_code = map.get('HttpStatusCode')
        self.request_id = map.get('RequestId')
        self.data = []
        if map.get('Data') is not None:
            for k in map.get('Data'):
                temp_model = ListNodeIOResponseData()
                self.data.append(temp_model.from_map(k))
        else:
            self.data = None
        return self


class ListNodeIOResponseData(TeaModel):
    def __init__(self, table_name=None, data=None):
        self.table_name = table_name    # type: str
        self.data = data                # type: str

    def validate(self):
        self.validate_required(self.table_name, 'table_name')
        self.validate_required(self.data, 'data')

    def to_map(self):
        result = {}
        result['TableName'] = self.table_name
        result['Data'] = self.data
        return result

    def from_map(self, map={}):
        self.table_name = map.get('TableName')
        self.data = map.get('Data')
        return self


class GetTopicInfluenceRequest(TeaModel):
    def __init__(self, topic_id=None):
        self.topic_id = topic_id        # type: int

    def validate(self):
        self.validate_required(self.topic_id, 'topic_id')

    def to_map(self):
        result = {}
        result['TopicId'] = self.topic_id
        return result

    def from_map(self, map={}):
        self.topic_id = map.get('TopicId')
        return self


class GetTopicInfluenceResponse(TeaModel):
    def __init__(self, success=None, error_code=None, error_message=None, http_status_code=None, request_id=None,
                 data=None):
        self.success = success          # type: bool
        self.error_code = error_code    # type: str
        self.error_message = error_message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.request_id = request_id    # type: str
        self.data = data                # type: GetTopicInfluenceResponseData

    def validate(self):
        self.validate_required(self.success, 'success')
        self.validate_required(self.error_code, 'error_code')
        self.validate_required(self.error_message, 'error_message')
        self.validate_required(self.http_status_code, 'http_status_code')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['Success'] = self.success
        result['ErrorCode'] = self.error_code
        result['ErrorMessage'] = self.error_message
        result['HttpStatusCode'] = self.http_status_code
        result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.success = map.get('Success')
        self.error_code = map.get('ErrorCode')
        self.error_message = map.get('ErrorMessage')
        self.http_status_code = map.get('HttpStatusCode')
        self.request_id = map.get('RequestId')
        if map.get('Data') is not None:
            temp_model = GetTopicInfluenceResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class GetTopicInfluenceResponseDataInfluences(TeaModel):
    def __init__(self, baseline_id=None, bizdate=None, in_group_id=None, baseline_name=None, owner=None, status=None,
                 project_id=None, priority=None, buffer=None):
        self.baseline_id = baseline_id  # type: int
        self.bizdate = bizdate          # type: int
        self.in_group_id = in_group_id  # type: int
        self.baseline_name = baseline_name  # type: str
        self.owner = owner              # type: str
        self.status = status            # type: str
        self.project_id = project_id    # type: int
        self.priority = priority        # type: int
        self.buffer = buffer            # type: int

    def validate(self):
        self.validate_required(self.baseline_id, 'baseline_id')
        self.validate_required(self.bizdate, 'bizdate')
        self.validate_required(self.in_group_id, 'in_group_id')
        self.validate_required(self.baseline_name, 'baseline_name')
        self.validate_required(self.owner, 'owner')
        self.validate_required(self.status, 'status')
        self.validate_required(self.project_id, 'project_id')
        self.validate_required(self.priority, 'priority')
        self.validate_required(self.buffer, 'buffer')

    def to_map(self):
        result = {}
        result['BaselineId'] = self.baseline_id
        result['Bizdate'] = self.bizdate
        result['InGroupId'] = self.in_group_id
        result['BaselineName'] = self.baseline_name
        result['Owner'] = self.owner
        result['Status'] = self.status
        result['ProjectId'] = self.project_id
        result['Priority'] = self.priority
        result['Buffer'] = self.buffer
        return result

    def from_map(self, map={}):
        self.baseline_id = map.get('BaselineId')
        self.bizdate = map.get('Bizdate')
        self.in_group_id = map.get('InGroupId')
        self.baseline_name = map.get('BaselineName')
        self.owner = map.get('Owner')
        self.status = map.get('Status')
        self.project_id = map.get('ProjectId')
        self.priority = map.get('Priority')
        self.buffer = map.get('Buffer')
        return self


class GetTopicInfluenceResponseData(TeaModel):
    def __init__(self, topic_id=None, influences=None):
        self.topic_id = topic_id        # type: int
        self.influences = influences    # type: List[GetTopicInfluenceResponseDataInfluences]

    def validate(self):
        self.validate_required(self.topic_id, 'topic_id')
        self.validate_required(self.influences, 'influences')
        if self.influences:
            for k in self.influences:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['TopicId'] = self.topic_id
        result['Influences'] = []
        if self.influences is not None:
            for k in self.influences:
                result['Influences'].append(k.to_map() if k else None)
        else:
            result['Influences'] = None
        return result

    def from_map(self, map={}):
        self.topic_id = map.get('TopicId')
        self.influences = []
        if map.get('Influences') is not None:
            for k in map.get('Influences'):
                temp_model = GetTopicInfluenceResponseDataInfluences()
                self.influences.append(temp_model.from_map(k))
        else:
            self.influences = None
        return self


class GetTopicRequest(TeaModel):
    def __init__(self, topic_id=None):
        self.topic_id = topic_id        # type: int

    def validate(self):
        self.validate_required(self.topic_id, 'topic_id')

    def to_map(self):
        result = {}
        result['TopicId'] = self.topic_id
        return result

    def from_map(self, map={}):
        self.topic_id = map.get('TopicId')
        return self


class GetTopicResponse(TeaModel):
    def __init__(self, success=None, error_code=None, error_message=None, http_status_code=None, request_id=None,
                 data=None):
        self.success = success          # type: bool
        self.error_code = error_code    # type: str
        self.error_message = error_message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.request_id = request_id    # type: str
        self.data = data                # type: GetTopicResponseData

    def validate(self):
        self.validate_required(self.success, 'success')
        self.validate_required(self.error_code, 'error_code')
        self.validate_required(self.error_message, 'error_message')
        self.validate_required(self.http_status_code, 'http_status_code')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['Success'] = self.success
        result['ErrorCode'] = self.error_code
        result['ErrorMessage'] = self.error_message
        result['HttpStatusCode'] = self.http_status_code
        result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.success = map.get('Success')
        self.error_code = map.get('ErrorCode')
        self.error_message = map.get('ErrorMessage')
        self.http_status_code = map.get('HttpStatusCode')
        self.request_id = map.get('RequestId')
        if map.get('Data') is not None:
            temp_model = GetTopicResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class GetTopicResponseData(TeaModel):
    def __init__(self, topic_id=None, topic_name=None, topic_status=None, topic_type=None, add_time=None,
                 alert_time=None, assigner=None, baseline_id=None, baseline_name=None, baseline_in_group_id=None,
                 baseline_status=None, baseline_buffer=None, buffer=None, deal_time=None, deal_user=None, fix_time=None,
                 happen_time=None, instance_id=None, next_alert_time=None, node_id=None, node_name=None, owner=None,
                 project_id=None):
        self.topic_id = topic_id        # type: int
        self.topic_name = topic_name    # type: str
        self.topic_status = topic_status  # type: str
        self.topic_type = topic_type    # type: str
        self.add_time = add_time        # type: int
        self.alert_time = alert_time    # type: int
        self.assigner = assigner        # type: str
        self.baseline_id = baseline_id  # type: int
        self.baseline_name = baseline_name  # type: str
        self.baseline_in_group_id = baseline_in_group_id  # type: int
        self.baseline_status = baseline_status  # type: str
        self.baseline_buffer = baseline_buffer  # type: int
        self.buffer = buffer            # type: int
        self.deal_time = deal_time      # type: int
        self.deal_user = deal_user      # type: str
        self.fix_time = fix_time        # type: int
        self.happen_time = happen_time  # type: int
        self.instance_id = instance_id  # type: int
        self.next_alert_time = next_alert_time  # type: int
        self.node_id = node_id          # type: int
        self.node_name = node_name      # type: str
        self.owner = owner              # type: str
        self.project_id = project_id    # type: int

    def validate(self):
        self.validate_required(self.topic_id, 'topic_id')
        self.validate_required(self.topic_name, 'topic_name')
        self.validate_required(self.topic_status, 'topic_status')
        self.validate_required(self.topic_type, 'topic_type')
        self.validate_required(self.add_time, 'add_time')
        self.validate_required(self.alert_time, 'alert_time')
        self.validate_required(self.assigner, 'assigner')
        self.validate_required(self.baseline_id, 'baseline_id')
        self.validate_required(self.baseline_name, 'baseline_name')
        self.validate_required(self.baseline_in_group_id, 'baseline_in_group_id')
        self.validate_required(self.baseline_status, 'baseline_status')
        self.validate_required(self.baseline_buffer, 'baseline_buffer')
        self.validate_required(self.buffer, 'buffer')
        self.validate_required(self.deal_time, 'deal_time')
        self.validate_required(self.deal_user, 'deal_user')
        self.validate_required(self.fix_time, 'fix_time')
        self.validate_required(self.happen_time, 'happen_time')
        self.validate_required(self.instance_id, 'instance_id')
        self.validate_required(self.next_alert_time, 'next_alert_time')
        self.validate_required(self.node_id, 'node_id')
        self.validate_required(self.node_name, 'node_name')
        self.validate_required(self.owner, 'owner')
        self.validate_required(self.project_id, 'project_id')

    def to_map(self):
        result = {}
        result['TopicId'] = self.topic_id
        result['TopicName'] = self.topic_name
        result['TopicStatus'] = self.topic_status
        result['TopicType'] = self.topic_type
        result['AddTime'] = self.add_time
        result['AlertTime'] = self.alert_time
        result['Assigner'] = self.assigner
        result['BaselineId'] = self.baseline_id
        result['BaselineName'] = self.baseline_name
        result['BaselineInGroupId'] = self.baseline_in_group_id
        result['BaselineStatus'] = self.baseline_status
        result['BaselineBuffer'] = self.baseline_buffer
        result['Buffer'] = self.buffer
        result['DealTime'] = self.deal_time
        result['DealUser'] = self.deal_user
        result['FixTime'] = self.fix_time
        result['HappenTime'] = self.happen_time
        result['InstanceId'] = self.instance_id
        result['NextAlertTime'] = self.next_alert_time
        result['NodeId'] = self.node_id
        result['NodeName'] = self.node_name
        result['Owner'] = self.owner
        result['ProjectId'] = self.project_id
        return result

    def from_map(self, map={}):
        self.topic_id = map.get('TopicId')
        self.topic_name = map.get('TopicName')
        self.topic_status = map.get('TopicStatus')
        self.topic_type = map.get('TopicType')
        self.add_time = map.get('AddTime')
        self.alert_time = map.get('AlertTime')
        self.assigner = map.get('Assigner')
        self.baseline_id = map.get('BaselineId')
        self.baseline_name = map.get('BaselineName')
        self.baseline_in_group_id = map.get('BaselineInGroupId')
        self.baseline_status = map.get('BaselineStatus')
        self.baseline_buffer = map.get('BaselineBuffer')
        self.buffer = map.get('Buffer')
        self.deal_time = map.get('DealTime')
        self.deal_user = map.get('DealUser')
        self.fix_time = map.get('FixTime')
        self.happen_time = map.get('HappenTime')
        self.instance_id = map.get('InstanceId')
        self.next_alert_time = map.get('NextAlertTime')
        self.node_id = map.get('NodeId')
        self.node_name = map.get('NodeName')
        self.owner = map.get('Owner')
        self.project_id = map.get('ProjectId')
        return self


class DeleteFromMetaCategoryRequest(TeaModel):
    def __init__(self, category_id=None, table_guid=None):
        self.category_id = category_id  # type: int
        self.table_guid = table_guid    # type: str

    def validate(self):
        self.validate_required(self.category_id, 'category_id')
        self.validate_required(self.table_guid, 'table_guid')

    def to_map(self):
        result = {}
        result['CategoryId'] = self.category_id
        result['TableGuid'] = self.table_guid
        return result

    def from_map(self, map={}):
        self.category_id = map.get('CategoryId')
        self.table_guid = map.get('TableGuid')
        return self


class DeleteFromMetaCategoryResponse(TeaModel):
    def __init__(self, request_id=None, error_code=None, error_message=None, http_status_code=None, success=None,
                 data=None):
        self.request_id = request_id    # type: str
        self.error_code = error_code    # type: str
        self.error_message = error_message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.success = success          # type: bool
        self.data = data                # type: bool

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.error_code, 'error_code')
        self.validate_required(self.error_message, 'error_message')
        self.validate_required(self.http_status_code, 'http_status_code')
        self.validate_required(self.success, 'success')
        self.validate_required(self.data, 'data')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['ErrorCode'] = self.error_code
        result['ErrorMessage'] = self.error_message
        result['HttpStatusCode'] = self.http_status_code
        result['Success'] = self.success
        result['Data'] = self.data
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.error_code = map.get('ErrorCode')
        self.error_message = map.get('ErrorMessage')
        self.http_status_code = map.get('HttpStatusCode')
        self.success = map.get('Success')
        self.data = map.get('Data')
        return self


class GetNodeRequest(TeaModel):
    def __init__(self, node_id=None, project_env=None):
        self.node_id = node_id          # type: int
        self.project_env = project_env  # type: str

    def validate(self):
        self.validate_required(self.node_id, 'node_id')
        self.validate_required(self.project_env, 'project_env')

    def to_map(self):
        result = {}
        result['NodeId'] = self.node_id
        result['ProjectEnv'] = self.project_env
        return result

    def from_map(self, map={}):
        self.node_id = map.get('NodeId')
        self.project_env = map.get('ProjectEnv')
        return self


class GetNodeResponse(TeaModel):
    def __init__(self, success=None, error_code=None, error_message=None, http_status_code=None, request_id=None,
                 data=None):
        self.success = success          # type: bool
        self.error_code = error_code    # type: str
        self.error_message = error_message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.request_id = request_id    # type: str
        self.data = data                # type: GetNodeResponseData

    def validate(self):
        self.validate_required(self.success, 'success')
        self.validate_required(self.error_code, 'error_code')
        self.validate_required(self.error_message, 'error_message')
        self.validate_required(self.http_status_code, 'http_status_code')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['Success'] = self.success
        result['ErrorCode'] = self.error_code
        result['ErrorMessage'] = self.error_message
        result['HttpStatusCode'] = self.http_status_code
        result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.success = map.get('Success')
        self.error_code = map.get('ErrorCode')
        self.error_message = map.get('ErrorMessage')
        self.http_status_code = map.get('HttpStatusCode')
        self.request_id = map.get('RequestId')
        if map.get('Data') is not None:
            temp_model = GetNodeResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class GetNodeResponseData(TeaModel):
    def __init__(self, node_id=None, owner_id=None, description=None, res_group_name=None, node_name=None,
                 cron_express=None, repeatability=None, program_type=None, project_id=None, scheduler_type=None,
                 param_values=None):
        self.node_id = node_id          # type: int
        self.owner_id = owner_id        # type: str
        self.description = description  # type: str
        self.res_group_name = res_group_name  # type: str
        self.node_name = node_name      # type: str
        self.cron_express = cron_express  # type: str
        self.repeatability = repeatability  # type: str
        self.program_type = program_type  # type: str
        self.project_id = project_id    # type: int
        self.scheduler_type = scheduler_type  # type: str
        self.param_values = param_values  # type: str

    def validate(self):
        self.validate_required(self.node_id, 'node_id')
        self.validate_required(self.owner_id, 'owner_id')
        self.validate_required(self.description, 'description')
        self.validate_required(self.res_group_name, 'res_group_name')
        self.validate_required(self.node_name, 'node_name')
        self.validate_required(self.cron_express, 'cron_express')
        self.validate_required(self.repeatability, 'repeatability')
        self.validate_required(self.program_type, 'program_type')
        self.validate_required(self.project_id, 'project_id')
        self.validate_required(self.scheduler_type, 'scheduler_type')
        self.validate_required(self.param_values, 'param_values')

    def to_map(self):
        result = {}
        result['NodeId'] = self.node_id
        result['OwnerId'] = self.owner_id
        result['Description'] = self.description
        result['ResGroupName'] = self.res_group_name
        result['NodeName'] = self.node_name
        result['CronExpress'] = self.cron_express
        result['Repeatability'] = self.repeatability
        result['ProgramType'] = self.program_type
        result['ProjectId'] = self.project_id
        result['SchedulerType'] = self.scheduler_type
        result['ParamValues'] = self.param_values
        return result

    def from_map(self, map={}):
        self.node_id = map.get('NodeId')
        self.owner_id = map.get('OwnerId')
        self.description = map.get('Description')
        self.res_group_name = map.get('ResGroupName')
        self.node_name = map.get('NodeName')
        self.cron_express = map.get('CronExpress')
        self.repeatability = map.get('Repeatability')
        self.program_type = map.get('ProgramType')
        self.project_id = map.get('ProjectId')
        self.scheduler_type = map.get('SchedulerType')
        self.param_values = map.get('ParamValues')
        return self


class ListNodesRequest(TeaModel):
    def __init__(self, owner=None, biz_name=None, program_type=None, page_number=None, page_size=None,
                 project_id=None, project_env=None, node_name=None):
        self.owner = owner              # type: str
        self.biz_name = biz_name        # type: str
        self.program_type = program_type  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size      # type: int
        self.project_id = project_id    # type: int
        self.project_env = project_env  # type: str
        self.node_name = node_name      # type: str

    def validate(self):
        self.validate_required(self.project_id, 'project_id')
        self.validate_required(self.project_env, 'project_env')

    def to_map(self):
        result = {}
        result['Owner'] = self.owner
        result['BizName'] = self.biz_name
        result['ProgramType'] = self.program_type
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        result['ProjectId'] = self.project_id
        result['ProjectEnv'] = self.project_env
        result['NodeName'] = self.node_name
        return result

    def from_map(self, map={}):
        self.owner = map.get('Owner')
        self.biz_name = map.get('BizName')
        self.program_type = map.get('ProgramType')
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        self.project_id = map.get('ProjectId')
        self.project_env = map.get('ProjectEnv')
        self.node_name = map.get('NodeName')
        return self


class ListNodesResponse(TeaModel):
    def __init__(self, success=None, http_status_code=None, error_code=None, error_message=None, request_id=None,
                 data=None):
        self.success = success          # type: bool
        self.http_status_code = http_status_code  # type: int
        self.error_code = error_code    # type: str
        self.error_message = error_message  # type: str
        self.request_id = request_id    # type: str
        self.data = data                # type: ListNodesResponseData

    def validate(self):
        self.validate_required(self.success, 'success')
        self.validate_required(self.http_status_code, 'http_status_code')
        self.validate_required(self.error_code, 'error_code')
        self.validate_required(self.error_message, 'error_message')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['Success'] = self.success
        result['HttpStatusCode'] = self.http_status_code
        result['ErrorCode'] = self.error_code
        result['ErrorMessage'] = self.error_message
        result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.success = map.get('Success')
        self.http_status_code = map.get('HttpStatusCode')
        self.error_code = map.get('ErrorCode')
        self.error_message = map.get('ErrorMessage')
        self.request_id = map.get('RequestId')
        if map.get('Data') is not None:
            temp_model = ListNodesResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class ListNodesResponseDataNodes(TeaModel):
    def __init__(self, node_id=None, node_name=None, cron_express=None, scheduler_type=None, program_type=None,
                 owner_id=None, project_id=None, repeatability=None, param_values=None, description=None,
                 res_group_name=None):
        self.node_id = node_id          # type: int
        self.node_name = node_name      # type: str
        self.cron_express = cron_express  # type: str
        self.scheduler_type = scheduler_type  # type: str
        self.program_type = program_type  # type: str
        self.owner_id = owner_id        # type: str
        self.project_id = project_id    # type: int
        self.repeatability = repeatability  # type: bool
        self.param_values = param_values  # type: str
        self.description = description  # type: str
        self.res_group_name = res_group_name  # type: str

    def validate(self):
        self.validate_required(self.node_id, 'node_id')
        self.validate_required(self.node_name, 'node_name')
        self.validate_required(self.cron_express, 'cron_express')
        self.validate_required(self.scheduler_type, 'scheduler_type')
        self.validate_required(self.program_type, 'program_type')
        self.validate_required(self.owner_id, 'owner_id')
        self.validate_required(self.project_id, 'project_id')
        self.validate_required(self.repeatability, 'repeatability')
        self.validate_required(self.param_values, 'param_values')
        self.validate_required(self.description, 'description')
        self.validate_required(self.res_group_name, 'res_group_name')

    def to_map(self):
        result = {}
        result['NodeId'] = self.node_id
        result['NodeName'] = self.node_name
        result['CronExpress'] = self.cron_express
        result['SchedulerType'] = self.scheduler_type
        result['ProgramType'] = self.program_type
        result['OwnerId'] = self.owner_id
        result['ProjectId'] = self.project_id
        result['Repeatability'] = self.repeatability
        result['ParamValues'] = self.param_values
        result['Description'] = self.description
        result['ResGroupName'] = self.res_group_name
        return result

    def from_map(self, map={}):
        self.node_id = map.get('NodeId')
        self.node_name = map.get('NodeName')
        self.cron_express = map.get('CronExpress')
        self.scheduler_type = map.get('SchedulerType')
        self.program_type = map.get('ProgramType')
        self.owner_id = map.get('OwnerId')
        self.project_id = map.get('ProjectId')
        self.repeatability = map.get('Repeatability')
        self.param_values = map.get('ParamValues')
        self.description = map.get('Description')
        self.res_group_name = map.get('ResGroupName')
        return self


class ListNodesResponseData(TeaModel):
    def __init__(self, page_number=None, page_size=None, total_count=None, nodes=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size      # type: int
        self.total_count = total_count  # type: int
        self.nodes = nodes              # type: List[ListNodesResponseDataNodes]

    def validate(self):
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.nodes, 'nodes')
        if self.nodes:
            for k in self.nodes:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        result['TotalCount'] = self.total_count
        result['Nodes'] = []
        if self.nodes is not None:
            for k in self.nodes:
                result['Nodes'].append(k.to_map() if k else None)
        else:
            result['Nodes'] = None
        return result

    def from_map(self, map={}):
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        self.total_count = map.get('TotalCount')
        self.nodes = []
        if map.get('Nodes') is not None:
            for k in map.get('Nodes'):
                temp_model = ListNodesResponseDataNodes()
                self.nodes.append(temp_model.from_map(k))
        else:
            self.nodes = None
        return self


class GetNodeCodeRequest(TeaModel):
    def __init__(self, node_id=None, project_env=None):
        self.node_id = node_id          # type: int
        self.project_env = project_env  # type: str

    def validate(self):
        self.validate_required(self.node_id, 'node_id')
        self.validate_required(self.project_env, 'project_env')

    def to_map(self):
        result = {}
        result['NodeId'] = self.node_id
        result['ProjectEnv'] = self.project_env
        return result

    def from_map(self, map={}):
        self.node_id = map.get('NodeId')
        self.project_env = map.get('ProjectEnv')
        return self


class GetNodeCodeResponse(TeaModel):
    def __init__(self, success=None, error_code=None, error_message=None, http_status_code=None, request_id=None,
                 data=None):
        self.success = success          # type: bool
        self.error_code = error_code    # type: str
        self.error_message = error_message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.request_id = request_id    # type: str
        self.data = data                # type: str

    def validate(self):
        self.validate_required(self.success, 'success')
        self.validate_required(self.error_code, 'error_code')
        self.validate_required(self.error_message, 'error_message')
        self.validate_required(self.http_status_code, 'http_status_code')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')

    def to_map(self):
        result = {}
        result['Success'] = self.success
        result['ErrorCode'] = self.error_code
        result['ErrorMessage'] = self.error_message
        result['HttpStatusCode'] = self.http_status_code
        result['RequestId'] = self.request_id
        result['Data'] = self.data
        return result

    def from_map(self, map={}):
        self.success = map.get('Success')
        self.error_code = map.get('ErrorCode')
        self.error_message = map.get('ErrorMessage')
        self.http_status_code = map.get('HttpStatusCode')
        self.request_id = map.get('RequestId')
        self.data = map.get('Data')
        return self


class EstablishRelationTableToBusinessRequest(TeaModel):
    def __init__(self, project_id=None, project_identifier=None, business_id=None, table_guid=None, folder_id=None):
        self.project_id = project_id    # type: int
        self.project_identifier = project_identifier  # type: str
        self.business_id = business_id  # type: str
        self.table_guid = table_guid    # type: str
        self.folder_id = folder_id      # type: str

    def validate(self):
        self.validate_required(self.business_id, 'business_id')
        self.validate_required(self.table_guid, 'table_guid')

    def to_map(self):
        result = {}
        result['ProjectId'] = self.project_id
        result['ProjectIdentifier'] = self.project_identifier
        result['BusinessId'] = self.business_id
        result['TableGuid'] = self.table_guid
        result['FolderId'] = self.folder_id
        return result

    def from_map(self, map={}):
        self.project_id = map.get('ProjectId')
        self.project_identifier = map.get('ProjectIdentifier')
        self.business_id = map.get('BusinessId')
        self.table_guid = map.get('TableGuid')
        self.folder_id = map.get('FolderId')
        return self


class EstablishRelationTableToBusinessResponse(TeaModel):
    def __init__(self, request_id=None, success=None, error_code=None, error_message=None, http_status_code=None):
        self.request_id = request_id    # type: str
        self.success = success          # type: bool
        self.error_code = error_code    # type: str
        self.error_message = error_message  # type: str
        self.http_status_code = http_status_code  # type: int

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.success, 'success')
        self.validate_required(self.error_code, 'error_code')
        self.validate_required(self.error_message, 'error_message')
        self.validate_required(self.http_status_code, 'http_status_code')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Success'] = self.success
        result['ErrorCode'] = self.error_code
        result['ErrorMessage'] = self.error_message
        result['HttpStatusCode'] = self.http_status_code
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.success = map.get('Success')
        self.error_code = map.get('ErrorCode')
        self.error_message = map.get('ErrorMessage')
        self.http_status_code = map.get('HttpStatusCode')
        return self


class UpdateDataServiceApiRequest(TeaModel):
    def __init__(self, tenant_id=None, project_id=None, api_id=None, request_method=None,
                 response_content_type=None, timeout=None, visible_range=None, protocols=None, wizard_details=None, script_details=None,
                 registration_details=None, api_path=None, api_description=None):
        self.tenant_id = tenant_id      # type: int
        self.project_id = project_id    # type: int
        self.api_id = api_id            # type: int
        self.request_method = request_method  # type: int
        self.response_content_type = response_content_type  # type: int
        self.timeout = timeout          # type: int
        self.visible_range = visible_range  # type: int
        self.protocols = protocols      # type: str
        self.wizard_details = wizard_details  # type: str
        self.script_details = script_details  # type: str
        self.registration_details = registration_details  # type: str
        self.api_path = api_path        # type: str
        self.api_description = api_description  # type: str

    def validate(self):
        self.validate_required(self.tenant_id, 'tenant_id')
        self.validate_required(self.project_id, 'project_id')
        self.validate_required(self.api_id, 'api_id')
        self.validate_required(self.request_method, 'request_method')
        self.validate_required(self.response_content_type, 'response_content_type')
        self.validate_required(self.timeout, 'timeout')
        self.validate_required(self.visible_range, 'visible_range')
        self.validate_required(self.protocols, 'protocols')
        self.validate_required(self.api_path, 'api_path')
        self.validate_required(self.api_description, 'api_description')

    def to_map(self):
        result = {}
        result['TenantId'] = self.tenant_id
        result['ProjectId'] = self.project_id
        result['ApiId'] = self.api_id
        result['RequestMethod'] = self.request_method
        result['ResponseContentType'] = self.response_content_type
        result['Timeout'] = self.timeout
        result['VisibleRange'] = self.visible_range
        result['Protocols'] = self.protocols
        result['WizardDetails'] = self.wizard_details
        result['ScriptDetails'] = self.script_details
        result['RegistrationDetails'] = self.registration_details
        result['ApiPath'] = self.api_path
        result['ApiDescription'] = self.api_description
        return result

    def from_map(self, map={}):
        self.tenant_id = map.get('TenantId')
        self.project_id = map.get('ProjectId')
        self.api_id = map.get('ApiId')
        self.request_method = map.get('RequestMethod')
        self.response_content_type = map.get('ResponseContentType')
        self.timeout = map.get('Timeout')
        self.visible_range = map.get('VisibleRange')
        self.protocols = map.get('Protocols')
        self.wizard_details = map.get('WizardDetails')
        self.script_details = map.get('ScriptDetails')
        self.registration_details = map.get('RegistrationDetails')
        self.api_path = map.get('ApiPath')
        self.api_description = map.get('ApiDescription')
        return self


class UpdateDataServiceApiResponse(TeaModel):
    def __init__(self, data=None, error_code=None, error_message=None, http_status_code=None, success=None,
                 request_id=None):
        self.data = data                # type: bool
        self.error_code = error_code    # type: str
        self.error_message = error_message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.success = success          # type: bool
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.data, 'data')
        self.validate_required(self.error_code, 'error_code')
        self.validate_required(self.error_message, 'error_message')
        self.validate_required(self.http_status_code, 'http_status_code')
        self.validate_required(self.success, 'success')
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['Data'] = self.data
        result['ErrorCode'] = self.error_code
        result['ErrorMessage'] = self.error_message
        result['HttpStatusCode'] = self.http_status_code
        result['Success'] = self.success
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.data = map.get('Data')
        self.error_code = map.get('ErrorCode')
        self.error_message = map.get('ErrorMessage')
        self.http_status_code = map.get('HttpStatusCode')
        self.success = map.get('Success')
        self.request_id = map.get('RequestId')
        return self


class UpdateUdfFileRequest(TeaModel):
    def __init__(self, file_folder_path=None, project_id=None, function_type=None, class_name=None, resources=None,
                 udf_description=None, cmd_description=None, parameter_description=None, return_value=None, example=None,
                 project_identifier=None, file_id=None):
        self.file_folder_path = file_folder_path  # type: str
        self.project_id = project_id    # type: int
        self.function_type = function_type  # type: str
        self.class_name = class_name    # type: str
        self.resources = resources      # type: str
        self.udf_description = udf_description  # type: str
        self.cmd_description = cmd_description  # type: str
        self.parameter_description = parameter_description  # type: str
        self.return_value = return_value  # type: str
        self.example = example          # type: str
        self.project_identifier = project_identifier  # type: str
        self.file_id = file_id          # type: str

    def validate(self):
        self.validate_required(self.function_type, 'function_type')
        self.validate_required(self.class_name, 'class_name')
        self.validate_required(self.resources, 'resources')
        self.validate_required(self.file_id, 'file_id')

    def to_map(self):
        result = {}
        result['FileFolderPath'] = self.file_folder_path
        result['ProjectId'] = self.project_id
        result['FunctionType'] = self.function_type
        result['ClassName'] = self.class_name
        result['Resources'] = self.resources
        result['UdfDescription'] = self.udf_description
        result['CmdDescription'] = self.cmd_description
        result['ParameterDescription'] = self.parameter_description
        result['ReturnValue'] = self.return_value
        result['Example'] = self.example
        result['ProjectIdentifier'] = self.project_identifier
        result['FileId'] = self.file_id
        return result

    def from_map(self, map={}):
        self.file_folder_path = map.get('FileFolderPath')
        self.project_id = map.get('ProjectId')
        self.function_type = map.get('FunctionType')
        self.class_name = map.get('ClassName')
        self.resources = map.get('Resources')
        self.udf_description = map.get('UdfDescription')
        self.cmd_description = map.get('CmdDescription')
        self.parameter_description = map.get('ParameterDescription')
        self.return_value = map.get('ReturnValue')
        self.example = map.get('Example')
        self.project_identifier = map.get('ProjectIdentifier')
        self.file_id = map.get('FileId')
        return self


class UpdateUdfFileResponse(TeaModel):
    def __init__(self, request_id=None, success=None, error_code=None, error_message=None, http_status_code=None):
        self.request_id = request_id    # type: str
        self.success = success          # type: bool
        self.error_code = error_code    # type: str
        self.error_message = error_message  # type: str
        self.http_status_code = http_status_code  # type: int

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.success, 'success')
        self.validate_required(self.error_code, 'error_code')
        self.validate_required(self.error_message, 'error_message')
        self.validate_required(self.http_status_code, 'http_status_code')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Success'] = self.success
        result['ErrorCode'] = self.error_code
        result['ErrorMessage'] = self.error_message
        result['HttpStatusCode'] = self.http_status_code
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.success = map.get('Success')
        self.error_code = map.get('ErrorCode')
        self.error_message = map.get('ErrorMessage')
        self.http_status_code = map.get('HttpStatusCode')
        return self


class CreateUdfFileRequest(TeaModel):
    def __init__(self, file_folder_path=None, project_id=None, file_name=None, function_type=None, class_name=None,
                 resources=None, udf_description=None, cmd_description=None, parameter_description=None, return_value=None,
                 example=None, project_identifier=None):
        self.file_folder_path = file_folder_path  # type: str
        self.project_id = project_id    # type: int
        self.file_name = file_name      # type: str
        self.function_type = function_type  # type: str
        self.class_name = class_name    # type: str
        self.resources = resources      # type: str
        self.udf_description = udf_description  # type: str
        self.cmd_description = cmd_description  # type: str
        self.parameter_description = parameter_description  # type: str
        self.return_value = return_value  # type: str
        self.example = example          # type: str
        self.project_identifier = project_identifier  # type: str

    def validate(self):
        self.validate_required(self.file_name, 'file_name')
        self.validate_required(self.function_type, 'function_type')
        self.validate_required(self.class_name, 'class_name')
        self.validate_required(self.resources, 'resources')

    def to_map(self):
        result = {}
        result['FileFolderPath'] = self.file_folder_path
        result['ProjectId'] = self.project_id
        result['FileName'] = self.file_name
        result['FunctionType'] = self.function_type
        result['ClassName'] = self.class_name
        result['Resources'] = self.resources
        result['UdfDescription'] = self.udf_description
        result['CmdDescription'] = self.cmd_description
        result['ParameterDescription'] = self.parameter_description
        result['ReturnValue'] = self.return_value
        result['Example'] = self.example
        result['ProjectIdentifier'] = self.project_identifier
        return result

    def from_map(self, map={}):
        self.file_folder_path = map.get('FileFolderPath')
        self.project_id = map.get('ProjectId')
        self.file_name = map.get('FileName')
        self.function_type = map.get('FunctionType')
        self.class_name = map.get('ClassName')
        self.resources = map.get('Resources')
        self.udf_description = map.get('UdfDescription')
        self.cmd_description = map.get('CmdDescription')
        self.parameter_description = map.get('ParameterDescription')
        self.return_value = map.get('ReturnValue')
        self.example = map.get('Example')
        self.project_identifier = map.get('ProjectIdentifier')
        return self


class CreateUdfFileResponse(TeaModel):
    def __init__(self, request_id=None, success=None, error_code=None, error_message=None, data=None,
                 http_status_code=None):
        self.request_id = request_id    # type: str
        self.success = success          # type: bool
        self.error_code = error_code    # type: str
        self.error_message = error_message  # type: str
        self.data = data                # type: int
        self.http_status_code = http_status_code  # type: int

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.success, 'success')
        self.validate_required(self.error_code, 'error_code')
        self.validate_required(self.error_message, 'error_message')
        self.validate_required(self.data, 'data')
        self.validate_required(self.http_status_code, 'http_status_code')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Success'] = self.success
        result['ErrorCode'] = self.error_code
        result['ErrorMessage'] = self.error_message
        result['Data'] = self.data
        result['HttpStatusCode'] = self.http_status_code
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.success = map.get('Success')
        self.error_code = map.get('ErrorCode')
        self.error_message = map.get('ErrorMessage')
        self.data = map.get('Data')
        self.http_status_code = map.get('HttpStatusCode')
        return self


class ListFilesRequest(TeaModel):
    def __init__(self, file_folder_path=None, project_id=None, keyword=None, project_identifier=None,
                 page_number=None, page_size=None, use_type=None, file_types=None, owner=None):
        self.file_folder_path = file_folder_path  # type: str
        self.project_id = project_id    # type: int
        self.keyword = keyword          # type: str
        self.project_identifier = project_identifier  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size      # type: int
        self.use_type = use_type        # type: str
        self.file_types = file_types    # type: str
        self.owner = owner              # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['FileFolderPath'] = self.file_folder_path
        result['ProjectId'] = self.project_id
        result['Keyword'] = self.keyword
        result['ProjectIdentifier'] = self.project_identifier
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        result['UseType'] = self.use_type
        result['FileTypes'] = self.file_types
        result['Owner'] = self.owner
        return result

    def from_map(self, map={}):
        self.file_folder_path = map.get('FileFolderPath')
        self.project_id = map.get('ProjectId')
        self.keyword = map.get('Keyword')
        self.project_identifier = map.get('ProjectIdentifier')
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        self.use_type = map.get('UseType')
        self.file_types = map.get('FileTypes')
        self.owner = map.get('Owner')
        return self


class ListFilesResponse(TeaModel):
    def __init__(self, request_id=None, success=None, error_code=None, error_message=None, http_status_code=None,
                 data=None):
        self.request_id = request_id    # type: str
        self.success = success          # type: bool
        self.error_code = error_code    # type: str
        self.error_message = error_message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.data = data                # type: ListFilesResponseData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.success, 'success')
        self.validate_required(self.error_code, 'error_code')
        self.validate_required(self.error_message, 'error_message')
        self.validate_required(self.http_status_code, 'http_status_code')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Success'] = self.success
        result['ErrorCode'] = self.error_code
        result['ErrorMessage'] = self.error_message
        result['HttpStatusCode'] = self.http_status_code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.success = map.get('Success')
        self.error_code = map.get('ErrorCode')
        self.error_message = map.get('ErrorMessage')
        self.http_status_code = map.get('HttpStatusCode')
        if map.get('Data') is not None:
            temp_model = ListFilesResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class ListFilesResponseDataFiles(TeaModel):
    def __init__(self, connection_name=None, parent_id=None, is_max_compute=None, create_time=None,
                 create_user=None, biz_id=None, file_folder_id=None, file_name=None, file_type=None, use_type=None,
                 file_description=None, content=None, node_id=None, current_version=None, owner=None, last_edit_user=None,
                 last_edit_time=None, commit_status=None, file_id=None):
        self.connection_name = connection_name  # type: str
        self.parent_id = parent_id      # type: int
        self.is_max_compute = is_max_compute  # type: bool
        self.create_time = create_time  # type: int
        self.create_user = create_user  # type: str
        self.biz_id = biz_id            # type: int
        self.file_folder_id = file_folder_id  # type: str
        self.file_name = file_name      # type: str
        self.file_type = file_type      # type: int
        self.use_type = use_type        # type: str
        self.file_description = file_description  # type: str
        self.content = content          # type: str
        self.node_id = node_id          # type: int
        self.current_version = current_version  # type: int
        self.owner = owner              # type: str
        self.last_edit_user = last_edit_user  # type: str
        self.last_edit_time = last_edit_time  # type: int
        self.commit_status = commit_status  # type: int
        self.file_id = file_id          # type: int

    def validate(self):
        self.validate_required(self.connection_name, 'connection_name')
        self.validate_required(self.parent_id, 'parent_id')
        self.validate_required(self.is_max_compute, 'is_max_compute')
        self.validate_required(self.create_time, 'create_time')
        self.validate_required(self.create_user, 'create_user')
        self.validate_required(self.biz_id, 'biz_id')
        self.validate_required(self.file_folder_id, 'file_folder_id')
        self.validate_required(self.file_name, 'file_name')
        self.validate_required(self.file_type, 'file_type')
        self.validate_required(self.use_type, 'use_type')
        self.validate_required(self.file_description, 'file_description')
        self.validate_required(self.content, 'content')
        self.validate_required(self.node_id, 'node_id')
        self.validate_required(self.current_version, 'current_version')
        self.validate_required(self.owner, 'owner')
        self.validate_required(self.last_edit_user, 'last_edit_user')
        self.validate_required(self.last_edit_time, 'last_edit_time')
        self.validate_required(self.commit_status, 'commit_status')
        self.validate_required(self.file_id, 'file_id')

    def to_map(self):
        result = {}
        result['ConnectionName'] = self.connection_name
        result['ParentId'] = self.parent_id
        result['IsMaxCompute'] = self.is_max_compute
        result['CreateTime'] = self.create_time
        result['CreateUser'] = self.create_user
        result['BizId'] = self.biz_id
        result['FileFolderId'] = self.file_folder_id
        result['FileName'] = self.file_name
        result['FileType'] = self.file_type
        result['UseType'] = self.use_type
        result['FileDescription'] = self.file_description
        result['Content'] = self.content
        result['NodeId'] = self.node_id
        result['CurrentVersion'] = self.current_version
        result['Owner'] = self.owner
        result['LastEditUser'] = self.last_edit_user
        result['LastEditTime'] = self.last_edit_time
        result['CommitStatus'] = self.commit_status
        result['FileId'] = self.file_id
        return result

    def from_map(self, map={}):
        self.connection_name = map.get('ConnectionName')
        self.parent_id = map.get('ParentId')
        self.is_max_compute = map.get('IsMaxCompute')
        self.create_time = map.get('CreateTime')
        self.create_user = map.get('CreateUser')
        self.biz_id = map.get('BizId')
        self.file_folder_id = map.get('FileFolderId')
        self.file_name = map.get('FileName')
        self.file_type = map.get('FileType')
        self.use_type = map.get('UseType')
        self.file_description = map.get('FileDescription')
        self.content = map.get('Content')
        self.node_id = map.get('NodeId')
        self.current_version = map.get('CurrentVersion')
        self.owner = map.get('Owner')
        self.last_edit_user = map.get('LastEditUser')
        self.last_edit_time = map.get('LastEditTime')
        self.commit_status = map.get('CommitStatus')
        self.file_id = map.get('FileId')
        return self


class ListFilesResponseData(TeaModel):
    def __init__(self, page_number=None, page_size=None, total_count=None, files=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size      # type: int
        self.total_count = total_count  # type: int
        self.files = files              # type: List[ListFilesResponseDataFiles]

    def validate(self):
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.files, 'files')
        if self.files:
            for k in self.files:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        result['TotalCount'] = self.total_count
        result['Files'] = []
        if self.files is not None:
            for k in self.files:
                result['Files'].append(k.to_map() if k else None)
        else:
            result['Files'] = None
        return result

    def from_map(self, map={}):
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        self.total_count = map.get('TotalCount')
        self.files = []
        if map.get('Files') is not None:
            for k in map.get('Files'):
                temp_model = ListFilesResponseDataFiles()
                self.files.append(temp_model.from_map(k))
        else:
            self.files = None
        return self


class ListDataServiceAuthorizedApisRequest(TeaModel):
    def __init__(self, project_id=None, page_number=None, page_size=None, tenant_id=None, api_name_keyword=None):
        self.project_id = project_id    # type: int
        self.page_number = page_number  # type: int
        self.page_size = page_size      # type: int
        self.tenant_id = tenant_id      # type: int
        self.api_name_keyword = api_name_keyword  # type: str

    def validate(self):
        self.validate_required(self.project_id, 'project_id')
        self.validate_required(self.tenant_id, 'tenant_id')

    def to_map(self):
        result = {}
        result['ProjectId'] = self.project_id
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        result['TenantId'] = self.tenant_id
        result['ApiNameKeyword'] = self.api_name_keyword
        return result

    def from_map(self, map={}):
        self.project_id = map.get('ProjectId')
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        self.tenant_id = map.get('TenantId')
        self.api_name_keyword = map.get('ApiNameKeyword')
        return self


class ListDataServiceAuthorizedApisResponse(TeaModel):
    def __init__(self, error_code=None, error_message=None, http_status_code=None, request_id=None, success=None,
                 data=None):
        self.error_code = error_code    # type: str
        self.error_message = error_message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.request_id = request_id    # type: str
        self.success = success          # type: bool
        self.data = data                # type: ListDataServiceAuthorizedApisResponseData

    def validate(self):
        self.validate_required(self.error_code, 'error_code')
        self.validate_required(self.error_message, 'error_message')
        self.validate_required(self.http_status_code, 'http_status_code')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.success, 'success')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['ErrorCode'] = self.error_code
        result['ErrorMessage'] = self.error_message
        result['HttpStatusCode'] = self.http_status_code
        result['RequestId'] = self.request_id
        result['Success'] = self.success
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.error_code = map.get('ErrorCode')
        self.error_message = map.get('ErrorMessage')
        self.http_status_code = map.get('HttpStatusCode')
        self.request_id = map.get('RequestId')
        self.success = map.get('Success')
        if map.get('Data') is not None:
            temp_model = ListDataServiceAuthorizedApisResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class ListDataServiceAuthorizedApisResponseDataApiAuthorizedList(TeaModel):
    def __init__(self, api_id=None, api_name=None, api_path=None, api_status=None, created_time=None,
                 creator_id=None, grant_created_time=None, grant_end_time=None, grant_operator_id=None, group_id=None,
                 modified_time=None, project_id=None, tenant_id=None):
        self.api_id = api_id            # type: int
        self.api_name = api_name        # type: str
        self.api_path = api_path        # type: str
        self.api_status = api_status    # type: int
        self.created_time = created_time  # type: str
        self.creator_id = creator_id    # type: str
        self.grant_created_time = grant_created_time  # type: str
        self.grant_end_time = grant_end_time  # type: str
        self.grant_operator_id = grant_operator_id  # type: str
        self.group_id = group_id        # type: str
        self.modified_time = modified_time  # type: str
        self.project_id = project_id    # type: int
        self.tenant_id = tenant_id      # type: int

    def validate(self):
        self.validate_required(self.api_id, 'api_id')
        self.validate_required(self.api_name, 'api_name')
        self.validate_required(self.api_path, 'api_path')
        self.validate_required(self.api_status, 'api_status')
        self.validate_required(self.created_time, 'created_time')
        self.validate_required(self.creator_id, 'creator_id')
        self.validate_required(self.grant_created_time, 'grant_created_time')
        self.validate_required(self.grant_end_time, 'grant_end_time')
        self.validate_required(self.grant_operator_id, 'grant_operator_id')
        self.validate_required(self.group_id, 'group_id')
        self.validate_required(self.modified_time, 'modified_time')
        self.validate_required(self.project_id, 'project_id')
        self.validate_required(self.tenant_id, 'tenant_id')

    def to_map(self):
        result = {}
        result['ApiId'] = self.api_id
        result['ApiName'] = self.api_name
        result['ApiPath'] = self.api_path
        result['ApiStatus'] = self.api_status
        result['CreatedTime'] = self.created_time
        result['CreatorId'] = self.creator_id
        result['GrantCreatedTime'] = self.grant_created_time
        result['GrantEndTime'] = self.grant_end_time
        result['GrantOperatorId'] = self.grant_operator_id
        result['GroupId'] = self.group_id
        result['ModifiedTime'] = self.modified_time
        result['ProjectId'] = self.project_id
        result['TenantId'] = self.tenant_id
        return result

    def from_map(self, map={}):
        self.api_id = map.get('ApiId')
        self.api_name = map.get('ApiName')
        self.api_path = map.get('ApiPath')
        self.api_status = map.get('ApiStatus')
        self.created_time = map.get('CreatedTime')
        self.creator_id = map.get('CreatorId')
        self.grant_created_time = map.get('GrantCreatedTime')
        self.grant_end_time = map.get('GrantEndTime')
        self.grant_operator_id = map.get('GrantOperatorId')
        self.group_id = map.get('GroupId')
        self.modified_time = map.get('ModifiedTime')
        self.project_id = map.get('ProjectId')
        self.tenant_id = map.get('TenantId')
        return self


class ListDataServiceAuthorizedApisResponseData(TeaModel):
    def __init__(self, page_number=None, page_size=None, total_count=None, api_authorized_list=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size      # type: int
        self.total_count = total_count  # type: int
        self.api_authorized_list = api_authorized_list  # type: List[ListDataServiceAuthorizedApisResponseDataApiAuthorizedList]

    def validate(self):
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.api_authorized_list, 'api_authorized_list')
        if self.api_authorized_list:
            for k in self.api_authorized_list:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        result['TotalCount'] = self.total_count
        result['ApiAuthorizedList'] = []
        if self.api_authorized_list is not None:
            for k in self.api_authorized_list:
                result['ApiAuthorizedList'].append(k.to_map() if k else None)
        else:
            result['ApiAuthorizedList'] = None
        return result

    def from_map(self, map={}):
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        self.total_count = map.get('TotalCount')
        self.api_authorized_list = []
        if map.get('ApiAuthorizedList') is not None:
            for k in map.get('ApiAuthorizedList'):
                temp_model = ListDataServiceAuthorizedApisResponseDataApiAuthorizedList()
                self.api_authorized_list.append(temp_model.from_map(k))
        else:
            self.api_authorized_list = None
        return self


class UpdateFileRequest(TeaModel):
    def __init__(self, file_folder_path=None, project_id=None, file_name=None, file_description=None, content=None,
                 auto_rerun_times=None, auto_rerun_interval_millis=None, rerun_mode=None, stop=None, para_value=None,
                 start_effect_date=None, end_effect_date=None, cron_express=None, cycle_type=None, dependent_type=None,
                 dependent_node_id_list=None, input_list=None, project_identifier=None, file_id=None, output_list=None,
                 resource_group_identifier=None, connection_name=None, owner=None):
        self.file_folder_path = file_folder_path  # type: str
        self.project_id = project_id    # type: int
        self.file_name = file_name      # type: str
        self.file_description = file_description  # type: str
        self.content = content          # type: str
        self.auto_rerun_times = auto_rerun_times  # type: int
        self.auto_rerun_interval_millis = auto_rerun_interval_millis  # type: int
        self.rerun_mode = rerun_mode    # type: str
        self.stop = stop                # type: bool
        self.para_value = para_value    # type: str
        self.start_effect_date = start_effect_date  # type: int
        self.end_effect_date = end_effect_date  # type: int
        self.cron_express = cron_express  # type: str
        self.cycle_type = cycle_type    # type: str
        self.dependent_type = dependent_type  # type: str
        self.dependent_node_id_list = dependent_node_id_list  # type: str
        self.input_list = input_list    # type: str
        self.project_identifier = project_identifier  # type: str
        self.file_id = file_id          # type: int
        self.output_list = output_list  # type: str
        self.resource_group_identifier = resource_group_identifier  # type: str
        self.connection_name = connection_name  # type: str
        self.owner = owner              # type: str

    def validate(self):
        self.validate_required(self.file_id, 'file_id')

    def to_map(self):
        result = {}
        result['FileFolderPath'] = self.file_folder_path
        result['ProjectId'] = self.project_id
        result['FileName'] = self.file_name
        result['FileDescription'] = self.file_description
        result['Content'] = self.content
        result['AutoRerunTimes'] = self.auto_rerun_times
        result['AutoRerunIntervalMillis'] = self.auto_rerun_interval_millis
        result['RerunMode'] = self.rerun_mode
        result['Stop'] = self.stop
        result['ParaValue'] = self.para_value
        result['StartEffectDate'] = self.start_effect_date
        result['EndEffectDate'] = self.end_effect_date
        result['CronExpress'] = self.cron_express
        result['CycleType'] = self.cycle_type
        result['DependentType'] = self.dependent_type
        result['DependentNodeIdList'] = self.dependent_node_id_list
        result['InputList'] = self.input_list
        result['ProjectIdentifier'] = self.project_identifier
        result['FileId'] = self.file_id
        result['OutputList'] = self.output_list
        result['ResourceGroupIdentifier'] = self.resource_group_identifier
        result['ConnectionName'] = self.connection_name
        result['Owner'] = self.owner
        return result

    def from_map(self, map={}):
        self.file_folder_path = map.get('FileFolderPath')
        self.project_id = map.get('ProjectId')
        self.file_name = map.get('FileName')
        self.file_description = map.get('FileDescription')
        self.content = map.get('Content')
        self.auto_rerun_times = map.get('AutoRerunTimes')
        self.auto_rerun_interval_millis = map.get('AutoRerunIntervalMillis')
        self.rerun_mode = map.get('RerunMode')
        self.stop = map.get('Stop')
        self.para_value = map.get('ParaValue')
        self.start_effect_date = map.get('StartEffectDate')
        self.end_effect_date = map.get('EndEffectDate')
        self.cron_express = map.get('CronExpress')
        self.cycle_type = map.get('CycleType')
        self.dependent_type = map.get('DependentType')
        self.dependent_node_id_list = map.get('DependentNodeIdList')
        self.input_list = map.get('InputList')
        self.project_identifier = map.get('ProjectIdentifier')
        self.file_id = map.get('FileId')
        self.output_list = map.get('OutputList')
        self.resource_group_identifier = map.get('ResourceGroupIdentifier')
        self.connection_name = map.get('ConnectionName')
        self.owner = map.get('Owner')
        return self


class UpdateFileResponse(TeaModel):
    def __init__(self, request_id=None, success=None, error_code=None, error_message=None, http_status_code=None):
        self.request_id = request_id    # type: str
        self.success = success          # type: bool
        self.error_code = error_code    # type: str
        self.error_message = error_message  # type: str
        self.http_status_code = http_status_code  # type: int

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.success, 'success')
        self.validate_required(self.error_code, 'error_code')
        self.validate_required(self.error_message, 'error_message')
        self.validate_required(self.http_status_code, 'http_status_code')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Success'] = self.success
        result['ErrorCode'] = self.error_code
        result['ErrorMessage'] = self.error_message
        result['HttpStatusCode'] = self.http_status_code
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.success = map.get('Success')
        self.error_code = map.get('ErrorCode')
        self.error_message = map.get('ErrorMessage')
        self.http_status_code = map.get('HttpStatusCode')
        return self


class DeleteFolderRequest(TeaModel):
    def __init__(self, project_id=None, project_identifier=None, folder_id=None):
        self.project_id = project_id    # type: int
        self.project_identifier = project_identifier  # type: str
        self.folder_id = folder_id      # type: str

    def validate(self):
        self.validate_required(self.folder_id, 'folder_id')

    def to_map(self):
        result = {}
        result['ProjectId'] = self.project_id
        result['ProjectIdentifier'] = self.project_identifier
        result['FolderId'] = self.folder_id
        return result

    def from_map(self, map={}):
        self.project_id = map.get('ProjectId')
        self.project_identifier = map.get('ProjectIdentifier')
        self.folder_id = map.get('FolderId')
        return self


class DeleteFolderResponse(TeaModel):
    def __init__(self, request_id=None, success=None, error_code=None, error_message=None, http_status_code=None):
        self.request_id = request_id    # type: str
        self.success = success          # type: bool
        self.error_code = error_code    # type: str
        self.error_message = error_message  # type: str
        self.http_status_code = http_status_code  # type: int

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.success, 'success')
        self.validate_required(self.error_code, 'error_code')
        self.validate_required(self.error_message, 'error_message')
        self.validate_required(self.http_status_code, 'http_status_code')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Success'] = self.success
        result['ErrorCode'] = self.error_code
        result['ErrorMessage'] = self.error_message
        result['HttpStatusCode'] = self.http_status_code
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.success = map.get('Success')
        self.error_code = map.get('ErrorCode')
        self.error_message = map.get('ErrorMessage')
        self.http_status_code = map.get('HttpStatusCode')
        return self


class ListFoldersRequest(TeaModel):
    def __init__(self, project_id=None, project_identifier=None, parent_folder_path=None, page_number=None,
                 page_size=None):
        self.project_id = project_id    # type: int
        self.project_identifier = project_identifier  # type: str
        self.parent_folder_path = parent_folder_path  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size      # type: int

    def validate(self):
        self.validate_required(self.parent_folder_path, 'parent_folder_path')
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_size, 'page_size')

    def to_map(self):
        result = {}
        result['ProjectId'] = self.project_id
        result['ProjectIdentifier'] = self.project_identifier
        result['ParentFolderPath'] = self.parent_folder_path
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        return result

    def from_map(self, map={}):
        self.project_id = map.get('ProjectId')
        self.project_identifier = map.get('ProjectIdentifier')
        self.parent_folder_path = map.get('ParentFolderPath')
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        return self


class ListFoldersResponse(TeaModel):
    def __init__(self, request_id=None, success=None, error_code=None, error_message=None, http_status_code=None,
                 data=None):
        self.request_id = request_id    # type: str
        self.success = success          # type: bool
        self.error_code = error_code    # type: str
        self.error_message = error_message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.data = data                # type: ListFoldersResponseData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.success, 'success')
        self.validate_required(self.error_code, 'error_code')
        self.validate_required(self.error_message, 'error_message')
        self.validate_required(self.http_status_code, 'http_status_code')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Success'] = self.success
        result['ErrorCode'] = self.error_code
        result['ErrorMessage'] = self.error_message
        result['HttpStatusCode'] = self.http_status_code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.success = map.get('Success')
        self.error_code = map.get('ErrorCode')
        self.error_message = map.get('ErrorMessage')
        self.http_status_code = map.get('HttpStatusCode')
        if map.get('Data') is not None:
            temp_model = ListFoldersResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class ListFoldersResponseDataFolders(TeaModel):
    def __init__(self, folder_id=None, folder_path=None):
        self.folder_id = folder_id      # type: str
        self.folder_path = folder_path  # type: str

    def validate(self):
        self.validate_required(self.folder_id, 'folder_id')
        self.validate_required(self.folder_path, 'folder_path')

    def to_map(self):
        result = {}
        result['FolderId'] = self.folder_id
        result['FolderPath'] = self.folder_path
        return result

    def from_map(self, map={}):
        self.folder_id = map.get('FolderId')
        self.folder_path = map.get('FolderPath')
        return self


class ListFoldersResponseData(TeaModel):
    def __init__(self, page_number=None, page_size=None, total_count=None, folders=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size      # type: int
        self.total_count = total_count  # type: int
        self.folders = folders          # type: List[ListFoldersResponseDataFolders]

    def validate(self):
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.folders, 'folders')
        if self.folders:
            for k in self.folders:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        result['TotalCount'] = self.total_count
        result['Folders'] = []
        if self.folders is not None:
            for k in self.folders:
                result['Folders'].append(k.to_map() if k else None)
        else:
            result['Folders'] = None
        return result

    def from_map(self, map={}):
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        self.total_count = map.get('TotalCount')
        self.folders = []
        if map.get('Folders') is not None:
            for k in map.get('Folders'):
                temp_model = ListFoldersResponseDataFolders()
                self.folders.append(temp_model.from_map(k))
        else:
            self.folders = None
        return self


class CheckMetaPartitionRequest(TeaModel):
    def __init__(self, table_guid=None, partition=None, cluster_id=None, database_name=None, table_name=None,
                 data_source_type=None):
        self.table_guid = table_guid    # type: str
        self.partition = partition      # type: str
        self.cluster_id = cluster_id    # type: str
        self.database_name = database_name  # type: str
        self.table_name = table_name    # type: str
        self.data_source_type = data_source_type  # type: str

    def validate(self):
        self.validate_required(self.partition, 'partition')

    def to_map(self):
        result = {}
        result['TableGuid'] = self.table_guid
        result['Partition'] = self.partition
        result['ClusterId'] = self.cluster_id
        result['DatabaseName'] = self.database_name
        result['TableName'] = self.table_name
        result['DataSourceType'] = self.data_source_type
        return result

    def from_map(self, map={}):
        self.table_guid = map.get('TableGuid')
        self.partition = map.get('Partition')
        self.cluster_id = map.get('ClusterId')
        self.database_name = map.get('DatabaseName')
        self.table_name = map.get('TableName')
        self.data_source_type = map.get('DataSourceType')
        return self


class CheckMetaPartitionResponse(TeaModel):
    def __init__(self, request_id=None, error_code=None, error_message=None, http_status_code=None, success=None,
                 data=None):
        self.request_id = request_id    # type: str
        self.error_code = error_code    # type: str
        self.error_message = error_message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.success = success          # type: bool
        self.data = data                # type: bool

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.error_code, 'error_code')
        self.validate_required(self.error_message, 'error_message')
        self.validate_required(self.http_status_code, 'http_status_code')
        self.validate_required(self.success, 'success')
        self.validate_required(self.data, 'data')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['ErrorCode'] = self.error_code
        result['ErrorMessage'] = self.error_message
        result['HttpStatusCode'] = self.http_status_code
        result['Success'] = self.success
        result['Data'] = self.data
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.error_code = map.get('ErrorCode')
        self.error_message = map.get('ErrorMessage')
        self.http_status_code = map.get('HttpStatusCode')
        self.success = map.get('Success')
        self.data = map.get('Data')
        return self


class UpdateFolderRequest(TeaModel):
    def __init__(self, project_id=None, project_identifier=None, folder_id=None, folder_name=None):
        self.project_id = project_id    # type: int
        self.project_identifier = project_identifier  # type: str
        self.folder_id = folder_id      # type: str
        self.folder_name = folder_name  # type: str

    def validate(self):
        self.validate_required(self.folder_id, 'folder_id')
        self.validate_required(self.folder_name, 'folder_name')

    def to_map(self):
        result = {}
        result['ProjectId'] = self.project_id
        result['ProjectIdentifier'] = self.project_identifier
        result['FolderId'] = self.folder_id
        result['FolderName'] = self.folder_name
        return result

    def from_map(self, map={}):
        self.project_id = map.get('ProjectId')
        self.project_identifier = map.get('ProjectIdentifier')
        self.folder_id = map.get('FolderId')
        self.folder_name = map.get('FolderName')
        return self


class UpdateFolderResponse(TeaModel):
    def __init__(self, request_id=None, success=None, error_code=None, error_message=None, http_status_code=None):
        self.request_id = request_id    # type: str
        self.success = success          # type: bool
        self.error_code = error_code    # type: str
        self.error_message = error_message  # type: str
        self.http_status_code = http_status_code  # type: int

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.success, 'success')
        self.validate_required(self.error_code, 'error_code')
        self.validate_required(self.error_message, 'error_message')
        self.validate_required(self.http_status_code, 'http_status_code')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Success'] = self.success
        result['ErrorCode'] = self.error_code
        result['ErrorMessage'] = self.error_message
        result['HttpStatusCode'] = self.http_status_code
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.success = map.get('Success')
        self.error_code = map.get('ErrorCode')
        self.error_message = map.get('ErrorMessage')
        self.http_status_code = map.get('HttpStatusCode')
        return self


class DeleteRemindRequest(TeaModel):
    def __init__(self, remind_id=None):
        self.remind_id = remind_id      # type: int

    def validate(self):
        self.validate_required(self.remind_id, 'remind_id')

    def to_map(self):
        result = {}
        result['RemindId'] = self.remind_id
        return result

    def from_map(self, map={}):
        self.remind_id = map.get('RemindId')
        return self


class DeleteRemindResponse(TeaModel):
    def __init__(self, success=None, error_code=None, error_message=None, http_status_code=None, request_id=None,
                 data=None):
        self.success = success          # type: bool
        self.error_code = error_code    # type: str
        self.error_message = error_message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.request_id = request_id    # type: str
        self.data = data                # type: bool

    def validate(self):
        self.validate_required(self.success, 'success')
        self.validate_required(self.error_code, 'error_code')
        self.validate_required(self.error_message, 'error_message')
        self.validate_required(self.http_status_code, 'http_status_code')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')

    def to_map(self):
        result = {}
        result['Success'] = self.success
        result['ErrorCode'] = self.error_code
        result['ErrorMessage'] = self.error_message
        result['HttpStatusCode'] = self.http_status_code
        result['RequestId'] = self.request_id
        result['Data'] = self.data
        return result

    def from_map(self, map={}):
        self.success = map.get('Success')
        self.error_code = map.get('ErrorCode')
        self.error_message = map.get('ErrorMessage')
        self.http_status_code = map.get('HttpStatusCode')
        self.request_id = map.get('RequestId')
        self.data = map.get('Data')
        return self


class AddToMetaCategoryRequest(TeaModel):
    def __init__(self, category_id=None, table_guid=None):
        self.category_id = category_id  # type: int
        self.table_guid = table_guid    # type: str

    def validate(self):
        self.validate_required(self.category_id, 'category_id')
        self.validate_required(self.table_guid, 'table_guid')

    def to_map(self):
        result = {}
        result['CategoryId'] = self.category_id
        result['TableGuid'] = self.table_guid
        return result

    def from_map(self, map={}):
        self.category_id = map.get('CategoryId')
        self.table_guid = map.get('TableGuid')
        return self


class AddToMetaCategoryResponse(TeaModel):
    def __init__(self, request_id=None, error_code=None, error_message=None, http_status_code=None, success=None,
                 data=None):
        self.request_id = request_id    # type: str
        self.error_code = error_code    # type: str
        self.error_message = error_message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.success = success          # type: bool
        self.data = data                # type: bool

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.error_code, 'error_code')
        self.validate_required(self.error_message, 'error_message')
        self.validate_required(self.http_status_code, 'http_status_code')
        self.validate_required(self.success, 'success')
        self.validate_required(self.data, 'data')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['ErrorCode'] = self.error_code
        result['ErrorMessage'] = self.error_message
        result['HttpStatusCode'] = self.http_status_code
        result['Success'] = self.success
        result['Data'] = self.data
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.error_code = map.get('ErrorCode')
        self.error_message = map.get('ErrorMessage')
        self.http_status_code = map.get('HttpStatusCode')
        self.success = map.get('Success')
        self.data = map.get('Data')
        return self


class ListInstancesRequest(TeaModel):
    def __init__(self, project_env=None, node_id=None, node_name=None, owner=None, project_id=None, biz_name=None,
                 program_type=None, page_number=None, page_size=None):
        self.project_env = project_env  # type: str
        self.node_id = node_id          # type: int
        self.node_name = node_name      # type: str
        self.owner = owner              # type: str
        self.project_id = project_id    # type: int
        self.biz_name = biz_name        # type: str
        self.program_type = program_type  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size      # type: int

    def validate(self):
        self.validate_required(self.project_env, 'project_env')
        self.validate_required(self.project_id, 'project_id')

    def to_map(self):
        result = {}
        result['ProjectEnv'] = self.project_env
        result['NodeId'] = self.node_id
        result['NodeName'] = self.node_name
        result['Owner'] = self.owner
        result['ProjectId'] = self.project_id
        result['BizName'] = self.biz_name
        result['ProgramType'] = self.program_type
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        return result

    def from_map(self, map={}):
        self.project_env = map.get('ProjectEnv')
        self.node_id = map.get('NodeId')
        self.node_name = map.get('NodeName')
        self.owner = map.get('Owner')
        self.project_id = map.get('ProjectId')
        self.biz_name = map.get('BizName')
        self.program_type = map.get('ProgramType')
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        return self


class ListInstancesResponse(TeaModel):
    def __init__(self, success=None, http_status_code=None, error_code=None, error_message=None, request_id=None,
                 data=None):
        self.success = success          # type: bool
        self.http_status_code = http_status_code  # type: int
        self.error_code = error_code    # type: str
        self.error_message = error_message  # type: str
        self.request_id = request_id    # type: str
        self.data = data                # type: ListInstancesResponseData

    def validate(self):
        self.validate_required(self.success, 'success')
        self.validate_required(self.http_status_code, 'http_status_code')
        self.validate_required(self.error_code, 'error_code')
        self.validate_required(self.error_message, 'error_message')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['Success'] = self.success
        result['HttpStatusCode'] = self.http_status_code
        result['ErrorCode'] = self.error_code
        result['ErrorMessage'] = self.error_message
        result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.success = map.get('Success')
        self.http_status_code = map.get('HttpStatusCode')
        self.error_code = map.get('ErrorCode')
        self.error_message = map.get('ErrorMessage')
        self.request_id = map.get('RequestId')
        if map.get('Data') is not None:
            temp_model = ListInstancesResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class ListInstancesResponseDataInstances(TeaModel):
    def __init__(self, node_id=None, instance_id=None, dag_id=None, dag_type=None, status=None, bizdate=None,
                 cyc_time=None, create_time=None, modify_time=None, node_name=None, begin_wait_time_time=None,
                 begin_wait_res_time=None, begin_running_time=None, param_values=None, finish_time=None):
        self.node_id = node_id          # type: int
        self.instance_id = instance_id  # type: int
        self.dag_id = dag_id            # type: int
        self.dag_type = dag_type        # type: str
        self.status = status            # type: str
        self.bizdate = bizdate          # type: int
        self.cyc_time = cyc_time        # type: int
        self.create_time = create_time  # type: int
        self.modify_time = modify_time  # type: int
        self.node_name = node_name      # type: str
        self.begin_wait_time_time = begin_wait_time_time  # type: int
        self.begin_wait_res_time = begin_wait_res_time  # type: int
        self.begin_running_time = begin_running_time  # type: int
        self.param_values = param_values  # type: str
        self.finish_time = finish_time  # type: int

    def validate(self):
        self.validate_required(self.node_id, 'node_id')
        self.validate_required(self.instance_id, 'instance_id')
        self.validate_required(self.dag_id, 'dag_id')
        self.validate_required(self.dag_type, 'dag_type')
        self.validate_required(self.status, 'status')
        self.validate_required(self.bizdate, 'bizdate')
        self.validate_required(self.cyc_time, 'cyc_time')
        self.validate_required(self.create_time, 'create_time')
        self.validate_required(self.modify_time, 'modify_time')
        self.validate_required(self.node_name, 'node_name')
        self.validate_required(self.begin_wait_time_time, 'begin_wait_time_time')
        self.validate_required(self.begin_wait_res_time, 'begin_wait_res_time')
        self.validate_required(self.begin_running_time, 'begin_running_time')
        self.validate_required(self.param_values, 'param_values')
        self.validate_required(self.finish_time, 'finish_time')

    def to_map(self):
        result = {}
        result['NodeId'] = self.node_id
        result['InstanceId'] = self.instance_id
        result['DagId'] = self.dag_id
        result['DagType'] = self.dag_type
        result['Status'] = self.status
        result['Bizdate'] = self.bizdate
        result['CycTime'] = self.cyc_time
        result['CreateTime'] = self.create_time
        result['ModifyTime'] = self.modify_time
        result['NodeName'] = self.node_name
        result['BeginWaitTimeTime'] = self.begin_wait_time_time
        result['BeginWaitResTime'] = self.begin_wait_res_time
        result['BeginRunningTime'] = self.begin_running_time
        result['ParamValues'] = self.param_values
        result['FinishTime'] = self.finish_time
        return result

    def from_map(self, map={}):
        self.node_id = map.get('NodeId')
        self.instance_id = map.get('InstanceId')
        self.dag_id = map.get('DagId')
        self.dag_type = map.get('DagType')
        self.status = map.get('Status')
        self.bizdate = map.get('Bizdate')
        self.cyc_time = map.get('CycTime')
        self.create_time = map.get('CreateTime')
        self.modify_time = map.get('ModifyTime')
        self.node_name = map.get('NodeName')
        self.begin_wait_time_time = map.get('BeginWaitTimeTime')
        self.begin_wait_res_time = map.get('BeginWaitResTime')
        self.begin_running_time = map.get('BeginRunningTime')
        self.param_values = map.get('ParamValues')
        self.finish_time = map.get('FinishTime')
        return self


class ListInstancesResponseData(TeaModel):
    def __init__(self, page_number=None, page_size=None, total_count=None, instances=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size      # type: int
        self.total_count = total_count  # type: int
        self.instances = instances      # type: List[ListInstancesResponseDataInstances]

    def validate(self):
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.instances, 'instances')
        if self.instances:
            for k in self.instances:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        result['TotalCount'] = self.total_count
        result['Instances'] = []
        if self.instances is not None:
            for k in self.instances:
                result['Instances'].append(k.to_map() if k else None)
        else:
            result['Instances'] = None
        return result

    def from_map(self, map={}):
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        self.total_count = map.get('TotalCount')
        self.instances = []
        if map.get('Instances') is not None:
            for k in map.get('Instances'):
                temp_model = ListInstancesResponseDataInstances()
                self.instances.append(temp_model.from_map(k))
        else:
            self.instances = None
        return self


class SetSuccessInstanceRequest(TeaModel):
    def __init__(self, instance_id=None, project_env=None):
        self.instance_id = instance_id  # type: int
        self.project_env = project_env  # type: str

    def validate(self):
        self.validate_required(self.instance_id, 'instance_id')
        self.validate_required(self.project_env, 'project_env')

    def to_map(self):
        result = {}
        result['InstanceId'] = self.instance_id
        result['ProjectEnv'] = self.project_env
        return result

    def from_map(self, map={}):
        self.instance_id = map.get('InstanceId')
        self.project_env = map.get('ProjectEnv')
        return self


class SetSuccessInstanceResponse(TeaModel):
    def __init__(self, error_code=None, error_message=None, http_status_code=None, request_id=None, success=None,
                 data=None):
        self.error_code = error_code    # type: str
        self.error_message = error_message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.request_id = request_id    # type: str
        self.success = success          # type: bool
        self.data = data                # type: bool

    def validate(self):
        self.validate_required(self.error_code, 'error_code')
        self.validate_required(self.error_message, 'error_message')
        self.validate_required(self.http_status_code, 'http_status_code')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.success, 'success')
        self.validate_required(self.data, 'data')

    def to_map(self):
        result = {}
        result['ErrorCode'] = self.error_code
        result['ErrorMessage'] = self.error_message
        result['HttpStatusCode'] = self.http_status_code
        result['RequestId'] = self.request_id
        result['Success'] = self.success
        result['Data'] = self.data
        return result

    def from_map(self, map={}):
        self.error_code = map.get('ErrorCode')
        self.error_message = map.get('ErrorMessage')
        self.http_status_code = map.get('HttpStatusCode')
        self.request_id = map.get('RequestId')
        self.success = map.get('Success')
        self.data = map.get('Data')
        return self


class CreateFileRequest(TeaModel):
    def __init__(self, file_folder_path=None, project_id=None, file_name=None, file_description=None,
                 file_type=None, owner=None, content=None, auto_rerun_times=None, auto_rerun_interval_millis=None,
                 rerun_mode=None, stop=None, para_value=None, start_effect_date=None, end_effect_date=None, cron_express=None,
                 cycle_type=None, dependent_type=None, dependent_node_id_list=None, input_list=None, project_identifier=None,
                 resource_group_identifier=None, resource_group_id=None, connection_name=None):
        self.file_folder_path = file_folder_path  # type: str
        self.project_id = project_id    # type: int
        self.file_name = file_name      # type: str
        self.file_description = file_description  # type: str
        self.file_type = file_type      # type: int
        self.owner = owner              # type: str
        self.content = content          # type: str
        self.auto_rerun_times = auto_rerun_times  # type: int
        self.auto_rerun_interval_millis = auto_rerun_interval_millis  # type: int
        self.rerun_mode = rerun_mode    # type: str
        self.stop = stop                # type: bool
        self.para_value = para_value    # type: str
        self.start_effect_date = start_effect_date  # type: int
        self.end_effect_date = end_effect_date  # type: int
        self.cron_express = cron_express  # type: str
        self.cycle_type = cycle_type    # type: str
        self.dependent_type = dependent_type  # type: str
        self.dependent_node_id_list = dependent_node_id_list  # type: str
        self.input_list = input_list    # type: str
        self.project_identifier = project_identifier  # type: str
        self.resource_group_identifier = resource_group_identifier  # type: str
        self.resource_group_id = resource_group_id  # type: int
        self.connection_name = connection_name  # type: str

    def validate(self):
        self.validate_required(self.file_name, 'file_name')
        self.validate_required(self.file_type, 'file_type')
        self.validate_required(self.input_list, 'input_list')

    def to_map(self):
        result = {}
        result['FileFolderPath'] = self.file_folder_path
        result['ProjectId'] = self.project_id
        result['FileName'] = self.file_name
        result['FileDescription'] = self.file_description
        result['FileType'] = self.file_type
        result['Owner'] = self.owner
        result['Content'] = self.content
        result['AutoRerunTimes'] = self.auto_rerun_times
        result['AutoRerunIntervalMillis'] = self.auto_rerun_interval_millis
        result['RerunMode'] = self.rerun_mode
        result['Stop'] = self.stop
        result['ParaValue'] = self.para_value
        result['StartEffectDate'] = self.start_effect_date
        result['EndEffectDate'] = self.end_effect_date
        result['CronExpress'] = self.cron_express
        result['CycleType'] = self.cycle_type
        result['DependentType'] = self.dependent_type
        result['DependentNodeIdList'] = self.dependent_node_id_list
        result['InputList'] = self.input_list
        result['ProjectIdentifier'] = self.project_identifier
        result['ResourceGroupIdentifier'] = self.resource_group_identifier
        result['ResourceGroupId'] = self.resource_group_id
        result['ConnectionName'] = self.connection_name
        return result

    def from_map(self, map={}):
        self.file_folder_path = map.get('FileFolderPath')
        self.project_id = map.get('ProjectId')
        self.file_name = map.get('FileName')
        self.file_description = map.get('FileDescription')
        self.file_type = map.get('FileType')
        self.owner = map.get('Owner')
        self.content = map.get('Content')
        self.auto_rerun_times = map.get('AutoRerunTimes')
        self.auto_rerun_interval_millis = map.get('AutoRerunIntervalMillis')
        self.rerun_mode = map.get('RerunMode')
        self.stop = map.get('Stop')
        self.para_value = map.get('ParaValue')
        self.start_effect_date = map.get('StartEffectDate')
        self.end_effect_date = map.get('EndEffectDate')
        self.cron_express = map.get('CronExpress')
        self.cycle_type = map.get('CycleType')
        self.dependent_type = map.get('DependentType')
        self.dependent_node_id_list = map.get('DependentNodeIdList')
        self.input_list = map.get('InputList')
        self.project_identifier = map.get('ProjectIdentifier')
        self.resource_group_identifier = map.get('ResourceGroupIdentifier')
        self.resource_group_id = map.get('ResourceGroupId')
        self.connection_name = map.get('ConnectionName')
        return self


class CreateFileResponse(TeaModel):
    def __init__(self, request_id=None, success=None, error_code=None, error_message=None, data=None,
                 http_status_code=None):
        self.request_id = request_id    # type: str
        self.success = success          # type: bool
        self.error_code = error_code    # type: str
        self.error_message = error_message  # type: str
        self.data = data                # type: int
        self.http_status_code = http_status_code  # type: int

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.success, 'success')
        self.validate_required(self.error_code, 'error_code')
        self.validate_required(self.error_message, 'error_message')
        self.validate_required(self.data, 'data')
        self.validate_required(self.http_status_code, 'http_status_code')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Success'] = self.success
        result['ErrorCode'] = self.error_code
        result['ErrorMessage'] = self.error_message
        result['Data'] = self.data
        result['HttpStatusCode'] = self.http_status_code
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.success = map.get('Success')
        self.error_code = map.get('ErrorCode')
        self.error_message = map.get('ErrorMessage')
        self.data = map.get('Data')
        self.http_status_code = map.get('HttpStatusCode')
        return self


class StopInstanceRequest(TeaModel):
    def __init__(self, instance_id=None, project_env=None):
        self.instance_id = instance_id  # type: int
        self.project_env = project_env  # type: str

    def validate(self):
        self.validate_required(self.instance_id, 'instance_id')
        self.validate_required(self.project_env, 'project_env')

    def to_map(self):
        result = {}
        result['InstanceId'] = self.instance_id
        result['ProjectEnv'] = self.project_env
        return result

    def from_map(self, map={}):
        self.instance_id = map.get('InstanceId')
        self.project_env = map.get('ProjectEnv')
        return self


class StopInstanceResponse(TeaModel):
    def __init__(self, error_code=None, error_message=None, http_status_code=None, request_id=None, success=None,
                 data=None):
        self.error_code = error_code    # type: str
        self.error_message = error_message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.request_id = request_id    # type: str
        self.success = success          # type: bool
        self.data = data                # type: bool

    def validate(self):
        self.validate_required(self.error_code, 'error_code')
        self.validate_required(self.error_message, 'error_message')
        self.validate_required(self.http_status_code, 'http_status_code')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.success, 'success')
        self.validate_required(self.data, 'data')

    def to_map(self):
        result = {}
        result['ErrorCode'] = self.error_code
        result['ErrorMessage'] = self.error_message
        result['HttpStatusCode'] = self.http_status_code
        result['RequestId'] = self.request_id
        result['Success'] = self.success
        result['Data'] = self.data
        return result

    def from_map(self, map={}):
        self.error_code = map.get('ErrorCode')
        self.error_message = map.get('ErrorMessage')
        self.http_status_code = map.get('HttpStatusCode')
        self.request_id = map.get('RequestId')
        self.success = map.get('Success')
        self.data = map.get('Data')
        return self


class ResumeInstanceRequest(TeaModel):
    def __init__(self, instance_id=None, project_env=None):
        self.instance_id = instance_id  # type: int
        self.project_env = project_env  # type: str

    def validate(self):
        self.validate_required(self.instance_id, 'instance_id')
        self.validate_required(self.project_env, 'project_env')

    def to_map(self):
        result = {}
        result['InstanceId'] = self.instance_id
        result['ProjectEnv'] = self.project_env
        return result

    def from_map(self, map={}):
        self.instance_id = map.get('InstanceId')
        self.project_env = map.get('ProjectEnv')
        return self


class ResumeInstanceResponse(TeaModel):
    def __init__(self, error_code=None, error_message=None, http_status_code=None, request_id=None, success=None,
                 data=None):
        self.error_code = error_code    # type: str
        self.error_message = error_message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.request_id = request_id    # type: str
        self.success = success          # type: bool
        self.data = data                # type: bool

    def validate(self):
        self.validate_required(self.error_code, 'error_code')
        self.validate_required(self.error_message, 'error_message')
        self.validate_required(self.http_status_code, 'http_status_code')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.success, 'success')
        self.validate_required(self.data, 'data')

    def to_map(self):
        result = {}
        result['ErrorCode'] = self.error_code
        result['ErrorMessage'] = self.error_message
        result['HttpStatusCode'] = self.http_status_code
        result['RequestId'] = self.request_id
        result['Success'] = self.success
        result['Data'] = self.data
        return result

    def from_map(self, map={}):
        self.error_code = map.get('ErrorCode')
        self.error_message = map.get('ErrorMessage')
        self.http_status_code = map.get('HttpStatusCode')
        self.request_id = map.get('RequestId')
        self.success = map.get('Success')
        self.data = map.get('Data')
        return self


class SuspendInstanceRequest(TeaModel):
    def __init__(self, instance_id=None, project_env=None):
        self.instance_id = instance_id  # type: int
        self.project_env = project_env  # type: str

    def validate(self):
        self.validate_required(self.instance_id, 'instance_id')
        self.validate_required(self.project_env, 'project_env')

    def to_map(self):
        result = {}
        result['InstanceId'] = self.instance_id
        result['ProjectEnv'] = self.project_env
        return result

    def from_map(self, map={}):
        self.instance_id = map.get('InstanceId')
        self.project_env = map.get('ProjectEnv')
        return self


class SuspendInstanceResponse(TeaModel):
    def __init__(self, error_code=None, error_message=None, http_status_code=None, request_id=None, success=None,
                 data=None):
        self.error_code = error_code    # type: str
        self.error_message = error_message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.request_id = request_id    # type: str
        self.success = success          # type: bool
        self.data = data                # type: bool

    def validate(self):
        self.validate_required(self.error_code, 'error_code')
        self.validate_required(self.error_message, 'error_message')
        self.validate_required(self.http_status_code, 'http_status_code')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.success, 'success')
        self.validate_required(self.data, 'data')

    def to_map(self):
        result = {}
        result['ErrorCode'] = self.error_code
        result['ErrorMessage'] = self.error_message
        result['HttpStatusCode'] = self.http_status_code
        result['RequestId'] = self.request_id
        result['Success'] = self.success
        result['Data'] = self.data
        return result

    def from_map(self, map={}):
        self.error_code = map.get('ErrorCode')
        self.error_message = map.get('ErrorMessage')
        self.http_status_code = map.get('HttpStatusCode')
        self.request_id = map.get('RequestId')
        self.success = map.get('Success')
        self.data = map.get('Data')
        return self


class RestartInstanceRequest(TeaModel):
    def __init__(self, instance_id=None, project_env=None):
        self.instance_id = instance_id  # type: int
        self.project_env = project_env  # type: str

    def validate(self):
        self.validate_required(self.instance_id, 'instance_id')
        self.validate_required(self.project_env, 'project_env')

    def to_map(self):
        result = {}
        result['InstanceId'] = self.instance_id
        result['ProjectEnv'] = self.project_env
        return result

    def from_map(self, map={}):
        self.instance_id = map.get('InstanceId')
        self.project_env = map.get('ProjectEnv')
        return self


class RestartInstanceResponse(TeaModel):
    def __init__(self, error_code=None, error_message=None, http_status_code=None, request_id=None, success=None,
                 data=None):
        self.error_code = error_code    # type: str
        self.error_message = error_message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.request_id = request_id    # type: str
        self.success = success          # type: bool
        self.data = data                # type: bool

    def validate(self):
        self.validate_required(self.error_code, 'error_code')
        self.validate_required(self.error_message, 'error_message')
        self.validate_required(self.http_status_code, 'http_status_code')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.success, 'success')
        self.validate_required(self.data, 'data')

    def to_map(self):
        result = {}
        result['ErrorCode'] = self.error_code
        result['ErrorMessage'] = self.error_message
        result['HttpStatusCode'] = self.http_status_code
        result['RequestId'] = self.request_id
        result['Success'] = self.success
        result['Data'] = self.data
        return result

    def from_map(self, map={}):
        self.error_code = map.get('ErrorCode')
        self.error_message = map.get('ErrorMessage')
        self.http_status_code = map.get('HttpStatusCode')
        self.request_id = map.get('RequestId')
        self.success = map.get('Success')
        self.data = map.get('Data')
        return self


class ListDataServiceApiAuthoritiesRequest(TeaModel):
    def __init__(self, project_id=None, page_number=None, page_size=None, tenant_id=None, api_name_keyword=None):
        self.project_id = project_id    # type: int
        self.page_number = page_number  # type: int
        self.page_size = page_size      # type: int
        self.tenant_id = tenant_id      # type: int
        self.api_name_keyword = api_name_keyword  # type: str

    def validate(self):
        self.validate_required(self.project_id, 'project_id')
        self.validate_required(self.tenant_id, 'tenant_id')

    def to_map(self):
        result = {}
        result['ProjectId'] = self.project_id
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        result['TenantId'] = self.tenant_id
        result['ApiNameKeyword'] = self.api_name_keyword
        return result

    def from_map(self, map={}):
        self.project_id = map.get('ProjectId')
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        self.tenant_id = map.get('TenantId')
        self.api_name_keyword = map.get('ApiNameKeyword')
        return self


class ListDataServiceApiAuthoritiesResponse(TeaModel):
    def __init__(self, error_code=None, error_message=None, http_status_code=None, request_id=None, success=None,
                 data=None):
        self.error_code = error_code    # type: str
        self.error_message = error_message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.request_id = request_id    # type: str
        self.success = success          # type: bool
        self.data = data                # type: ListDataServiceApiAuthoritiesResponseData

    def validate(self):
        self.validate_required(self.error_code, 'error_code')
        self.validate_required(self.error_message, 'error_message')
        self.validate_required(self.http_status_code, 'http_status_code')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.success, 'success')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['ErrorCode'] = self.error_code
        result['ErrorMessage'] = self.error_message
        result['HttpStatusCode'] = self.http_status_code
        result['RequestId'] = self.request_id
        result['Success'] = self.success
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.error_code = map.get('ErrorCode')
        self.error_message = map.get('ErrorMessage')
        self.http_status_code = map.get('HttpStatusCode')
        self.request_id = map.get('RequestId')
        self.success = map.get('Success')
        if map.get('Data') is not None:
            temp_model = ListDataServiceApiAuthoritiesResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class ListDataServiceApiAuthoritiesResponseDataApiAuthorizationListAuthorizationRecords(TeaModel):
    def __init__(self, created_time=None, creator_id=None, end_time=None, project_id=None):
        self.created_time = created_time  # type: str
        self.creator_id = creator_id    # type: str
        self.end_time = end_time        # type: str
        self.project_id = project_id    # type: int

    def validate(self):
        self.validate_required(self.created_time, 'created_time')
        self.validate_required(self.creator_id, 'creator_id')
        self.validate_required(self.end_time, 'end_time')
        self.validate_required(self.project_id, 'project_id')

    def to_map(self):
        result = {}
        result['CreatedTime'] = self.created_time
        result['CreatorId'] = self.creator_id
        result['EndTime'] = self.end_time
        result['ProjectId'] = self.project_id
        return result

    def from_map(self, map={}):
        self.created_time = map.get('CreatedTime')
        self.creator_id = map.get('CreatorId')
        self.end_time = map.get('EndTime')
        self.project_id = map.get('ProjectId')
        return self


class ListDataServiceApiAuthoritiesResponseDataApiAuthorizationList(TeaModel):
    def __init__(self, api_id=None, api_name=None, api_path=None, api_status=None, created_time=None,
                 creator_id=None, group_id=None, modified_time=None, project_id=None, tenant_id=None,
                 authorization_records=None):
        self.api_id = api_id            # type: int
        self.api_name = api_name        # type: str
        self.api_path = api_path        # type: str
        self.api_status = api_status    # type: int
        self.created_time = created_time  # type: str
        self.creator_id = creator_id    # type: str
        self.group_id = group_id        # type: str
        self.modified_time = modified_time  # type: str
        self.project_id = project_id    # type: int
        self.tenant_id = tenant_id      # type: int
        self.authorization_records = authorization_records  # type: List[ListDataServiceApiAuthoritiesResponseDataApiAuthorizationListAuthorizationRecords]

    def validate(self):
        self.validate_required(self.api_id, 'api_id')
        self.validate_required(self.api_name, 'api_name')
        self.validate_required(self.api_path, 'api_path')
        self.validate_required(self.api_status, 'api_status')
        self.validate_required(self.created_time, 'created_time')
        self.validate_required(self.creator_id, 'creator_id')
        self.validate_required(self.group_id, 'group_id')
        self.validate_required(self.modified_time, 'modified_time')
        self.validate_required(self.project_id, 'project_id')
        self.validate_required(self.tenant_id, 'tenant_id')
        self.validate_required(self.authorization_records, 'authorization_records')
        if self.authorization_records:
            for k in self.authorization_records:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['ApiId'] = self.api_id
        result['ApiName'] = self.api_name
        result['ApiPath'] = self.api_path
        result['ApiStatus'] = self.api_status
        result['CreatedTime'] = self.created_time
        result['CreatorId'] = self.creator_id
        result['GroupId'] = self.group_id
        result['ModifiedTime'] = self.modified_time
        result['ProjectId'] = self.project_id
        result['TenantId'] = self.tenant_id
        result['AuthorizationRecords'] = []
        if self.authorization_records is not None:
            for k in self.authorization_records:
                result['AuthorizationRecords'].append(k.to_map() if k else None)
        else:
            result['AuthorizationRecords'] = None
        return result

    def from_map(self, map={}):
        self.api_id = map.get('ApiId')
        self.api_name = map.get('ApiName')
        self.api_path = map.get('ApiPath')
        self.api_status = map.get('ApiStatus')
        self.created_time = map.get('CreatedTime')
        self.creator_id = map.get('CreatorId')
        self.group_id = map.get('GroupId')
        self.modified_time = map.get('ModifiedTime')
        self.project_id = map.get('ProjectId')
        self.tenant_id = map.get('TenantId')
        self.authorization_records = []
        if map.get('AuthorizationRecords') is not None:
            for k in map.get('AuthorizationRecords'):
                temp_model = ListDataServiceApiAuthoritiesResponseDataApiAuthorizationListAuthorizationRecords()
                self.authorization_records.append(temp_model.from_map(k))
        else:
            self.authorization_records = None
        return self


class ListDataServiceApiAuthoritiesResponseData(TeaModel):
    def __init__(self, page_number=None, page_size=None, total_count=None, api_authorization_list=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size      # type: int
        self.total_count = total_count  # type: int
        self.api_authorization_list = api_authorization_list  # type: List[ListDataServiceApiAuthoritiesResponseDataApiAuthorizationList]

    def validate(self):
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.api_authorization_list, 'api_authorization_list')
        if self.api_authorization_list:
            for k in self.api_authorization_list:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        result['TotalCount'] = self.total_count
        result['ApiAuthorizationList'] = []
        if self.api_authorization_list is not None:
            for k in self.api_authorization_list:
                result['ApiAuthorizationList'].append(k.to_map() if k else None)
        else:
            result['ApiAuthorizationList'] = None
        return result

    def from_map(self, map={}):
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        self.total_count = map.get('TotalCount')
        self.api_authorization_list = []
        if map.get('ApiAuthorizationList') is not None:
            for k in map.get('ApiAuthorizationList'):
                temp_model = ListDataServiceApiAuthoritiesResponseDataApiAuthorizationList()
                self.api_authorization_list.append(temp_model.from_map(k))
        else:
            self.api_authorization_list = None
        return self


class ListDataServicePublishedApisRequest(TeaModel):
    def __init__(self, page_number=None, page_size=None, project_id=None, tenant_id=None, api_name_keyword=None,
                 api_path_keyword=None, creator_id=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size      # type: int
        self.project_id = project_id    # type: int
        self.tenant_id = tenant_id      # type: int
        self.api_name_keyword = api_name_keyword  # type: str
        self.api_path_keyword = api_path_keyword  # type: str
        self.creator_id = creator_id    # type: str

    def validate(self):
        self.validate_required(self.project_id, 'project_id')
        self.validate_required(self.tenant_id, 'tenant_id')

    def to_map(self):
        result = {}
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        result['ProjectId'] = self.project_id
        result['TenantId'] = self.tenant_id
        result['ApiNameKeyword'] = self.api_name_keyword
        result['ApiPathKeyword'] = self.api_path_keyword
        result['CreatorId'] = self.creator_id
        return result

    def from_map(self, map={}):
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        self.project_id = map.get('ProjectId')
        self.tenant_id = map.get('TenantId')
        self.api_name_keyword = map.get('ApiNameKeyword')
        self.api_path_keyword = map.get('ApiPathKeyword')
        self.creator_id = map.get('CreatorId')
        return self


class ListDataServicePublishedApisResponse(TeaModel):
    def __init__(self, error_code=None, error_message=None, http_status_code=None, request_id=None, success=None,
                 data=None):
        self.error_code = error_code    # type: str
        self.error_message = error_message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.request_id = request_id    # type: str
        self.success = success          # type: bool
        self.data = data                # type: ListDataServicePublishedApisResponseData

    def validate(self):
        self.validate_required(self.error_code, 'error_code')
        self.validate_required(self.error_message, 'error_message')
        self.validate_required(self.http_status_code, 'http_status_code')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.success, 'success')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['ErrorCode'] = self.error_code
        result['ErrorMessage'] = self.error_message
        result['HttpStatusCode'] = self.http_status_code
        result['RequestId'] = self.request_id
        result['Success'] = self.success
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.error_code = map.get('ErrorCode')
        self.error_message = map.get('ErrorMessage')
        self.http_status_code = map.get('HttpStatusCode')
        self.request_id = map.get('RequestId')
        self.success = map.get('Success')
        if map.get('Data') is not None:
            temp_model = ListDataServicePublishedApisResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class ListDataServicePublishedApisResponseDataApisRegistrationDetailsRegistrationErrorCodes(TeaModel):
    def __init__(self, error_code=None, error_message=None, error_solution=None):
        self.error_code = error_code    # type: str
        self.error_message = error_message  # type: str
        self.error_solution = error_solution  # type: str

    def validate(self):
        self.validate_required(self.error_code, 'error_code')
        self.validate_required(self.error_message, 'error_message')
        self.validate_required(self.error_solution, 'error_solution')

    def to_map(self):
        result = {}
        result['ErrorCode'] = self.error_code
        result['ErrorMessage'] = self.error_message
        result['ErrorSolution'] = self.error_solution
        return result

    def from_map(self, map={}):
        self.error_code = map.get('ErrorCode')
        self.error_message = map.get('ErrorMessage')
        self.error_solution = map.get('ErrorSolution')
        return self


class ListDataServicePublishedApisResponseDataApisRegistrationDetailsRegistrationRequestParameters(TeaModel):
    def __init__(self, default_value=None, example_value=None, is_required_parameter=None,
                 parameter_data_type=None, parameter_description=None, parameter_name=None, parameter_operator=None,
                 parameter_position=None):
        self.default_value = default_value  # type: str
        self.example_value = example_value  # type: str
        self.is_required_parameter = is_required_parameter  # type: bool
        self.parameter_data_type = parameter_data_type  # type: int
        self.parameter_description = parameter_description  # type: str
        self.parameter_name = parameter_name  # type: str
        self.parameter_operator = parameter_operator  # type: int
        self.parameter_position = parameter_position  # type: int

    def validate(self):
        self.validate_required(self.default_value, 'default_value')
        self.validate_required(self.example_value, 'example_value')
        self.validate_required(self.is_required_parameter, 'is_required_parameter')
        self.validate_required(self.parameter_data_type, 'parameter_data_type')
        self.validate_required(self.parameter_description, 'parameter_description')
        self.validate_required(self.parameter_name, 'parameter_name')
        self.validate_required(self.parameter_operator, 'parameter_operator')
        self.validate_required(self.parameter_position, 'parameter_position')

    def to_map(self):
        result = {}
        result['DefaultValue'] = self.default_value
        result['ExampleValue'] = self.example_value
        result['IsRequiredParameter'] = self.is_required_parameter
        result['ParameterDataType'] = self.parameter_data_type
        result['ParameterDescription'] = self.parameter_description
        result['ParameterName'] = self.parameter_name
        result['ParameterOperator'] = self.parameter_operator
        result['ParameterPosition'] = self.parameter_position
        return result

    def from_map(self, map={}):
        self.default_value = map.get('DefaultValue')
        self.example_value = map.get('ExampleValue')
        self.is_required_parameter = map.get('IsRequiredParameter')
        self.parameter_data_type = map.get('ParameterDataType')
        self.parameter_description = map.get('ParameterDescription')
        self.parameter_name = map.get('ParameterName')
        self.parameter_operator = map.get('ParameterOperator')
        self.parameter_position = map.get('ParameterPosition')
        return self


class ListDataServicePublishedApisResponseDataApisRegistrationDetails(TeaModel):
    def __init__(self, failed_result_sample=None, service_content_type=None, service_host=None, service_path=None,
                 service_request_body_description=None, successful_result_sample=None, registration_error_codes=None,
                 registration_request_parameters=None):
        self.failed_result_sample = failed_result_sample  # type: str
        self.service_content_type = service_content_type  # type: int
        self.service_host = service_host  # type: str
        self.service_path = service_path  # type: str
        self.service_request_body_description = service_request_body_description  # type: str
        self.successful_result_sample = successful_result_sample  # type: str
        self.registration_error_codes = registration_error_codes  # type: List[ListDataServicePublishedApisResponseDataApisRegistrationDetailsRegistrationErrorCodes]
        self.registration_request_parameters = registration_request_parameters  # type: List[ListDataServicePublishedApisResponseDataApisRegistrationDetailsRegistrationRequestParameters]

    def validate(self):
        self.validate_required(self.failed_result_sample, 'failed_result_sample')
        self.validate_required(self.service_content_type, 'service_content_type')
        self.validate_required(self.service_host, 'service_host')
        self.validate_required(self.service_path, 'service_path')
        self.validate_required(self.service_request_body_description, 'service_request_body_description')
        self.validate_required(self.successful_result_sample, 'successful_result_sample')
        self.validate_required(self.registration_error_codes, 'registration_error_codes')
        if self.registration_error_codes:
            for k in self.registration_error_codes:
                if k:
                    k.validate()
        self.validate_required(self.registration_request_parameters, 'registration_request_parameters')
        if self.registration_request_parameters:
            for k in self.registration_request_parameters:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['FailedResultSample'] = self.failed_result_sample
        result['ServiceContentType'] = self.service_content_type
        result['ServiceHost'] = self.service_host
        result['ServicePath'] = self.service_path
        result['ServiceRequestBodyDescription'] = self.service_request_body_description
        result['SuccessfulResultSample'] = self.successful_result_sample
        result['RegistrationErrorCodes'] = []
        if self.registration_error_codes is not None:
            for k in self.registration_error_codes:
                result['RegistrationErrorCodes'].append(k.to_map() if k else None)
        else:
            result['RegistrationErrorCodes'] = None
        result['RegistrationRequestParameters'] = []
        if self.registration_request_parameters is not None:
            for k in self.registration_request_parameters:
                result['RegistrationRequestParameters'].append(k.to_map() if k else None)
        else:
            result['RegistrationRequestParameters'] = None
        return result

    def from_map(self, map={}):
        self.failed_result_sample = map.get('FailedResultSample')
        self.service_content_type = map.get('ServiceContentType')
        self.service_host = map.get('ServiceHost')
        self.service_path = map.get('ServicePath')
        self.service_request_body_description = map.get('ServiceRequestBodyDescription')
        self.successful_result_sample = map.get('SuccessfulResultSample')
        self.registration_error_codes = []
        if map.get('RegistrationErrorCodes') is not None:
            for k in map.get('RegistrationErrorCodes'):
                temp_model = ListDataServicePublishedApisResponseDataApisRegistrationDetailsRegistrationErrorCodes()
                self.registration_error_codes.append(temp_model.from_map(k))
        else:
            self.registration_error_codes = None
        self.registration_request_parameters = []
        if map.get('RegistrationRequestParameters') is not None:
            for k in map.get('RegistrationRequestParameters'):
                temp_model = ListDataServicePublishedApisResponseDataApisRegistrationDetailsRegistrationRequestParameters()
                self.registration_request_parameters.append(temp_model.from_map(k))
        else:
            self.registration_request_parameters = None
        return self


class ListDataServicePublishedApisResponseDataApisScriptDetailsScriptErrorCodes(TeaModel):
    def __init__(self, error_code=None, error_message=None, error_solution=None):
        self.error_code = error_code    # type: str
        self.error_message = error_message  # type: str
        self.error_solution = error_solution  # type: str

    def validate(self):
        self.validate_required(self.error_code, 'error_code')
        self.validate_required(self.error_message, 'error_message')
        self.validate_required(self.error_solution, 'error_solution')

    def to_map(self):
        result = {}
        result['ErrorCode'] = self.error_code
        result['ErrorMessage'] = self.error_message
        result['ErrorSolution'] = self.error_solution
        return result

    def from_map(self, map={}):
        self.error_code = map.get('ErrorCode')
        self.error_message = map.get('ErrorMessage')
        self.error_solution = map.get('ErrorSolution')
        return self


class ListDataServicePublishedApisResponseDataApisScriptDetailsScriptRequestParameters(TeaModel):
    def __init__(self, default_value=None, example_value=None, is_required_parameter=None,
                 parameter_data_type=None, parameter_description=None, parameter_name=None, parameter_operator=None,
                 parameter_position=None):
        self.default_value = default_value  # type: str
        self.example_value = example_value  # type: str
        self.is_required_parameter = is_required_parameter  # type: bool
        self.parameter_data_type = parameter_data_type  # type: int
        self.parameter_description = parameter_description  # type: str
        self.parameter_name = parameter_name  # type: str
        self.parameter_operator = parameter_operator  # type: int
        self.parameter_position = parameter_position  # type: int

    def validate(self):
        self.validate_required(self.default_value, 'default_value')
        self.validate_required(self.example_value, 'example_value')
        self.validate_required(self.is_required_parameter, 'is_required_parameter')
        self.validate_required(self.parameter_data_type, 'parameter_data_type')
        self.validate_required(self.parameter_description, 'parameter_description')
        self.validate_required(self.parameter_name, 'parameter_name')
        self.validate_required(self.parameter_operator, 'parameter_operator')
        self.validate_required(self.parameter_position, 'parameter_position')

    def to_map(self):
        result = {}
        result['DefaultValue'] = self.default_value
        result['ExampleValue'] = self.example_value
        result['IsRequiredParameter'] = self.is_required_parameter
        result['ParameterDataType'] = self.parameter_data_type
        result['ParameterDescription'] = self.parameter_description
        result['ParameterName'] = self.parameter_name
        result['ParameterOperator'] = self.parameter_operator
        result['ParameterPosition'] = self.parameter_position
        return result

    def from_map(self, map={}):
        self.default_value = map.get('DefaultValue')
        self.example_value = map.get('ExampleValue')
        self.is_required_parameter = map.get('IsRequiredParameter')
        self.parameter_data_type = map.get('ParameterDataType')
        self.parameter_description = map.get('ParameterDescription')
        self.parameter_name = map.get('ParameterName')
        self.parameter_operator = map.get('ParameterOperator')
        self.parameter_position = map.get('ParameterPosition')
        return self


class ListDataServicePublishedApisResponseDataApisScriptDetailsScriptResponseParameters(TeaModel):
    def __init__(self, example_value=None, parameter_data_type=None, parameter_description=None,
                 parameter_name=None):
        self.example_value = example_value  # type: str
        self.parameter_data_type = parameter_data_type  # type: int
        self.parameter_description = parameter_description  # type: str
        self.parameter_name = parameter_name  # type: str

    def validate(self):
        self.validate_required(self.example_value, 'example_value')
        self.validate_required(self.parameter_data_type, 'parameter_data_type')
        self.validate_required(self.parameter_description, 'parameter_description')
        self.validate_required(self.parameter_name, 'parameter_name')

    def to_map(self):
        result = {}
        result['ExampleValue'] = self.example_value
        result['ParameterDataType'] = self.parameter_data_type
        result['ParameterDescription'] = self.parameter_description
        result['ParameterName'] = self.parameter_name
        return result

    def from_map(self, map={}):
        self.example_value = map.get('ExampleValue')
        self.parameter_data_type = map.get('ParameterDataType')
        self.parameter_description = map.get('ParameterDescription')
        self.parameter_name = map.get('ParameterName')
        return self


class ListDataServicePublishedApisResponseDataApisScriptDetailsScriptConnection(TeaModel):
    def __init__(self, connection_id=None, table_name=None):
        self.connection_id = connection_id  # type: int
        self.table_name = table_name    # type: str

    def validate(self):
        self.validate_required(self.connection_id, 'connection_id')
        self.validate_required(self.table_name, 'table_name')

    def to_map(self):
        result = {}
        result['ConnectionId'] = self.connection_id
        result['TableName'] = self.table_name
        return result

    def from_map(self, map={}):
        self.connection_id = map.get('ConnectionId')
        self.table_name = map.get('TableName')
        return self


class ListDataServicePublishedApisResponseDataApisScriptDetails(TeaModel):
    def __init__(self, failed_result_sample=None, is_paged_response=None, script=None,
                 successful_result_sample=None, script_error_codes=None, script_request_parameters=None, script_response_parameters=None,
                 script_connection=None):
        self.failed_result_sample = failed_result_sample  # type: str
        self.is_paged_response = is_paged_response  # type: bool
        self.script = script            # type: str
        self.successful_result_sample = successful_result_sample  # type: str
        self.script_error_codes = script_error_codes  # type: List[ListDataServicePublishedApisResponseDataApisScriptDetailsScriptErrorCodes]
        self.script_request_parameters = script_request_parameters  # type: List[ListDataServicePublishedApisResponseDataApisScriptDetailsScriptRequestParameters]
        self.script_response_parameters = script_response_parameters  # type: List[ListDataServicePublishedApisResponseDataApisScriptDetailsScriptResponseParameters]
        self.script_connection = script_connection  # type: ListDataServicePublishedApisResponseDataApisScriptDetailsScriptConnection

    def validate(self):
        self.validate_required(self.failed_result_sample, 'failed_result_sample')
        self.validate_required(self.is_paged_response, 'is_paged_response')
        self.validate_required(self.script, 'script')
        self.validate_required(self.successful_result_sample, 'successful_result_sample')
        self.validate_required(self.script_error_codes, 'script_error_codes')
        if self.script_error_codes:
            for k in self.script_error_codes:
                if k:
                    k.validate()
        self.validate_required(self.script_request_parameters, 'script_request_parameters')
        if self.script_request_parameters:
            for k in self.script_request_parameters:
                if k:
                    k.validate()
        self.validate_required(self.script_response_parameters, 'script_response_parameters')
        if self.script_response_parameters:
            for k in self.script_response_parameters:
                if k:
                    k.validate()
        self.validate_required(self.script_connection, 'script_connection')
        if self.script_connection:
            self.script_connection.validate()

    def to_map(self):
        result = {}
        result['FailedResultSample'] = self.failed_result_sample
        result['IsPagedResponse'] = self.is_paged_response
        result['Script'] = self.script
        result['SuccessfulResultSample'] = self.successful_result_sample
        result['ScriptErrorCodes'] = []
        if self.script_error_codes is not None:
            for k in self.script_error_codes:
                result['ScriptErrorCodes'].append(k.to_map() if k else None)
        else:
            result['ScriptErrorCodes'] = None
        result['ScriptRequestParameters'] = []
        if self.script_request_parameters is not None:
            for k in self.script_request_parameters:
                result['ScriptRequestParameters'].append(k.to_map() if k else None)
        else:
            result['ScriptRequestParameters'] = None
        result['ScriptResponseParameters'] = []
        if self.script_response_parameters is not None:
            for k in self.script_response_parameters:
                result['ScriptResponseParameters'].append(k.to_map() if k else None)
        else:
            result['ScriptResponseParameters'] = None
        if self.script_connection is not None:
            result['ScriptConnection'] = self.script_connection.to_map()
        else:
            result['ScriptConnection'] = None
        return result

    def from_map(self, map={}):
        self.failed_result_sample = map.get('FailedResultSample')
        self.is_paged_response = map.get('IsPagedResponse')
        self.script = map.get('Script')
        self.successful_result_sample = map.get('SuccessfulResultSample')
        self.script_error_codes = []
        if map.get('ScriptErrorCodes') is not None:
            for k in map.get('ScriptErrorCodes'):
                temp_model = ListDataServicePublishedApisResponseDataApisScriptDetailsScriptErrorCodes()
                self.script_error_codes.append(temp_model.from_map(k))
        else:
            self.script_error_codes = None
        self.script_request_parameters = []
        if map.get('ScriptRequestParameters') is not None:
            for k in map.get('ScriptRequestParameters'):
                temp_model = ListDataServicePublishedApisResponseDataApisScriptDetailsScriptRequestParameters()
                self.script_request_parameters.append(temp_model.from_map(k))
        else:
            self.script_request_parameters = None
        self.script_response_parameters = []
        if map.get('ScriptResponseParameters') is not None:
            for k in map.get('ScriptResponseParameters'):
                temp_model = ListDataServicePublishedApisResponseDataApisScriptDetailsScriptResponseParameters()
                self.script_response_parameters.append(temp_model.from_map(k))
        else:
            self.script_response_parameters = None
        if map.get('ScriptConnection') is not None:
            temp_model = ListDataServicePublishedApisResponseDataApisScriptDetailsScriptConnection()
            self.script_connection = temp_model.from_map(map['ScriptConnection'])
        else:
            self.script_connection = None
        return self


class ListDataServicePublishedApisResponseDataApisWizardDetailsWizardErrorCodes(TeaModel):
    def __init__(self, error_code=None, error_message=None, error_solution=None):
        self.error_code = error_code    # type: str
        self.error_message = error_message  # type: str
        self.error_solution = error_solution  # type: str

    def validate(self):
        self.validate_required(self.error_code, 'error_code')
        self.validate_required(self.error_message, 'error_message')
        self.validate_required(self.error_solution, 'error_solution')

    def to_map(self):
        result = {}
        result['ErrorCode'] = self.error_code
        result['ErrorMessage'] = self.error_message
        result['ErrorSolution'] = self.error_solution
        return result

    def from_map(self, map={}):
        self.error_code = map.get('ErrorCode')
        self.error_message = map.get('ErrorMessage')
        self.error_solution = map.get('ErrorSolution')
        return self


class ListDataServicePublishedApisResponseDataApisWizardDetailsWizardRequestParameters(TeaModel):
    def __init__(self, default_value=None, example_value=None, is_required_parameter=None,
                 parameter_data_type=None, parameter_description=None, parameter_name=None, parameter_operator=None,
                 parameter_position=None):
        self.default_value = default_value  # type: str
        self.example_value = example_value  # type: str
        self.is_required_parameter = is_required_parameter  # type: bool
        self.parameter_data_type = parameter_data_type  # type: int
        self.parameter_description = parameter_description  # type: str
        self.parameter_name = parameter_name  # type: str
        self.parameter_operator = parameter_operator  # type: int
        self.parameter_position = parameter_position  # type: int

    def validate(self):
        self.validate_required(self.default_value, 'default_value')
        self.validate_required(self.example_value, 'example_value')
        self.validate_required(self.is_required_parameter, 'is_required_parameter')
        self.validate_required(self.parameter_data_type, 'parameter_data_type')
        self.validate_required(self.parameter_description, 'parameter_description')
        self.validate_required(self.parameter_name, 'parameter_name')
        self.validate_required(self.parameter_operator, 'parameter_operator')
        self.validate_required(self.parameter_position, 'parameter_position')

    def to_map(self):
        result = {}
        result['DefaultValue'] = self.default_value
        result['ExampleValue'] = self.example_value
        result['IsRequiredParameter'] = self.is_required_parameter
        result['ParameterDataType'] = self.parameter_data_type
        result['ParameterDescription'] = self.parameter_description
        result['ParameterName'] = self.parameter_name
        result['ParameterOperator'] = self.parameter_operator
        result['ParameterPosition'] = self.parameter_position
        return result

    def from_map(self, map={}):
        self.default_value = map.get('DefaultValue')
        self.example_value = map.get('ExampleValue')
        self.is_required_parameter = map.get('IsRequiredParameter')
        self.parameter_data_type = map.get('ParameterDataType')
        self.parameter_description = map.get('ParameterDescription')
        self.parameter_name = map.get('ParameterName')
        self.parameter_operator = map.get('ParameterOperator')
        self.parameter_position = map.get('ParameterPosition')
        return self


class ListDataServicePublishedApisResponseDataApisWizardDetailsWizardResponseParameters(TeaModel):
    def __init__(self, example_value=None, parameter_data_type=None, parameter_description=None,
                 parameter_name=None):
        self.example_value = example_value  # type: str
        self.parameter_data_type = parameter_data_type  # type: int
        self.parameter_description = parameter_description  # type: str
        self.parameter_name = parameter_name  # type: str

    def validate(self):
        self.validate_required(self.example_value, 'example_value')
        self.validate_required(self.parameter_data_type, 'parameter_data_type')
        self.validate_required(self.parameter_description, 'parameter_description')
        self.validate_required(self.parameter_name, 'parameter_name')

    def to_map(self):
        result = {}
        result['ExampleValue'] = self.example_value
        result['ParameterDataType'] = self.parameter_data_type
        result['ParameterDescription'] = self.parameter_description
        result['ParameterName'] = self.parameter_name
        return result

    def from_map(self, map={}):
        self.example_value = map.get('ExampleValue')
        self.parameter_data_type = map.get('ParameterDataType')
        self.parameter_description = map.get('ParameterDescription')
        self.parameter_name = map.get('ParameterName')
        return self


class ListDataServicePublishedApisResponseDataApisWizardDetailsWizardConnection(TeaModel):
    def __init__(self, connection_id=None, table_name=None):
        self.connection_id = connection_id  # type: int
        self.table_name = table_name    # type: str

    def validate(self):
        self.validate_required(self.connection_id, 'connection_id')
        self.validate_required(self.table_name, 'table_name')

    def to_map(self):
        result = {}
        result['ConnectionId'] = self.connection_id
        result['TableName'] = self.table_name
        return result

    def from_map(self, map={}):
        self.connection_id = map.get('ConnectionId')
        self.table_name = map.get('TableName')
        return self


class ListDataServicePublishedApisResponseDataApisWizardDetails(TeaModel):
    def __init__(self, failed_result_sample=None, is_paged_response=None, successful_result_sample=None,
                 wizard_error_codes=None, wizard_request_parameters=None, wizard_response_parameters=None, wizard_connection=None):
        self.failed_result_sample = failed_result_sample  # type: str
        self.is_paged_response = is_paged_response  # type: bool
        self.successful_result_sample = successful_result_sample  # type: str
        self.wizard_error_codes = wizard_error_codes  # type: List[ListDataServicePublishedApisResponseDataApisWizardDetailsWizardErrorCodes]
        self.wizard_request_parameters = wizard_request_parameters  # type: List[ListDataServicePublishedApisResponseDataApisWizardDetailsWizardRequestParameters]
        self.wizard_response_parameters = wizard_response_parameters  # type: List[ListDataServicePublishedApisResponseDataApisWizardDetailsWizardResponseParameters]
        self.wizard_connection = wizard_connection  # type: ListDataServicePublishedApisResponseDataApisWizardDetailsWizardConnection

    def validate(self):
        self.validate_required(self.failed_result_sample, 'failed_result_sample')
        self.validate_required(self.is_paged_response, 'is_paged_response')
        self.validate_required(self.successful_result_sample, 'successful_result_sample')
        self.validate_required(self.wizard_error_codes, 'wizard_error_codes')
        if self.wizard_error_codes:
            for k in self.wizard_error_codes:
                if k:
                    k.validate()
        self.validate_required(self.wizard_request_parameters, 'wizard_request_parameters')
        if self.wizard_request_parameters:
            for k in self.wizard_request_parameters:
                if k:
                    k.validate()
        self.validate_required(self.wizard_response_parameters, 'wizard_response_parameters')
        if self.wizard_response_parameters:
            for k in self.wizard_response_parameters:
                if k:
                    k.validate()
        self.validate_required(self.wizard_connection, 'wizard_connection')
        if self.wizard_connection:
            self.wizard_connection.validate()

    def to_map(self):
        result = {}
        result['FailedResultSample'] = self.failed_result_sample
        result['IsPagedResponse'] = self.is_paged_response
        result['SuccessfulResultSample'] = self.successful_result_sample
        result['WizardErrorCodes'] = []
        if self.wizard_error_codes is not None:
            for k in self.wizard_error_codes:
                result['WizardErrorCodes'].append(k.to_map() if k else None)
        else:
            result['WizardErrorCodes'] = None
        result['WizardRequestParameters'] = []
        if self.wizard_request_parameters is not None:
            for k in self.wizard_request_parameters:
                result['WizardRequestParameters'].append(k.to_map() if k else None)
        else:
            result['WizardRequestParameters'] = None
        result['WizardResponseParameters'] = []
        if self.wizard_response_parameters is not None:
            for k in self.wizard_response_parameters:
                result['WizardResponseParameters'].append(k.to_map() if k else None)
        else:
            result['WizardResponseParameters'] = None
        if self.wizard_connection is not None:
            result['WizardConnection'] = self.wizard_connection.to_map()
        else:
            result['WizardConnection'] = None
        return result

    def from_map(self, map={}):
        self.failed_result_sample = map.get('FailedResultSample')
        self.is_paged_response = map.get('IsPagedResponse')
        self.successful_result_sample = map.get('SuccessfulResultSample')
        self.wizard_error_codes = []
        if map.get('WizardErrorCodes') is not None:
            for k in map.get('WizardErrorCodes'):
                temp_model = ListDataServicePublishedApisResponseDataApisWizardDetailsWizardErrorCodes()
                self.wizard_error_codes.append(temp_model.from_map(k))
        else:
            self.wizard_error_codes = None
        self.wizard_request_parameters = []
        if map.get('WizardRequestParameters') is not None:
            for k in map.get('WizardRequestParameters'):
                temp_model = ListDataServicePublishedApisResponseDataApisWizardDetailsWizardRequestParameters()
                self.wizard_request_parameters.append(temp_model.from_map(k))
        else:
            self.wizard_request_parameters = None
        self.wizard_response_parameters = []
        if map.get('WizardResponseParameters') is not None:
            for k in map.get('WizardResponseParameters'):
                temp_model = ListDataServicePublishedApisResponseDataApisWizardDetailsWizardResponseParameters()
                self.wizard_response_parameters.append(temp_model.from_map(k))
        else:
            self.wizard_response_parameters = None
        if map.get('WizardConnection') is not None:
            temp_model = ListDataServicePublishedApisResponseDataApisWizardDetailsWizardConnection()
            self.wizard_connection = temp_model.from_map(map['WizardConnection'])
        else:
            self.wizard_connection = None
        return self


class ListDataServicePublishedApisResponseDataApis(TeaModel):
    def __init__(self, api_id=None, api_mode=None, api_name=None, api_path=None, created_time=None, creator_id=None,
                 description=None, group_id=None, modified_time=None, operator_id=None, project_id=None, request_method=None,
                 response_content_type=None, status=None, tenant_id=None, timeout=None, visible_range=None, registration_details=None,
                 script_details=None, wizard_details=None, protocols=None):
        self.api_id = api_id            # type: int
        self.api_mode = api_mode        # type: int
        self.api_name = api_name        # type: str
        self.api_path = api_path        # type: str
        self.created_time = created_time  # type: str
        self.creator_id = creator_id    # type: str
        self.description = description  # type: str
        self.group_id = group_id        # type: str
        self.modified_time = modified_time  # type: str
        self.operator_id = operator_id  # type: str
        self.project_id = project_id    # type: int
        self.request_method = request_method  # type: int
        self.response_content_type = response_content_type  # type: int
        self.status = status            # type: int
        self.tenant_id = tenant_id      # type: int
        self.timeout = timeout          # type: int
        self.visible_range = visible_range  # type: int
        self.registration_details = registration_details  # type: ListDataServicePublishedApisResponseDataApisRegistrationDetails
        self.script_details = script_details  # type: ListDataServicePublishedApisResponseDataApisScriptDetails
        self.wizard_details = wizard_details  # type: ListDataServicePublishedApisResponseDataApisWizardDetails
        self.protocols = protocols      # type: List[int]

    def validate(self):
        self.validate_required(self.api_id, 'api_id')
        self.validate_required(self.api_mode, 'api_mode')
        self.validate_required(self.api_name, 'api_name')
        self.validate_required(self.api_path, 'api_path')
        self.validate_required(self.created_time, 'created_time')
        self.validate_required(self.creator_id, 'creator_id')
        self.validate_required(self.description, 'description')
        self.validate_required(self.group_id, 'group_id')
        self.validate_required(self.modified_time, 'modified_time')
        self.validate_required(self.operator_id, 'operator_id')
        self.validate_required(self.project_id, 'project_id')
        self.validate_required(self.request_method, 'request_method')
        self.validate_required(self.response_content_type, 'response_content_type')
        self.validate_required(self.status, 'status')
        self.validate_required(self.tenant_id, 'tenant_id')
        self.validate_required(self.timeout, 'timeout')
        self.validate_required(self.visible_range, 'visible_range')
        self.validate_required(self.registration_details, 'registration_details')
        if self.registration_details:
            self.registration_details.validate()
        self.validate_required(self.script_details, 'script_details')
        if self.script_details:
            self.script_details.validate()
        self.validate_required(self.wizard_details, 'wizard_details')
        if self.wizard_details:
            self.wizard_details.validate()
        self.validate_required(self.protocols, 'protocols')

    def to_map(self):
        result = {}
        result['ApiId'] = self.api_id
        result['ApiMode'] = self.api_mode
        result['ApiName'] = self.api_name
        result['ApiPath'] = self.api_path
        result['CreatedTime'] = self.created_time
        result['CreatorId'] = self.creator_id
        result['Description'] = self.description
        result['GroupId'] = self.group_id
        result['ModifiedTime'] = self.modified_time
        result['OperatorId'] = self.operator_id
        result['ProjectId'] = self.project_id
        result['RequestMethod'] = self.request_method
        result['ResponseContentType'] = self.response_content_type
        result['Status'] = self.status
        result['TenantId'] = self.tenant_id
        result['Timeout'] = self.timeout
        result['VisibleRange'] = self.visible_range
        if self.registration_details is not None:
            result['RegistrationDetails'] = self.registration_details.to_map()
        else:
            result['RegistrationDetails'] = None
        if self.script_details is not None:
            result['ScriptDetails'] = self.script_details.to_map()
        else:
            result['ScriptDetails'] = None
        if self.wizard_details is not None:
            result['WizardDetails'] = self.wizard_details.to_map()
        else:
            result['WizardDetails'] = None
        result['Protocols'] = self.protocols
        return result

    def from_map(self, map={}):
        self.api_id = map.get('ApiId')
        self.api_mode = map.get('ApiMode')
        self.api_name = map.get('ApiName')
        self.api_path = map.get('ApiPath')
        self.created_time = map.get('CreatedTime')
        self.creator_id = map.get('CreatorId')
        self.description = map.get('Description')
        self.group_id = map.get('GroupId')
        self.modified_time = map.get('ModifiedTime')
        self.operator_id = map.get('OperatorId')
        self.project_id = map.get('ProjectId')
        self.request_method = map.get('RequestMethod')
        self.response_content_type = map.get('ResponseContentType')
        self.status = map.get('Status')
        self.tenant_id = map.get('TenantId')
        self.timeout = map.get('Timeout')
        self.visible_range = map.get('VisibleRange')
        if map.get('RegistrationDetails') is not None:
            temp_model = ListDataServicePublishedApisResponseDataApisRegistrationDetails()
            self.registration_details = temp_model.from_map(map['RegistrationDetails'])
        else:
            self.registration_details = None
        if map.get('ScriptDetails') is not None:
            temp_model = ListDataServicePublishedApisResponseDataApisScriptDetails()
            self.script_details = temp_model.from_map(map['ScriptDetails'])
        else:
            self.script_details = None
        if map.get('WizardDetails') is not None:
            temp_model = ListDataServicePublishedApisResponseDataApisWizardDetails()
            self.wizard_details = temp_model.from_map(map['WizardDetails'])
        else:
            self.wizard_details = None
        self.protocols = map.get('Protocols')
        return self


class ListDataServicePublishedApisResponseData(TeaModel):
    def __init__(self, page_number=None, page_size=None, total_count=None, apis=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size      # type: int
        self.total_count = total_count  # type: int
        self.apis = apis                # type: List[ListDataServicePublishedApisResponseDataApis]

    def validate(self):
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.apis, 'apis')
        if self.apis:
            for k in self.apis:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        result['TotalCount'] = self.total_count
        result['Apis'] = []
        if self.apis is not None:
            for k in self.apis:
                result['Apis'].append(k.to_map() if k else None)
        else:
            result['Apis'] = None
        return result

    def from_map(self, map={}):
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        self.total_count = map.get('TotalCount')
        self.apis = []
        if map.get('Apis') is not None:
            for k in map.get('Apis'):
                temp_model = ListDataServicePublishedApisResponseDataApis()
                self.apis.append(temp_model.from_map(k))
        else:
            self.apis = None
        return self


class GetInstanceLogRequest(TeaModel):
    def __init__(self, instance_id=None, project_env=None):
        self.instance_id = instance_id  # type: int
        self.project_env = project_env  # type: str

    def validate(self):
        self.validate_required(self.instance_id, 'instance_id')
        self.validate_required(self.project_env, 'project_env')

    def to_map(self):
        result = {}
        result['InstanceId'] = self.instance_id
        result['ProjectEnv'] = self.project_env
        return result

    def from_map(self, map={}):
        self.instance_id = map.get('InstanceId')
        self.project_env = map.get('ProjectEnv')
        return self


class GetInstanceLogResponse(TeaModel):
    def __init__(self, error_code=None, error_message=None, http_status_code=None, request_id=None, success=None,
                 data=None):
        self.error_code = error_code    # type: str
        self.error_message = error_message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.request_id = request_id    # type: str
        self.success = success          # type: bool
        self.data = data                # type: str

    def validate(self):
        self.validate_required(self.error_code, 'error_code')
        self.validate_required(self.error_message, 'error_message')
        self.validate_required(self.http_status_code, 'http_status_code')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.success, 'success')
        self.validate_required(self.data, 'data')

    def to_map(self):
        result = {}
        result['ErrorCode'] = self.error_code
        result['ErrorMessage'] = self.error_message
        result['HttpStatusCode'] = self.http_status_code
        result['RequestId'] = self.request_id
        result['Success'] = self.success
        result['Data'] = self.data
        return result

    def from_map(self, map={}):
        self.error_code = map.get('ErrorCode')
        self.error_message = map.get('ErrorMessage')
        self.http_status_code = map.get('HttpStatusCode')
        self.request_id = map.get('RequestId')
        self.success = map.get('Success')
        self.data = map.get('Data')
        return self


class CreateFolderRequest(TeaModel):
    def __init__(self, project_id=None, project_identifier=None, folder_path=None):
        self.project_id = project_id    # type: int
        self.project_identifier = project_identifier  # type: str
        self.folder_path = folder_path  # type: str

    def validate(self):
        self.validate_required(self.folder_path, 'folder_path')

    def to_map(self):
        result = {}
        result['ProjectId'] = self.project_id
        result['ProjectIdentifier'] = self.project_identifier
        result['FolderPath'] = self.folder_path
        return result

    def from_map(self, map={}):
        self.project_id = map.get('ProjectId')
        self.project_identifier = map.get('ProjectIdentifier')
        self.folder_path = map.get('FolderPath')
        return self


class CreateFolderResponse(TeaModel):
    def __init__(self, request_id=None, success=None, error_code=None, error_message=None, data=None,
                 http_status_code=None):
        self.request_id = request_id    # type: str
        self.success = success          # type: bool
        self.error_code = error_code    # type: str
        self.error_message = error_message  # type: str
        self.data = data                # type: str
        self.http_status_code = http_status_code  # type: int

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.success, 'success')
        self.validate_required(self.error_code, 'error_code')
        self.validate_required(self.error_message, 'error_message')
        self.validate_required(self.data, 'data')
        self.validate_required(self.http_status_code, 'http_status_code')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Success'] = self.success
        result['ErrorCode'] = self.error_code
        result['ErrorMessage'] = self.error_message
        result['Data'] = self.data
        result['HttpStatusCode'] = self.http_status_code
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.success = map.get('Success')
        self.error_code = map.get('ErrorCode')
        self.error_message = map.get('ErrorMessage')
        self.data = map.get('Data')
        self.http_status_code = map.get('HttpStatusCode')
        return self


class GetBusinessRequest(TeaModel):
    def __init__(self, project_id=None, project_identifier=None, business_id=None):
        self.project_id = project_id    # type: int
        self.project_identifier = project_identifier  # type: str
        self.business_id = business_id  # type: int

    def validate(self):
        self.validate_required(self.business_id, 'business_id')

    def to_map(self):
        result = {}
        result['ProjectId'] = self.project_id
        result['ProjectIdentifier'] = self.project_identifier
        result['BusinessId'] = self.business_id
        return result

    def from_map(self, map={}):
        self.project_id = map.get('ProjectId')
        self.project_identifier = map.get('ProjectIdentifier')
        self.business_id = map.get('BusinessId')
        return self


class GetBusinessResponse(TeaModel):
    def __init__(self, request_id=None, success=None, error_code=None, error_message=None, http_status_code=None,
                 data=None):
        self.request_id = request_id    # type: str
        self.success = success          # type: bool
        self.error_code = error_code    # type: str
        self.error_message = error_message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.data = data                # type: GetBusinessResponseData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.success, 'success')
        self.validate_required(self.error_code, 'error_code')
        self.validate_required(self.error_message, 'error_message')
        self.validate_required(self.http_status_code, 'http_status_code')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Success'] = self.success
        result['ErrorCode'] = self.error_code
        result['ErrorMessage'] = self.error_message
        result['HttpStatusCode'] = self.http_status_code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.success = map.get('Success')
        self.error_code = map.get('ErrorCode')
        self.error_message = map.get('ErrorMessage')
        self.http_status_code = map.get('HttpStatusCode')
        if map.get('Data') is not None:
            temp_model = GetBusinessResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class GetBusinessResponseData(TeaModel):
    def __init__(self, business_id=None, business_name=None, project_id=None, owner=None, description=None,
                 use_type=None):
        self.business_id = business_id  # type: int
        self.business_name = business_name  # type: str
        self.project_id = project_id    # type: str
        self.owner = owner              # type: str
        self.description = description  # type: str
        self.use_type = use_type        # type: str

    def validate(self):
        self.validate_required(self.business_id, 'business_id')
        self.validate_required(self.business_name, 'business_name')
        self.validate_required(self.project_id, 'project_id')
        self.validate_required(self.owner, 'owner')
        self.validate_required(self.description, 'description')
        self.validate_required(self.use_type, 'use_type')

    def to_map(self):
        result = {}
        result['BusinessId'] = self.business_id
        result['BusinessName'] = self.business_name
        result['ProjectId'] = self.project_id
        result['Owner'] = self.owner
        result['Description'] = self.description
        result['UseType'] = self.use_type
        return result

    def from_map(self, map={}):
        self.business_id = map.get('BusinessId')
        self.business_name = map.get('BusinessName')
        self.project_id = map.get('ProjectId')
        self.owner = map.get('Owner')
        self.description = map.get('Description')
        self.use_type = map.get('UseType')
        return self


class GetInstanceRequest(TeaModel):
    def __init__(self, instance_id=None, project_env=None):
        self.instance_id = instance_id  # type: int
        self.project_env = project_env  # type: str

    def validate(self):
        self.validate_required(self.instance_id, 'instance_id')
        self.validate_required(self.project_env, 'project_env')

    def to_map(self):
        result = {}
        result['InstanceId'] = self.instance_id
        result['ProjectEnv'] = self.project_env
        return result

    def from_map(self, map={}):
        self.instance_id = map.get('InstanceId')
        self.project_env = map.get('ProjectEnv')
        return self


class GetInstanceResponse(TeaModel):
    def __init__(self, error_code=None, error_message=None, http_status_code=None, request_id=None, success=None,
                 data=None):
        self.error_code = error_code    # type: str
        self.error_message = error_message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.request_id = request_id    # type: str
        self.success = success          # type: bool
        self.data = data                # type: GetInstanceResponseData

    def validate(self):
        self.validate_required(self.error_code, 'error_code')
        self.validate_required(self.error_message, 'error_message')
        self.validate_required(self.http_status_code, 'http_status_code')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.success, 'success')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['ErrorCode'] = self.error_code
        result['ErrorMessage'] = self.error_message
        result['HttpStatusCode'] = self.http_status_code
        result['RequestId'] = self.request_id
        result['Success'] = self.success
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.error_code = map.get('ErrorCode')
        self.error_message = map.get('ErrorMessage')
        self.http_status_code = map.get('HttpStatusCode')
        self.request_id = map.get('RequestId')
        self.success = map.get('Success')
        if map.get('Data') is not None:
            temp_model = GetInstanceResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class GetInstanceResponseData(TeaModel):
    def __init__(self, node_id=None, instance_id=None, dag_id=None, dag_type=None, status=None, bizdate=None,
                 param_values=None, cyc_time=None, finish_time=None, begin_wait_time_time=None, begin_wait_res_time=None,
                 begin_running_time=None, create_time=None, modify_time=None, node_name=None):
        self.node_id = node_id          # type: int
        self.instance_id = instance_id  # type: int
        self.dag_id = dag_id            # type: int
        self.dag_type = dag_type        # type: str
        self.status = status            # type: str
        self.bizdate = bizdate          # type: int
        self.param_values = param_values  # type: str
        self.cyc_time = cyc_time        # type: int
        self.finish_time = finish_time  # type: int
        self.begin_wait_time_time = begin_wait_time_time  # type: int
        self.begin_wait_res_time = begin_wait_res_time  # type: int
        self.begin_running_time = begin_running_time  # type: int
        self.create_time = create_time  # type: int
        self.modify_time = modify_time  # type: int
        self.node_name = node_name      # type: str

    def validate(self):
        self.validate_required(self.node_id, 'node_id')
        self.validate_required(self.instance_id, 'instance_id')
        self.validate_required(self.dag_id, 'dag_id')
        self.validate_required(self.dag_type, 'dag_type')
        self.validate_required(self.status, 'status')
        self.validate_required(self.bizdate, 'bizdate')
        self.validate_required(self.param_values, 'param_values')
        self.validate_required(self.cyc_time, 'cyc_time')
        self.validate_required(self.finish_time, 'finish_time')
        self.validate_required(self.begin_wait_time_time, 'begin_wait_time_time')
        self.validate_required(self.begin_wait_res_time, 'begin_wait_res_time')
        self.validate_required(self.begin_running_time, 'begin_running_time')
        self.validate_required(self.create_time, 'create_time')
        self.validate_required(self.modify_time, 'modify_time')
        self.validate_required(self.node_name, 'node_name')

    def to_map(self):
        result = {}
        result['NodeId'] = self.node_id
        result['InstanceId'] = self.instance_id
        result['DagId'] = self.dag_id
        result['DagType'] = self.dag_type
        result['Status'] = self.status
        result['Bizdate'] = self.bizdate
        result['ParamValues'] = self.param_values
        result['CycTime'] = self.cyc_time
        result['FinishTime'] = self.finish_time
        result['BeginWaitTimeTime'] = self.begin_wait_time_time
        result['BeginWaitResTime'] = self.begin_wait_res_time
        result['BeginRunningTime'] = self.begin_running_time
        result['CreateTime'] = self.create_time
        result['ModifyTime'] = self.modify_time
        result['NodeName'] = self.node_name
        return result

    def from_map(self, map={}):
        self.node_id = map.get('NodeId')
        self.instance_id = map.get('InstanceId')
        self.dag_id = map.get('DagId')
        self.dag_type = map.get('DagType')
        self.status = map.get('Status')
        self.bizdate = map.get('Bizdate')
        self.param_values = map.get('ParamValues')
        self.cyc_time = map.get('CycTime')
        self.finish_time = map.get('FinishTime')
        self.begin_wait_time_time = map.get('BeginWaitTimeTime')
        self.begin_wait_res_time = map.get('BeginWaitResTime')
        self.begin_running_time = map.get('BeginRunningTime')
        self.create_time = map.get('CreateTime')
        self.modify_time = map.get('ModifyTime')
        self.node_name = map.get('NodeName')
        return self


class GetFileRequest(TeaModel):
    def __init__(self, project_id=None, project_identifier=None, file_id=None):
        self.project_id = project_id    # type: int
        self.project_identifier = project_identifier  # type: str
        self.file_id = file_id          # type: int

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['ProjectId'] = self.project_id
        result['ProjectIdentifier'] = self.project_identifier
        result['FileId'] = self.file_id
        return result

    def from_map(self, map={}):
        self.project_id = map.get('ProjectId')
        self.project_identifier = map.get('ProjectIdentifier')
        self.file_id = map.get('FileId')
        return self


class GetFileResponse(TeaModel):
    def __init__(self, request_id=None, success=None, error_code=None, error_message=None, http_status_code=None,
                 data=None):
        self.request_id = request_id    # type: str
        self.success = success          # type: bool
        self.error_code = error_code    # type: str
        self.error_message = error_message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.data = data                # type: GetFileResponseData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.success, 'success')
        self.validate_required(self.error_code, 'error_code')
        self.validate_required(self.error_message, 'error_message')
        self.validate_required(self.http_status_code, 'http_status_code')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Success'] = self.success
        result['ErrorCode'] = self.error_code
        result['ErrorMessage'] = self.error_message
        result['HttpStatusCode'] = self.http_status_code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.success = map.get('Success')
        self.error_code = map.get('ErrorCode')
        self.error_message = map.get('ErrorMessage')
        self.http_status_code = map.get('HttpStatusCode')
        if map.get('Data') is not None:
            temp_model = GetFileResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class GetFileResponseDataFile(TeaModel):
    def __init__(self, connection_name=None, parent_id=None, is_max_compute=None, create_time=None,
                 create_user=None, biz_id=None, file_folder_id=None, file_name=None, file_type=None, use_type=None,
                 file_description=None, content=None, node_id=None, current_version=None, owner=None, last_edit_user=None,
                 last_edit_time=None, commit_status=None):
        self.connection_name = connection_name  # type: str
        self.parent_id = parent_id      # type: int
        self.is_max_compute = is_max_compute  # type: bool
        self.create_time = create_time  # type: int
        self.create_user = create_user  # type: str
        self.biz_id = biz_id            # type: int
        self.file_folder_id = file_folder_id  # type: str
        self.file_name = file_name      # type: str
        self.file_type = file_type      # type: int
        self.use_type = use_type        # type: str
        self.file_description = file_description  # type: str
        self.content = content          # type: str
        self.node_id = node_id          # type: int
        self.current_version = current_version  # type: int
        self.owner = owner              # type: str
        self.last_edit_user = last_edit_user  # type: str
        self.last_edit_time = last_edit_time  # type: int
        self.commit_status = commit_status  # type: int

    def validate(self):
        self.validate_required(self.connection_name, 'connection_name')
        self.validate_required(self.parent_id, 'parent_id')
        self.validate_required(self.is_max_compute, 'is_max_compute')
        self.validate_required(self.create_time, 'create_time')
        self.validate_required(self.create_user, 'create_user')
        self.validate_required(self.biz_id, 'biz_id')
        self.validate_required(self.file_folder_id, 'file_folder_id')
        self.validate_required(self.file_name, 'file_name')
        self.validate_required(self.file_type, 'file_type')
        self.validate_required(self.use_type, 'use_type')
        self.validate_required(self.file_description, 'file_description')
        self.validate_required(self.content, 'content')
        self.validate_required(self.node_id, 'node_id')
        self.validate_required(self.current_version, 'current_version')
        self.validate_required(self.owner, 'owner')
        self.validate_required(self.last_edit_user, 'last_edit_user')
        self.validate_required(self.last_edit_time, 'last_edit_time')
        self.validate_required(self.commit_status, 'commit_status')

    def to_map(self):
        result = {}
        result['ConnectionName'] = self.connection_name
        result['ParentId'] = self.parent_id
        result['IsMaxCompute'] = self.is_max_compute
        result['CreateTime'] = self.create_time
        result['CreateUser'] = self.create_user
        result['BizId'] = self.biz_id
        result['FileFolderId'] = self.file_folder_id
        result['FileName'] = self.file_name
        result['FileType'] = self.file_type
        result['UseType'] = self.use_type
        result['FileDescription'] = self.file_description
        result['Content'] = self.content
        result['NodeId'] = self.node_id
        result['CurrentVersion'] = self.current_version
        result['Owner'] = self.owner
        result['LastEditUser'] = self.last_edit_user
        result['LastEditTime'] = self.last_edit_time
        result['CommitStatus'] = self.commit_status
        return result

    def from_map(self, map={}):
        self.connection_name = map.get('ConnectionName')
        self.parent_id = map.get('ParentId')
        self.is_max_compute = map.get('IsMaxCompute')
        self.create_time = map.get('CreateTime')
        self.create_user = map.get('CreateUser')
        self.biz_id = map.get('BizId')
        self.file_folder_id = map.get('FileFolderId')
        self.file_name = map.get('FileName')
        self.file_type = map.get('FileType')
        self.use_type = map.get('UseType')
        self.file_description = map.get('FileDescription')
        self.content = map.get('Content')
        self.node_id = map.get('NodeId')
        self.current_version = map.get('CurrentVersion')
        self.owner = map.get('Owner')
        self.last_edit_user = map.get('LastEditUser')
        self.last_edit_time = map.get('LastEditTime')
        self.commit_status = map.get('CommitStatus')
        return self


class GetFileResponseDataNodeConfigurationInputList(TeaModel):
    def __init__(self, input=None):
        self.input = input              # type: str

    def validate(self):
        self.validate_required(self.input, 'input')

    def to_map(self):
        result = {}
        result['Input'] = self.input
        return result

    def from_map(self, map={}):
        self.input = map.get('Input')
        return self


class GetFileResponseDataNodeConfigurationOutputList(TeaModel):
    def __init__(self, output=None, ref_table_name=None):
        self.output = output            # type: str
        self.ref_table_name = ref_table_name  # type: str

    def validate(self):
        self.validate_required(self.output, 'output')
        self.validate_required(self.ref_table_name, 'ref_table_name')

    def to_map(self):
        result = {}
        result['Output'] = self.output
        result['RefTableName'] = self.ref_table_name
        return result

    def from_map(self, map={}):
        self.output = map.get('Output')
        self.ref_table_name = map.get('RefTableName')
        return self


class GetFileResponseDataNodeConfiguration(TeaModel):
    def __init__(self, auto_rerun_times=None, auto_rerun_interval_millis=None, rerun_mode=None, stop=None,
                 para_value=None, start_effect_date=None, end_effect_date=None, cron_express=None, cycle_type=None,
                 dependent_type=None, dependent_node_id_list=None, resource_group_id=None, input_list=None, output_list=None):
        self.auto_rerun_times = auto_rerun_times  # type: int
        self.auto_rerun_interval_millis = auto_rerun_interval_millis  # type: int
        self.rerun_mode = rerun_mode    # type: str
        self.stop = stop                # type: bool
        self.para_value = para_value    # type: str
        self.start_effect_date = start_effect_date  # type: int
        self.end_effect_date = end_effect_date  # type: int
        self.cron_express = cron_express  # type: str
        self.cycle_type = cycle_type    # type: str
        self.dependent_type = dependent_type  # type: str
        self.dependent_node_id_list = dependent_node_id_list  # type: str
        self.resource_group_id = resource_group_id  # type: int
        self.input_list = input_list    # type: List[GetFileResponseDataNodeConfigurationInputList]
        self.output_list = output_list  # type: List[GetFileResponseDataNodeConfigurationOutputList]

    def validate(self):
        self.validate_required(self.auto_rerun_times, 'auto_rerun_times')
        self.validate_required(self.auto_rerun_interval_millis, 'auto_rerun_interval_millis')
        self.validate_required(self.rerun_mode, 'rerun_mode')
        self.validate_required(self.stop, 'stop')
        self.validate_required(self.para_value, 'para_value')
        self.validate_required(self.start_effect_date, 'start_effect_date')
        self.validate_required(self.end_effect_date, 'end_effect_date')
        self.validate_required(self.cron_express, 'cron_express')
        self.validate_required(self.cycle_type, 'cycle_type')
        self.validate_required(self.dependent_type, 'dependent_type')
        self.validate_required(self.dependent_node_id_list, 'dependent_node_id_list')
        self.validate_required(self.resource_group_id, 'resource_group_id')
        self.validate_required(self.input_list, 'input_list')
        if self.input_list:
            for k in self.input_list:
                if k:
                    k.validate()
        self.validate_required(self.output_list, 'output_list')
        if self.output_list:
            for k in self.output_list:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['AutoRerunTimes'] = self.auto_rerun_times
        result['AutoRerunIntervalMillis'] = self.auto_rerun_interval_millis
        result['RerunMode'] = self.rerun_mode
        result['Stop'] = self.stop
        result['ParaValue'] = self.para_value
        result['StartEffectDate'] = self.start_effect_date
        result['EndEffectDate'] = self.end_effect_date
        result['CronExpress'] = self.cron_express
        result['CycleType'] = self.cycle_type
        result['DependentType'] = self.dependent_type
        result['DependentNodeIdList'] = self.dependent_node_id_list
        result['ResourceGroupId'] = self.resource_group_id
        result['InputList'] = []
        if self.input_list is not None:
            for k in self.input_list:
                result['InputList'].append(k.to_map() if k else None)
        else:
            result['InputList'] = None
        result['OutputList'] = []
        if self.output_list is not None:
            for k in self.output_list:
                result['OutputList'].append(k.to_map() if k else None)
        else:
            result['OutputList'] = None
        return result

    def from_map(self, map={}):
        self.auto_rerun_times = map.get('AutoRerunTimes')
        self.auto_rerun_interval_millis = map.get('AutoRerunIntervalMillis')
        self.rerun_mode = map.get('RerunMode')
        self.stop = map.get('Stop')
        self.para_value = map.get('ParaValue')
        self.start_effect_date = map.get('StartEffectDate')
        self.end_effect_date = map.get('EndEffectDate')
        self.cron_express = map.get('CronExpress')
        self.cycle_type = map.get('CycleType')
        self.dependent_type = map.get('DependentType')
        self.dependent_node_id_list = map.get('DependentNodeIdList')
        self.resource_group_id = map.get('ResourceGroupId')
        self.input_list = []
        if map.get('InputList') is not None:
            for k in map.get('InputList'):
                temp_model = GetFileResponseDataNodeConfigurationInputList()
                self.input_list.append(temp_model.from_map(k))
        else:
            self.input_list = None
        self.output_list = []
        if map.get('OutputList') is not None:
            for k in map.get('OutputList'):
                temp_model = GetFileResponseDataNodeConfigurationOutputList()
                self.output_list.append(temp_model.from_map(k))
        else:
            self.output_list = None
        return self


class GetFileResponseData(TeaModel):
    def __init__(self, file=None, node_configuration=None):
        self.file = file                # type: GetFileResponseDataFile
        self.node_configuration = node_configuration  # type: GetFileResponseDataNodeConfiguration

    def validate(self):
        self.validate_required(self.file, 'file')
        if self.file:
            self.file.validate()
        self.validate_required(self.node_configuration, 'node_configuration')
        if self.node_configuration:
            self.node_configuration.validate()

    def to_map(self):
        result = {}
        if self.file is not None:
            result['File'] = self.file.to_map()
        else:
            result['File'] = None
        if self.node_configuration is not None:
            result['NodeConfiguration'] = self.node_configuration.to_map()
        else:
            result['NodeConfiguration'] = None
        return result

    def from_map(self, map={}):
        if map.get('File') is not None:
            temp_model = GetFileResponseDataFile()
            self.file = temp_model.from_map(map['File'])
        else:
            self.file = None
        if map.get('NodeConfiguration') is not None:
            temp_model = GetFileResponseDataNodeConfiguration()
            self.node_configuration = temp_model.from_map(map['NodeConfiguration'])
        else:
            self.node_configuration = None
        return self


class ListBusinessRequest(TeaModel):
    def __init__(self, project_id=None, project_identifier=None, page_number=None, page_size=None, keyword=None):
        self.project_id = project_id    # type: int
        self.project_identifier = project_identifier  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size      # type: int
        self.keyword = keyword          # type: str

    def validate(self):
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_size, 'page_size')

    def to_map(self):
        result = {}
        result['ProjectId'] = self.project_id
        result['ProjectIdentifier'] = self.project_identifier
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        result['Keyword'] = self.keyword
        return result

    def from_map(self, map={}):
        self.project_id = map.get('ProjectId')
        self.project_identifier = map.get('ProjectIdentifier')
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        self.keyword = map.get('Keyword')
        return self


class ListBusinessResponse(TeaModel):
    def __init__(self, request_id=None, success=None, error_code=None, error_message=None, http_status_code=None,
                 data=None):
        self.request_id = request_id    # type: str
        self.success = success          # type: bool
        self.error_code = error_code    # type: str
        self.error_message = error_message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.data = data                # type: ListBusinessResponseData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.success, 'success')
        self.validate_required(self.error_code, 'error_code')
        self.validate_required(self.error_message, 'error_message')
        self.validate_required(self.http_status_code, 'http_status_code')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Success'] = self.success
        result['ErrorCode'] = self.error_code
        result['ErrorMessage'] = self.error_message
        result['HttpStatusCode'] = self.http_status_code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.success = map.get('Success')
        self.error_code = map.get('ErrorCode')
        self.error_message = map.get('ErrorMessage')
        self.http_status_code = map.get('HttpStatusCode')
        if map.get('Data') is not None:
            temp_model = ListBusinessResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class ListBusinessResponseDataBusiness(TeaModel):
    def __init__(self, business_id=None, business_name=None, project_id=None, owner=None, description=None,
                 use_type=None):
        self.business_id = business_id  # type: int
        self.business_name = business_name  # type: str
        self.project_id = project_id    # type: int
        self.owner = owner              # type: str
        self.description = description  # type: str
        self.use_type = use_type        # type: str

    def validate(self):
        self.validate_required(self.business_id, 'business_id')
        self.validate_required(self.business_name, 'business_name')
        self.validate_required(self.project_id, 'project_id')
        self.validate_required(self.owner, 'owner')
        self.validate_required(self.description, 'description')
        self.validate_required(self.use_type, 'use_type')

    def to_map(self):
        result = {}
        result['BusinessId'] = self.business_id
        result['BusinessName'] = self.business_name
        result['ProjectId'] = self.project_id
        result['Owner'] = self.owner
        result['Description'] = self.description
        result['UseType'] = self.use_type
        return result

    def from_map(self, map={}):
        self.business_id = map.get('BusinessId')
        self.business_name = map.get('BusinessName')
        self.project_id = map.get('ProjectId')
        self.owner = map.get('Owner')
        self.description = map.get('Description')
        self.use_type = map.get('UseType')
        return self


class ListBusinessResponseData(TeaModel):
    def __init__(self, page_number=None, page_size=None, total_count=None, business=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size      # type: int
        self.total_count = total_count  # type: int
        self.business = business        # type: List[ListBusinessResponseDataBusiness]

    def validate(self):
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.business, 'business')
        if self.business:
            for k in self.business:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        result['TotalCount'] = self.total_count
        result['Business'] = []
        if self.business is not None:
            for k in self.business:
                result['Business'].append(k.to_map() if k else None)
        else:
            result['Business'] = None
        return result

    def from_map(self, map={}):
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        self.total_count = map.get('TotalCount')
        self.business = []
        if map.get('Business') is not None:
            for k in map.get('Business'):
                temp_model = ListBusinessResponseDataBusiness()
                self.business.append(temp_model.from_map(k))
        else:
            self.business = None
        return self


class GetMetaDBTableListRequest(TeaModel):
    def __init__(self, page_number=None, page_size=None, app_guid=None, cluster_id=None, database_name=None,
                 data_source_type=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size      # type: int
        self.app_guid = app_guid        # type: str
        self.cluster_id = cluster_id    # type: str
        self.database_name = database_name  # type: str
        self.data_source_type = data_source_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        result['AppGuid'] = self.app_guid
        result['ClusterId'] = self.cluster_id
        result['DatabaseName'] = self.database_name
        result['DataSourceType'] = self.data_source_type
        return result

    def from_map(self, map={}):
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        self.app_guid = map.get('AppGuid')
        self.cluster_id = map.get('ClusterId')
        self.database_name = map.get('DatabaseName')
        self.data_source_type = map.get('DataSourceType')
        return self


class GetMetaDBTableListResponse(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = request_id    # type: str
        self.data = data                # type: GetMetaDBTableListResponseData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('Data') is not None:
            temp_model = GetMetaDBTableListResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class GetMetaDBTableListResponseDataTableEntityList(TeaModel):
    def __init__(self, table_name=None, table_guid=None, database_name=None):
        self.table_name = table_name    # type: str
        self.table_guid = table_guid    # type: str
        self.database_name = database_name  # type: str

    def validate(self):
        self.validate_required(self.table_name, 'table_name')
        self.validate_required(self.table_guid, 'table_guid')
        self.validate_required(self.database_name, 'database_name')

    def to_map(self):
        result = {}
        result['TableName'] = self.table_name
        result['TableGuid'] = self.table_guid
        result['DatabaseName'] = self.database_name
        return result

    def from_map(self, map={}):
        self.table_name = map.get('TableName')
        self.table_guid = map.get('TableGuid')
        self.database_name = map.get('DatabaseName')
        return self


class GetMetaDBTableListResponseData(TeaModel):
    def __init__(self, page_number=None, page_size=None, total_count=None, table_entity_list=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size      # type: int
        self.total_count = total_count  # type: int
        self.table_entity_list = table_entity_list  # type: List[GetMetaDBTableListResponseDataTableEntityList]

    def validate(self):
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.table_entity_list, 'table_entity_list')
        if self.table_entity_list:
            for k in self.table_entity_list:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        result['TotalCount'] = self.total_count
        result['TableEntityList'] = []
        if self.table_entity_list is not None:
            for k in self.table_entity_list:
                result['TableEntityList'].append(k.to_map() if k else None)
        else:
            result['TableEntityList'] = None
        return result

    def from_map(self, map={}):
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        self.total_count = map.get('TotalCount')
        self.table_entity_list = []
        if map.get('TableEntityList') is not None:
            for k in map.get('TableEntityList'):
                temp_model = GetMetaDBTableListResponseDataTableEntityList()
                self.table_entity_list.append(temp_model.from_map(k))
        else:
            self.table_entity_list = None
        return self


class CheckMetaTableRequest(TeaModel):
    def __init__(self, table_guid=None, cluster_id=None, database_name=None, table_name=None, data_source_type=None):
        self.table_guid = table_guid    # type: str
        self.cluster_id = cluster_id    # type: str
        self.database_name = database_name  # type: str
        self.table_name = table_name    # type: str
        self.data_source_type = data_source_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['TableGuid'] = self.table_guid
        result['ClusterId'] = self.cluster_id
        result['DatabaseName'] = self.database_name
        result['TableName'] = self.table_name
        result['DataSourceType'] = self.data_source_type
        return result

    def from_map(self, map={}):
        self.table_guid = map.get('TableGuid')
        self.cluster_id = map.get('ClusterId')
        self.database_name = map.get('DatabaseName')
        self.table_name = map.get('TableName')
        self.data_source_type = map.get('DataSourceType')
        return self


class CheckMetaTableResponse(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = request_id    # type: str
        self.data = data                # type: bool

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Data'] = self.data
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.data = map.get('Data')
        return self


class GetFolderRequest(TeaModel):
    def __init__(self, project_id=None, project_identifier=None, folder_id=None, folder_path=None):
        self.project_id = project_id    # type: int
        self.project_identifier = project_identifier  # type: str
        self.folder_id = folder_id      # type: str
        self.folder_path = folder_path  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['ProjectId'] = self.project_id
        result['ProjectIdentifier'] = self.project_identifier
        result['FolderId'] = self.folder_id
        result['FolderPath'] = self.folder_path
        return result

    def from_map(self, map={}):
        self.project_id = map.get('ProjectId')
        self.project_identifier = map.get('ProjectIdentifier')
        self.folder_id = map.get('FolderId')
        self.folder_path = map.get('FolderPath')
        return self


class GetFolderResponse(TeaModel):
    def __init__(self, request_id=None, success=None, error_code=None, error_message=None, http_status_code=None,
                 data=None):
        self.request_id = request_id    # type: str
        self.success = success          # type: bool
        self.error_code = error_code    # type: str
        self.error_message = error_message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.data = data                # type: GetFolderResponseData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.success, 'success')
        self.validate_required(self.error_code, 'error_code')
        self.validate_required(self.error_message, 'error_message')
        self.validate_required(self.http_status_code, 'http_status_code')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Success'] = self.success
        result['ErrorCode'] = self.error_code
        result['ErrorMessage'] = self.error_message
        result['HttpStatusCode'] = self.http_status_code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.success = map.get('Success')
        self.error_code = map.get('ErrorCode')
        self.error_message = map.get('ErrorMessage')
        self.http_status_code = map.get('HttpStatusCode')
        if map.get('Data') is not None:
            temp_model = GetFolderResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class GetFolderResponseData(TeaModel):
    def __init__(self, folder_id=None, folder_path=None):
        self.folder_id = folder_id      # type: str
        self.folder_path = folder_path  # type: str

    def validate(self):
        self.validate_required(self.folder_id, 'folder_id')
        self.validate_required(self.folder_path, 'folder_path')

    def to_map(self):
        result = {}
        result['FolderId'] = self.folder_id
        result['FolderPath'] = self.folder_path
        return result

    def from_map(self, map={}):
        self.folder_id = map.get('FolderId')
        self.folder_path = map.get('FolderPath')
        return self


class DeployFileRequest(TeaModel):
    def __init__(self, project_id=None, project_identifier=None, file_id=None, comment=None, node_id=None):
        self.project_id = project_id    # type: int
        self.project_identifier = project_identifier  # type: str
        self.file_id = file_id          # type: int
        self.comment = comment          # type: str
        self.node_id = node_id          # type: int

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['ProjectId'] = self.project_id
        result['ProjectIdentifier'] = self.project_identifier
        result['FileId'] = self.file_id
        result['Comment'] = self.comment
        result['NodeId'] = self.node_id
        return result

    def from_map(self, map={}):
        self.project_id = map.get('ProjectId')
        self.project_identifier = map.get('ProjectIdentifier')
        self.file_id = map.get('FileId')
        self.comment = map.get('Comment')
        self.node_id = map.get('NodeId')
        return self


class DeployFileResponse(TeaModel):
    def __init__(self, request_id=None, success=None, error_code=None, error_message=None, data=None,
                 http_status_code=None):
        self.request_id = request_id    # type: str
        self.success = success          # type: bool
        self.error_code = error_code    # type: str
        self.error_message = error_message  # type: str
        self.data = data                # type: int
        self.http_status_code = http_status_code  # type: int

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.success, 'success')
        self.validate_required(self.error_code, 'error_code')
        self.validate_required(self.error_message, 'error_message')
        self.validate_required(self.data, 'data')
        self.validate_required(self.http_status_code, 'http_status_code')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Success'] = self.success
        result['ErrorCode'] = self.error_code
        result['ErrorMessage'] = self.error_message
        result['Data'] = self.data
        result['HttpStatusCode'] = self.http_status_code
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.success = map.get('Success')
        self.error_code = map.get('ErrorCode')
        self.error_message = map.get('ErrorMessage')
        self.data = map.get('Data')
        self.http_status_code = map.get('HttpStatusCode')
        return self


class DeleteBusinessRequest(TeaModel):
    def __init__(self, project_id=None, project_identifier=None, business_id=None):
        self.project_id = project_id    # type: int
        self.project_identifier = project_identifier  # type: str
        self.business_id = business_id  # type: int

    def validate(self):
        self.validate_required(self.business_id, 'business_id')

    def to_map(self):
        result = {}
        result['ProjectId'] = self.project_id
        result['ProjectIdentifier'] = self.project_identifier
        result['BusinessId'] = self.business_id
        return result

    def from_map(self, map={}):
        self.project_id = map.get('ProjectId')
        self.project_identifier = map.get('ProjectIdentifier')
        self.business_id = map.get('BusinessId')
        return self


class DeleteBusinessResponse(TeaModel):
    def __init__(self, request_id=None, success=None, error_code=None, error_message=None, http_status_code=None):
        self.request_id = request_id    # type: str
        self.success = success          # type: bool
        self.error_code = error_code    # type: str
        self.error_message = error_message  # type: str
        self.http_status_code = http_status_code  # type: int

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.success, 'success')
        self.validate_required(self.error_code, 'error_code')
        self.validate_required(self.error_message, 'error_message')
        self.validate_required(self.http_status_code, 'http_status_code')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Success'] = self.success
        result['ErrorCode'] = self.error_code
        result['ErrorMessage'] = self.error_message
        result['HttpStatusCode'] = self.http_status_code
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.success = map.get('Success')
        self.error_code = map.get('ErrorCode')
        self.error_message = map.get('ErrorMessage')
        self.http_status_code = map.get('HttpStatusCode')
        return self


class DeleteFileRequest(TeaModel):
    def __init__(self, project_id=None, project_identifier=None, file_id=None):
        self.project_id = project_id    # type: int
        self.project_identifier = project_identifier  # type: str
        self.file_id = file_id          # type: int

    def validate(self):
        self.validate_required(self.file_id, 'file_id')

    def to_map(self):
        result = {}
        result['ProjectId'] = self.project_id
        result['ProjectIdentifier'] = self.project_identifier
        result['FileId'] = self.file_id
        return result

    def from_map(self, map={}):
        self.project_id = map.get('ProjectId')
        self.project_identifier = map.get('ProjectIdentifier')
        self.file_id = map.get('FileId')
        return self


class DeleteFileResponse(TeaModel):
    def __init__(self, request_id=None, success=None, error_code=None, error_message=None, http_status_code=None):
        self.request_id = request_id    # type: str
        self.success = success          # type: bool
        self.error_code = error_code    # type: str
        self.error_message = error_message  # type: str
        self.http_status_code = http_status_code  # type: int

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.success, 'success')
        self.validate_required(self.error_code, 'error_code')
        self.validate_required(self.error_message, 'error_message')
        self.validate_required(self.http_status_code, 'http_status_code')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Success'] = self.success
        result['ErrorCode'] = self.error_code
        result['ErrorMessage'] = self.error_message
        result['HttpStatusCode'] = self.http_status_code
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.success = map.get('Success')
        self.error_code = map.get('ErrorCode')
        self.error_message = map.get('ErrorMessage')
        self.http_status_code = map.get('HttpStatusCode')
        return self


class ListQualityRulesRequest(TeaModel):
    def __init__(self, project_name=None, entity_id=None, page_number=None, page_size=None):
        self.project_name = project_name  # type: str
        self.entity_id = entity_id      # type: int
        self.page_number = page_number  # type: int
        self.page_size = page_size      # type: int

    def validate(self):
        self.validate_required(self.project_name, 'project_name')
        self.validate_required(self.entity_id, 'entity_id')
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_size, 'page_size')

    def to_map(self):
        result = {}
        result['ProjectName'] = self.project_name
        result['EntityId'] = self.entity_id
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        return result

    def from_map(self, map={}):
        self.project_name = map.get('ProjectName')
        self.entity_id = map.get('EntityId')
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        return self


class ListQualityRulesResponse(TeaModel):
    def __init__(self, error_code=None, success=None, error_message=None, http_status_code=None, request_id=None,
                 data=None):
        self.error_code = error_code    # type: str
        self.success = success          # type: bool
        self.error_message = error_message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.request_id = request_id    # type: str
        self.data = data                # type: ListQualityRulesResponseData

    def validate(self):
        self.validate_required(self.error_code, 'error_code')
        self.validate_required(self.success, 'success')
        self.validate_required(self.error_message, 'error_message')
        self.validate_required(self.http_status_code, 'http_status_code')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['ErrorCode'] = self.error_code
        result['Success'] = self.success
        result['ErrorMessage'] = self.error_message
        result['HttpStatusCode'] = self.http_status_code
        result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.error_code = map.get('ErrorCode')
        self.success = map.get('Success')
        self.error_message = map.get('ErrorMessage')
        self.http_status_code = map.get('HttpStatusCode')
        self.request_id = map.get('RequestId')
        if map.get('Data') is not None:
            temp_model = ListQualityRulesResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class ListQualityRulesResponseDataRules(TeaModel):
    def __init__(self, project_name=None, table_name=None, id=None, entity_id=None, property=None, method_id=None,
                 method_name=None, on_duty=None, rule_type=None, block_type=None, template_id=None, template_name=None,
                 rule_checker_relation_id=None, checker_id=None, fix_check=None, trend=None, warning_threshold=None, critical_threshold=None,
                 history_warning_threshold=None, history_critical_threshold=None, property_key=None, match_expression=None, comment=None,
                 expect_value=None):
        self.project_name = project_name  # type: str
        self.table_name = table_name    # type: str
        self.id = id                    # type: int
        self.entity_id = entity_id      # type: int
        self.property = property        # type: str
        self.method_id = method_id      # type: int
        self.method_name = method_name  # type: str
        self.on_duty = on_duty          # type: str
        self.rule_type = rule_type      # type: int
        self.block_type = block_type    # type: int
        self.template_id = template_id  # type: int
        self.template_name = template_name  # type: str
        self.rule_checker_relation_id = rule_checker_relation_id  # type: int
        self.checker_id = checker_id    # type: int
        self.fix_check = fix_check      # type: bool
        self.trend = trend              # type: str
        self.warning_threshold = warning_threshold  # type: str
        self.critical_threshold = critical_threshold  # type: str
        self.history_warning_threshold = history_warning_threshold  # type: str
        self.history_critical_threshold = history_critical_threshold  # type: str
        self.property_key = property_key  # type: str
        self.match_expression = match_expression  # type: str
        self.comment = comment          # type: str
        self.expect_value = expect_value  # type: str

    def validate(self):
        self.validate_required(self.project_name, 'project_name')
        self.validate_required(self.table_name, 'table_name')
        self.validate_required(self.id, 'id')
        self.validate_required(self.entity_id, 'entity_id')
        self.validate_required(self.property, 'property')
        self.validate_required(self.method_id, 'method_id')
        self.validate_required(self.method_name, 'method_name')
        self.validate_required(self.on_duty, 'on_duty')
        self.validate_required(self.rule_type, 'rule_type')
        self.validate_required(self.block_type, 'block_type')
        self.validate_required(self.template_id, 'template_id')
        self.validate_required(self.template_name, 'template_name')
        self.validate_required(self.rule_checker_relation_id, 'rule_checker_relation_id')
        self.validate_required(self.checker_id, 'checker_id')
        self.validate_required(self.fix_check, 'fix_check')
        self.validate_required(self.trend, 'trend')
        self.validate_required(self.warning_threshold, 'warning_threshold')
        self.validate_required(self.critical_threshold, 'critical_threshold')
        self.validate_required(self.history_warning_threshold, 'history_warning_threshold')
        self.validate_required(self.history_critical_threshold, 'history_critical_threshold')
        self.validate_required(self.property_key, 'property_key')
        self.validate_required(self.match_expression, 'match_expression')
        self.validate_required(self.comment, 'comment')
        self.validate_required(self.expect_value, 'expect_value')

    def to_map(self):
        result = {}
        result['ProjectName'] = self.project_name
        result['TableName'] = self.table_name
        result['Id'] = self.id
        result['EntityId'] = self.entity_id
        result['Property'] = self.property
        result['MethodId'] = self.method_id
        result['MethodName'] = self.method_name
        result['OnDuty'] = self.on_duty
        result['RuleType'] = self.rule_type
        result['BlockType'] = self.block_type
        result['TemplateId'] = self.template_id
        result['TemplateName'] = self.template_name
        result['RuleCheckerRelationId'] = self.rule_checker_relation_id
        result['CheckerId'] = self.checker_id
        result['FixCheck'] = self.fix_check
        result['Trend'] = self.trend
        result['WarningThreshold'] = self.warning_threshold
        result['CriticalThreshold'] = self.critical_threshold
        result['HistoryWarningThreshold'] = self.history_warning_threshold
        result['HistoryCriticalThreshold'] = self.history_critical_threshold
        result['PropertyKey'] = self.property_key
        result['MatchExpression'] = self.match_expression
        result['Comment'] = self.comment
        result['ExpectValue'] = self.expect_value
        return result

    def from_map(self, map={}):
        self.project_name = map.get('ProjectName')
        self.table_name = map.get('TableName')
        self.id = map.get('Id')
        self.entity_id = map.get('EntityId')
        self.property = map.get('Property')
        self.method_id = map.get('MethodId')
        self.method_name = map.get('MethodName')
        self.on_duty = map.get('OnDuty')
        self.rule_type = map.get('RuleType')
        self.block_type = map.get('BlockType')
        self.template_id = map.get('TemplateId')
        self.template_name = map.get('TemplateName')
        self.rule_checker_relation_id = map.get('RuleCheckerRelationId')
        self.checker_id = map.get('CheckerId')
        self.fix_check = map.get('FixCheck')
        self.trend = map.get('Trend')
        self.warning_threshold = map.get('WarningThreshold')
        self.critical_threshold = map.get('CriticalThreshold')
        self.history_warning_threshold = map.get('HistoryWarningThreshold')
        self.history_critical_threshold = map.get('HistoryCriticalThreshold')
        self.property_key = map.get('PropertyKey')
        self.match_expression = map.get('MatchExpression')
        self.comment = map.get('Comment')
        self.expect_value = map.get('ExpectValue')
        return self


class ListQualityRulesResponseData(TeaModel):
    def __init__(self, total_count=None, page_number=None, page_size=None, rules=None):
        self.total_count = total_count  # type: int
        self.page_number = page_number  # type: int
        self.page_size = page_size      # type: int
        self.rules = rules              # type: List[ListQualityRulesResponseDataRules]

    def validate(self):
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.rules, 'rules')
        if self.rules:
            for k in self.rules:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['TotalCount'] = self.total_count
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        result['Rules'] = []
        if self.rules is not None:
            for k in self.rules:
                result['Rules'].append(k.to_map() if k else None)
        else:
            result['Rules'] = None
        return result

    def from_map(self, map={}):
        self.total_count = map.get('TotalCount')
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        self.rules = []
        if map.get('Rules') is not None:
            for k in map.get('Rules'):
                temp_model = ListQualityRulesResponseDataRules()
                self.rules.append(temp_model.from_map(k))
        else:
            self.rules = None
        return self


class CreateRemindRequest(TeaModel):
    def __init__(self, remind_name=None, dnd_end=None, remind_unit=None, node_ids=None, baseline_ids=None,
                 project_id=None, biz_process_ids=None, remind_type=None, max_alert_times=None, alert_interval=None,
                 detail=None, alert_unit=None, alert_methods=None, alert_targets=None, robot_urls=None):
        self.remind_name = remind_name  # type: str
        self.dnd_end = dnd_end          # type: str
        self.remind_unit = remind_unit  # type: str
        self.node_ids = node_ids        # type: str
        self.baseline_ids = baseline_ids  # type: str
        self.project_id = project_id    # type: int
        self.biz_process_ids = biz_process_ids  # type: str
        self.remind_type = remind_type  # type: str
        self.max_alert_times = max_alert_times  # type: int
        self.alert_interval = alert_interval  # type: int
        self.detail = detail            # type: str
        self.alert_unit = alert_unit    # type: str
        self.alert_methods = alert_methods  # type: str
        self.alert_targets = alert_targets  # type: str
        self.robot_urls = robot_urls    # type: str

    def validate(self):
        self.validate_required(self.remind_name, 'remind_name')
        self.validate_required(self.remind_unit, 'remind_unit')
        self.validate_required(self.remind_type, 'remind_type')
        self.validate_required(self.alert_unit, 'alert_unit')

    def to_map(self):
        result = {}
        result['RemindName'] = self.remind_name
        result['DndEnd'] = self.dnd_end
        result['RemindUnit'] = self.remind_unit
        result['NodeIds'] = self.node_ids
        result['BaselineIds'] = self.baseline_ids
        result['ProjectId'] = self.project_id
        result['BizProcessIds'] = self.biz_process_ids
        result['RemindType'] = self.remind_type
        result['MaxAlertTimes'] = self.max_alert_times
        result['AlertInterval'] = self.alert_interval
        result['Detail'] = self.detail
        result['AlertUnit'] = self.alert_unit
        result['AlertMethods'] = self.alert_methods
        result['AlertTargets'] = self.alert_targets
        result['RobotUrls'] = self.robot_urls
        return result

    def from_map(self, map={}):
        self.remind_name = map.get('RemindName')
        self.dnd_end = map.get('DndEnd')
        self.remind_unit = map.get('RemindUnit')
        self.node_ids = map.get('NodeIds')
        self.baseline_ids = map.get('BaselineIds')
        self.project_id = map.get('ProjectId')
        self.biz_process_ids = map.get('BizProcessIds')
        self.remind_type = map.get('RemindType')
        self.max_alert_times = map.get('MaxAlertTimes')
        self.alert_interval = map.get('AlertInterval')
        self.detail = map.get('Detail')
        self.alert_unit = map.get('AlertUnit')
        self.alert_methods = map.get('AlertMethods')
        self.alert_targets = map.get('AlertTargets')
        self.robot_urls = map.get('RobotUrls')
        return self


class CreateRemindResponse(TeaModel):
    def __init__(self, success=None, error_code=None, error_message=None, http_status_code=None, request_id=None,
                 data=None):
        self.success = success          # type: bool
        self.error_code = error_code    # type: str
        self.error_message = error_message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.request_id = request_id    # type: str
        self.data = data                # type: int

    def validate(self):
        self.validate_required(self.success, 'success')
        self.validate_required(self.error_code, 'error_code')
        self.validate_required(self.error_message, 'error_message')
        self.validate_required(self.http_status_code, 'http_status_code')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')

    def to_map(self):
        result = {}
        result['Success'] = self.success
        result['ErrorCode'] = self.error_code
        result['ErrorMessage'] = self.error_message
        result['HttpStatusCode'] = self.http_status_code
        result['RequestId'] = self.request_id
        result['Data'] = self.data
        return result

    def from_map(self, map={}):
        self.success = map.get('Success')
        self.error_code = map.get('ErrorCode')
        self.error_message = map.get('ErrorMessage')
        self.http_status_code = map.get('HttpStatusCode')
        self.request_id = map.get('RequestId')
        self.data = map.get('Data')
        return self


class GetQualityRuleRequest(TeaModel):
    def __init__(self, rule_id=None, project_name=None):
        self.rule_id = rule_id          # type: int
        self.project_name = project_name  # type: str

    def validate(self):
        self.validate_required(self.rule_id, 'rule_id')
        self.validate_required(self.project_name, 'project_name')

    def to_map(self):
        result = {}
        result['RuleId'] = self.rule_id
        result['ProjectName'] = self.project_name
        return result

    def from_map(self, map={}):
        self.rule_id = map.get('RuleId')
        self.project_name = map.get('ProjectName')
        return self


class GetQualityRuleResponse(TeaModel):
    def __init__(self, success=None, error_code=None, error_message=None, http_status_code=None, request_id=None,
                 data=None):
        self.success = success          # type: bool
        self.error_code = error_code    # type: str
        self.error_message = error_message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.request_id = request_id    # type: str
        self.data = data                # type: GetQualityRuleResponseData

    def validate(self):
        self.validate_required(self.success, 'success')
        self.validate_required(self.error_code, 'error_code')
        self.validate_required(self.error_message, 'error_message')
        self.validate_required(self.http_status_code, 'http_status_code')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['Success'] = self.success
        result['ErrorCode'] = self.error_code
        result['ErrorMessage'] = self.error_message
        result['HttpStatusCode'] = self.http_status_code
        result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.success = map.get('Success')
        self.error_code = map.get('ErrorCode')
        self.error_message = map.get('ErrorMessage')
        self.http_status_code = map.get('HttpStatusCode')
        self.request_id = map.get('RequestId')
        if map.get('Data') is not None:
            temp_model = GetQualityRuleResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class GetQualityRuleResponseData(TeaModel):
    def __init__(self, id=None, entity_id=None, property=None, method_id=None, method_name=None,
                 where_condition=None, on_duty=None, rule_type=None, block_type=None, template_id=None, template_name=None,
                 comment=None, rule_name=None, predict_type=None, warning_threshold=None, critical_threshold=None,
                 operator=None, expect_value=None, trend=None, checker_name=None, checker=None, fix_check=None):
        self.id = id                    # type: int
        self.entity_id = entity_id      # type: int
        self.property = property        # type: str
        self.method_id = method_id      # type: int
        self.method_name = method_name  # type: str
        self.where_condition = where_condition  # type: str
        self.on_duty = on_duty          # type: str
        self.rule_type = rule_type      # type: int
        self.block_type = block_type    # type: int
        self.template_id = template_id  # type: int
        self.template_name = template_name  # type: str
        self.comment = comment          # type: str
        self.rule_name = rule_name      # type: str
        self.predict_type = predict_type  # type: int
        self.warning_threshold = warning_threshold  # type: str
        self.critical_threshold = critical_threshold  # type: str
        self.operator = operator        # type: str
        self.expect_value = expect_value  # type: str
        self.trend = trend              # type: str
        self.checker_name = checker_name  # type: str
        self.checker = checker          # type: int
        self.fix_check = fix_check      # type: bool

    def validate(self):
        self.validate_required(self.id, 'id')
        self.validate_required(self.entity_id, 'entity_id')
        self.validate_required(self.property, 'property')
        self.validate_required(self.method_id, 'method_id')
        self.validate_required(self.method_name, 'method_name')
        self.validate_required(self.where_condition, 'where_condition')
        self.validate_required(self.on_duty, 'on_duty')
        self.validate_required(self.rule_type, 'rule_type')
        self.validate_required(self.block_type, 'block_type')
        self.validate_required(self.template_id, 'template_id')
        self.validate_required(self.template_name, 'template_name')
        self.validate_required(self.comment, 'comment')
        self.validate_required(self.rule_name, 'rule_name')
        self.validate_required(self.predict_type, 'predict_type')
        self.validate_required(self.warning_threshold, 'warning_threshold')
        self.validate_required(self.critical_threshold, 'critical_threshold')
        self.validate_required(self.operator, 'operator')
        self.validate_required(self.expect_value, 'expect_value')
        self.validate_required(self.trend, 'trend')
        self.validate_required(self.checker_name, 'checker_name')
        self.validate_required(self.checker, 'checker')
        self.validate_required(self.fix_check, 'fix_check')

    def to_map(self):
        result = {}
        result['Id'] = self.id
        result['EntityId'] = self.entity_id
        result['Property'] = self.property
        result['MethodId'] = self.method_id
        result['MethodName'] = self.method_name
        result['WhereCondition'] = self.where_condition
        result['OnDuty'] = self.on_duty
        result['RuleType'] = self.rule_type
        result['BlockType'] = self.block_type
        result['TemplateId'] = self.template_id
        result['TemplateName'] = self.template_name
        result['Comment'] = self.comment
        result['RuleName'] = self.rule_name
        result['PredictType'] = self.predict_type
        result['WarningThreshold'] = self.warning_threshold
        result['CriticalThreshold'] = self.critical_threshold
        result['Operator'] = self.operator
        result['ExpectValue'] = self.expect_value
        result['Trend'] = self.trend
        result['CheckerName'] = self.checker_name
        result['Checker'] = self.checker
        result['FixCheck'] = self.fix_check
        return result

    def from_map(self, map={}):
        self.id = map.get('Id')
        self.entity_id = map.get('EntityId')
        self.property = map.get('Property')
        self.method_id = map.get('MethodId')
        self.method_name = map.get('MethodName')
        self.where_condition = map.get('WhereCondition')
        self.on_duty = map.get('OnDuty')
        self.rule_type = map.get('RuleType')
        self.block_type = map.get('BlockType')
        self.template_id = map.get('TemplateId')
        self.template_name = map.get('TemplateName')
        self.comment = map.get('Comment')
        self.rule_name = map.get('RuleName')
        self.predict_type = map.get('PredictType')
        self.warning_threshold = map.get('WarningThreshold')
        self.critical_threshold = map.get('CriticalThreshold')
        self.operator = map.get('Operator')
        self.expect_value = map.get('ExpectValue')
        self.trend = map.get('Trend')
        self.checker_name = map.get('CheckerName')
        self.checker = map.get('Checker')
        self.fix_check = map.get('FixCheck')
        return self


class GetDeploymentRequest(TeaModel):
    def __init__(self, project_id=None, project_identifier=None, deployment_id=None):
        self.project_id = project_id    # type: int
        self.project_identifier = project_identifier  # type: str
        self.deployment_id = deployment_id  # type: int

    def validate(self):
        self.validate_required(self.deployment_id, 'deployment_id')

    def to_map(self):
        result = {}
        result['ProjectId'] = self.project_id
        result['ProjectIdentifier'] = self.project_identifier
        result['DeploymentId'] = self.deployment_id
        return result

    def from_map(self, map={}):
        self.project_id = map.get('ProjectId')
        self.project_identifier = map.get('ProjectIdentifier')
        self.deployment_id = map.get('DeploymentId')
        return self


class GetDeploymentResponse(TeaModel):
    def __init__(self, request_id=None, success=None, error_code=None, error_message=None, http_status_code=None,
                 data=None):
        self.request_id = request_id    # type: str
        self.success = success          # type: bool
        self.error_code = error_code    # type: str
        self.error_message = error_message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.data = data                # type: GetDeploymentResponseData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.success, 'success')
        self.validate_required(self.error_code, 'error_code')
        self.validate_required(self.error_message, 'error_message')
        self.validate_required(self.http_status_code, 'http_status_code')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Success'] = self.success
        result['ErrorCode'] = self.error_code
        result['ErrorMessage'] = self.error_message
        result['HttpStatusCode'] = self.http_status_code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.success = map.get('Success')
        self.error_code = map.get('ErrorCode')
        self.error_message = map.get('ErrorMessage')
        self.http_status_code = map.get('HttpStatusCode')
        if map.get('Data') is not None:
            temp_model = GetDeploymentResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class GetDeploymentResponseDataDeployment(TeaModel):
    def __init__(self, name=None, creator_id=None, handler_id=None, create_time=None, execute_time=None, status=None,
                 from_environment=None, to_environment=None, error_message=None):
        self.name = name                # type: str
        self.creator_id = creator_id    # type: str
        self.handler_id = handler_id    # type: str
        self.create_time = create_time  # type: int
        self.execute_time = execute_time  # type: int
        self.status = status            # type: int
        self.from_environment = from_environment  # type: int
        self.to_environment = to_environment  # type: int
        self.error_message = error_message  # type: str

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.creator_id, 'creator_id')
        self.validate_required(self.handler_id, 'handler_id')
        self.validate_required(self.create_time, 'create_time')
        self.validate_required(self.execute_time, 'execute_time')
        self.validate_required(self.status, 'status')
        self.validate_required(self.from_environment, 'from_environment')
        self.validate_required(self.to_environment, 'to_environment')
        self.validate_required(self.error_message, 'error_message')

    def to_map(self):
        result = {}
        result['Name'] = self.name
        result['CreatorId'] = self.creator_id
        result['HandlerId'] = self.handler_id
        result['CreateTime'] = self.create_time
        result['ExecuteTime'] = self.execute_time
        result['Status'] = self.status
        result['FromEnvironment'] = self.from_environment
        result['ToEnvironment'] = self.to_environment
        result['ErrorMessage'] = self.error_message
        return result

    def from_map(self, map={}):
        self.name = map.get('Name')
        self.creator_id = map.get('CreatorId')
        self.handler_id = map.get('HandlerId')
        self.create_time = map.get('CreateTime')
        self.execute_time = map.get('ExecuteTime')
        self.status = map.get('Status')
        self.from_environment = map.get('FromEnvironment')
        self.to_environment = map.get('ToEnvironment')
        self.error_message = map.get('ErrorMessage')
        return self


class GetDeploymentResponseData(TeaModel):
    def __init__(self, deployment=None):
        self.deployment = deployment    # type: GetDeploymentResponseDataDeployment

    def validate(self):
        self.validate_required(self.deployment, 'deployment')
        if self.deployment:
            self.deployment.validate()

    def to_map(self):
        result = {}
        if self.deployment is not None:
            result['Deployment'] = self.deployment.to_map()
        else:
            result['Deployment'] = None
        return result

    def from_map(self, map={}):
        if map.get('Deployment') is not None:
            temp_model = GetDeploymentResponseDataDeployment()
            self.deployment = temp_model.from_map(map['Deployment'])
        else:
            self.deployment = None
        return self


class UpdateRemindRequest(TeaModel):
    def __init__(self, remind_id=None, remind_name=None, dnd_end=None, remind_unit=None, node_ids=None,
                 baseline_ids=None, project_id=None, biz_process_ids=None, remind_type=None, max_alert_times=None,
                 alert_interval=None, detail=None, alert_unit=None, alert_methods=None, alert_targets=None, use_flag=None,
                 robot_urls=None):
        self.remind_id = remind_id      # type: int
        self.remind_name = remind_name  # type: str
        self.dnd_end = dnd_end          # type: str
        self.remind_unit = remind_unit  # type: str
        self.node_ids = node_ids        # type: str
        self.baseline_ids = baseline_ids  # type: str
        self.project_id = project_id    # type: int
        self.biz_process_ids = biz_process_ids  # type: str
        self.remind_type = remind_type  # type: str
        self.max_alert_times = max_alert_times  # type: int
        self.alert_interval = alert_interval  # type: int
        self.detail = detail            # type: str
        self.alert_unit = alert_unit    # type: str
        self.alert_methods = alert_methods  # type: str
        self.alert_targets = alert_targets  # type: str
        self.use_flag = use_flag        # type: bool
        self.robot_urls = robot_urls    # type: str

    def validate(self):
        self.validate_required(self.remind_id, 'remind_id')

    def to_map(self):
        result = {}
        result['RemindId'] = self.remind_id
        result['RemindName'] = self.remind_name
        result['DndEnd'] = self.dnd_end
        result['RemindUnit'] = self.remind_unit
        result['NodeIds'] = self.node_ids
        result['BaselineIds'] = self.baseline_ids
        result['ProjectId'] = self.project_id
        result['BizProcessIds'] = self.biz_process_ids
        result['RemindType'] = self.remind_type
        result['MaxAlertTimes'] = self.max_alert_times
        result['AlertInterval'] = self.alert_interval
        result['Detail'] = self.detail
        result['AlertUnit'] = self.alert_unit
        result['AlertMethods'] = self.alert_methods
        result['AlertTargets'] = self.alert_targets
        result['UseFlag'] = self.use_flag
        result['RobotUrls'] = self.robot_urls
        return result

    def from_map(self, map={}):
        self.remind_id = map.get('RemindId')
        self.remind_name = map.get('RemindName')
        self.dnd_end = map.get('DndEnd')
        self.remind_unit = map.get('RemindUnit')
        self.node_ids = map.get('NodeIds')
        self.baseline_ids = map.get('BaselineIds')
        self.project_id = map.get('ProjectId')
        self.biz_process_ids = map.get('BizProcessIds')
        self.remind_type = map.get('RemindType')
        self.max_alert_times = map.get('MaxAlertTimes')
        self.alert_interval = map.get('AlertInterval')
        self.detail = map.get('Detail')
        self.alert_unit = map.get('AlertUnit')
        self.alert_methods = map.get('AlertMethods')
        self.alert_targets = map.get('AlertTargets')
        self.use_flag = map.get('UseFlag')
        self.robot_urls = map.get('RobotUrls')
        return self


class UpdateRemindResponse(TeaModel):
    def __init__(self, success=None, error_code=None, error_message=None, http_status_code=None, request_id=None,
                 data=None):
        self.success = success          # type: bool
        self.error_code = error_code    # type: str
        self.error_message = error_message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.request_id = request_id    # type: str
        self.data = data                # type: bool

    def validate(self):
        self.validate_required(self.success, 'success')
        self.validate_required(self.error_code, 'error_code')
        self.validate_required(self.error_message, 'error_message')
        self.validate_required(self.http_status_code, 'http_status_code')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')

    def to_map(self):
        result = {}
        result['Success'] = self.success
        result['ErrorCode'] = self.error_code
        result['ErrorMessage'] = self.error_message
        result['HttpStatusCode'] = self.http_status_code
        result['RequestId'] = self.request_id
        result['Data'] = self.data
        return result

    def from_map(self, map={}):
        self.success = map.get('Success')
        self.error_code = map.get('ErrorCode')
        self.error_message = map.get('ErrorMessage')
        self.http_status_code = map.get('HttpStatusCode')
        self.request_id = map.get('RequestId')
        self.data = map.get('Data')
        return self


class GetMetaColumnLineageRequest(TeaModel):
    def __init__(self, column_guid=None, direction=None, page_num=None, page_size=None, cluster_id=None,
                 database_name=None, table_name=None, column_name=None, data_source_type=None):
        self.column_guid = column_guid  # type: str
        self.direction = direction      # type: str
        self.page_num = page_num        # type: int
        self.page_size = page_size      # type: int
        self.cluster_id = cluster_id    # type: str
        self.database_name = database_name  # type: str
        self.table_name = table_name    # type: str
        self.column_name = column_name  # type: str
        self.data_source_type = data_source_type  # type: str

    def validate(self):
        self.validate_required(self.direction, 'direction')

    def to_map(self):
        result = {}
        result['ColumnGuid'] = self.column_guid
        result['Direction'] = self.direction
        result['PageNum'] = self.page_num
        result['PageSize'] = self.page_size
        result['ClusterId'] = self.cluster_id
        result['DatabaseName'] = self.database_name
        result['TableName'] = self.table_name
        result['ColumnName'] = self.column_name
        result['DataSourceType'] = self.data_source_type
        return result

    def from_map(self, map={}):
        self.column_guid = map.get('ColumnGuid')
        self.direction = map.get('Direction')
        self.page_num = map.get('PageNum')
        self.page_size = map.get('PageSize')
        self.cluster_id = map.get('ClusterId')
        self.database_name = map.get('DatabaseName')
        self.table_name = map.get('TableName')
        self.column_name = map.get('ColumnName')
        self.data_source_type = map.get('DataSourceType')
        return self


class GetMetaColumnLineageResponse(TeaModel):
    def __init__(self, request_id=None, error_code=None, error_message=None, http_status_code=None, success=None,
                 data=None):
        self.request_id = request_id    # type: str
        self.error_code = error_code    # type: str
        self.error_message = error_message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.success = success          # type: bool
        self.data = data                # type: GetMetaColumnLineageResponseData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.error_code, 'error_code')
        self.validate_required(self.error_message, 'error_message')
        self.validate_required(self.http_status_code, 'http_status_code')
        self.validate_required(self.success, 'success')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['ErrorCode'] = self.error_code
        result['ErrorMessage'] = self.error_message
        result['HttpStatusCode'] = self.http_status_code
        result['Success'] = self.success
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.error_code = map.get('ErrorCode')
        self.error_message = map.get('ErrorMessage')
        self.http_status_code = map.get('HttpStatusCode')
        self.success = map.get('Success')
        if map.get('Data') is not None:
            temp_model = GetMetaColumnLineageResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class GetMetaColumnLineageResponseDataDataEntityList(TeaModel):
    def __init__(self, column_name=None, column_guid=None, cluster_id=None, database_name=None, table_name=None):
        self.column_name = column_name  # type: str
        self.column_guid = column_guid  # type: str
        self.cluster_id = cluster_id    # type: str
        self.database_name = database_name  # type: str
        self.table_name = table_name    # type: str

    def validate(self):
        self.validate_required(self.column_name, 'column_name')
        self.validate_required(self.column_guid, 'column_guid')
        self.validate_required(self.cluster_id, 'cluster_id')
        self.validate_required(self.database_name, 'database_name')
        self.validate_required(self.table_name, 'table_name')

    def to_map(self):
        result = {}
        result['ColumnName'] = self.column_name
        result['ColumnGuid'] = self.column_guid
        result['ClusterId'] = self.cluster_id
        result['DatabaseName'] = self.database_name
        result['TableName'] = self.table_name
        return result

    def from_map(self, map={}):
        self.column_name = map.get('ColumnName')
        self.column_guid = map.get('ColumnGuid')
        self.cluster_id = map.get('ClusterId')
        self.database_name = map.get('DatabaseName')
        self.table_name = map.get('TableName')
        return self


class GetMetaColumnLineageResponseData(TeaModel):
    def __init__(self, total_count=None, page_num=None, page_size=None, data_entity_list=None):
        self.total_count = total_count  # type: int
        self.page_num = page_num        # type: int
        self.page_size = page_size      # type: int
        self.data_entity_list = data_entity_list  # type: List[GetMetaColumnLineageResponseDataDataEntityList]

    def validate(self):
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.page_num, 'page_num')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.data_entity_list, 'data_entity_list')
        if self.data_entity_list:
            for k in self.data_entity_list:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['TotalCount'] = self.total_count
        result['PageNum'] = self.page_num
        result['PageSize'] = self.page_size
        result['DataEntityList'] = []
        if self.data_entity_list is not None:
            for k in self.data_entity_list:
                result['DataEntityList'].append(k.to_map() if k else None)
        else:
            result['DataEntityList'] = None
        return result

    def from_map(self, map={}):
        self.total_count = map.get('TotalCount')
        self.page_num = map.get('PageNum')
        self.page_size = map.get('PageSize')
        self.data_entity_list = []
        if map.get('DataEntityList') is not None:
            for k in map.get('DataEntityList'):
                temp_model = GetMetaColumnLineageResponseDataDataEntityList()
                self.data_entity_list.append(temp_model.from_map(k))
        else:
            self.data_entity_list = None
        return self


class UpdateBusinessRequest(TeaModel):
    def __init__(self, project_id=None, project_identifier=None, business_name=None, description=None, owner=None,
                 business_id=None):
        self.project_id = project_id    # type: int
        self.project_identifier = project_identifier  # type: str
        self.business_name = business_name  # type: str
        self.description = description  # type: str
        self.owner = owner              # type: str
        self.business_id = business_id  # type: int

    def validate(self):
        self.validate_required(self.business_id, 'business_id')

    def to_map(self):
        result = {}
        result['ProjectId'] = self.project_id
        result['ProjectIdentifier'] = self.project_identifier
        result['BusinessName'] = self.business_name
        result['Description'] = self.description
        result['Owner'] = self.owner
        result['BusinessId'] = self.business_id
        return result

    def from_map(self, map={}):
        self.project_id = map.get('ProjectId')
        self.project_identifier = map.get('ProjectIdentifier')
        self.business_name = map.get('BusinessName')
        self.description = map.get('Description')
        self.owner = map.get('Owner')
        self.business_id = map.get('BusinessId')
        return self


class UpdateBusinessResponse(TeaModel):
    def __init__(self, request_id=None, success=None, error_code=None, error_message=None, http_status_code=None):
        self.request_id = request_id    # type: str
        self.success = success          # type: bool
        self.error_code = error_code    # type: str
        self.error_message = error_message  # type: str
        self.http_status_code = http_status_code  # type: int

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.success, 'success')
        self.validate_required(self.error_code, 'error_code')
        self.validate_required(self.error_message, 'error_message')
        self.validate_required(self.http_status_code, 'http_status_code')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Success'] = self.success
        result['ErrorCode'] = self.error_code
        result['ErrorMessage'] = self.error_message
        result['HttpStatusCode'] = self.http_status_code
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.success = map.get('Success')
        self.error_code = map.get('ErrorCode')
        self.error_message = map.get('ErrorMessage')
        self.http_status_code = map.get('HttpStatusCode')
        return self


class UpdateQualityRuleRequest(TeaModel):
    def __init__(self, block_type=None, entity_id=None, comment=None, checker=None, expect_value=None, id=None,
                 trend=None, method_name=None, operator=None, project_name=None, property=None, property_type=None,
                 rule_type=None, where_condition=None, critical_threshold=None, warning_threshold=None, template_id=None,
                 rule_name=None, predict_type=None):
        self.block_type = block_type    # type: int
        self.entity_id = entity_id      # type: int
        self.comment = comment          # type: str
        self.checker = checker          # type: int
        self.expect_value = expect_value  # type: str
        self.id = id                    # type: int
        self.trend = trend              # type: str
        self.method_name = method_name  # type: str
        self.operator = operator        # type: str
        self.project_name = project_name  # type: str
        self.property = property        # type: str
        self.property_type = property_type  # type: str
        self.rule_type = rule_type      # type: int
        self.where_condition = where_condition  # type: str
        self.critical_threshold = critical_threshold  # type: str
        self.warning_threshold = warning_threshold  # type: str
        self.template_id = template_id  # type: int
        self.rule_name = rule_name      # type: str
        self.predict_type = predict_type  # type: int

    def validate(self):
        self.validate_required(self.id, 'id')
        self.validate_required(self.project_name, 'project_name')

    def to_map(self):
        result = {}
        result['BlockType'] = self.block_type
        result['EntityId'] = self.entity_id
        result['Comment'] = self.comment
        result['Checker'] = self.checker
        result['ExpectValue'] = self.expect_value
        result['Id'] = self.id
        result['Trend'] = self.trend
        result['MethodName'] = self.method_name
        result['Operator'] = self.operator
        result['ProjectName'] = self.project_name
        result['Property'] = self.property
        result['PropertyType'] = self.property_type
        result['RuleType'] = self.rule_type
        result['WhereCondition'] = self.where_condition
        result['CriticalThreshold'] = self.critical_threshold
        result['WarningThreshold'] = self.warning_threshold
        result['TemplateId'] = self.template_id
        result['RuleName'] = self.rule_name
        result['PredictType'] = self.predict_type
        return result

    def from_map(self, map={}):
        self.block_type = map.get('BlockType')
        self.entity_id = map.get('EntityId')
        self.comment = map.get('Comment')
        self.checker = map.get('Checker')
        self.expect_value = map.get('ExpectValue')
        self.id = map.get('Id')
        self.trend = map.get('Trend')
        self.method_name = map.get('MethodName')
        self.operator = map.get('Operator')
        self.project_name = map.get('ProjectName')
        self.property = map.get('Property')
        self.property_type = map.get('PropertyType')
        self.rule_type = map.get('RuleType')
        self.where_condition = map.get('WhereCondition')
        self.critical_threshold = map.get('CriticalThreshold')
        self.warning_threshold = map.get('WarningThreshold')
        self.template_id = map.get('TemplateId')
        self.rule_name = map.get('RuleName')
        self.predict_type = map.get('PredictType')
        return self


class UpdateQualityRuleResponse(TeaModel):
    def __init__(self, error_code=None, data=None, success=None, error_message=None, http_status_code=None,
                 request_id=None):
        self.error_code = error_code    # type: str
        self.data = data                # type: bool
        self.success = success          # type: bool
        self.error_message = error_message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.error_code, 'error_code')
        self.validate_required(self.data, 'data')
        self.validate_required(self.success, 'success')
        self.validate_required(self.error_message, 'error_message')
        self.validate_required(self.http_status_code, 'http_status_code')
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['ErrorCode'] = self.error_code
        result['Data'] = self.data
        result['Success'] = self.success
        result['ErrorMessage'] = self.error_message
        result['HttpStatusCode'] = self.http_status_code
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.error_code = map.get('ErrorCode')
        self.data = map.get('Data')
        self.success = map.get('Success')
        self.error_message = map.get('ErrorMessage')
        self.http_status_code = map.get('HttpStatusCode')
        self.request_id = map.get('RequestId')
        return self


class DeleteQualityRuleRequest(TeaModel):
    def __init__(self, project_name=None, rule_id=None):
        self.project_name = project_name  # type: str
        self.rule_id = rule_id          # type: int

    def validate(self):
        self.validate_required(self.project_name, 'project_name')
        self.validate_required(self.rule_id, 'rule_id')

    def to_map(self):
        result = {}
        result['ProjectName'] = self.project_name
        result['RuleId'] = self.rule_id
        return result

    def from_map(self, map={}):
        self.project_name = map.get('ProjectName')
        self.rule_id = map.get('RuleId')
        return self


class DeleteQualityRuleResponse(TeaModel):
    def __init__(self, error_code=None, data=None, error_message=None, success=None, http_status_code=None,
                 request_id=None):
        self.error_code = error_code    # type: str
        self.data = data                # type: bool
        self.error_message = error_message  # type: str
        self.success = success          # type: bool
        self.http_status_code = http_status_code  # type: int
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.error_code, 'error_code')
        self.validate_required(self.data, 'data')
        self.validate_required(self.error_message, 'error_message')
        self.validate_required(self.success, 'success')
        self.validate_required(self.http_status_code, 'http_status_code')
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['ErrorCode'] = self.error_code
        result['Data'] = self.data
        result['ErrorMessage'] = self.error_message
        result['Success'] = self.success
        result['HttpStatusCode'] = self.http_status_code
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.error_code = map.get('ErrorCode')
        self.data = map.get('Data')
        self.error_message = map.get('ErrorMessage')
        self.success = map.get('Success')
        self.http_status_code = map.get('HttpStatusCode')
        self.request_id = map.get('RequestId')
        return self


class SubmitFileRequest(TeaModel):
    def __init__(self, project_id=None, project_identifier=None, file_id=None, comment=None):
        self.project_id = project_id    # type: int
        self.project_identifier = project_identifier  # type: str
        self.file_id = file_id          # type: int
        self.comment = comment          # type: str

    def validate(self):
        self.validate_required(self.file_id, 'file_id')

    def to_map(self):
        result = {}
        result['ProjectId'] = self.project_id
        result['ProjectIdentifier'] = self.project_identifier
        result['FileId'] = self.file_id
        result['Comment'] = self.comment
        return result

    def from_map(self, map={}):
        self.project_id = map.get('ProjectId')
        self.project_identifier = map.get('ProjectIdentifier')
        self.file_id = map.get('FileId')
        self.comment = map.get('Comment')
        return self


class SubmitFileResponse(TeaModel):
    def __init__(self, request_id=None, success=None, error_code=None, error_message=None, data=None,
                 http_status_code=None):
        self.request_id = request_id    # type: str
        self.success = success          # type: bool
        self.error_code = error_code    # type: str
        self.error_message = error_message  # type: str
        self.data = data                # type: int
        self.http_status_code = http_status_code  # type: int

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.success, 'success')
        self.validate_required(self.error_code, 'error_code')
        self.validate_required(self.error_message, 'error_message')
        self.validate_required(self.data, 'data')
        self.validate_required(self.http_status_code, 'http_status_code')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Success'] = self.success
        result['ErrorCode'] = self.error_code
        result['ErrorMessage'] = self.error_message
        result['Data'] = self.data
        result['HttpStatusCode'] = self.http_status_code
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.success = map.get('Success')
        self.error_code = map.get('ErrorCode')
        self.error_message = map.get('ErrorMessage')
        self.data = map.get('Data')
        self.http_status_code = map.get('HttpStatusCode')
        return self


class GetDataServiceApiRequest(TeaModel):
    def __init__(self, tenant_id=None, project_id=None, api_id=None):
        self.tenant_id = tenant_id      # type: int
        self.project_id = project_id    # type: int
        self.api_id = api_id            # type: int

    def validate(self):
        self.validate_required(self.tenant_id, 'tenant_id')
        self.validate_required(self.project_id, 'project_id')
        self.validate_required(self.api_id, 'api_id')

    def to_map(self):
        result = {}
        result['TenantId'] = self.tenant_id
        result['ProjectId'] = self.project_id
        result['ApiId'] = self.api_id
        return result

    def from_map(self, map={}):
        self.tenant_id = map.get('TenantId')
        self.project_id = map.get('ProjectId')
        self.api_id = map.get('ApiId')
        return self


class GetDataServiceApiResponse(TeaModel):
    def __init__(self, error_code=None, error_message=None, http_status_code=None, request_id=None, success=None,
                 data=None):
        self.error_code = error_code    # type: str
        self.error_message = error_message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.request_id = request_id    # type: str
        self.success = success          # type: bool
        self.data = data                # type: GetDataServiceApiResponseData

    def validate(self):
        self.validate_required(self.error_code, 'error_code')
        self.validate_required(self.error_message, 'error_message')
        self.validate_required(self.http_status_code, 'http_status_code')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.success, 'success')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['ErrorCode'] = self.error_code
        result['ErrorMessage'] = self.error_message
        result['HttpStatusCode'] = self.http_status_code
        result['RequestId'] = self.request_id
        result['Success'] = self.success
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.error_code = map.get('ErrorCode')
        self.error_message = map.get('ErrorMessage')
        self.http_status_code = map.get('HttpStatusCode')
        self.request_id = map.get('RequestId')
        self.success = map.get('Success')
        if map.get('Data') is not None:
            temp_model = GetDataServiceApiResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class GetDataServiceApiResponseDataRegistrationDetailsRegistrationErrorCodes(TeaModel):
    def __init__(self, error_code=None, error_message=None, error_solution=None):
        self.error_code = error_code    # type: str
        self.error_message = error_message  # type: str
        self.error_solution = error_solution  # type: str

    def validate(self):
        self.validate_required(self.error_code, 'error_code')
        self.validate_required(self.error_message, 'error_message')
        self.validate_required(self.error_solution, 'error_solution')

    def to_map(self):
        result = {}
        result['ErrorCode'] = self.error_code
        result['ErrorMessage'] = self.error_message
        result['ErrorSolution'] = self.error_solution
        return result

    def from_map(self, map={}):
        self.error_code = map.get('ErrorCode')
        self.error_message = map.get('ErrorMessage')
        self.error_solution = map.get('ErrorSolution')
        return self


class GetDataServiceApiResponseDataRegistrationDetailsRegistrationRequestParameters(TeaModel):
    def __init__(self, column_name=None, default_value=None, example_value=None, is_required_parameter=None,
                 parameter_data_type=None, parameter_description=None, parameter_name=None, parameter_operator=None,
                 parameter_position=None):
        self.column_name = column_name  # type: str
        self.default_value = default_value  # type: str
        self.example_value = example_value  # type: str
        self.is_required_parameter = is_required_parameter  # type: bool
        self.parameter_data_type = parameter_data_type  # type: int
        self.parameter_description = parameter_description  # type: str
        self.parameter_name = parameter_name  # type: str
        self.parameter_operator = parameter_operator  # type: int
        self.parameter_position = parameter_position  # type: int

    def validate(self):
        self.validate_required(self.column_name, 'column_name')
        self.validate_required(self.default_value, 'default_value')
        self.validate_required(self.example_value, 'example_value')
        self.validate_required(self.is_required_parameter, 'is_required_parameter')
        self.validate_required(self.parameter_data_type, 'parameter_data_type')
        self.validate_required(self.parameter_description, 'parameter_description')
        self.validate_required(self.parameter_name, 'parameter_name')
        self.validate_required(self.parameter_operator, 'parameter_operator')
        self.validate_required(self.parameter_position, 'parameter_position')

    def to_map(self):
        result = {}
        result['ColumnName'] = self.column_name
        result['DefaultValue'] = self.default_value
        result['ExampleValue'] = self.example_value
        result['IsRequiredParameter'] = self.is_required_parameter
        result['ParameterDataType'] = self.parameter_data_type
        result['ParameterDescription'] = self.parameter_description
        result['ParameterName'] = self.parameter_name
        result['ParameterOperator'] = self.parameter_operator
        result['ParameterPosition'] = self.parameter_position
        return result

    def from_map(self, map={}):
        self.column_name = map.get('ColumnName')
        self.default_value = map.get('DefaultValue')
        self.example_value = map.get('ExampleValue')
        self.is_required_parameter = map.get('IsRequiredParameter')
        self.parameter_data_type = map.get('ParameterDataType')
        self.parameter_description = map.get('ParameterDescription')
        self.parameter_name = map.get('ParameterName')
        self.parameter_operator = map.get('ParameterOperator')
        self.parameter_position = map.get('ParameterPosition')
        return self


class GetDataServiceApiResponseDataRegistrationDetails(TeaModel):
    def __init__(self, failed_result_sample=None, service_content_type=None, service_host=None, service_path=None,
                 service_request_body_description=None, successful_result_sample=None, registration_error_codes=None,
                 registration_request_parameters=None):
        self.failed_result_sample = failed_result_sample  # type: str
        self.service_content_type = service_content_type  # type: int
        self.service_host = service_host  # type: str
        self.service_path = service_path  # type: str
        self.service_request_body_description = service_request_body_description  # type: str
        self.successful_result_sample = successful_result_sample  # type: str
        self.registration_error_codes = registration_error_codes  # type: List[GetDataServiceApiResponseDataRegistrationDetailsRegistrationErrorCodes]
        self.registration_request_parameters = registration_request_parameters  # type: List[GetDataServiceApiResponseDataRegistrationDetailsRegistrationRequestParameters]

    def validate(self):
        self.validate_required(self.failed_result_sample, 'failed_result_sample')
        self.validate_required(self.service_content_type, 'service_content_type')
        self.validate_required(self.service_host, 'service_host')
        self.validate_required(self.service_path, 'service_path')
        self.validate_required(self.service_request_body_description, 'service_request_body_description')
        self.validate_required(self.successful_result_sample, 'successful_result_sample')
        self.validate_required(self.registration_error_codes, 'registration_error_codes')
        if self.registration_error_codes:
            for k in self.registration_error_codes:
                if k:
                    k.validate()
        self.validate_required(self.registration_request_parameters, 'registration_request_parameters')
        if self.registration_request_parameters:
            for k in self.registration_request_parameters:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['FailedResultSample'] = self.failed_result_sample
        result['ServiceContentType'] = self.service_content_type
        result['ServiceHost'] = self.service_host
        result['ServicePath'] = self.service_path
        result['ServiceRequestBodyDescription'] = self.service_request_body_description
        result['SuccessfulResultSample'] = self.successful_result_sample
        result['RegistrationErrorCodes'] = []
        if self.registration_error_codes is not None:
            for k in self.registration_error_codes:
                result['RegistrationErrorCodes'].append(k.to_map() if k else None)
        else:
            result['RegistrationErrorCodes'] = None
        result['RegistrationRequestParameters'] = []
        if self.registration_request_parameters is not None:
            for k in self.registration_request_parameters:
                result['RegistrationRequestParameters'].append(k.to_map() if k else None)
        else:
            result['RegistrationRequestParameters'] = None
        return result

    def from_map(self, map={}):
        self.failed_result_sample = map.get('FailedResultSample')
        self.service_content_type = map.get('ServiceContentType')
        self.service_host = map.get('ServiceHost')
        self.service_path = map.get('ServicePath')
        self.service_request_body_description = map.get('ServiceRequestBodyDescription')
        self.successful_result_sample = map.get('SuccessfulResultSample')
        self.registration_error_codes = []
        if map.get('RegistrationErrorCodes') is not None:
            for k in map.get('RegistrationErrorCodes'):
                temp_model = GetDataServiceApiResponseDataRegistrationDetailsRegistrationErrorCodes()
                self.registration_error_codes.append(temp_model.from_map(k))
        else:
            self.registration_error_codes = None
        self.registration_request_parameters = []
        if map.get('RegistrationRequestParameters') is not None:
            for k in map.get('RegistrationRequestParameters'):
                temp_model = GetDataServiceApiResponseDataRegistrationDetailsRegistrationRequestParameters()
                self.registration_request_parameters.append(temp_model.from_map(k))
        else:
            self.registration_request_parameters = None
        return self


class GetDataServiceApiResponseDataScriptDetailsScriptRequestParameters(TeaModel):
    def __init__(self, column_name=None, default_value=None, example_value=None, is_required_parameter=None,
                 parameter_data_type=None, parameter_description=None, parameter_name=None, parameter_operator=None,
                 parameter_position=None):
        self.column_name = column_name  # type: str
        self.default_value = default_value  # type: str
        self.example_value = example_value  # type: str
        self.is_required_parameter = is_required_parameter  # type: bool
        self.parameter_data_type = parameter_data_type  # type: int
        self.parameter_description = parameter_description  # type: str
        self.parameter_name = parameter_name  # type: str
        self.parameter_operator = parameter_operator  # type: int
        self.parameter_position = parameter_position  # type: int

    def validate(self):
        self.validate_required(self.column_name, 'column_name')
        self.validate_required(self.default_value, 'default_value')
        self.validate_required(self.example_value, 'example_value')
        self.validate_required(self.is_required_parameter, 'is_required_parameter')
        self.validate_required(self.parameter_data_type, 'parameter_data_type')
        self.validate_required(self.parameter_description, 'parameter_description')
        self.validate_required(self.parameter_name, 'parameter_name')
        self.validate_required(self.parameter_operator, 'parameter_operator')
        self.validate_required(self.parameter_position, 'parameter_position')

    def to_map(self):
        result = {}
        result['ColumnName'] = self.column_name
        result['DefaultValue'] = self.default_value
        result['ExampleValue'] = self.example_value
        result['IsRequiredParameter'] = self.is_required_parameter
        result['ParameterDataType'] = self.parameter_data_type
        result['ParameterDescription'] = self.parameter_description
        result['ParameterName'] = self.parameter_name
        result['ParameterOperator'] = self.parameter_operator
        result['ParameterPosition'] = self.parameter_position
        return result

    def from_map(self, map={}):
        self.column_name = map.get('ColumnName')
        self.default_value = map.get('DefaultValue')
        self.example_value = map.get('ExampleValue')
        self.is_required_parameter = map.get('IsRequiredParameter')
        self.parameter_data_type = map.get('ParameterDataType')
        self.parameter_description = map.get('ParameterDescription')
        self.parameter_name = map.get('ParameterName')
        self.parameter_operator = map.get('ParameterOperator')
        self.parameter_position = map.get('ParameterPosition')
        return self


class GetDataServiceApiResponseDataScriptDetailsScriptResponseParameters(TeaModel):
    def __init__(self, column_name=None, example_value=None, parameter_data_type=None, parameter_description=None,
                 parameter_name=None):
        self.column_name = column_name  # type: str
        self.example_value = example_value  # type: str
        self.parameter_data_type = parameter_data_type  # type: int
        self.parameter_description = parameter_description  # type: str
        self.parameter_name = parameter_name  # type: str

    def validate(self):
        self.validate_required(self.column_name, 'column_name')
        self.validate_required(self.example_value, 'example_value')
        self.validate_required(self.parameter_data_type, 'parameter_data_type')
        self.validate_required(self.parameter_description, 'parameter_description')
        self.validate_required(self.parameter_name, 'parameter_name')

    def to_map(self):
        result = {}
        result['ColumnName'] = self.column_name
        result['ExampleValue'] = self.example_value
        result['ParameterDataType'] = self.parameter_data_type
        result['ParameterDescription'] = self.parameter_description
        result['ParameterName'] = self.parameter_name
        return result

    def from_map(self, map={}):
        self.column_name = map.get('ColumnName')
        self.example_value = map.get('ExampleValue')
        self.parameter_data_type = map.get('ParameterDataType')
        self.parameter_description = map.get('ParameterDescription')
        self.parameter_name = map.get('ParameterName')
        return self


class GetDataServiceApiResponseDataScriptDetailsScriptConnection(TeaModel):
    def __init__(self, connection_id=None, table_name=None):
        self.connection_id = connection_id  # type: int
        self.table_name = table_name    # type: str

    def validate(self):
        self.validate_required(self.connection_id, 'connection_id')
        self.validate_required(self.table_name, 'table_name')

    def to_map(self):
        result = {}
        result['ConnectionId'] = self.connection_id
        result['TableName'] = self.table_name
        return result

    def from_map(self, map={}):
        self.connection_id = map.get('ConnectionId')
        self.table_name = map.get('TableName')
        return self


class GetDataServiceApiResponseDataScriptDetails(TeaModel):
    def __init__(self, is_paged_response=None, script=None, script_request_parameters=None,
                 script_response_parameters=None, script_connection=None):
        self.is_paged_response = is_paged_response  # type: bool
        self.script = script            # type: str
        self.script_request_parameters = script_request_parameters  # type: List[GetDataServiceApiResponseDataScriptDetailsScriptRequestParameters]
        self.script_response_parameters = script_response_parameters  # type: List[GetDataServiceApiResponseDataScriptDetailsScriptResponseParameters]
        self.script_connection = script_connection  # type: GetDataServiceApiResponseDataScriptDetailsScriptConnection

    def validate(self):
        self.validate_required(self.is_paged_response, 'is_paged_response')
        self.validate_required(self.script, 'script')
        self.validate_required(self.script_request_parameters, 'script_request_parameters')
        if self.script_request_parameters:
            for k in self.script_request_parameters:
                if k:
                    k.validate()
        self.validate_required(self.script_response_parameters, 'script_response_parameters')
        if self.script_response_parameters:
            for k in self.script_response_parameters:
                if k:
                    k.validate()
        self.validate_required(self.script_connection, 'script_connection')
        if self.script_connection:
            self.script_connection.validate()

    def to_map(self):
        result = {}
        result['IsPagedResponse'] = self.is_paged_response
        result['Script'] = self.script
        result['ScriptRequestParameters'] = []
        if self.script_request_parameters is not None:
            for k in self.script_request_parameters:
                result['ScriptRequestParameters'].append(k.to_map() if k else None)
        else:
            result['ScriptRequestParameters'] = None
        result['ScriptResponseParameters'] = []
        if self.script_response_parameters is not None:
            for k in self.script_response_parameters:
                result['ScriptResponseParameters'].append(k.to_map() if k else None)
        else:
            result['ScriptResponseParameters'] = None
        if self.script_connection is not None:
            result['ScriptConnection'] = self.script_connection.to_map()
        else:
            result['ScriptConnection'] = None
        return result

    def from_map(self, map={}):
        self.is_paged_response = map.get('IsPagedResponse')
        self.script = map.get('Script')
        self.script_request_parameters = []
        if map.get('ScriptRequestParameters') is not None:
            for k in map.get('ScriptRequestParameters'):
                temp_model = GetDataServiceApiResponseDataScriptDetailsScriptRequestParameters()
                self.script_request_parameters.append(temp_model.from_map(k))
        else:
            self.script_request_parameters = None
        self.script_response_parameters = []
        if map.get('ScriptResponseParameters') is not None:
            for k in map.get('ScriptResponseParameters'):
                temp_model = GetDataServiceApiResponseDataScriptDetailsScriptResponseParameters()
                self.script_response_parameters.append(temp_model.from_map(k))
        else:
            self.script_response_parameters = None
        if map.get('ScriptConnection') is not None:
            temp_model = GetDataServiceApiResponseDataScriptDetailsScriptConnection()
            self.script_connection = temp_model.from_map(map['ScriptConnection'])
        else:
            self.script_connection = None
        return self


class GetDataServiceApiResponseDataWizardDetailsWizardRequestParameters(TeaModel):
    def __init__(self, column_name=None, default_value=None, example_value=None, is_required_parameter=None,
                 parameter_data_type=None, parameter_description=None, parameter_name=None, parameter_operator=None,
                 parameter_position=None):
        self.column_name = column_name  # type: str
        self.default_value = default_value  # type: str
        self.example_value = example_value  # type: str
        self.is_required_parameter = is_required_parameter  # type: bool
        self.parameter_data_type = parameter_data_type  # type: int
        self.parameter_description = parameter_description  # type: str
        self.parameter_name = parameter_name  # type: str
        self.parameter_operator = parameter_operator  # type: int
        self.parameter_position = parameter_position  # type: int

    def validate(self):
        self.validate_required(self.column_name, 'column_name')
        self.validate_required(self.default_value, 'default_value')
        self.validate_required(self.example_value, 'example_value')
        self.validate_required(self.is_required_parameter, 'is_required_parameter')
        self.validate_required(self.parameter_data_type, 'parameter_data_type')
        self.validate_required(self.parameter_description, 'parameter_description')
        self.validate_required(self.parameter_name, 'parameter_name')
        self.validate_required(self.parameter_operator, 'parameter_operator')
        self.validate_required(self.parameter_position, 'parameter_position')

    def to_map(self):
        result = {}
        result['ColumnName'] = self.column_name
        result['DefaultValue'] = self.default_value
        result['ExampleValue'] = self.example_value
        result['IsRequiredParameter'] = self.is_required_parameter
        result['ParameterDataType'] = self.parameter_data_type
        result['ParameterDescription'] = self.parameter_description
        result['ParameterName'] = self.parameter_name
        result['ParameterOperator'] = self.parameter_operator
        result['ParameterPosition'] = self.parameter_position
        return result

    def from_map(self, map={}):
        self.column_name = map.get('ColumnName')
        self.default_value = map.get('DefaultValue')
        self.example_value = map.get('ExampleValue')
        self.is_required_parameter = map.get('IsRequiredParameter')
        self.parameter_data_type = map.get('ParameterDataType')
        self.parameter_description = map.get('ParameterDescription')
        self.parameter_name = map.get('ParameterName')
        self.parameter_operator = map.get('ParameterOperator')
        self.parameter_position = map.get('ParameterPosition')
        return self


class GetDataServiceApiResponseDataWizardDetailsWizardResponseParameters(TeaModel):
    def __init__(self, column_name=None, example_value=None, parameter_data_type=None, parameter_description=None,
                 parameter_name=None):
        self.column_name = column_name  # type: str
        self.example_value = example_value  # type: str
        self.parameter_data_type = parameter_data_type  # type: int
        self.parameter_description = parameter_description  # type: str
        self.parameter_name = parameter_name  # type: str

    def validate(self):
        self.validate_required(self.column_name, 'column_name')
        self.validate_required(self.example_value, 'example_value')
        self.validate_required(self.parameter_data_type, 'parameter_data_type')
        self.validate_required(self.parameter_description, 'parameter_description')
        self.validate_required(self.parameter_name, 'parameter_name')

    def to_map(self):
        result = {}
        result['ColumnName'] = self.column_name
        result['ExampleValue'] = self.example_value
        result['ParameterDataType'] = self.parameter_data_type
        result['ParameterDescription'] = self.parameter_description
        result['ParameterName'] = self.parameter_name
        return result

    def from_map(self, map={}):
        self.column_name = map.get('ColumnName')
        self.example_value = map.get('ExampleValue')
        self.parameter_data_type = map.get('ParameterDataType')
        self.parameter_description = map.get('ParameterDescription')
        self.parameter_name = map.get('ParameterName')
        return self


class GetDataServiceApiResponseDataWizardDetailsWizardConnection(TeaModel):
    def __init__(self, connection_id=None, table_name=None):
        self.connection_id = connection_id  # type: int
        self.table_name = table_name    # type: str

    def validate(self):
        self.validate_required(self.connection_id, 'connection_id')
        self.validate_required(self.table_name, 'table_name')

    def to_map(self):
        result = {}
        result['ConnectionId'] = self.connection_id
        result['TableName'] = self.table_name
        return result

    def from_map(self, map={}):
        self.connection_id = map.get('ConnectionId')
        self.table_name = map.get('TableName')
        return self


class GetDataServiceApiResponseDataWizardDetails(TeaModel):
    def __init__(self, is_paged_response=None, wizard_request_parameters=None, wizard_response_parameters=None,
                 wizard_connection=None):
        self.is_paged_response = is_paged_response  # type: bool
        self.wizard_request_parameters = wizard_request_parameters  # type: List[GetDataServiceApiResponseDataWizardDetailsWizardRequestParameters]
        self.wizard_response_parameters = wizard_response_parameters  # type: List[GetDataServiceApiResponseDataWizardDetailsWizardResponseParameters]
        self.wizard_connection = wizard_connection  # type: GetDataServiceApiResponseDataWizardDetailsWizardConnection

    def validate(self):
        self.validate_required(self.is_paged_response, 'is_paged_response')
        self.validate_required(self.wizard_request_parameters, 'wizard_request_parameters')
        if self.wizard_request_parameters:
            for k in self.wizard_request_parameters:
                if k:
                    k.validate()
        self.validate_required(self.wizard_response_parameters, 'wizard_response_parameters')
        if self.wizard_response_parameters:
            for k in self.wizard_response_parameters:
                if k:
                    k.validate()
        self.validate_required(self.wizard_connection, 'wizard_connection')
        if self.wizard_connection:
            self.wizard_connection.validate()

    def to_map(self):
        result = {}
        result['IsPagedResponse'] = self.is_paged_response
        result['WizardRequestParameters'] = []
        if self.wizard_request_parameters is not None:
            for k in self.wizard_request_parameters:
                result['WizardRequestParameters'].append(k.to_map() if k else None)
        else:
            result['WizardRequestParameters'] = None
        result['WizardResponseParameters'] = []
        if self.wizard_response_parameters is not None:
            for k in self.wizard_response_parameters:
                result['WizardResponseParameters'].append(k.to_map() if k else None)
        else:
            result['WizardResponseParameters'] = None
        if self.wizard_connection is not None:
            result['WizardConnection'] = self.wizard_connection.to_map()
        else:
            result['WizardConnection'] = None
        return result

    def from_map(self, map={}):
        self.is_paged_response = map.get('IsPagedResponse')
        self.wizard_request_parameters = []
        if map.get('WizardRequestParameters') is not None:
            for k in map.get('WizardRequestParameters'):
                temp_model = GetDataServiceApiResponseDataWizardDetailsWizardRequestParameters()
                self.wizard_request_parameters.append(temp_model.from_map(k))
        else:
            self.wizard_request_parameters = None
        self.wizard_response_parameters = []
        if map.get('WizardResponseParameters') is not None:
            for k in map.get('WizardResponseParameters'):
                temp_model = GetDataServiceApiResponseDataWizardDetailsWizardResponseParameters()
                self.wizard_response_parameters.append(temp_model.from_map(k))
        else:
            self.wizard_response_parameters = None
        if map.get('WizardConnection') is not None:
            temp_model = GetDataServiceApiResponseDataWizardDetailsWizardConnection()
            self.wizard_connection = temp_model.from_map(map['WizardConnection'])
        else:
            self.wizard_connection = None
        return self


class GetDataServiceApiResponseData(TeaModel):
    def __init__(self, api_id=None, api_mode=None, api_name=None, api_path=None, created_time=None, creator_id=None,
                 description=None, group_id=None, modified_time=None, operator_id=None, project_id=None, request_method=None,
                 response_content_type=None, status=None, tenant_id=None, timeout=None, visible_range=None, folder_id=None,
                 registration_details=None, script_details=None, wizard_details=None, protocols=None):
        self.api_id = api_id            # type: int
        self.api_mode = api_mode        # type: int
        self.api_name = api_name        # type: str
        self.api_path = api_path        # type: str
        self.created_time = created_time  # type: str
        self.creator_id = creator_id    # type: str
        self.description = description  # type: str
        self.group_id = group_id        # type: str
        self.modified_time = modified_time  # type: str
        self.operator_id = operator_id  # type: str
        self.project_id = project_id    # type: int
        self.request_method = request_method  # type: int
        self.response_content_type = response_content_type  # type: int
        self.status = status            # type: int
        self.tenant_id = tenant_id      # type: int
        self.timeout = timeout          # type: int
        self.visible_range = visible_range  # type: int
        self.folder_id = folder_id      # type: int
        self.registration_details = registration_details  # type: GetDataServiceApiResponseDataRegistrationDetails
        self.script_details = script_details  # type: GetDataServiceApiResponseDataScriptDetails
        self.wizard_details = wizard_details  # type: GetDataServiceApiResponseDataWizardDetails
        self.protocols = protocols      # type: List[int]

    def validate(self):
        self.validate_required(self.api_id, 'api_id')
        self.validate_required(self.api_mode, 'api_mode')
        self.validate_required(self.api_name, 'api_name')
        self.validate_required(self.api_path, 'api_path')
        self.validate_required(self.created_time, 'created_time')
        self.validate_required(self.creator_id, 'creator_id')
        self.validate_required(self.description, 'description')
        self.validate_required(self.group_id, 'group_id')
        self.validate_required(self.modified_time, 'modified_time')
        self.validate_required(self.operator_id, 'operator_id')
        self.validate_required(self.project_id, 'project_id')
        self.validate_required(self.request_method, 'request_method')
        self.validate_required(self.response_content_type, 'response_content_type')
        self.validate_required(self.status, 'status')
        self.validate_required(self.tenant_id, 'tenant_id')
        self.validate_required(self.timeout, 'timeout')
        self.validate_required(self.visible_range, 'visible_range')
        self.validate_required(self.folder_id, 'folder_id')
        self.validate_required(self.registration_details, 'registration_details')
        if self.registration_details:
            self.registration_details.validate()
        self.validate_required(self.script_details, 'script_details')
        if self.script_details:
            self.script_details.validate()
        self.validate_required(self.wizard_details, 'wizard_details')
        if self.wizard_details:
            self.wizard_details.validate()
        self.validate_required(self.protocols, 'protocols')

    def to_map(self):
        result = {}
        result['ApiId'] = self.api_id
        result['ApiMode'] = self.api_mode
        result['ApiName'] = self.api_name
        result['ApiPath'] = self.api_path
        result['CreatedTime'] = self.created_time
        result['CreatorId'] = self.creator_id
        result['Description'] = self.description
        result['GroupId'] = self.group_id
        result['ModifiedTime'] = self.modified_time
        result['OperatorId'] = self.operator_id
        result['ProjectId'] = self.project_id
        result['RequestMethod'] = self.request_method
        result['ResponseContentType'] = self.response_content_type
        result['Status'] = self.status
        result['TenantId'] = self.tenant_id
        result['Timeout'] = self.timeout
        result['VisibleRange'] = self.visible_range
        result['FolderId'] = self.folder_id
        if self.registration_details is not None:
            result['RegistrationDetails'] = self.registration_details.to_map()
        else:
            result['RegistrationDetails'] = None
        if self.script_details is not None:
            result['ScriptDetails'] = self.script_details.to_map()
        else:
            result['ScriptDetails'] = None
        if self.wizard_details is not None:
            result['WizardDetails'] = self.wizard_details.to_map()
        else:
            result['WizardDetails'] = None
        result['Protocols'] = self.protocols
        return result

    def from_map(self, map={}):
        self.api_id = map.get('ApiId')
        self.api_mode = map.get('ApiMode')
        self.api_name = map.get('ApiName')
        self.api_path = map.get('ApiPath')
        self.created_time = map.get('CreatedTime')
        self.creator_id = map.get('CreatorId')
        self.description = map.get('Description')
        self.group_id = map.get('GroupId')
        self.modified_time = map.get('ModifiedTime')
        self.operator_id = map.get('OperatorId')
        self.project_id = map.get('ProjectId')
        self.request_method = map.get('RequestMethod')
        self.response_content_type = map.get('ResponseContentType')
        self.status = map.get('Status')
        self.tenant_id = map.get('TenantId')
        self.timeout = map.get('Timeout')
        self.visible_range = map.get('VisibleRange')
        self.folder_id = map.get('FolderId')
        if map.get('RegistrationDetails') is not None:
            temp_model = GetDataServiceApiResponseDataRegistrationDetails()
            self.registration_details = temp_model.from_map(map['RegistrationDetails'])
        else:
            self.registration_details = None
        if map.get('ScriptDetails') is not None:
            temp_model = GetDataServiceApiResponseDataScriptDetails()
            self.script_details = temp_model.from_map(map['ScriptDetails'])
        else:
            self.script_details = None
        if map.get('WizardDetails') is not None:
            temp_model = GetDataServiceApiResponseDataWizardDetails()
            self.wizard_details = temp_model.from_map(map['WizardDetails'])
        else:
            self.wizard_details = None
        self.protocols = map.get('Protocols')
        return self


class ListDataServiceApisRequest(TeaModel):
    def __init__(self, page_number=None, page_size=None, project_id=None, tenant_id=None, api_name_keyword=None,
                 api_path_keyword=None, creator_id=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size      # type: int
        self.project_id = project_id    # type: int
        self.tenant_id = tenant_id      # type: int
        self.api_name_keyword = api_name_keyword  # type: str
        self.api_path_keyword = api_path_keyword  # type: str
        self.creator_id = creator_id    # type: str

    def validate(self):
        self.validate_required(self.project_id, 'project_id')
        self.validate_required(self.tenant_id, 'tenant_id')

    def to_map(self):
        result = {}
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        result['ProjectId'] = self.project_id
        result['TenantId'] = self.tenant_id
        result['ApiNameKeyword'] = self.api_name_keyword
        result['ApiPathKeyword'] = self.api_path_keyword
        result['CreatorId'] = self.creator_id
        return result

    def from_map(self, map={}):
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        self.project_id = map.get('ProjectId')
        self.tenant_id = map.get('TenantId')
        self.api_name_keyword = map.get('ApiNameKeyword')
        self.api_path_keyword = map.get('ApiPathKeyword')
        self.creator_id = map.get('CreatorId')
        return self


class ListDataServiceApisResponse(TeaModel):
    def __init__(self, error_code=None, error_message=None, http_status_code=None, request_id=None, success=None,
                 data=None):
        self.error_code = error_code    # type: str
        self.error_message = error_message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.request_id = request_id    # type: str
        self.success = success          # type: bool
        self.data = data                # type: ListDataServiceApisResponseData

    def validate(self):
        self.validate_required(self.error_code, 'error_code')
        self.validate_required(self.error_message, 'error_message')
        self.validate_required(self.http_status_code, 'http_status_code')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.success, 'success')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['ErrorCode'] = self.error_code
        result['ErrorMessage'] = self.error_message
        result['HttpStatusCode'] = self.http_status_code
        result['RequestId'] = self.request_id
        result['Success'] = self.success
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.error_code = map.get('ErrorCode')
        self.error_message = map.get('ErrorMessage')
        self.http_status_code = map.get('HttpStatusCode')
        self.request_id = map.get('RequestId')
        self.success = map.get('Success')
        if map.get('Data') is not None:
            temp_model = ListDataServiceApisResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class ListDataServiceApisResponseDataApisRegistrationDetailsRegistrationErrorCodes(TeaModel):
    def __init__(self, error_code=None, error_message=None, error_solution=None):
        self.error_code = error_code    # type: str
        self.error_message = error_message  # type: str
        self.error_solution = error_solution  # type: str

    def validate(self):
        self.validate_required(self.error_code, 'error_code')
        self.validate_required(self.error_message, 'error_message')
        self.validate_required(self.error_solution, 'error_solution')

    def to_map(self):
        result = {}
        result['ErrorCode'] = self.error_code
        result['ErrorMessage'] = self.error_message
        result['ErrorSolution'] = self.error_solution
        return result

    def from_map(self, map={}):
        self.error_code = map.get('ErrorCode')
        self.error_message = map.get('ErrorMessage')
        self.error_solution = map.get('ErrorSolution')
        return self


class ListDataServiceApisResponseDataApisRegistrationDetailsRegistrationRequestParameters(TeaModel):
    def __init__(self, column_name=None, default_value=None, example_value=None, is_required_parameter=None,
                 parameter_data_type=None, parameter_description=None, parameter_name=None, parameter_operator=None,
                 parameter_position=None):
        self.column_name = column_name  # type: str
        self.default_value = default_value  # type: str
        self.example_value = example_value  # type: str
        self.is_required_parameter = is_required_parameter  # type: bool
        self.parameter_data_type = parameter_data_type  # type: int
        self.parameter_description = parameter_description  # type: str
        self.parameter_name = parameter_name  # type: str
        self.parameter_operator = parameter_operator  # type: int
        self.parameter_position = parameter_position  # type: int

    def validate(self):
        self.validate_required(self.column_name, 'column_name')
        self.validate_required(self.default_value, 'default_value')
        self.validate_required(self.example_value, 'example_value')
        self.validate_required(self.is_required_parameter, 'is_required_parameter')
        self.validate_required(self.parameter_data_type, 'parameter_data_type')
        self.validate_required(self.parameter_description, 'parameter_description')
        self.validate_required(self.parameter_name, 'parameter_name')
        self.validate_required(self.parameter_operator, 'parameter_operator')
        self.validate_required(self.parameter_position, 'parameter_position')

    def to_map(self):
        result = {}
        result['ColumnName'] = self.column_name
        result['DefaultValue'] = self.default_value
        result['ExampleValue'] = self.example_value
        result['IsRequiredParameter'] = self.is_required_parameter
        result['ParameterDataType'] = self.parameter_data_type
        result['ParameterDescription'] = self.parameter_description
        result['ParameterName'] = self.parameter_name
        result['ParameterOperator'] = self.parameter_operator
        result['ParameterPosition'] = self.parameter_position
        return result

    def from_map(self, map={}):
        self.column_name = map.get('ColumnName')
        self.default_value = map.get('DefaultValue')
        self.example_value = map.get('ExampleValue')
        self.is_required_parameter = map.get('IsRequiredParameter')
        self.parameter_data_type = map.get('ParameterDataType')
        self.parameter_description = map.get('ParameterDescription')
        self.parameter_name = map.get('ParameterName')
        self.parameter_operator = map.get('ParameterOperator')
        self.parameter_position = map.get('ParameterPosition')
        return self


class ListDataServiceApisResponseDataApisRegistrationDetails(TeaModel):
    def __init__(self, failed_result_sample=None, service_content_type=None, service_host=None, service_path=None,
                 service_request_body_description=None, successful_result_sample=None, registration_error_codes=None,
                 registration_request_parameters=None):
        self.failed_result_sample = failed_result_sample  # type: str
        self.service_content_type = service_content_type  # type: int
        self.service_host = service_host  # type: str
        self.service_path = service_path  # type: str
        self.service_request_body_description = service_request_body_description  # type: str
        self.successful_result_sample = successful_result_sample  # type: str
        self.registration_error_codes = registration_error_codes  # type: List[ListDataServiceApisResponseDataApisRegistrationDetailsRegistrationErrorCodes]
        self.registration_request_parameters = registration_request_parameters  # type: List[ListDataServiceApisResponseDataApisRegistrationDetailsRegistrationRequestParameters]

    def validate(self):
        self.validate_required(self.failed_result_sample, 'failed_result_sample')
        self.validate_required(self.service_content_type, 'service_content_type')
        self.validate_required(self.service_host, 'service_host')
        self.validate_required(self.service_path, 'service_path')
        self.validate_required(self.service_request_body_description, 'service_request_body_description')
        self.validate_required(self.successful_result_sample, 'successful_result_sample')
        self.validate_required(self.registration_error_codes, 'registration_error_codes')
        if self.registration_error_codes:
            for k in self.registration_error_codes:
                if k:
                    k.validate()
        self.validate_required(self.registration_request_parameters, 'registration_request_parameters')
        if self.registration_request_parameters:
            for k in self.registration_request_parameters:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['FailedResultSample'] = self.failed_result_sample
        result['ServiceContentType'] = self.service_content_type
        result['ServiceHost'] = self.service_host
        result['ServicePath'] = self.service_path
        result['ServiceRequestBodyDescription'] = self.service_request_body_description
        result['SuccessfulResultSample'] = self.successful_result_sample
        result['RegistrationErrorCodes'] = []
        if self.registration_error_codes is not None:
            for k in self.registration_error_codes:
                result['RegistrationErrorCodes'].append(k.to_map() if k else None)
        else:
            result['RegistrationErrorCodes'] = None
        result['RegistrationRequestParameters'] = []
        if self.registration_request_parameters is not None:
            for k in self.registration_request_parameters:
                result['RegistrationRequestParameters'].append(k.to_map() if k else None)
        else:
            result['RegistrationRequestParameters'] = None
        return result

    def from_map(self, map={}):
        self.failed_result_sample = map.get('FailedResultSample')
        self.service_content_type = map.get('ServiceContentType')
        self.service_host = map.get('ServiceHost')
        self.service_path = map.get('ServicePath')
        self.service_request_body_description = map.get('ServiceRequestBodyDescription')
        self.successful_result_sample = map.get('SuccessfulResultSample')
        self.registration_error_codes = []
        if map.get('RegistrationErrorCodes') is not None:
            for k in map.get('RegistrationErrorCodes'):
                temp_model = ListDataServiceApisResponseDataApisRegistrationDetailsRegistrationErrorCodes()
                self.registration_error_codes.append(temp_model.from_map(k))
        else:
            self.registration_error_codes = None
        self.registration_request_parameters = []
        if map.get('RegistrationRequestParameters') is not None:
            for k in map.get('RegistrationRequestParameters'):
                temp_model = ListDataServiceApisResponseDataApisRegistrationDetailsRegistrationRequestParameters()
                self.registration_request_parameters.append(temp_model.from_map(k))
        else:
            self.registration_request_parameters = None
        return self


class ListDataServiceApisResponseDataApisScriptDetailsScriptRequestParameters(TeaModel):
    def __init__(self, column_name=None, default_value=None, example_value=None, is_required_parameter=None,
                 parameter_data_type=None, parameter_description=None, parameter_name=None, parameter_operator=None,
                 parameter_position=None):
        self.column_name = column_name  # type: str
        self.default_value = default_value  # type: str
        self.example_value = example_value  # type: str
        self.is_required_parameter = is_required_parameter  # type: bool
        self.parameter_data_type = parameter_data_type  # type: int
        self.parameter_description = parameter_description  # type: str
        self.parameter_name = parameter_name  # type: str
        self.parameter_operator = parameter_operator  # type: int
        self.parameter_position = parameter_position  # type: int

    def validate(self):
        self.validate_required(self.column_name, 'column_name')
        self.validate_required(self.default_value, 'default_value')
        self.validate_required(self.example_value, 'example_value')
        self.validate_required(self.is_required_parameter, 'is_required_parameter')
        self.validate_required(self.parameter_data_type, 'parameter_data_type')
        self.validate_required(self.parameter_description, 'parameter_description')
        self.validate_required(self.parameter_name, 'parameter_name')
        self.validate_required(self.parameter_operator, 'parameter_operator')
        self.validate_required(self.parameter_position, 'parameter_position')

    def to_map(self):
        result = {}
        result['ColumnName'] = self.column_name
        result['DefaultValue'] = self.default_value
        result['ExampleValue'] = self.example_value
        result['IsRequiredParameter'] = self.is_required_parameter
        result['ParameterDataType'] = self.parameter_data_type
        result['ParameterDescription'] = self.parameter_description
        result['ParameterName'] = self.parameter_name
        result['ParameterOperator'] = self.parameter_operator
        result['ParameterPosition'] = self.parameter_position
        return result

    def from_map(self, map={}):
        self.column_name = map.get('ColumnName')
        self.default_value = map.get('DefaultValue')
        self.example_value = map.get('ExampleValue')
        self.is_required_parameter = map.get('IsRequiredParameter')
        self.parameter_data_type = map.get('ParameterDataType')
        self.parameter_description = map.get('ParameterDescription')
        self.parameter_name = map.get('ParameterName')
        self.parameter_operator = map.get('ParameterOperator')
        self.parameter_position = map.get('ParameterPosition')
        return self


class ListDataServiceApisResponseDataApisScriptDetailsScriptResponseParameters(TeaModel):
    def __init__(self, column_name=None, example_value=None, parameter_data_type=None, parameter_description=None,
                 parameter_name=None):
        self.column_name = column_name  # type: str
        self.example_value = example_value  # type: str
        self.parameter_data_type = parameter_data_type  # type: int
        self.parameter_description = parameter_description  # type: str
        self.parameter_name = parameter_name  # type: str

    def validate(self):
        self.validate_required(self.column_name, 'column_name')
        self.validate_required(self.example_value, 'example_value')
        self.validate_required(self.parameter_data_type, 'parameter_data_type')
        self.validate_required(self.parameter_description, 'parameter_description')
        self.validate_required(self.parameter_name, 'parameter_name')

    def to_map(self):
        result = {}
        result['ColumnName'] = self.column_name
        result['ExampleValue'] = self.example_value
        result['ParameterDataType'] = self.parameter_data_type
        result['ParameterDescription'] = self.parameter_description
        result['ParameterName'] = self.parameter_name
        return result

    def from_map(self, map={}):
        self.column_name = map.get('ColumnName')
        self.example_value = map.get('ExampleValue')
        self.parameter_data_type = map.get('ParameterDataType')
        self.parameter_description = map.get('ParameterDescription')
        self.parameter_name = map.get('ParameterName')
        return self


class ListDataServiceApisResponseDataApisScriptDetailsScriptConnection(TeaModel):
    def __init__(self, connection_id=None, table_name=None):
        self.connection_id = connection_id  # type: int
        self.table_name = table_name    # type: str

    def validate(self):
        self.validate_required(self.connection_id, 'connection_id')
        self.validate_required(self.table_name, 'table_name')

    def to_map(self):
        result = {}
        result['ConnectionId'] = self.connection_id
        result['TableName'] = self.table_name
        return result

    def from_map(self, map={}):
        self.connection_id = map.get('ConnectionId')
        self.table_name = map.get('TableName')
        return self


class ListDataServiceApisResponseDataApisScriptDetails(TeaModel):
    def __init__(self, is_paged_response=None, script=None, script_request_parameters=None,
                 script_response_parameters=None, script_connection=None):
        self.is_paged_response = is_paged_response  # type: bool
        self.script = script            # type: str
        self.script_request_parameters = script_request_parameters  # type: List[ListDataServiceApisResponseDataApisScriptDetailsScriptRequestParameters]
        self.script_response_parameters = script_response_parameters  # type: List[ListDataServiceApisResponseDataApisScriptDetailsScriptResponseParameters]
        self.script_connection = script_connection  # type: ListDataServiceApisResponseDataApisScriptDetailsScriptConnection

    def validate(self):
        self.validate_required(self.is_paged_response, 'is_paged_response')
        self.validate_required(self.script, 'script')
        self.validate_required(self.script_request_parameters, 'script_request_parameters')
        if self.script_request_parameters:
            for k in self.script_request_parameters:
                if k:
                    k.validate()
        self.validate_required(self.script_response_parameters, 'script_response_parameters')
        if self.script_response_parameters:
            for k in self.script_response_parameters:
                if k:
                    k.validate()
        self.validate_required(self.script_connection, 'script_connection')
        if self.script_connection:
            self.script_connection.validate()

    def to_map(self):
        result = {}
        result['IsPagedResponse'] = self.is_paged_response
        result['Script'] = self.script
        result['ScriptRequestParameters'] = []
        if self.script_request_parameters is not None:
            for k in self.script_request_parameters:
                result['ScriptRequestParameters'].append(k.to_map() if k else None)
        else:
            result['ScriptRequestParameters'] = None
        result['ScriptResponseParameters'] = []
        if self.script_response_parameters is not None:
            for k in self.script_response_parameters:
                result['ScriptResponseParameters'].append(k.to_map() if k else None)
        else:
            result['ScriptResponseParameters'] = None
        if self.script_connection is not None:
            result['ScriptConnection'] = self.script_connection.to_map()
        else:
            result['ScriptConnection'] = None
        return result

    def from_map(self, map={}):
        self.is_paged_response = map.get('IsPagedResponse')
        self.script = map.get('Script')
        self.script_request_parameters = []
        if map.get('ScriptRequestParameters') is not None:
            for k in map.get('ScriptRequestParameters'):
                temp_model = ListDataServiceApisResponseDataApisScriptDetailsScriptRequestParameters()
                self.script_request_parameters.append(temp_model.from_map(k))
        else:
            self.script_request_parameters = None
        self.script_response_parameters = []
        if map.get('ScriptResponseParameters') is not None:
            for k in map.get('ScriptResponseParameters'):
                temp_model = ListDataServiceApisResponseDataApisScriptDetailsScriptResponseParameters()
                self.script_response_parameters.append(temp_model.from_map(k))
        else:
            self.script_response_parameters = None
        if map.get('ScriptConnection') is not None:
            temp_model = ListDataServiceApisResponseDataApisScriptDetailsScriptConnection()
            self.script_connection = temp_model.from_map(map['ScriptConnection'])
        else:
            self.script_connection = None
        return self


class ListDataServiceApisResponseDataApisWizardDetailsWizardRequestParameters(TeaModel):
    def __init__(self, column_name=None, default_value=None, example_value=None, is_required_parameter=None,
                 parameter_data_type=None, parameter_description=None, parameter_name=None, parameter_operator=None,
                 parameter_position=None):
        self.column_name = column_name  # type: str
        self.default_value = default_value  # type: str
        self.example_value = example_value  # type: str
        self.is_required_parameter = is_required_parameter  # type: bool
        self.parameter_data_type = parameter_data_type  # type: int
        self.parameter_description = parameter_description  # type: str
        self.parameter_name = parameter_name  # type: str
        self.parameter_operator = parameter_operator  # type: int
        self.parameter_position = parameter_position  # type: int

    def validate(self):
        self.validate_required(self.column_name, 'column_name')
        self.validate_required(self.default_value, 'default_value')
        self.validate_required(self.example_value, 'example_value')
        self.validate_required(self.is_required_parameter, 'is_required_parameter')
        self.validate_required(self.parameter_data_type, 'parameter_data_type')
        self.validate_required(self.parameter_description, 'parameter_description')
        self.validate_required(self.parameter_name, 'parameter_name')
        self.validate_required(self.parameter_operator, 'parameter_operator')
        self.validate_required(self.parameter_position, 'parameter_position')

    def to_map(self):
        result = {}
        result['ColumnName'] = self.column_name
        result['DefaultValue'] = self.default_value
        result['ExampleValue'] = self.example_value
        result['IsRequiredParameter'] = self.is_required_parameter
        result['ParameterDataType'] = self.parameter_data_type
        result['ParameterDescription'] = self.parameter_description
        result['ParameterName'] = self.parameter_name
        result['ParameterOperator'] = self.parameter_operator
        result['ParameterPosition'] = self.parameter_position
        return result

    def from_map(self, map={}):
        self.column_name = map.get('ColumnName')
        self.default_value = map.get('DefaultValue')
        self.example_value = map.get('ExampleValue')
        self.is_required_parameter = map.get('IsRequiredParameter')
        self.parameter_data_type = map.get('ParameterDataType')
        self.parameter_description = map.get('ParameterDescription')
        self.parameter_name = map.get('ParameterName')
        self.parameter_operator = map.get('ParameterOperator')
        self.parameter_position = map.get('ParameterPosition')
        return self


class ListDataServiceApisResponseDataApisWizardDetailsWizardResponseParameters(TeaModel):
    def __init__(self, column_name=None, example_value=None, parameter_data_type=None, parameter_description=None,
                 parameter_name=None):
        self.column_name = column_name  # type: str
        self.example_value = example_value  # type: str
        self.parameter_data_type = parameter_data_type  # type: int
        self.parameter_description = parameter_description  # type: str
        self.parameter_name = parameter_name  # type: str

    def validate(self):
        self.validate_required(self.column_name, 'column_name')
        self.validate_required(self.example_value, 'example_value')
        self.validate_required(self.parameter_data_type, 'parameter_data_type')
        self.validate_required(self.parameter_description, 'parameter_description')
        self.validate_required(self.parameter_name, 'parameter_name')

    def to_map(self):
        result = {}
        result['ColumnName'] = self.column_name
        result['ExampleValue'] = self.example_value
        result['ParameterDataType'] = self.parameter_data_type
        result['ParameterDescription'] = self.parameter_description
        result['ParameterName'] = self.parameter_name
        return result

    def from_map(self, map={}):
        self.column_name = map.get('ColumnName')
        self.example_value = map.get('ExampleValue')
        self.parameter_data_type = map.get('ParameterDataType')
        self.parameter_description = map.get('ParameterDescription')
        self.parameter_name = map.get('ParameterName')
        return self


class ListDataServiceApisResponseDataApisWizardDetailsWizardConnection(TeaModel):
    def __init__(self, connection_id=None, table_name=None):
        self.connection_id = connection_id  # type: int
        self.table_name = table_name    # type: str

    def validate(self):
        self.validate_required(self.connection_id, 'connection_id')
        self.validate_required(self.table_name, 'table_name')

    def to_map(self):
        result = {}
        result['ConnectionId'] = self.connection_id
        result['TableName'] = self.table_name
        return result

    def from_map(self, map={}):
        self.connection_id = map.get('ConnectionId')
        self.table_name = map.get('TableName')
        return self


class ListDataServiceApisResponseDataApisWizardDetails(TeaModel):
    def __init__(self, is_paged_response=None, wizard_request_parameters=None, wizard_response_parameters=None,
                 wizard_connection=None):
        self.is_paged_response = is_paged_response  # type: bool
        self.wizard_request_parameters = wizard_request_parameters  # type: List[ListDataServiceApisResponseDataApisWizardDetailsWizardRequestParameters]
        self.wizard_response_parameters = wizard_response_parameters  # type: List[ListDataServiceApisResponseDataApisWizardDetailsWizardResponseParameters]
        self.wizard_connection = wizard_connection  # type: ListDataServiceApisResponseDataApisWizardDetailsWizardConnection

    def validate(self):
        self.validate_required(self.is_paged_response, 'is_paged_response')
        self.validate_required(self.wizard_request_parameters, 'wizard_request_parameters')
        if self.wizard_request_parameters:
            for k in self.wizard_request_parameters:
                if k:
                    k.validate()
        self.validate_required(self.wizard_response_parameters, 'wizard_response_parameters')
        if self.wizard_response_parameters:
            for k in self.wizard_response_parameters:
                if k:
                    k.validate()
        self.validate_required(self.wizard_connection, 'wizard_connection')
        if self.wizard_connection:
            self.wizard_connection.validate()

    def to_map(self):
        result = {}
        result['IsPagedResponse'] = self.is_paged_response
        result['WizardRequestParameters'] = []
        if self.wizard_request_parameters is not None:
            for k in self.wizard_request_parameters:
                result['WizardRequestParameters'].append(k.to_map() if k else None)
        else:
            result['WizardRequestParameters'] = None
        result['WizardResponseParameters'] = []
        if self.wizard_response_parameters is not None:
            for k in self.wizard_response_parameters:
                result['WizardResponseParameters'].append(k.to_map() if k else None)
        else:
            result['WizardResponseParameters'] = None
        if self.wizard_connection is not None:
            result['WizardConnection'] = self.wizard_connection.to_map()
        else:
            result['WizardConnection'] = None
        return result

    def from_map(self, map={}):
        self.is_paged_response = map.get('IsPagedResponse')
        self.wizard_request_parameters = []
        if map.get('WizardRequestParameters') is not None:
            for k in map.get('WizardRequestParameters'):
                temp_model = ListDataServiceApisResponseDataApisWizardDetailsWizardRequestParameters()
                self.wizard_request_parameters.append(temp_model.from_map(k))
        else:
            self.wizard_request_parameters = None
        self.wizard_response_parameters = []
        if map.get('WizardResponseParameters') is not None:
            for k in map.get('WizardResponseParameters'):
                temp_model = ListDataServiceApisResponseDataApisWizardDetailsWizardResponseParameters()
                self.wizard_response_parameters.append(temp_model.from_map(k))
        else:
            self.wizard_response_parameters = None
        if map.get('WizardConnection') is not None:
            temp_model = ListDataServiceApisResponseDataApisWizardDetailsWizardConnection()
            self.wizard_connection = temp_model.from_map(map['WizardConnection'])
        else:
            self.wizard_connection = None
        return self


class ListDataServiceApisResponseDataApis(TeaModel):
    def __init__(self, api_id=None, api_mode=None, api_name=None, api_path=None, created_time=None, creator_id=None,
                 description=None, group_id=None, modified_time=None, operator_id=None, project_id=None, request_method=None,
                 response_content_type=None, status=None, tenant_id=None, timeout=None, visible_range=None, folder_id=None,
                 registration_details=None, script_details=None, wizard_details=None, protocols=None):
        self.api_id = api_id            # type: int
        self.api_mode = api_mode        # type: int
        self.api_name = api_name        # type: str
        self.api_path = api_path        # type: str
        self.created_time = created_time  # type: str
        self.creator_id = creator_id    # type: str
        self.description = description  # type: str
        self.group_id = group_id        # type: str
        self.modified_time = modified_time  # type: str
        self.operator_id = operator_id  # type: str
        self.project_id = project_id    # type: int
        self.request_method = request_method  # type: int
        self.response_content_type = response_content_type  # type: int
        self.status = status            # type: int
        self.tenant_id = tenant_id      # type: int
        self.timeout = timeout          # type: int
        self.visible_range = visible_range  # type: int
        self.folder_id = folder_id      # type: int
        self.registration_details = registration_details  # type: ListDataServiceApisResponseDataApisRegistrationDetails
        self.script_details = script_details  # type: ListDataServiceApisResponseDataApisScriptDetails
        self.wizard_details = wizard_details  # type: ListDataServiceApisResponseDataApisWizardDetails
        self.protocols = protocols      # type: List[int]

    def validate(self):
        self.validate_required(self.api_id, 'api_id')
        self.validate_required(self.api_mode, 'api_mode')
        self.validate_required(self.api_name, 'api_name')
        self.validate_required(self.api_path, 'api_path')
        self.validate_required(self.created_time, 'created_time')
        self.validate_required(self.creator_id, 'creator_id')
        self.validate_required(self.description, 'description')
        self.validate_required(self.group_id, 'group_id')
        self.validate_required(self.modified_time, 'modified_time')
        self.validate_required(self.operator_id, 'operator_id')
        self.validate_required(self.project_id, 'project_id')
        self.validate_required(self.request_method, 'request_method')
        self.validate_required(self.response_content_type, 'response_content_type')
        self.validate_required(self.status, 'status')
        self.validate_required(self.tenant_id, 'tenant_id')
        self.validate_required(self.timeout, 'timeout')
        self.validate_required(self.visible_range, 'visible_range')
        self.validate_required(self.folder_id, 'folder_id')
        self.validate_required(self.registration_details, 'registration_details')
        if self.registration_details:
            self.registration_details.validate()
        self.validate_required(self.script_details, 'script_details')
        if self.script_details:
            self.script_details.validate()
        self.validate_required(self.wizard_details, 'wizard_details')
        if self.wizard_details:
            self.wizard_details.validate()
        self.validate_required(self.protocols, 'protocols')

    def to_map(self):
        result = {}
        result['ApiId'] = self.api_id
        result['ApiMode'] = self.api_mode
        result['ApiName'] = self.api_name
        result['ApiPath'] = self.api_path
        result['CreatedTime'] = self.created_time
        result['CreatorId'] = self.creator_id
        result['Description'] = self.description
        result['GroupId'] = self.group_id
        result['ModifiedTime'] = self.modified_time
        result['OperatorId'] = self.operator_id
        result['ProjectId'] = self.project_id
        result['RequestMethod'] = self.request_method
        result['ResponseContentType'] = self.response_content_type
        result['Status'] = self.status
        result['TenantId'] = self.tenant_id
        result['Timeout'] = self.timeout
        result['VisibleRange'] = self.visible_range
        result['FolderId'] = self.folder_id
        if self.registration_details is not None:
            result['RegistrationDetails'] = self.registration_details.to_map()
        else:
            result['RegistrationDetails'] = None
        if self.script_details is not None:
            result['ScriptDetails'] = self.script_details.to_map()
        else:
            result['ScriptDetails'] = None
        if self.wizard_details is not None:
            result['WizardDetails'] = self.wizard_details.to_map()
        else:
            result['WizardDetails'] = None
        result['Protocols'] = self.protocols
        return result

    def from_map(self, map={}):
        self.api_id = map.get('ApiId')
        self.api_mode = map.get('ApiMode')
        self.api_name = map.get('ApiName')
        self.api_path = map.get('ApiPath')
        self.created_time = map.get('CreatedTime')
        self.creator_id = map.get('CreatorId')
        self.description = map.get('Description')
        self.group_id = map.get('GroupId')
        self.modified_time = map.get('ModifiedTime')
        self.operator_id = map.get('OperatorId')
        self.project_id = map.get('ProjectId')
        self.request_method = map.get('RequestMethod')
        self.response_content_type = map.get('ResponseContentType')
        self.status = map.get('Status')
        self.tenant_id = map.get('TenantId')
        self.timeout = map.get('Timeout')
        self.visible_range = map.get('VisibleRange')
        self.folder_id = map.get('FolderId')
        if map.get('RegistrationDetails') is not None:
            temp_model = ListDataServiceApisResponseDataApisRegistrationDetails()
            self.registration_details = temp_model.from_map(map['RegistrationDetails'])
        else:
            self.registration_details = None
        if map.get('ScriptDetails') is not None:
            temp_model = ListDataServiceApisResponseDataApisScriptDetails()
            self.script_details = temp_model.from_map(map['ScriptDetails'])
        else:
            self.script_details = None
        if map.get('WizardDetails') is not None:
            temp_model = ListDataServiceApisResponseDataApisWizardDetails()
            self.wizard_details = temp_model.from_map(map['WizardDetails'])
        else:
            self.wizard_details = None
        self.protocols = map.get('Protocols')
        return self


class ListDataServiceApisResponseData(TeaModel):
    def __init__(self, page_number=None, page_size=None, total_count=None, apis=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size      # type: int
        self.total_count = total_count  # type: int
        self.apis = apis                # type: List[ListDataServiceApisResponseDataApis]

    def validate(self):
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.apis, 'apis')
        if self.apis:
            for k in self.apis:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        result['TotalCount'] = self.total_count
        result['Apis'] = []
        if self.apis is not None:
            for k in self.apis:
                result['Apis'].append(k.to_map() if k else None)
        else:
            result['Apis'] = None
        return result

    def from_map(self, map={}):
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        self.total_count = map.get('TotalCount')
        self.apis = []
        if map.get('Apis') is not None:
            for k in map.get('Apis'):
                temp_model = ListDataServiceApisResponseDataApis()
                self.apis.append(temp_model.from_map(k))
        else:
            self.apis = None
        return self


class GetDataServicePublishedApiRequest(TeaModel):
    def __init__(self, project_id=None, tenant_id=None, api_id=None):
        self.project_id = project_id    # type: int
        self.tenant_id = tenant_id      # type: int
        self.api_id = api_id            # type: int

    def validate(self):
        self.validate_required(self.project_id, 'project_id')
        self.validate_required(self.tenant_id, 'tenant_id')
        self.validate_required(self.api_id, 'api_id')

    def to_map(self):
        result = {}
        result['ProjectId'] = self.project_id
        result['TenantId'] = self.tenant_id
        result['ApiId'] = self.api_id
        return result

    def from_map(self, map={}):
        self.project_id = map.get('ProjectId')
        self.tenant_id = map.get('TenantId')
        self.api_id = map.get('ApiId')
        return self


class GetDataServicePublishedApiResponse(TeaModel):
    def __init__(self, error_code=None, error_message=None, http_status_code=None, request_id=None, success=None,
                 data=None):
        self.error_code = error_code    # type: str
        self.error_message = error_message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.request_id = request_id    # type: str
        self.success = success          # type: bool
        self.data = data                # type: GetDataServicePublishedApiResponseData

    def validate(self):
        self.validate_required(self.error_code, 'error_code')
        self.validate_required(self.error_message, 'error_message')
        self.validate_required(self.http_status_code, 'http_status_code')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.success, 'success')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['ErrorCode'] = self.error_code
        result['ErrorMessage'] = self.error_message
        result['HttpStatusCode'] = self.http_status_code
        result['RequestId'] = self.request_id
        result['Success'] = self.success
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.error_code = map.get('ErrorCode')
        self.error_message = map.get('ErrorMessage')
        self.http_status_code = map.get('HttpStatusCode')
        self.request_id = map.get('RequestId')
        self.success = map.get('Success')
        if map.get('Data') is not None:
            temp_model = GetDataServicePublishedApiResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class GetDataServicePublishedApiResponseDataRegistrationDetailsRegistrationErrorCodes(TeaModel):
    def __init__(self, error_code=None, error_message=None, error_solution=None):
        self.error_code = error_code    # type: str
        self.error_message = error_message  # type: str
        self.error_solution = error_solution  # type: str

    def validate(self):
        self.validate_required(self.error_code, 'error_code')
        self.validate_required(self.error_message, 'error_message')
        self.validate_required(self.error_solution, 'error_solution')

    def to_map(self):
        result = {}
        result['ErrorCode'] = self.error_code
        result['ErrorMessage'] = self.error_message
        result['ErrorSolution'] = self.error_solution
        return result

    def from_map(self, map={}):
        self.error_code = map.get('ErrorCode')
        self.error_message = map.get('ErrorMessage')
        self.error_solution = map.get('ErrorSolution')
        return self


class GetDataServicePublishedApiResponseDataRegistrationDetailsRegistrationRequestParameters(TeaModel):
    def __init__(self, default_value=None, example_value=None, is_required_parameter=None,
                 parameter_data_type=None, parameter_description=None, parameter_name=None, parameter_operator=None,
                 parameter_position=None):
        self.default_value = default_value  # type: str
        self.example_value = example_value  # type: str
        self.is_required_parameter = is_required_parameter  # type: bool
        self.parameter_data_type = parameter_data_type  # type: int
        self.parameter_description = parameter_description  # type: str
        self.parameter_name = parameter_name  # type: str
        self.parameter_operator = parameter_operator  # type: int
        self.parameter_position = parameter_position  # type: int

    def validate(self):
        self.validate_required(self.default_value, 'default_value')
        self.validate_required(self.example_value, 'example_value')
        self.validate_required(self.is_required_parameter, 'is_required_parameter')
        self.validate_required(self.parameter_data_type, 'parameter_data_type')
        self.validate_required(self.parameter_description, 'parameter_description')
        self.validate_required(self.parameter_name, 'parameter_name')
        self.validate_required(self.parameter_operator, 'parameter_operator')
        self.validate_required(self.parameter_position, 'parameter_position')

    def to_map(self):
        result = {}
        result['DefaultValue'] = self.default_value
        result['ExampleValue'] = self.example_value
        result['IsRequiredParameter'] = self.is_required_parameter
        result['ParameterDataType'] = self.parameter_data_type
        result['ParameterDescription'] = self.parameter_description
        result['ParameterName'] = self.parameter_name
        result['ParameterOperator'] = self.parameter_operator
        result['ParameterPosition'] = self.parameter_position
        return result

    def from_map(self, map={}):
        self.default_value = map.get('DefaultValue')
        self.example_value = map.get('ExampleValue')
        self.is_required_parameter = map.get('IsRequiredParameter')
        self.parameter_data_type = map.get('ParameterDataType')
        self.parameter_description = map.get('ParameterDescription')
        self.parameter_name = map.get('ParameterName')
        self.parameter_operator = map.get('ParameterOperator')
        self.parameter_position = map.get('ParameterPosition')
        return self


class GetDataServicePublishedApiResponseDataRegistrationDetails(TeaModel):
    def __init__(self, failed_result_sample=None, service_content_type=None, service_host=None, service_path=None,
                 service_request_body_description=None, successful_result_sample=None, registration_error_codes=None,
                 registration_request_parameters=None):
        self.failed_result_sample = failed_result_sample  # type: str
        self.service_content_type = service_content_type  # type: int
        self.service_host = service_host  # type: str
        self.service_path = service_path  # type: str
        self.service_request_body_description = service_request_body_description  # type: str
        self.successful_result_sample = successful_result_sample  # type: str
        self.registration_error_codes = registration_error_codes  # type: List[GetDataServicePublishedApiResponseDataRegistrationDetailsRegistrationErrorCodes]
        self.registration_request_parameters = registration_request_parameters  # type: List[GetDataServicePublishedApiResponseDataRegistrationDetailsRegistrationRequestParameters]

    def validate(self):
        self.validate_required(self.failed_result_sample, 'failed_result_sample')
        self.validate_required(self.service_content_type, 'service_content_type')
        self.validate_required(self.service_host, 'service_host')
        self.validate_required(self.service_path, 'service_path')
        self.validate_required(self.service_request_body_description, 'service_request_body_description')
        self.validate_required(self.successful_result_sample, 'successful_result_sample')
        self.validate_required(self.registration_error_codes, 'registration_error_codes')
        if self.registration_error_codes:
            for k in self.registration_error_codes:
                if k:
                    k.validate()
        self.validate_required(self.registration_request_parameters, 'registration_request_parameters')
        if self.registration_request_parameters:
            for k in self.registration_request_parameters:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['FailedResultSample'] = self.failed_result_sample
        result['ServiceContentType'] = self.service_content_type
        result['ServiceHost'] = self.service_host
        result['ServicePath'] = self.service_path
        result['ServiceRequestBodyDescription'] = self.service_request_body_description
        result['SuccessfulResultSample'] = self.successful_result_sample
        result['RegistrationErrorCodes'] = []
        if self.registration_error_codes is not None:
            for k in self.registration_error_codes:
                result['RegistrationErrorCodes'].append(k.to_map() if k else None)
        else:
            result['RegistrationErrorCodes'] = None
        result['RegistrationRequestParameters'] = []
        if self.registration_request_parameters is not None:
            for k in self.registration_request_parameters:
                result['RegistrationRequestParameters'].append(k.to_map() if k else None)
        else:
            result['RegistrationRequestParameters'] = None
        return result

    def from_map(self, map={}):
        self.failed_result_sample = map.get('FailedResultSample')
        self.service_content_type = map.get('ServiceContentType')
        self.service_host = map.get('ServiceHost')
        self.service_path = map.get('ServicePath')
        self.service_request_body_description = map.get('ServiceRequestBodyDescription')
        self.successful_result_sample = map.get('SuccessfulResultSample')
        self.registration_error_codes = []
        if map.get('RegistrationErrorCodes') is not None:
            for k in map.get('RegistrationErrorCodes'):
                temp_model = GetDataServicePublishedApiResponseDataRegistrationDetailsRegistrationErrorCodes()
                self.registration_error_codes.append(temp_model.from_map(k))
        else:
            self.registration_error_codes = None
        self.registration_request_parameters = []
        if map.get('RegistrationRequestParameters') is not None:
            for k in map.get('RegistrationRequestParameters'):
                temp_model = GetDataServicePublishedApiResponseDataRegistrationDetailsRegistrationRequestParameters()
                self.registration_request_parameters.append(temp_model.from_map(k))
        else:
            self.registration_request_parameters = None
        return self


class GetDataServicePublishedApiResponseDataScriptDetailsScriptErrorCodes(TeaModel):
    def __init__(self, error_code=None, error_message=None, error_solution=None):
        self.error_code = error_code    # type: str
        self.error_message = error_message  # type: str
        self.error_solution = error_solution  # type: str

    def validate(self):
        self.validate_required(self.error_code, 'error_code')
        self.validate_required(self.error_message, 'error_message')
        self.validate_required(self.error_solution, 'error_solution')

    def to_map(self):
        result = {}
        result['ErrorCode'] = self.error_code
        result['ErrorMessage'] = self.error_message
        result['ErrorSolution'] = self.error_solution
        return result

    def from_map(self, map={}):
        self.error_code = map.get('ErrorCode')
        self.error_message = map.get('ErrorMessage')
        self.error_solution = map.get('ErrorSolution')
        return self


class GetDataServicePublishedApiResponseDataScriptDetailsScriptRequestParameters(TeaModel):
    def __init__(self, default_value=None, example_value=None, is_required_parameter=None,
                 parameter_data_type=None, parameter_description=None, parameter_name=None, parameter_operator=None,
                 parameter_position=None):
        self.default_value = default_value  # type: str
        self.example_value = example_value  # type: str
        self.is_required_parameter = is_required_parameter  # type: bool
        self.parameter_data_type = parameter_data_type  # type: int
        self.parameter_description = parameter_description  # type: str
        self.parameter_name = parameter_name  # type: str
        self.parameter_operator = parameter_operator  # type: int
        self.parameter_position = parameter_position  # type: int

    def validate(self):
        self.validate_required(self.default_value, 'default_value')
        self.validate_required(self.example_value, 'example_value')
        self.validate_required(self.is_required_parameter, 'is_required_parameter')
        self.validate_required(self.parameter_data_type, 'parameter_data_type')
        self.validate_required(self.parameter_description, 'parameter_description')
        self.validate_required(self.parameter_name, 'parameter_name')
        self.validate_required(self.parameter_operator, 'parameter_operator')
        self.validate_required(self.parameter_position, 'parameter_position')

    def to_map(self):
        result = {}
        result['DefaultValue'] = self.default_value
        result['ExampleValue'] = self.example_value
        result['IsRequiredParameter'] = self.is_required_parameter
        result['ParameterDataType'] = self.parameter_data_type
        result['ParameterDescription'] = self.parameter_description
        result['ParameterName'] = self.parameter_name
        result['ParameterOperator'] = self.parameter_operator
        result['ParameterPosition'] = self.parameter_position
        return result

    def from_map(self, map={}):
        self.default_value = map.get('DefaultValue')
        self.example_value = map.get('ExampleValue')
        self.is_required_parameter = map.get('IsRequiredParameter')
        self.parameter_data_type = map.get('ParameterDataType')
        self.parameter_description = map.get('ParameterDescription')
        self.parameter_name = map.get('ParameterName')
        self.parameter_operator = map.get('ParameterOperator')
        self.parameter_position = map.get('ParameterPosition')
        return self


class GetDataServicePublishedApiResponseDataScriptDetailsScriptResponseParameters(TeaModel):
    def __init__(self, example_value=None, parameter_data_type=None, parameter_description=None,
                 parameter_name=None):
        self.example_value = example_value  # type: str
        self.parameter_data_type = parameter_data_type  # type: int
        self.parameter_description = parameter_description  # type: str
        self.parameter_name = parameter_name  # type: str

    def validate(self):
        self.validate_required(self.example_value, 'example_value')
        self.validate_required(self.parameter_data_type, 'parameter_data_type')
        self.validate_required(self.parameter_description, 'parameter_description')
        self.validate_required(self.parameter_name, 'parameter_name')

    def to_map(self):
        result = {}
        result['ExampleValue'] = self.example_value
        result['ParameterDataType'] = self.parameter_data_type
        result['ParameterDescription'] = self.parameter_description
        result['ParameterName'] = self.parameter_name
        return result

    def from_map(self, map={}):
        self.example_value = map.get('ExampleValue')
        self.parameter_data_type = map.get('ParameterDataType')
        self.parameter_description = map.get('ParameterDescription')
        self.parameter_name = map.get('ParameterName')
        return self


class GetDataServicePublishedApiResponseDataScriptDetailsScriptConnection(TeaModel):
    def __init__(self, connection_id=None, table_name=None):
        self.connection_id = connection_id  # type: int
        self.table_name = table_name    # type: str

    def validate(self):
        self.validate_required(self.connection_id, 'connection_id')
        self.validate_required(self.table_name, 'table_name')

    def to_map(self):
        result = {}
        result['ConnectionId'] = self.connection_id
        result['TableName'] = self.table_name
        return result

    def from_map(self, map={}):
        self.connection_id = map.get('ConnectionId')
        self.table_name = map.get('TableName')
        return self


class GetDataServicePublishedApiResponseDataScriptDetails(TeaModel):
    def __init__(self, failed_result_sample=None, is_paged_response=None, script=None,
                 successful_result_sample=None, script_error_codes=None, script_request_parameters=None, script_response_parameters=None,
                 script_connection=None):
        self.failed_result_sample = failed_result_sample  # type: str
        self.is_paged_response = is_paged_response  # type: bool
        self.script = script            # type: str
        self.successful_result_sample = successful_result_sample  # type: str
        self.script_error_codes = script_error_codes  # type: List[GetDataServicePublishedApiResponseDataScriptDetailsScriptErrorCodes]
        self.script_request_parameters = script_request_parameters  # type: List[GetDataServicePublishedApiResponseDataScriptDetailsScriptRequestParameters]
        self.script_response_parameters = script_response_parameters  # type: List[GetDataServicePublishedApiResponseDataScriptDetailsScriptResponseParameters]
        self.script_connection = script_connection  # type: GetDataServicePublishedApiResponseDataScriptDetailsScriptConnection

    def validate(self):
        self.validate_required(self.failed_result_sample, 'failed_result_sample')
        self.validate_required(self.is_paged_response, 'is_paged_response')
        self.validate_required(self.script, 'script')
        self.validate_required(self.successful_result_sample, 'successful_result_sample')
        self.validate_required(self.script_error_codes, 'script_error_codes')
        if self.script_error_codes:
            for k in self.script_error_codes:
                if k:
                    k.validate()
        self.validate_required(self.script_request_parameters, 'script_request_parameters')
        if self.script_request_parameters:
            for k in self.script_request_parameters:
                if k:
                    k.validate()
        self.validate_required(self.script_response_parameters, 'script_response_parameters')
        if self.script_response_parameters:
            for k in self.script_response_parameters:
                if k:
                    k.validate()
        self.validate_required(self.script_connection, 'script_connection')
        if self.script_connection:
            self.script_connection.validate()

    def to_map(self):
        result = {}
        result['FailedResultSample'] = self.failed_result_sample
        result['IsPagedResponse'] = self.is_paged_response
        result['Script'] = self.script
        result['SuccessfulResultSample'] = self.successful_result_sample
        result['ScriptErrorCodes'] = []
        if self.script_error_codes is not None:
            for k in self.script_error_codes:
                result['ScriptErrorCodes'].append(k.to_map() if k else None)
        else:
            result['ScriptErrorCodes'] = None
        result['ScriptRequestParameters'] = []
        if self.script_request_parameters is not None:
            for k in self.script_request_parameters:
                result['ScriptRequestParameters'].append(k.to_map() if k else None)
        else:
            result['ScriptRequestParameters'] = None
        result['ScriptResponseParameters'] = []
        if self.script_response_parameters is not None:
            for k in self.script_response_parameters:
                result['ScriptResponseParameters'].append(k.to_map() if k else None)
        else:
            result['ScriptResponseParameters'] = None
        if self.script_connection is not None:
            result['ScriptConnection'] = self.script_connection.to_map()
        else:
            result['ScriptConnection'] = None
        return result

    def from_map(self, map={}):
        self.failed_result_sample = map.get('FailedResultSample')
        self.is_paged_response = map.get('IsPagedResponse')
        self.script = map.get('Script')
        self.successful_result_sample = map.get('SuccessfulResultSample')
        self.script_error_codes = []
        if map.get('ScriptErrorCodes') is not None:
            for k in map.get('ScriptErrorCodes'):
                temp_model = GetDataServicePublishedApiResponseDataScriptDetailsScriptErrorCodes()
                self.script_error_codes.append(temp_model.from_map(k))
        else:
            self.script_error_codes = None
        self.script_request_parameters = []
        if map.get('ScriptRequestParameters') is not None:
            for k in map.get('ScriptRequestParameters'):
                temp_model = GetDataServicePublishedApiResponseDataScriptDetailsScriptRequestParameters()
                self.script_request_parameters.append(temp_model.from_map(k))
        else:
            self.script_request_parameters = None
        self.script_response_parameters = []
        if map.get('ScriptResponseParameters') is not None:
            for k in map.get('ScriptResponseParameters'):
                temp_model = GetDataServicePublishedApiResponseDataScriptDetailsScriptResponseParameters()
                self.script_response_parameters.append(temp_model.from_map(k))
        else:
            self.script_response_parameters = None
        if map.get('ScriptConnection') is not None:
            temp_model = GetDataServicePublishedApiResponseDataScriptDetailsScriptConnection()
            self.script_connection = temp_model.from_map(map['ScriptConnection'])
        else:
            self.script_connection = None
        return self


class GetDataServicePublishedApiResponseDataWizardDetailsWizardErrorCodes(TeaModel):
    def __init__(self, error_code=None, error_message=None, error_solution=None):
        self.error_code = error_code    # type: str
        self.error_message = error_message  # type: str
        self.error_solution = error_solution  # type: str

    def validate(self):
        self.validate_required(self.error_code, 'error_code')
        self.validate_required(self.error_message, 'error_message')
        self.validate_required(self.error_solution, 'error_solution')

    def to_map(self):
        result = {}
        result['ErrorCode'] = self.error_code
        result['ErrorMessage'] = self.error_message
        result['ErrorSolution'] = self.error_solution
        return result

    def from_map(self, map={}):
        self.error_code = map.get('ErrorCode')
        self.error_message = map.get('ErrorMessage')
        self.error_solution = map.get('ErrorSolution')
        return self


class GetDataServicePublishedApiResponseDataWizardDetailsWizardRequestParameters(TeaModel):
    def __init__(self, default_value=None, example_value=None, is_required_parameter=None,
                 parameter_data_type=None, parameter_description=None, parameter_name=None, parameter_operator=None,
                 parameter_position=None):
        self.default_value = default_value  # type: str
        self.example_value = example_value  # type: str
        self.is_required_parameter = is_required_parameter  # type: bool
        self.parameter_data_type = parameter_data_type  # type: int
        self.parameter_description = parameter_description  # type: str
        self.parameter_name = parameter_name  # type: str
        self.parameter_operator = parameter_operator  # type: int
        self.parameter_position = parameter_position  # type: int

    def validate(self):
        self.validate_required(self.default_value, 'default_value')
        self.validate_required(self.example_value, 'example_value')
        self.validate_required(self.is_required_parameter, 'is_required_parameter')
        self.validate_required(self.parameter_data_type, 'parameter_data_type')
        self.validate_required(self.parameter_description, 'parameter_description')
        self.validate_required(self.parameter_name, 'parameter_name')
        self.validate_required(self.parameter_operator, 'parameter_operator')
        self.validate_required(self.parameter_position, 'parameter_position')

    def to_map(self):
        result = {}
        result['DefaultValue'] = self.default_value
        result['ExampleValue'] = self.example_value
        result['IsRequiredParameter'] = self.is_required_parameter
        result['ParameterDataType'] = self.parameter_data_type
        result['ParameterDescription'] = self.parameter_description
        result['ParameterName'] = self.parameter_name
        result['ParameterOperator'] = self.parameter_operator
        result['ParameterPosition'] = self.parameter_position
        return result

    def from_map(self, map={}):
        self.default_value = map.get('DefaultValue')
        self.example_value = map.get('ExampleValue')
        self.is_required_parameter = map.get('IsRequiredParameter')
        self.parameter_data_type = map.get('ParameterDataType')
        self.parameter_description = map.get('ParameterDescription')
        self.parameter_name = map.get('ParameterName')
        self.parameter_operator = map.get('ParameterOperator')
        self.parameter_position = map.get('ParameterPosition')
        return self


class GetDataServicePublishedApiResponseDataWizardDetailsWizardResponseParameters(TeaModel):
    def __init__(self, example_value=None, parameter_data_type=None, parameter_description=None,
                 parameter_name=None):
        self.example_value = example_value  # type: str
        self.parameter_data_type = parameter_data_type  # type: int
        self.parameter_description = parameter_description  # type: str
        self.parameter_name = parameter_name  # type: str

    def validate(self):
        self.validate_required(self.example_value, 'example_value')
        self.validate_required(self.parameter_data_type, 'parameter_data_type')
        self.validate_required(self.parameter_description, 'parameter_description')
        self.validate_required(self.parameter_name, 'parameter_name')

    def to_map(self):
        result = {}
        result['ExampleValue'] = self.example_value
        result['ParameterDataType'] = self.parameter_data_type
        result['ParameterDescription'] = self.parameter_description
        result['ParameterName'] = self.parameter_name
        return result

    def from_map(self, map={}):
        self.example_value = map.get('ExampleValue')
        self.parameter_data_type = map.get('ParameterDataType')
        self.parameter_description = map.get('ParameterDescription')
        self.parameter_name = map.get('ParameterName')
        return self


class GetDataServicePublishedApiResponseDataWizardDetailsWizardConnection(TeaModel):
    def __init__(self, connection_id=None, table_name=None):
        self.connection_id = connection_id  # type: int
        self.table_name = table_name    # type: str

    def validate(self):
        self.validate_required(self.connection_id, 'connection_id')
        self.validate_required(self.table_name, 'table_name')

    def to_map(self):
        result = {}
        result['ConnectionId'] = self.connection_id
        result['TableName'] = self.table_name
        return result

    def from_map(self, map={}):
        self.connection_id = map.get('ConnectionId')
        self.table_name = map.get('TableName')
        return self


class GetDataServicePublishedApiResponseDataWizardDetails(TeaModel):
    def __init__(self, failed_result_sample=None, is_paged_response=None, successful_result_sample=None,
                 wizard_error_codes=None, wizard_request_parameters=None, wizard_response_parameters=None, wizard_connection=None):
        self.failed_result_sample = failed_result_sample  # type: str
        self.is_paged_response = is_paged_response  # type: bool
        self.successful_result_sample = successful_result_sample  # type: str
        self.wizard_error_codes = wizard_error_codes  # type: List[GetDataServicePublishedApiResponseDataWizardDetailsWizardErrorCodes]
        self.wizard_request_parameters = wizard_request_parameters  # type: List[GetDataServicePublishedApiResponseDataWizardDetailsWizardRequestParameters]
        self.wizard_response_parameters = wizard_response_parameters  # type: List[GetDataServicePublishedApiResponseDataWizardDetailsWizardResponseParameters]
        self.wizard_connection = wizard_connection  # type: GetDataServicePublishedApiResponseDataWizardDetailsWizardConnection

    def validate(self):
        self.validate_required(self.failed_result_sample, 'failed_result_sample')
        self.validate_required(self.is_paged_response, 'is_paged_response')
        self.validate_required(self.successful_result_sample, 'successful_result_sample')
        self.validate_required(self.wizard_error_codes, 'wizard_error_codes')
        if self.wizard_error_codes:
            for k in self.wizard_error_codes:
                if k:
                    k.validate()
        self.validate_required(self.wizard_request_parameters, 'wizard_request_parameters')
        if self.wizard_request_parameters:
            for k in self.wizard_request_parameters:
                if k:
                    k.validate()
        self.validate_required(self.wizard_response_parameters, 'wizard_response_parameters')
        if self.wizard_response_parameters:
            for k in self.wizard_response_parameters:
                if k:
                    k.validate()
        self.validate_required(self.wizard_connection, 'wizard_connection')
        if self.wizard_connection:
            self.wizard_connection.validate()

    def to_map(self):
        result = {}
        result['FailedResultSample'] = self.failed_result_sample
        result['IsPagedResponse'] = self.is_paged_response
        result['SuccessfulResultSample'] = self.successful_result_sample
        result['WizardErrorCodes'] = []
        if self.wizard_error_codes is not None:
            for k in self.wizard_error_codes:
                result['WizardErrorCodes'].append(k.to_map() if k else None)
        else:
            result['WizardErrorCodes'] = None
        result['WizardRequestParameters'] = []
        if self.wizard_request_parameters is not None:
            for k in self.wizard_request_parameters:
                result['WizardRequestParameters'].append(k.to_map() if k else None)
        else:
            result['WizardRequestParameters'] = None
        result['WizardResponseParameters'] = []
        if self.wizard_response_parameters is not None:
            for k in self.wizard_response_parameters:
                result['WizardResponseParameters'].append(k.to_map() if k else None)
        else:
            result['WizardResponseParameters'] = None
        if self.wizard_connection is not None:
            result['WizardConnection'] = self.wizard_connection.to_map()
        else:
            result['WizardConnection'] = None
        return result

    def from_map(self, map={}):
        self.failed_result_sample = map.get('FailedResultSample')
        self.is_paged_response = map.get('IsPagedResponse')
        self.successful_result_sample = map.get('SuccessfulResultSample')
        self.wizard_error_codes = []
        if map.get('WizardErrorCodes') is not None:
            for k in map.get('WizardErrorCodes'):
                temp_model = GetDataServicePublishedApiResponseDataWizardDetailsWizardErrorCodes()
                self.wizard_error_codes.append(temp_model.from_map(k))
        else:
            self.wizard_error_codes = None
        self.wizard_request_parameters = []
        if map.get('WizardRequestParameters') is not None:
            for k in map.get('WizardRequestParameters'):
                temp_model = GetDataServicePublishedApiResponseDataWizardDetailsWizardRequestParameters()
                self.wizard_request_parameters.append(temp_model.from_map(k))
        else:
            self.wizard_request_parameters = None
        self.wizard_response_parameters = []
        if map.get('WizardResponseParameters') is not None:
            for k in map.get('WizardResponseParameters'):
                temp_model = GetDataServicePublishedApiResponseDataWizardDetailsWizardResponseParameters()
                self.wizard_response_parameters.append(temp_model.from_map(k))
        else:
            self.wizard_response_parameters = None
        if map.get('WizardConnection') is not None:
            temp_model = GetDataServicePublishedApiResponseDataWizardDetailsWizardConnection()
            self.wizard_connection = temp_model.from_map(map['WizardConnection'])
        else:
            self.wizard_connection = None
        return self


class GetDataServicePublishedApiResponseData(TeaModel):
    def __init__(self, api_id=None, api_mode=None, api_name=None, api_path=None, created_time=None, creator_id=None,
                 description=None, group_id=None, modified_time=None, operator_id=None, project_id=None, request_method=None,
                 response_content_type=None, status=None, tenant_id=None, timeout=None, visible_range=None, registration_details=None,
                 script_details=None, wizard_details=None, protocols=None):
        self.api_id = api_id            # type: int
        self.api_mode = api_mode        # type: int
        self.api_name = api_name        # type: str
        self.api_path = api_path        # type: str
        self.created_time = created_time  # type: str
        self.creator_id = creator_id    # type: str
        self.description = description  # type: str
        self.group_id = group_id        # type: str
        self.modified_time = modified_time  # type: str
        self.operator_id = operator_id  # type: str
        self.project_id = project_id    # type: int
        self.request_method = request_method  # type: int
        self.response_content_type = response_content_type  # type: int
        self.status = status            # type: int
        self.tenant_id = tenant_id      # type: int
        self.timeout = timeout          # type: int
        self.visible_range = visible_range  # type: int
        self.registration_details = registration_details  # type: GetDataServicePublishedApiResponseDataRegistrationDetails
        self.script_details = script_details  # type: GetDataServicePublishedApiResponseDataScriptDetails
        self.wizard_details = wizard_details  # type: GetDataServicePublishedApiResponseDataWizardDetails
        self.protocols = protocols      # type: List[int]

    def validate(self):
        self.validate_required(self.api_id, 'api_id')
        self.validate_required(self.api_mode, 'api_mode')
        self.validate_required(self.api_name, 'api_name')
        self.validate_required(self.api_path, 'api_path')
        self.validate_required(self.created_time, 'created_time')
        self.validate_required(self.creator_id, 'creator_id')
        self.validate_required(self.description, 'description')
        self.validate_required(self.group_id, 'group_id')
        self.validate_required(self.modified_time, 'modified_time')
        self.validate_required(self.operator_id, 'operator_id')
        self.validate_required(self.project_id, 'project_id')
        self.validate_required(self.request_method, 'request_method')
        self.validate_required(self.response_content_type, 'response_content_type')
        self.validate_required(self.status, 'status')
        self.validate_required(self.tenant_id, 'tenant_id')
        self.validate_required(self.timeout, 'timeout')
        self.validate_required(self.visible_range, 'visible_range')
        self.validate_required(self.registration_details, 'registration_details')
        if self.registration_details:
            self.registration_details.validate()
        self.validate_required(self.script_details, 'script_details')
        if self.script_details:
            self.script_details.validate()
        self.validate_required(self.wizard_details, 'wizard_details')
        if self.wizard_details:
            self.wizard_details.validate()
        self.validate_required(self.protocols, 'protocols')

    def to_map(self):
        result = {}
        result['ApiId'] = self.api_id
        result['ApiMode'] = self.api_mode
        result['ApiName'] = self.api_name
        result['ApiPath'] = self.api_path
        result['CreatedTime'] = self.created_time
        result['CreatorId'] = self.creator_id
        result['Description'] = self.description
        result['GroupId'] = self.group_id
        result['ModifiedTime'] = self.modified_time
        result['OperatorId'] = self.operator_id
        result['ProjectId'] = self.project_id
        result['RequestMethod'] = self.request_method
        result['ResponseContentType'] = self.response_content_type
        result['Status'] = self.status
        result['TenantId'] = self.tenant_id
        result['Timeout'] = self.timeout
        result['VisibleRange'] = self.visible_range
        if self.registration_details is not None:
            result['RegistrationDetails'] = self.registration_details.to_map()
        else:
            result['RegistrationDetails'] = None
        if self.script_details is not None:
            result['ScriptDetails'] = self.script_details.to_map()
        else:
            result['ScriptDetails'] = None
        if self.wizard_details is not None:
            result['WizardDetails'] = self.wizard_details.to_map()
        else:
            result['WizardDetails'] = None
        result['Protocols'] = self.protocols
        return result

    def from_map(self, map={}):
        self.api_id = map.get('ApiId')
        self.api_mode = map.get('ApiMode')
        self.api_name = map.get('ApiName')
        self.api_path = map.get('ApiPath')
        self.created_time = map.get('CreatedTime')
        self.creator_id = map.get('CreatorId')
        self.description = map.get('Description')
        self.group_id = map.get('GroupId')
        self.modified_time = map.get('ModifiedTime')
        self.operator_id = map.get('OperatorId')
        self.project_id = map.get('ProjectId')
        self.request_method = map.get('RequestMethod')
        self.response_content_type = map.get('ResponseContentType')
        self.status = map.get('Status')
        self.tenant_id = map.get('TenantId')
        self.timeout = map.get('Timeout')
        self.visible_range = map.get('VisibleRange')
        if map.get('RegistrationDetails') is not None:
            temp_model = GetDataServicePublishedApiResponseDataRegistrationDetails()
            self.registration_details = temp_model.from_map(map['RegistrationDetails'])
        else:
            self.registration_details = None
        if map.get('ScriptDetails') is not None:
            temp_model = GetDataServicePublishedApiResponseDataScriptDetails()
            self.script_details = temp_model.from_map(map['ScriptDetails'])
        else:
            self.script_details = None
        if map.get('WizardDetails') is not None:
            temp_model = GetDataServicePublishedApiResponseDataWizardDetails()
            self.wizard_details = temp_model.from_map(map['WizardDetails'])
        else:
            self.wizard_details = None
        self.protocols = map.get('Protocols')
        return self


class GetBaselineKeyPathRequest(TeaModel):
    def __init__(self, baseline_id=None, bizdate=None, in_group_id=None):
        self.baseline_id = baseline_id  # type: int
        self.bizdate = bizdate          # type: str
        self.in_group_id = in_group_id  # type: int

    def validate(self):
        self.validate_required(self.baseline_id, 'baseline_id')
        self.validate_required(self.bizdate, 'bizdate')
        self.validate_required(self.in_group_id, 'in_group_id')

    def to_map(self):
        result = {}
        result['BaselineId'] = self.baseline_id
        result['Bizdate'] = self.bizdate
        result['InGroupId'] = self.in_group_id
        return result

    def from_map(self, map={}):
        self.baseline_id = map.get('BaselineId')
        self.bizdate = map.get('Bizdate')
        self.in_group_id = map.get('InGroupId')
        return self


class GetBaselineKeyPathResponse(TeaModel):
    def __init__(self, success=None, error_code=None, error_message=None, http_status_code=None, request_id=None,
                 data=None):
        self.success = success          # type: bool
        self.error_code = error_code    # type: str
        self.error_message = error_message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.request_id = request_id    # type: str
        self.data = data                # type: List[GetBaselineKeyPathResponseData]

    def validate(self):
        self.validate_required(self.success, 'success')
        self.validate_required(self.error_code, 'error_code')
        self.validate_required(self.error_message, 'error_message')
        self.validate_required(self.http_status_code, 'http_status_code')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['Success'] = self.success
        result['ErrorCode'] = self.error_code
        result['ErrorMessage'] = self.error_message
        result['HttpStatusCode'] = self.http_status_code
        result['RequestId'] = self.request_id
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.success = map.get('Success')
        self.error_code = map.get('ErrorCode')
        self.error_message = map.get('ErrorMessage')
        self.http_status_code = map.get('HttpStatusCode')
        self.request_id = map.get('RequestId')
        self.data = []
        if map.get('Data') is not None:
            for k in map.get('Data'):
                temp_model = GetBaselineKeyPathResponseData()
                self.data.append(temp_model.from_map(k))
        else:
            self.data = None
        return self


class GetBaselineKeyPathResponseDataRuns(TeaModel):
    def __init__(self, abs_time=None, begin_cast=None, begin_running_time=None, begin_wait_res_time=None,
                 begin_wait_time_time=None, bizdate=None, cyc_time=None, end_cast=None, finish_time=None, in_group_id=None,
                 instance_id=None, node_id=None, node_name=None, owner=None, project_id=None, status=None):
        self.abs_time = abs_time        # type: int
        self.begin_cast = begin_cast    # type: int
        self.begin_running_time = begin_running_time  # type: int
        self.begin_wait_res_time = begin_wait_res_time  # type: int
        self.begin_wait_time_time = begin_wait_time_time  # type: int
        self.bizdate = bizdate          # type: int
        self.cyc_time = cyc_time        # type: int
        self.end_cast = end_cast        # type: int
        self.finish_time = finish_time  # type: int
        self.in_group_id = in_group_id  # type: int
        self.instance_id = instance_id  # type: int
        self.node_id = node_id          # type: int
        self.node_name = node_name      # type: str
        self.owner = owner              # type: str
        self.project_id = project_id    # type: int
        self.status = status            # type: str

    def validate(self):
        self.validate_required(self.abs_time, 'abs_time')
        self.validate_required(self.begin_cast, 'begin_cast')
        self.validate_required(self.begin_running_time, 'begin_running_time')
        self.validate_required(self.begin_wait_res_time, 'begin_wait_res_time')
        self.validate_required(self.begin_wait_time_time, 'begin_wait_time_time')
        self.validate_required(self.bizdate, 'bizdate')
        self.validate_required(self.cyc_time, 'cyc_time')
        self.validate_required(self.end_cast, 'end_cast')
        self.validate_required(self.finish_time, 'finish_time')
        self.validate_required(self.in_group_id, 'in_group_id')
        self.validate_required(self.instance_id, 'instance_id')
        self.validate_required(self.node_id, 'node_id')
        self.validate_required(self.node_name, 'node_name')
        self.validate_required(self.owner, 'owner')
        self.validate_required(self.project_id, 'project_id')
        self.validate_required(self.status, 'status')

    def to_map(self):
        result = {}
        result['AbsTime'] = self.abs_time
        result['BeginCast'] = self.begin_cast
        result['BeginRunningTime'] = self.begin_running_time
        result['BeginWaitResTime'] = self.begin_wait_res_time
        result['BeginWaitTimeTime'] = self.begin_wait_time_time
        result['Bizdate'] = self.bizdate
        result['CycTime'] = self.cyc_time
        result['EndCast'] = self.end_cast
        result['FinishTime'] = self.finish_time
        result['InGroupId'] = self.in_group_id
        result['InstanceId'] = self.instance_id
        result['NodeId'] = self.node_id
        result['NodeName'] = self.node_name
        result['Owner'] = self.owner
        result['ProjectId'] = self.project_id
        result['Status'] = self.status
        return result

    def from_map(self, map={}):
        self.abs_time = map.get('AbsTime')
        self.begin_cast = map.get('BeginCast')
        self.begin_running_time = map.get('BeginRunningTime')
        self.begin_wait_res_time = map.get('BeginWaitResTime')
        self.begin_wait_time_time = map.get('BeginWaitTimeTime')
        self.bizdate = map.get('Bizdate')
        self.cyc_time = map.get('CycTime')
        self.end_cast = map.get('EndCast')
        self.finish_time = map.get('FinishTime')
        self.in_group_id = map.get('InGroupId')
        self.instance_id = map.get('InstanceId')
        self.node_id = map.get('NodeId')
        self.node_name = map.get('NodeName')
        self.owner = map.get('Owner')
        self.project_id = map.get('ProjectId')
        self.status = map.get('Status')
        return self


class GetBaselineKeyPathResponseDataTopics(TeaModel):
    def __init__(self, instance_id=None, topic_id=None, topic_name=None, add_time=None):
        self.instance_id = instance_id  # type: int
        self.topic_id = topic_id        # type: int
        self.topic_name = topic_name    # type: int
        self.add_time = add_time        # type: int

    def validate(self):
        self.validate_required(self.instance_id, 'instance_id')
        self.validate_required(self.topic_id, 'topic_id')
        self.validate_required(self.topic_name, 'topic_name')
        self.validate_required(self.add_time, 'add_time')

    def to_map(self):
        result = {}
        result['InstanceId'] = self.instance_id
        result['TopicId'] = self.topic_id
        result['TopicName'] = self.topic_name
        result['AddTime'] = self.add_time
        return result

    def from_map(self, map={}):
        self.instance_id = map.get('InstanceId')
        self.topic_id = map.get('TopicId')
        self.topic_name = map.get('TopicName')
        self.add_time = map.get('AddTime')
        return self


class GetBaselineKeyPathResponseData(TeaModel):
    def __init__(self, instance_id=None, project_id=None, node_id=None, node_name=None, bizdate=None,
                 in_group_id=None, owner=None, prg_type=None, runs=None, topics=None):
        self.instance_id = instance_id  # type: int
        self.project_id = project_id    # type: int
        self.node_id = node_id          # type: int
        self.node_name = node_name      # type: str
        self.bizdate = bizdate          # type: int
        self.in_group_id = in_group_id  # type: int
        self.owner = owner              # type: str
        self.prg_type = prg_type        # type: int
        self.runs = runs                # type: List[GetBaselineKeyPathResponseDataRuns]
        self.topics = topics            # type: List[GetBaselineKeyPathResponseDataTopics]

    def validate(self):
        self.validate_required(self.instance_id, 'instance_id')
        self.validate_required(self.project_id, 'project_id')
        self.validate_required(self.node_id, 'node_id')
        self.validate_required(self.node_name, 'node_name')
        self.validate_required(self.bizdate, 'bizdate')
        self.validate_required(self.in_group_id, 'in_group_id')
        self.validate_required(self.owner, 'owner')
        self.validate_required(self.prg_type, 'prg_type')
        self.validate_required(self.runs, 'runs')
        if self.runs:
            for k in self.runs:
                if k:
                    k.validate()
        self.validate_required(self.topics, 'topics')
        if self.topics:
            for k in self.topics:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['InstanceId'] = self.instance_id
        result['ProjectId'] = self.project_id
        result['NodeId'] = self.node_id
        result['NodeName'] = self.node_name
        result['Bizdate'] = self.bizdate
        result['InGroupId'] = self.in_group_id
        result['Owner'] = self.owner
        result['PrgType'] = self.prg_type
        result['Runs'] = []
        if self.runs is not None:
            for k in self.runs:
                result['Runs'].append(k.to_map() if k else None)
        else:
            result['Runs'] = None
        result['Topics'] = []
        if self.topics is not None:
            for k in self.topics:
                result['Topics'].append(k.to_map() if k else None)
        else:
            result['Topics'] = None
        return result

    def from_map(self, map={}):
        self.instance_id = map.get('InstanceId')
        self.project_id = map.get('ProjectId')
        self.node_id = map.get('NodeId')
        self.node_name = map.get('NodeName')
        self.bizdate = map.get('Bizdate')
        self.in_group_id = map.get('InGroupId')
        self.owner = map.get('Owner')
        self.prg_type = map.get('PrgType')
        self.runs = []
        if map.get('Runs') is not None:
            for k in map.get('Runs'):
                temp_model = GetBaselineKeyPathResponseDataRuns()
                self.runs.append(temp_model.from_map(k))
        else:
            self.runs = None
        self.topics = []
        if map.get('Topics') is not None:
            for k in map.get('Topics'):
                temp_model = GetBaselineKeyPathResponseDataTopics()
                self.topics.append(temp_model.from_map(k))
        else:
            self.topics = None
        return self


class GetRemindRequest(TeaModel):
    def __init__(self, remind_id=None):
        self.remind_id = remind_id      # type: int

    def validate(self):
        self.validate_required(self.remind_id, 'remind_id')

    def to_map(self):
        result = {}
        result['RemindId'] = self.remind_id
        return result

    def from_map(self, map={}):
        self.remind_id = map.get('RemindId')
        return self


class GetRemindResponse(TeaModel):
    def __init__(self, success=None, error_code=None, error_message=None, http_status_code=None, request_id=None,
                 data=None):
        self.success = success          # type: bool
        self.error_code = error_code    # type: str
        self.error_message = error_message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.request_id = request_id    # type: str
        self.data = data                # type: GetRemindResponseData

    def validate(self):
        self.validate_required(self.success, 'success')
        self.validate_required(self.error_code, 'error_code')
        self.validate_required(self.error_message, 'error_message')
        self.validate_required(self.http_status_code, 'http_status_code')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['Success'] = self.success
        result['ErrorCode'] = self.error_code
        result['ErrorMessage'] = self.error_message
        result['HttpStatusCode'] = self.http_status_code
        result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.success = map.get('Success')
        self.error_code = map.get('ErrorCode')
        self.error_message = map.get('ErrorMessage')
        self.http_status_code = map.get('HttpStatusCode')
        self.request_id = map.get('RequestId')
        if map.get('Data') is not None:
            temp_model = GetRemindResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class GetRemindResponseDataRobots(TeaModel):
    def __init__(self, web_url=None, at_all=None):
        self.web_url = web_url          # type: str
        self.at_all = at_all            # type: bool

    def validate(self):
        self.validate_required(self.web_url, 'web_url')
        self.validate_required(self.at_all, 'at_all')

    def to_map(self):
        result = {}
        result['WebUrl'] = self.web_url
        result['AtAll'] = self.at_all
        return result

    def from_map(self, map={}):
        self.web_url = map.get('WebUrl')
        self.at_all = map.get('AtAll')
        return self


class GetRemindResponseDataNodes(TeaModel):
    def __init__(self, node_id=None, node_name=None, owner=None, project_id=None):
        self.node_id = node_id          # type: int
        self.node_name = node_name      # type: str
        self.owner = owner              # type: str
        self.project_id = project_id    # type: int

    def validate(self):
        self.validate_required(self.node_id, 'node_id')
        self.validate_required(self.node_name, 'node_name')
        self.validate_required(self.owner, 'owner')
        self.validate_required(self.project_id, 'project_id')

    def to_map(self):
        result = {}
        result['NodeId'] = self.node_id
        result['NodeName'] = self.node_name
        result['Owner'] = self.owner
        result['ProjectId'] = self.project_id
        return result

    def from_map(self, map={}):
        self.node_id = map.get('NodeId')
        self.node_name = map.get('NodeName')
        self.owner = map.get('Owner')
        self.project_id = map.get('ProjectId')
        return self


class GetRemindResponseDataBaselines(TeaModel):
    def __init__(self, baseline_id=None, baseline_name=None):
        self.baseline_id = baseline_id  # type: int
        self.baseline_name = baseline_name  # type: str

    def validate(self):
        self.validate_required(self.baseline_id, 'baseline_id')
        self.validate_required(self.baseline_name, 'baseline_name')

    def to_map(self):
        result = {}
        result['BaselineId'] = self.baseline_id
        result['BaselineName'] = self.baseline_name
        return result

    def from_map(self, map={}):
        self.baseline_id = map.get('BaselineId')
        self.baseline_name = map.get('BaselineName')
        return self


class GetRemindResponseDataProjects(TeaModel):
    def __init__(self, project_id=None):
        self.project_id = project_id    # type: int

    def validate(self):
        self.validate_required(self.project_id, 'project_id')

    def to_map(self):
        result = {}
        result['ProjectId'] = self.project_id
        return result

    def from_map(self, map={}):
        self.project_id = map.get('ProjectId')
        return self


class GetRemindResponseDataBizProcesses(TeaModel):
    def __init__(self, biz_id=None, biz_process_name=None):
        self.biz_id = biz_id            # type: int
        self.biz_process_name = biz_process_name  # type: str

    def validate(self):
        self.validate_required(self.biz_id, 'biz_id')
        self.validate_required(self.biz_process_name, 'biz_process_name')

    def to_map(self):
        result = {}
        result['BizId'] = self.biz_id
        result['BizProcessName'] = self.biz_process_name
        return result

    def from_map(self, map={}):
        self.biz_id = map.get('BizId')
        self.biz_process_name = map.get('BizProcessName')
        return self


class GetRemindResponseData(TeaModel):
    def __init__(self, remind_id=None, remind_name=None, dnd_start=None, dnd_end=None, remind_unit=None,
                 remind_type=None, alert_unit=None, useflag=None, founder=None, alert_interval=None, detail=None,
                 max_alert_times=None, robots=None, nodes=None, baselines=None, projects=None, biz_processes=None,
                 alert_methods=None, alert_targets=None):
        self.remind_id = remind_id      # type: int
        self.remind_name = remind_name  # type: str
        self.dnd_start = dnd_start      # type: str
        self.dnd_end = dnd_end          # type: str
        self.remind_unit = remind_unit  # type: str
        self.remind_type = remind_type  # type: str
        self.alert_unit = alert_unit    # type: str
        self.useflag = useflag          # type: bool
        self.founder = founder          # type: str
        self.alert_interval = alert_interval  # type: int
        self.detail = detail            # type: str
        self.max_alert_times = max_alert_times  # type: int
        self.robots = robots            # type: List[GetRemindResponseDataRobots]
        self.nodes = nodes              # type: List[GetRemindResponseDataNodes]
        self.baselines = baselines      # type: List[GetRemindResponseDataBaselines]
        self.projects = projects        # type: List[GetRemindResponseDataProjects]
        self.biz_processes = biz_processes  # type: List[GetRemindResponseDataBizProcesses]
        self.alert_methods = alert_methods  # type: List[str]
        self.alert_targets = alert_targets  # type: List[str]

    def validate(self):
        self.validate_required(self.remind_id, 'remind_id')
        self.validate_required(self.remind_name, 'remind_name')
        self.validate_required(self.dnd_start, 'dnd_start')
        self.validate_required(self.dnd_end, 'dnd_end')
        self.validate_required(self.remind_unit, 'remind_unit')
        self.validate_required(self.remind_type, 'remind_type')
        self.validate_required(self.alert_unit, 'alert_unit')
        self.validate_required(self.useflag, 'useflag')
        self.validate_required(self.founder, 'founder')
        self.validate_required(self.alert_interval, 'alert_interval')
        self.validate_required(self.detail, 'detail')
        self.validate_required(self.max_alert_times, 'max_alert_times')
        self.validate_required(self.robots, 'robots')
        if self.robots:
            for k in self.robots:
                if k:
                    k.validate()
        self.validate_required(self.nodes, 'nodes')
        if self.nodes:
            for k in self.nodes:
                if k:
                    k.validate()
        self.validate_required(self.baselines, 'baselines')
        if self.baselines:
            for k in self.baselines:
                if k:
                    k.validate()
        self.validate_required(self.projects, 'projects')
        if self.projects:
            for k in self.projects:
                if k:
                    k.validate()
        self.validate_required(self.biz_processes, 'biz_processes')
        if self.biz_processes:
            for k in self.biz_processes:
                if k:
                    k.validate()
        self.validate_required(self.alert_methods, 'alert_methods')
        self.validate_required(self.alert_targets, 'alert_targets')

    def to_map(self):
        result = {}
        result['RemindId'] = self.remind_id
        result['RemindName'] = self.remind_name
        result['DndStart'] = self.dnd_start
        result['DndEnd'] = self.dnd_end
        result['RemindUnit'] = self.remind_unit
        result['RemindType'] = self.remind_type
        result['AlertUnit'] = self.alert_unit
        result['Useflag'] = self.useflag
        result['Founder'] = self.founder
        result['AlertInterval'] = self.alert_interval
        result['Detail'] = self.detail
        result['MaxAlertTimes'] = self.max_alert_times
        result['Robots'] = []
        if self.robots is not None:
            for k in self.robots:
                result['Robots'].append(k.to_map() if k else None)
        else:
            result['Robots'] = None
        result['Nodes'] = []
        if self.nodes is not None:
            for k in self.nodes:
                result['Nodes'].append(k.to_map() if k else None)
        else:
            result['Nodes'] = None
        result['Baselines'] = []
        if self.baselines is not None:
            for k in self.baselines:
                result['Baselines'].append(k.to_map() if k else None)
        else:
            result['Baselines'] = None
        result['Projects'] = []
        if self.projects is not None:
            for k in self.projects:
                result['Projects'].append(k.to_map() if k else None)
        else:
            result['Projects'] = None
        result['BizProcesses'] = []
        if self.biz_processes is not None:
            for k in self.biz_processes:
                result['BizProcesses'].append(k.to_map() if k else None)
        else:
            result['BizProcesses'] = None
        result['AlertMethods'] = self.alert_methods
        result['AlertTargets'] = self.alert_targets
        return result

    def from_map(self, map={}):
        self.remind_id = map.get('RemindId')
        self.remind_name = map.get('RemindName')
        self.dnd_start = map.get('DndStart')
        self.dnd_end = map.get('DndEnd')
        self.remind_unit = map.get('RemindUnit')
        self.remind_type = map.get('RemindType')
        self.alert_unit = map.get('AlertUnit')
        self.useflag = map.get('Useflag')
        self.founder = map.get('Founder')
        self.alert_interval = map.get('AlertInterval')
        self.detail = map.get('Detail')
        self.max_alert_times = map.get('MaxAlertTimes')
        self.robots = []
        if map.get('Robots') is not None:
            for k in map.get('Robots'):
                temp_model = GetRemindResponseDataRobots()
                self.robots.append(temp_model.from_map(k))
        else:
            self.robots = None
        self.nodes = []
        if map.get('Nodes') is not None:
            for k in map.get('Nodes'):
                temp_model = GetRemindResponseDataNodes()
                self.nodes.append(temp_model.from_map(k))
        else:
            self.nodes = None
        self.baselines = []
        if map.get('Baselines') is not None:
            for k in map.get('Baselines'):
                temp_model = GetRemindResponseDataBaselines()
                self.baselines.append(temp_model.from_map(k))
        else:
            self.baselines = None
        self.projects = []
        if map.get('Projects') is not None:
            for k in map.get('Projects'):
                temp_model = GetRemindResponseDataProjects()
                self.projects.append(temp_model.from_map(k))
        else:
            self.projects = None
        self.biz_processes = []
        if map.get('BizProcesses') is not None:
            for k in map.get('BizProcesses'):
                temp_model = GetRemindResponseDataBizProcesses()
                self.biz_processes.append(temp_model.from_map(k))
        else:
            self.biz_processes = None
        self.alert_methods = map.get('AlertMethods')
        self.alert_targets = map.get('AlertTargets')
        return self


class GetMetaTableIntroWikiRequest(TeaModel):
    def __init__(self, table_guid=None, wiki_version=None):
        self.table_guid = table_guid    # type: str
        self.wiki_version = wiki_version  # type: int

    def validate(self):
        self.validate_required(self.table_guid, 'table_guid')

    def to_map(self):
        result = {}
        result['TableGuid'] = self.table_guid
        result['WikiVersion'] = self.wiki_version
        return result

    def from_map(self, map={}):
        self.table_guid = map.get('TableGuid')
        self.wiki_version = map.get('WikiVersion')
        return self


class GetMetaTableIntroWikiResponse(TeaModel):
    def __init__(self, request_id=None, error_code=None, error_message=None, http_status_code=None, success=None,
                 data=None):
        self.request_id = request_id    # type: str
        self.error_code = error_code    # type: str
        self.error_message = error_message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.success = success          # type: bool
        self.data = data                # type: GetMetaTableIntroWikiResponseData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.error_code, 'error_code')
        self.validate_required(self.error_message, 'error_message')
        self.validate_required(self.http_status_code, 'http_status_code')
        self.validate_required(self.success, 'success')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['ErrorCode'] = self.error_code
        result['ErrorMessage'] = self.error_message
        result['HttpStatusCode'] = self.http_status_code
        result['Success'] = self.success
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.error_code = map.get('ErrorCode')
        self.error_message = map.get('ErrorMessage')
        self.http_status_code = map.get('HttpStatusCode')
        self.success = map.get('Success')
        if map.get('Data') is not None:
            temp_model = GetMetaTableIntroWikiResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class GetMetaTableIntroWikiResponseData(TeaModel):
    def __init__(self, create_time=None, modified_time=None, creator=None, version=None, creator_name=None,
                 content=None):
        self.create_time = create_time  # type: int
        self.modified_time = modified_time  # type: int
        self.creator = creator          # type: str
        self.version = version          # type: int
        self.creator_name = creator_name  # type: str
        self.content = content          # type: str

    def validate(self):
        self.validate_required(self.create_time, 'create_time')
        self.validate_required(self.modified_time, 'modified_time')
        self.validate_required(self.creator, 'creator')
        self.validate_required(self.version, 'version')
        self.validate_required(self.creator_name, 'creator_name')
        self.validate_required(self.content, 'content')

    def to_map(self):
        result = {}
        result['CreateTime'] = self.create_time
        result['ModifiedTime'] = self.modified_time
        result['Creator'] = self.creator
        result['Version'] = self.version
        result['CreatorName'] = self.creator_name
        result['Content'] = self.content
        return result

    def from_map(self, map={}):
        self.create_time = map.get('CreateTime')
        self.modified_time = map.get('ModifiedTime')
        self.creator = map.get('Creator')
        self.version = map.get('Version')
        self.creator_name = map.get('CreatorName')
        self.content = map.get('Content')
        return self


class GetBaselineStatusRequest(TeaModel):
    def __init__(self, baseline_id=None, bizdate=None, in_group_id=None):
        self.baseline_id = baseline_id  # type: int
        self.bizdate = bizdate          # type: str
        self.in_group_id = in_group_id  # type: int

    def validate(self):
        self.validate_required(self.baseline_id, 'baseline_id')
        self.validate_required(self.bizdate, 'bizdate')
        self.validate_required(self.in_group_id, 'in_group_id')

    def to_map(self):
        result = {}
        result['BaselineId'] = self.baseline_id
        result['Bizdate'] = self.bizdate
        result['InGroupId'] = self.in_group_id
        return result

    def from_map(self, map={}):
        self.baseline_id = map.get('BaselineId')
        self.bizdate = map.get('Bizdate')
        self.in_group_id = map.get('InGroupId')
        return self


class GetBaselineStatusResponse(TeaModel):
    def __init__(self, success=None, error_code=None, error_message=None, http_status_code=None, request_id=None,
                 data=None):
        self.success = success          # type: bool
        self.error_code = error_code    # type: str
        self.error_message = error_message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.request_id = request_id    # type: str
        self.data = data                # type: GetBaselineStatusResponseData

    def validate(self):
        self.validate_required(self.success, 'success')
        self.validate_required(self.error_code, 'error_code')
        self.validate_required(self.error_message, 'error_message')
        self.validate_required(self.http_status_code, 'http_status_code')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['Success'] = self.success
        result['ErrorCode'] = self.error_code
        result['ErrorMessage'] = self.error_message
        result['HttpStatusCode'] = self.http_status_code
        result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.success = map.get('Success')
        self.error_code = map.get('ErrorCode')
        self.error_message = map.get('ErrorMessage')
        self.http_status_code = map.get('HttpStatusCode')
        self.request_id = map.get('RequestId')
        if map.get('Data') is not None:
            temp_model = GetBaselineStatusResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class GetBaselineStatusResponseDataLastInstance(TeaModel):
    def __init__(self, instance_id=None, status=None, project_id=None, owner=None, node_id=None, finish_time=None,
                 end_cast=None, node_name=None):
        self.instance_id = instance_id  # type: int
        self.status = status            # type: str
        self.project_id = project_id    # type: int
        self.owner = owner              # type: str
        self.node_id = node_id          # type: int
        self.finish_time = finish_time  # type: int
        self.end_cast = end_cast        # type: int
        self.node_name = node_name      # type: str

    def validate(self):
        self.validate_required(self.instance_id, 'instance_id')
        self.validate_required(self.status, 'status')
        self.validate_required(self.project_id, 'project_id')
        self.validate_required(self.owner, 'owner')
        self.validate_required(self.node_id, 'node_id')
        self.validate_required(self.finish_time, 'finish_time')
        self.validate_required(self.end_cast, 'end_cast')
        self.validate_required(self.node_name, 'node_name')

    def to_map(self):
        result = {}
        result['InstanceId'] = self.instance_id
        result['Status'] = self.status
        result['ProjectId'] = self.project_id
        result['Owner'] = self.owner
        result['NodeId'] = self.node_id
        result['FinishTime'] = self.finish_time
        result['EndCast'] = self.end_cast
        result['NodeName'] = self.node_name
        return result

    def from_map(self, map={}):
        self.instance_id = map.get('InstanceId')
        self.status = map.get('Status')
        self.project_id = map.get('ProjectId')
        self.owner = map.get('Owner')
        self.node_id = map.get('NodeId')
        self.finish_time = map.get('FinishTime')
        self.end_cast = map.get('EndCast')
        self.node_name = map.get('NodeName')
        return self


class GetBaselineStatusResponseDataBlockInstance(TeaModel):
    def __init__(self, instance_id=None, status=None, project_id=None, owner=None, node_id=None, finish_time=None,
                 end_cast=None, node_name=None):
        self.instance_id = instance_id  # type: int
        self.status = status            # type: str
        self.project_id = project_id    # type: int
        self.owner = owner              # type: str
        self.node_id = node_id          # type: int
        self.finish_time = finish_time  # type: int
        self.end_cast = end_cast        # type: int
        self.node_name = node_name      # type: str

    def validate(self):
        self.validate_required(self.instance_id, 'instance_id')
        self.validate_required(self.status, 'status')
        self.validate_required(self.project_id, 'project_id')
        self.validate_required(self.owner, 'owner')
        self.validate_required(self.node_id, 'node_id')
        self.validate_required(self.finish_time, 'finish_time')
        self.validate_required(self.end_cast, 'end_cast')
        self.validate_required(self.node_name, 'node_name')

    def to_map(self):
        result = {}
        result['InstanceId'] = self.instance_id
        result['Status'] = self.status
        result['ProjectId'] = self.project_id
        result['Owner'] = self.owner
        result['NodeId'] = self.node_id
        result['FinishTime'] = self.finish_time
        result['EndCast'] = self.end_cast
        result['NodeName'] = self.node_name
        return result

    def from_map(self, map={}):
        self.instance_id = map.get('InstanceId')
        self.status = map.get('Status')
        self.project_id = map.get('ProjectId')
        self.owner = map.get('Owner')
        self.node_id = map.get('NodeId')
        self.finish_time = map.get('FinishTime')
        self.end_cast = map.get('EndCast')
        self.node_name = map.get('NodeName')
        return self


class GetBaselineStatusResponseData(TeaModel):
    def __init__(self, baseline_name=None, baseline_id=None, bizdate=None, owner=None, exp_time=None,
                 finish_time=None, end_cast=None, sla_time=None, priority=None, project_id=None, buffer=None, status=None,
                 finish_status=None, in_group_id=None, last_instance=None, block_instance=None):
        self.baseline_name = baseline_name  # type: str
        self.baseline_id = baseline_id  # type: int
        self.bizdate = bizdate          # type: int
        self.owner = owner              # type: str
        self.exp_time = exp_time        # type: int
        self.finish_time = finish_time  # type: int
        self.end_cast = end_cast        # type: int
        self.sla_time = sla_time        # type: int
        self.priority = priority        # type: int
        self.project_id = project_id    # type: int
        self.buffer = buffer            # type: float
        self.status = status            # type: str
        self.finish_status = finish_status  # type: str
        self.in_group_id = in_group_id  # type: int
        self.last_instance = last_instance  # type: GetBaselineStatusResponseDataLastInstance
        self.block_instance = block_instance  # type: GetBaselineStatusResponseDataBlockInstance

    def validate(self):
        self.validate_required(self.baseline_name, 'baseline_name')
        self.validate_required(self.baseline_id, 'baseline_id')
        self.validate_required(self.bizdate, 'bizdate')
        self.validate_required(self.owner, 'owner')
        self.validate_required(self.exp_time, 'exp_time')
        self.validate_required(self.finish_time, 'finish_time')
        self.validate_required(self.end_cast, 'end_cast')
        self.validate_required(self.sla_time, 'sla_time')
        self.validate_required(self.priority, 'priority')
        self.validate_required(self.project_id, 'project_id')
        self.validate_required(self.buffer, 'buffer')
        self.validate_required(self.status, 'status')
        self.validate_required(self.finish_status, 'finish_status')
        self.validate_required(self.in_group_id, 'in_group_id')
        self.validate_required(self.last_instance, 'last_instance')
        if self.last_instance:
            self.last_instance.validate()
        self.validate_required(self.block_instance, 'block_instance')
        if self.block_instance:
            self.block_instance.validate()

    def to_map(self):
        result = {}
        result['BaselineName'] = self.baseline_name
        result['BaselineId'] = self.baseline_id
        result['Bizdate'] = self.bizdate
        result['Owner'] = self.owner
        result['ExpTime'] = self.exp_time
        result['FinishTime'] = self.finish_time
        result['EndCast'] = self.end_cast
        result['SlaTime'] = self.sla_time
        result['Priority'] = self.priority
        result['ProjectId'] = self.project_id
        result['Buffer'] = self.buffer
        result['Status'] = self.status
        result['FinishStatus'] = self.finish_status
        result['InGroupId'] = self.in_group_id
        if self.last_instance is not None:
            result['LastInstance'] = self.last_instance.to_map()
        else:
            result['LastInstance'] = None
        if self.block_instance is not None:
            result['BlockInstance'] = self.block_instance.to_map()
        else:
            result['BlockInstance'] = None
        return result

    def from_map(self, map={}):
        self.baseline_name = map.get('BaselineName')
        self.baseline_id = map.get('BaselineId')
        self.bizdate = map.get('Bizdate')
        self.owner = map.get('Owner')
        self.exp_time = map.get('ExpTime')
        self.finish_time = map.get('FinishTime')
        self.end_cast = map.get('EndCast')
        self.sla_time = map.get('SlaTime')
        self.priority = map.get('Priority')
        self.project_id = map.get('ProjectId')
        self.buffer = map.get('Buffer')
        self.status = map.get('Status')
        self.finish_status = map.get('FinishStatus')
        self.in_group_id = map.get('InGroupId')
        if map.get('LastInstance') is not None:
            temp_model = GetBaselineStatusResponseDataLastInstance()
            self.last_instance = temp_model.from_map(map['LastInstance'])
        else:
            self.last_instance = None
        if map.get('BlockInstance') is not None:
            temp_model = GetBaselineStatusResponseDataBlockInstance()
            self.block_instance = temp_model.from_map(map['BlockInstance'])
        else:
            self.block_instance = None
        return self


class DeleteDataServiceApiRequest(TeaModel):
    def __init__(self, tenant_id=None, project_id=None, api_id=None):
        self.tenant_id = tenant_id      # type: int
        self.project_id = project_id    # type: int
        self.api_id = api_id            # type: int

    def validate(self):
        self.validate_required(self.tenant_id, 'tenant_id')
        self.validate_required(self.project_id, 'project_id')
        self.validate_required(self.api_id, 'api_id')

    def to_map(self):
        result = {}
        result['TenantId'] = self.tenant_id
        result['ProjectId'] = self.project_id
        result['ApiId'] = self.api_id
        return result

    def from_map(self, map={}):
        self.tenant_id = map.get('TenantId')
        self.project_id = map.get('ProjectId')
        self.api_id = map.get('ApiId')
        return self


class DeleteDataServiceApiResponse(TeaModel):
    def __init__(self, data=None, error_code=None, error_message=None, http_status_code=None, request_id=None,
                 success=None):
        self.data = data                # type: bool
        self.error_code = error_code    # type: str
        self.error_message = error_message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.request_id = request_id    # type: str
        self.success = success          # type: bool

    def validate(self):
        self.validate_required(self.data, 'data')
        self.validate_required(self.error_code, 'error_code')
        self.validate_required(self.error_message, 'error_message')
        self.validate_required(self.http_status_code, 'http_status_code')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.success, 'success')

    def to_map(self):
        result = {}
        result['Data'] = self.data
        result['ErrorCode'] = self.error_code
        result['ErrorMessage'] = self.error_message
        result['HttpStatusCode'] = self.http_status_code
        result['RequestId'] = self.request_id
        result['Success'] = self.success
        return result

    def from_map(self, map={}):
        self.data = map.get('Data')
        self.error_code = map.get('ErrorCode')
        self.error_message = map.get('ErrorMessage')
        self.http_status_code = map.get('HttpStatusCode')
        self.request_id = map.get('RequestId')
        self.success = map.get('Success')
        return self


class PublishDataServiceApiRequest(TeaModel):
    def __init__(self, tenant_id=None, project_id=None, api_id=None):
        self.tenant_id = tenant_id      # type: int
        self.project_id = project_id    # type: int
        self.api_id = api_id            # type: int

    def validate(self):
        self.validate_required(self.tenant_id, 'tenant_id')
        self.validate_required(self.project_id, 'project_id')
        self.validate_required(self.api_id, 'api_id')

    def to_map(self):
        result = {}
        result['TenantId'] = self.tenant_id
        result['ProjectId'] = self.project_id
        result['ApiId'] = self.api_id
        return result

    def from_map(self, map={}):
        self.tenant_id = map.get('TenantId')
        self.project_id = map.get('ProjectId')
        self.api_id = map.get('ApiId')
        return self


class PublishDataServiceApiResponse(TeaModel):
    def __init__(self, data=None, error_code=None, error_message=None, http_status_code=None, request_id=None,
                 success=None):
        self.data = data                # type: bool
        self.error_code = error_code    # type: str
        self.error_message = error_message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.request_id = request_id    # type: str
        self.success = success          # type: bool

    def validate(self):
        self.validate_required(self.data, 'data')
        self.validate_required(self.error_code, 'error_code')
        self.validate_required(self.error_message, 'error_message')
        self.validate_required(self.http_status_code, 'http_status_code')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.success, 'success')

    def to_map(self):
        result = {}
        result['Data'] = self.data
        result['ErrorCode'] = self.error_code
        result['ErrorMessage'] = self.error_message
        result['HttpStatusCode'] = self.http_status_code
        result['RequestId'] = self.request_id
        result['Success'] = self.success
        return result

    def from_map(self, map={}):
        self.data = map.get('Data')
        self.error_code = map.get('ErrorCode')
        self.error_message = map.get('ErrorMessage')
        self.http_status_code = map.get('HttpStatusCode')
        self.request_id = map.get('RequestId')
        self.success = map.get('Success')
        return self


class GetMetaTableLineageRequest(TeaModel):
    def __init__(self, table_guid=None, direction=None, next_primary_key=None, page_size=None, cluster_id=None,
                 database_name=None, table_name=None, data_source_type=None):
        self.table_guid = table_guid    # type: str
        self.direction = direction      # type: str
        self.next_primary_key = next_primary_key  # type: str
        self.page_size = page_size      # type: int
        self.cluster_id = cluster_id    # type: str
        self.database_name = database_name  # type: str
        self.table_name = table_name    # type: str
        self.data_source_type = data_source_type  # type: str

    def validate(self):
        self.validate_required(self.direction, 'direction')

    def to_map(self):
        result = {}
        result['TableGuid'] = self.table_guid
        result['Direction'] = self.direction
        result['NextPrimaryKey'] = self.next_primary_key
        result['PageSize'] = self.page_size
        result['ClusterId'] = self.cluster_id
        result['DatabaseName'] = self.database_name
        result['TableName'] = self.table_name
        result['DataSourceType'] = self.data_source_type
        return result

    def from_map(self, map={}):
        self.table_guid = map.get('TableGuid')
        self.direction = map.get('Direction')
        self.next_primary_key = map.get('NextPrimaryKey')
        self.page_size = map.get('PageSize')
        self.cluster_id = map.get('ClusterId')
        self.database_name = map.get('DatabaseName')
        self.table_name = map.get('TableName')
        self.data_source_type = map.get('DataSourceType')
        return self


class GetMetaTableLineageResponse(TeaModel):
    def __init__(self, request_id=None, error_code=None, error_message=None, http_status_code=None, success=None,
                 data=None):
        self.request_id = request_id    # type: str
        self.error_code = error_code    # type: str
        self.error_message = error_message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.success = success          # type: bool
        self.data = data                # type: GetMetaTableLineageResponseData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.error_code, 'error_code')
        self.validate_required(self.error_message, 'error_message')
        self.validate_required(self.http_status_code, 'http_status_code')
        self.validate_required(self.success, 'success')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['ErrorCode'] = self.error_code
        result['ErrorMessage'] = self.error_message
        result['HttpStatusCode'] = self.http_status_code
        result['Success'] = self.success
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.error_code = map.get('ErrorCode')
        self.error_message = map.get('ErrorMessage')
        self.http_status_code = map.get('HttpStatusCode')
        self.success = map.get('Success')
        if map.get('Data') is not None:
            temp_model = GetMetaTableLineageResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class GetMetaTableLineageResponseDataDataEntityList(TeaModel):
    def __init__(self, table_name=None, table_guid=None):
        self.table_name = table_name    # type: str
        self.table_guid = table_guid    # type: str

    def validate(self):
        self.validate_required(self.table_name, 'table_name')
        self.validate_required(self.table_guid, 'table_guid')

    def to_map(self):
        result = {}
        result['TableName'] = self.table_name
        result['TableGuid'] = self.table_guid
        return result

    def from_map(self, map={}):
        self.table_name = map.get('TableName')
        self.table_guid = map.get('TableGuid')
        return self


class GetMetaTableLineageResponseData(TeaModel):
    def __init__(self, has_next=None, next_primary_key=None, data_entity_list=None):
        self.has_next = has_next        # type: bool
        self.next_primary_key = next_primary_key  # type: str
        self.data_entity_list = data_entity_list  # type: List[GetMetaTableLineageResponseDataDataEntityList]

    def validate(self):
        self.validate_required(self.has_next, 'has_next')
        self.validate_required(self.next_primary_key, 'next_primary_key')
        self.validate_required(self.data_entity_list, 'data_entity_list')
        if self.data_entity_list:
            for k in self.data_entity_list:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['HasNext'] = self.has_next
        result['NextPrimaryKey'] = self.next_primary_key
        result['DataEntityList'] = []
        if self.data_entity_list is not None:
            for k in self.data_entity_list:
                result['DataEntityList'].append(k.to_map() if k else None)
        else:
            result['DataEntityList'] = None
        return result

    def from_map(self, map={}):
        self.has_next = map.get('HasNext')
        self.next_primary_key = map.get('NextPrimaryKey')
        self.data_entity_list = []
        if map.get('DataEntityList') is not None:
            for k in map.get('DataEntityList'):
                temp_model = GetMetaTableLineageResponseDataDataEntityList()
                self.data_entity_list.append(temp_model.from_map(k))
        else:
            self.data_entity_list = None
        return self


class ListBaselineStatusesRequest(TeaModel):
    def __init__(self, page_number=None, page_size=None, bizdate=None, priority=None, search_text=None, owner=None,
                 topic_id=None, finish_status=None, status=None, baseline_types=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size      # type: int
        self.bizdate = bizdate          # type: str
        self.priority = priority        # type: str
        self.search_text = search_text  # type: str
        self.owner = owner              # type: str
        self.topic_id = topic_id        # type: int
        self.finish_status = finish_status  # type: str
        self.status = status            # type: str
        self.baseline_types = baseline_types  # type: str

    def validate(self):
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.bizdate, 'bizdate')

    def to_map(self):
        result = {}
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        result['Bizdate'] = self.bizdate
        result['Priority'] = self.priority
        result['SearchText'] = self.search_text
        result['Owner'] = self.owner
        result['TopicId'] = self.topic_id
        result['FinishStatus'] = self.finish_status
        result['Status'] = self.status
        result['BaselineTypes'] = self.baseline_types
        return result

    def from_map(self, map={}):
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        self.bizdate = map.get('Bizdate')
        self.priority = map.get('Priority')
        self.search_text = map.get('SearchText')
        self.owner = map.get('Owner')
        self.topic_id = map.get('TopicId')
        self.finish_status = map.get('FinishStatus')
        self.status = map.get('Status')
        self.baseline_types = map.get('BaselineTypes')
        return self


class ListBaselineStatusesResponse(TeaModel):
    def __init__(self, success=None, error_code=None, error_message=None, http_status_code=None, request_id=None,
                 data=None):
        self.success = success          # type: bool
        self.error_code = error_code    # type: str
        self.error_message = error_message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.request_id = request_id    # type: str
        self.data = data                # type: ListBaselineStatusesResponseData

    def validate(self):
        self.validate_required(self.success, 'success')
        self.validate_required(self.error_code, 'error_code')
        self.validate_required(self.error_message, 'error_message')
        self.validate_required(self.http_status_code, 'http_status_code')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['Success'] = self.success
        result['ErrorCode'] = self.error_code
        result['ErrorMessage'] = self.error_message
        result['HttpStatusCode'] = self.http_status_code
        result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.success = map.get('Success')
        self.error_code = map.get('ErrorCode')
        self.error_message = map.get('ErrorMessage')
        self.http_status_code = map.get('HttpStatusCode')
        self.request_id = map.get('RequestId')
        if map.get('Data') is not None:
            temp_model = ListBaselineStatusesResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class ListBaselineStatusesResponseDataBaselineStatuses(TeaModel):
    def __init__(self, baseline_name=None, baseline_id=None, bizdate=None, owner=None, exp_time=None,
                 finish_time=None, end_cast=None, sla_time=None, priority=None, project_id=None, buffer=None, status=None,
                 finish_status=None, in_group_id=None):
        self.baseline_name = baseline_name  # type: str
        self.baseline_id = baseline_id  # type: int
        self.bizdate = bizdate          # type: int
        self.owner = owner              # type: str
        self.exp_time = exp_time        # type: int
        self.finish_time = finish_time  # type: int
        self.end_cast = end_cast        # type: int
        self.sla_time = sla_time        # type: int
        self.priority = priority        # type: int
        self.project_id = project_id    # type: int
        self.buffer = buffer            # type: int
        self.status = status            # type: str
        self.finish_status = finish_status  # type: str
        self.in_group_id = in_group_id  # type: int

    def validate(self):
        self.validate_required(self.baseline_name, 'baseline_name')
        self.validate_required(self.baseline_id, 'baseline_id')
        self.validate_required(self.bizdate, 'bizdate')
        self.validate_required(self.owner, 'owner')
        self.validate_required(self.exp_time, 'exp_time')
        self.validate_required(self.finish_time, 'finish_time')
        self.validate_required(self.end_cast, 'end_cast')
        self.validate_required(self.sla_time, 'sla_time')
        self.validate_required(self.priority, 'priority')
        self.validate_required(self.project_id, 'project_id')
        self.validate_required(self.buffer, 'buffer')
        self.validate_required(self.status, 'status')
        self.validate_required(self.finish_status, 'finish_status')
        self.validate_required(self.in_group_id, 'in_group_id')

    def to_map(self):
        result = {}
        result['BaselineName'] = self.baseline_name
        result['BaselineId'] = self.baseline_id
        result['Bizdate'] = self.bizdate
        result['Owner'] = self.owner
        result['ExpTime'] = self.exp_time
        result['FinishTime'] = self.finish_time
        result['EndCast'] = self.end_cast
        result['SlaTime'] = self.sla_time
        result['Priority'] = self.priority
        result['ProjectId'] = self.project_id
        result['Buffer'] = self.buffer
        result['Status'] = self.status
        result['FinishStatus'] = self.finish_status
        result['InGroupId'] = self.in_group_id
        return result

    def from_map(self, map={}):
        self.baseline_name = map.get('BaselineName')
        self.baseline_id = map.get('BaselineId')
        self.bizdate = map.get('Bizdate')
        self.owner = map.get('Owner')
        self.exp_time = map.get('ExpTime')
        self.finish_time = map.get('FinishTime')
        self.end_cast = map.get('EndCast')
        self.sla_time = map.get('SlaTime')
        self.priority = map.get('Priority')
        self.project_id = map.get('ProjectId')
        self.buffer = map.get('Buffer')
        self.status = map.get('Status')
        self.finish_status = map.get('FinishStatus')
        self.in_group_id = map.get('InGroupId')
        return self


class ListBaselineStatusesResponseData(TeaModel):
    def __init__(self, page_number=None, page_size=None, total_count=None, baseline_statuses=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size      # type: int
        self.total_count = total_count  # type: int
        self.baseline_statuses = baseline_statuses  # type: List[ListBaselineStatusesResponseDataBaselineStatuses]

    def validate(self):
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.baseline_statuses, 'baseline_statuses')
        if self.baseline_statuses:
            for k in self.baseline_statuses:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        result['TotalCount'] = self.total_count
        result['BaselineStatuses'] = []
        if self.baseline_statuses is not None:
            for k in self.baseline_statuses:
                result['BaselineStatuses'].append(k.to_map() if k else None)
        else:
            result['BaselineStatuses'] = None
        return result

    def from_map(self, map={}):
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        self.total_count = map.get('TotalCount')
        self.baseline_statuses = []
        if map.get('BaselineStatuses') is not None:
            for k in map.get('BaselineStatuses'):
                temp_model = ListBaselineStatusesResponseDataBaselineStatuses()
                self.baseline_statuses.append(temp_model.from_map(k))
        else:
            self.baseline_statuses = None
        return self


class ListRemindsRequest(TeaModel):
    def __init__(self, page_number=None, page_size=None, founder=None, node_id=None, remind_types=None,
                 alert_target=None, search_text=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size      # type: int
        self.founder = founder          # type: str
        self.node_id = node_id          # type: int
        self.remind_types = remind_types  # type: str
        self.alert_target = alert_target  # type: str
        self.search_text = search_text  # type: str

    def validate(self):
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_size, 'page_size')

    def to_map(self):
        result = {}
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        result['Founder'] = self.founder
        result['NodeId'] = self.node_id
        result['RemindTypes'] = self.remind_types
        result['AlertTarget'] = self.alert_target
        result['SearchText'] = self.search_text
        return result

    def from_map(self, map={}):
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        self.founder = map.get('Founder')
        self.node_id = map.get('NodeId')
        self.remind_types = map.get('RemindTypes')
        self.alert_target = map.get('AlertTarget')
        self.search_text = map.get('SearchText')
        return self


class ListRemindsResponse(TeaModel):
    def __init__(self, success=None, error_code=None, error_message=None, http_status_code=None, request_id=None,
                 data=None):
        self.success = success          # type: bool
        self.error_code = error_code    # type: str
        self.error_message = error_message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.request_id = request_id    # type: str
        self.data = data                # type: ListRemindsResponseData

    def validate(self):
        self.validate_required(self.success, 'success')
        self.validate_required(self.error_code, 'error_code')
        self.validate_required(self.error_message, 'error_message')
        self.validate_required(self.http_status_code, 'http_status_code')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['Success'] = self.success
        result['ErrorCode'] = self.error_code
        result['ErrorMessage'] = self.error_message
        result['HttpStatusCode'] = self.http_status_code
        result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.success = map.get('Success')
        self.error_code = map.get('ErrorCode')
        self.error_message = map.get('ErrorMessage')
        self.http_status_code = map.get('HttpStatusCode')
        self.request_id = map.get('RequestId')
        if map.get('Data') is not None:
            temp_model = ListRemindsResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class ListRemindsResponseDataReminds(TeaModel):
    def __init__(self, remind_id=None, remind_name=None, dnd_start=None, dnd_end=None, remind_unit=None,
                 remind_type=None, alert_unit=None, useflag=None, founder=None, node_ids=None, baseline_ids=None,
                 project_ids=None, biz_process_ids=None, alert_methods=None, alert_targets=None):
        self.remind_id = remind_id      # type: int
        self.remind_name = remind_name  # type: str
        self.dnd_start = dnd_start      # type: str
        self.dnd_end = dnd_end          # type: str
        self.remind_unit = remind_unit  # type: str
        self.remind_type = remind_type  # type: str
        self.alert_unit = alert_unit    # type: str
        self.useflag = useflag          # type: bool
        self.founder = founder          # type: str
        self.node_ids = node_ids        # type: List[int]
        self.baseline_ids = baseline_ids  # type: List[int]
        self.project_ids = project_ids  # type: List[int]
        self.biz_process_ids = biz_process_ids  # type: List[int]
        self.alert_methods = alert_methods  # type: List[str]
        self.alert_targets = alert_targets  # type: List[str]

    def validate(self):
        self.validate_required(self.remind_id, 'remind_id')
        self.validate_required(self.remind_name, 'remind_name')
        self.validate_required(self.dnd_start, 'dnd_start')
        self.validate_required(self.dnd_end, 'dnd_end')
        self.validate_required(self.remind_unit, 'remind_unit')
        self.validate_required(self.remind_type, 'remind_type')
        self.validate_required(self.alert_unit, 'alert_unit')
        self.validate_required(self.useflag, 'useflag')
        self.validate_required(self.founder, 'founder')
        self.validate_required(self.node_ids, 'node_ids')
        self.validate_required(self.baseline_ids, 'baseline_ids')
        self.validate_required(self.project_ids, 'project_ids')
        self.validate_required(self.biz_process_ids, 'biz_process_ids')
        self.validate_required(self.alert_methods, 'alert_methods')
        self.validate_required(self.alert_targets, 'alert_targets')

    def to_map(self):
        result = {}
        result['RemindId'] = self.remind_id
        result['RemindName'] = self.remind_name
        result['DndStart'] = self.dnd_start
        result['DndEnd'] = self.dnd_end
        result['RemindUnit'] = self.remind_unit
        result['RemindType'] = self.remind_type
        result['AlertUnit'] = self.alert_unit
        result['Useflag'] = self.useflag
        result['Founder'] = self.founder
        result['NodeIds'] = self.node_ids
        result['BaselineIds'] = self.baseline_ids
        result['ProjectIds'] = self.project_ids
        result['BizProcessIds'] = self.biz_process_ids
        result['AlertMethods'] = self.alert_methods
        result['AlertTargets'] = self.alert_targets
        return result

    def from_map(self, map={}):
        self.remind_id = map.get('RemindId')
        self.remind_name = map.get('RemindName')
        self.dnd_start = map.get('DndStart')
        self.dnd_end = map.get('DndEnd')
        self.remind_unit = map.get('RemindUnit')
        self.remind_type = map.get('RemindType')
        self.alert_unit = map.get('AlertUnit')
        self.useflag = map.get('Useflag')
        self.founder = map.get('Founder')
        self.node_ids = map.get('NodeIds')
        self.baseline_ids = map.get('BaselineIds')
        self.project_ids = map.get('ProjectIds')
        self.biz_process_ids = map.get('BizProcessIds')
        self.alert_methods = map.get('AlertMethods')
        self.alert_targets = map.get('AlertTargets')
        return self


class ListRemindsResponseData(TeaModel):
    def __init__(self, page_number=None, page_size=None, total_count=None, reminds=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size      # type: int
        self.total_count = total_count  # type: int
        self.reminds = reminds          # type: List[ListRemindsResponseDataReminds]

    def validate(self):
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.reminds, 'reminds')
        if self.reminds:
            for k in self.reminds:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        result['TotalCount'] = self.total_count
        result['Reminds'] = []
        if self.reminds is not None:
            for k in self.reminds:
                result['Reminds'].append(k.to_map() if k else None)
        else:
            result['Reminds'] = None
        return result

    def from_map(self, map={}):
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        self.total_count = map.get('TotalCount')
        self.reminds = []
        if map.get('Reminds') is not None:
            for k in map.get('Reminds'):
                temp_model = ListRemindsResponseDataReminds()
                self.reminds.append(temp_model.from_map(k))
        else:
            self.reminds = None
        return self


class DeleteQualityEntityRequest(TeaModel):
    def __init__(self, entity_id=None, project_name=None, env_type=None):
        self.entity_id = entity_id      # type: int
        self.project_name = project_name  # type: str
        self.env_type = env_type        # type: str

    def validate(self):
        self.validate_required(self.entity_id, 'entity_id')
        self.validate_required(self.project_name, 'project_name')
        self.validate_required(self.env_type, 'env_type')

    def to_map(self):
        result = {}
        result['EntityId'] = self.entity_id
        result['ProjectName'] = self.project_name
        result['EnvType'] = self.env_type
        return result

    def from_map(self, map={}):
        self.entity_id = map.get('EntityId')
        self.project_name = map.get('ProjectName')
        self.env_type = map.get('EnvType')
        return self


class DeleteQualityEntityResponse(TeaModel):
    def __init__(self, success=None, error_code=None, error_message=None, http_status_code=None, data=None,
                 request_id=None):
        self.success = success          # type: bool
        self.error_code = error_code    # type: str
        self.error_message = error_message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.data = data                # type: bool
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.success, 'success')
        self.validate_required(self.error_code, 'error_code')
        self.validate_required(self.error_message, 'error_message')
        self.validate_required(self.http_status_code, 'http_status_code')
        self.validate_required(self.data, 'data')
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['Success'] = self.success
        result['ErrorCode'] = self.error_code
        result['ErrorMessage'] = self.error_message
        result['HttpStatusCode'] = self.http_status_code
        result['Data'] = self.data
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.success = map.get('Success')
        self.error_code = map.get('ErrorCode')
        self.error_message = map.get('ErrorMessage')
        self.http_status_code = map.get('HttpStatusCode')
        self.data = map.get('Data')
        self.request_id = map.get('RequestId')
        return self


class CreateQualityFollowerRequest(TeaModel):
    def __init__(self, project_name=None, follower=None, alarm_mode=None, entity_id=None):
        self.project_name = project_name  # type: str
        self.follower = follower        # type: str
        self.alarm_mode = alarm_mode    # type: int
        self.entity_id = entity_id      # type: int

    def validate(self):
        self.validate_required(self.project_name, 'project_name')
        self.validate_required(self.follower, 'follower')
        self.validate_required(self.alarm_mode, 'alarm_mode')
        self.validate_required(self.entity_id, 'entity_id')

    def to_map(self):
        result = {}
        result['ProjectName'] = self.project_name
        result['Follower'] = self.follower
        result['AlarmMode'] = self.alarm_mode
        result['EntityId'] = self.entity_id
        return result

    def from_map(self, map={}):
        self.project_name = map.get('ProjectName')
        self.follower = map.get('Follower')
        self.alarm_mode = map.get('AlarmMode')
        self.entity_id = map.get('EntityId')
        return self


class CreateQualityFollowerResponse(TeaModel):
    def __init__(self, error_code=None, data=None, success=None, error_message=None, http_status_code=None,
                 request_id=None):
        self.error_code = error_code    # type: str
        self.data = data                # type: int
        self.success = success          # type: bool
        self.error_message = error_message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.error_code, 'error_code')
        self.validate_required(self.data, 'data')
        self.validate_required(self.success, 'success')
        self.validate_required(self.error_message, 'error_message')
        self.validate_required(self.http_status_code, 'http_status_code')
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['ErrorCode'] = self.error_code
        result['Data'] = self.data
        result['Success'] = self.success
        result['ErrorMessage'] = self.error_message
        result['HttpStatusCode'] = self.http_status_code
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.error_code = map.get('ErrorCode')
        self.data = map.get('Data')
        self.success = map.get('Success')
        self.error_message = map.get('ErrorMessage')
        self.http_status_code = map.get('HttpStatusCode')
        self.request_id = map.get('RequestId')
        return self


class CreateDataServiceApiRequest(TeaModel):
    def __init__(self, tenant_id=None, project_id=None, api_name=None, group_id=None, api_mode=None,
                 request_method=None, response_content_type=None, timeout=None, visible_range=None, protocols=None,
                 wizard_details=None, script_details=None, registration_details=None, api_path=None, api_description=None,
                 folder_id=None):
        self.tenant_id = tenant_id      # type: int
        self.project_id = project_id    # type: int
        self.api_name = api_name        # type: str
        self.group_id = group_id        # type: str
        self.api_mode = api_mode        # type: int
        self.request_method = request_method  # type: int
        self.response_content_type = response_content_type  # type: int
        self.timeout = timeout          # type: int
        self.visible_range = visible_range  # type: int
        self.protocols = protocols      # type: str
        self.wizard_details = wizard_details  # type: str
        self.script_details = script_details  # type: str
        self.registration_details = registration_details  # type: str
        self.api_path = api_path        # type: str
        self.api_description = api_description  # type: str
        self.folder_id = folder_id      # type: int

    def validate(self):
        self.validate_required(self.tenant_id, 'tenant_id')
        self.validate_required(self.project_id, 'project_id')
        self.validate_required(self.api_name, 'api_name')
        self.validate_required(self.group_id, 'group_id')
        self.validate_required(self.api_mode, 'api_mode')
        self.validate_required(self.request_method, 'request_method')
        self.validate_required(self.response_content_type, 'response_content_type')
        self.validate_required(self.timeout, 'timeout')
        self.validate_required(self.visible_range, 'visible_range')
        self.validate_required(self.protocols, 'protocols')
        self.validate_required(self.api_path, 'api_path')
        self.validate_required(self.api_description, 'api_description')

    def to_map(self):
        result = {}
        result['TenantId'] = self.tenant_id
        result['ProjectId'] = self.project_id
        result['ApiName'] = self.api_name
        result['GroupId'] = self.group_id
        result['ApiMode'] = self.api_mode
        result['RequestMethod'] = self.request_method
        result['ResponseContentType'] = self.response_content_type
        result['Timeout'] = self.timeout
        result['VisibleRange'] = self.visible_range
        result['Protocols'] = self.protocols
        result['WizardDetails'] = self.wizard_details
        result['ScriptDetails'] = self.script_details
        result['RegistrationDetails'] = self.registration_details
        result['ApiPath'] = self.api_path
        result['ApiDescription'] = self.api_description
        result['FolderId'] = self.folder_id
        return result

    def from_map(self, map={}):
        self.tenant_id = map.get('TenantId')
        self.project_id = map.get('ProjectId')
        self.api_name = map.get('ApiName')
        self.group_id = map.get('GroupId')
        self.api_mode = map.get('ApiMode')
        self.request_method = map.get('RequestMethod')
        self.response_content_type = map.get('ResponseContentType')
        self.timeout = map.get('Timeout')
        self.visible_range = map.get('VisibleRange')
        self.protocols = map.get('Protocols')
        self.wizard_details = map.get('WizardDetails')
        self.script_details = map.get('ScriptDetails')
        self.registration_details = map.get('RegistrationDetails')
        self.api_path = map.get('ApiPath')
        self.api_description = map.get('ApiDescription')
        self.folder_id = map.get('FolderId')
        return self


class CreateDataServiceApiResponse(TeaModel):
    def __init__(self, data=None, error_code=None, error_message=None, http_status_code=None, success=None,
                 request_id=None):
        self.data = data                # type: int
        self.error_code = error_code    # type: str
        self.error_message = error_message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.success = success          # type: bool
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.data, 'data')
        self.validate_required(self.error_code, 'error_code')
        self.validate_required(self.error_message, 'error_message')
        self.validate_required(self.http_status_code, 'http_status_code')
        self.validate_required(self.success, 'success')
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['Data'] = self.data
        result['ErrorCode'] = self.error_code
        result['ErrorMessage'] = self.error_message
        result['HttpStatusCode'] = self.http_status_code
        result['Success'] = self.success
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.data = map.get('Data')
        self.error_code = map.get('ErrorCode')
        self.error_message = map.get('ErrorMessage')
        self.http_status_code = map.get('HttpStatusCode')
        self.success = map.get('Success')
        self.request_id = map.get('RequestId')
        return self


class AbolishDataServiceApiRequest(TeaModel):
    def __init__(self, tenant_id=None, project_id=None, api_id=None):
        self.tenant_id = tenant_id      # type: int
        self.project_id = project_id    # type: int
        self.api_id = api_id            # type: int

    def validate(self):
        self.validate_required(self.tenant_id, 'tenant_id')
        self.validate_required(self.project_id, 'project_id')
        self.validate_required(self.api_id, 'api_id')

    def to_map(self):
        result = {}
        result['TenantId'] = self.tenant_id
        result['ProjectId'] = self.project_id
        result['ApiId'] = self.api_id
        return result

    def from_map(self, map={}):
        self.tenant_id = map.get('TenantId')
        self.project_id = map.get('ProjectId')
        self.api_id = map.get('ApiId')
        return self


class AbolishDataServiceApiResponse(TeaModel):
    def __init__(self, data=None, error_code=None, error_message=None, http_status_code=None, request_id=None,
                 success=None):
        self.data = data                # type: bool
        self.error_code = error_code    # type: str
        self.error_message = error_message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.request_id = request_id    # type: str
        self.success = success          # type: bool

    def validate(self):
        self.validate_required(self.data, 'data')
        self.validate_required(self.error_code, 'error_code')
        self.validate_required(self.error_message, 'error_message')
        self.validate_required(self.http_status_code, 'http_status_code')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.success, 'success')

    def to_map(self):
        result = {}
        result['Data'] = self.data
        result['ErrorCode'] = self.error_code
        result['ErrorMessage'] = self.error_message
        result['HttpStatusCode'] = self.http_status_code
        result['RequestId'] = self.request_id
        result['Success'] = self.success
        return result

    def from_map(self, map={}):
        self.data = map.get('Data')
        self.error_code = map.get('ErrorCode')
        self.error_message = map.get('ErrorMessage')
        self.http_status_code = map.get('HttpStatusCode')
        self.request_id = map.get('RequestId')
        self.success = map.get('Success')
        return self


class GetQualityEntityRequest(TeaModel):
    def __init__(self, project_name=None, table_name=None, env_type=None, match_expression=None):
        self.project_name = project_name  # type: str
        self.table_name = table_name    # type: str
        self.env_type = env_type        # type: str
        self.match_expression = match_expression  # type: str

    def validate(self):
        self.validate_required(self.project_name, 'project_name')
        self.validate_required(self.table_name, 'table_name')
        self.validate_required(self.env_type, 'env_type')

    def to_map(self):
        result = {}
        result['ProjectName'] = self.project_name
        result['TableName'] = self.table_name
        result['EnvType'] = self.env_type
        result['MatchExpression'] = self.match_expression
        return result

    def from_map(self, map={}):
        self.project_name = map.get('ProjectName')
        self.table_name = map.get('TableName')
        self.env_type = map.get('EnvType')
        self.match_expression = map.get('MatchExpression')
        return self


class GetQualityEntityResponse(TeaModel):
    def __init__(self, success=None, error_code=None, error_message=None, http_status_code=None, request_id=None,
                 data=None):
        self.success = success          # type: bool
        self.error_code = error_code    # type: str
        self.error_message = error_message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.request_id = request_id    # type: str
        self.data = data                # type: List[GetQualityEntityResponseData]

    def validate(self):
        self.validate_required(self.success, 'success')
        self.validate_required(self.error_code, 'error_code')
        self.validate_required(self.error_message, 'error_message')
        self.validate_required(self.http_status_code, 'http_status_code')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['Success'] = self.success
        result['ErrorCode'] = self.error_code
        result['ErrorMessage'] = self.error_message
        result['HttpStatusCode'] = self.http_status_code
        result['RequestId'] = self.request_id
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.success = map.get('Success')
        self.error_code = map.get('ErrorCode')
        self.error_message = map.get('ErrorMessage')
        self.http_status_code = map.get('HttpStatusCode')
        self.request_id = map.get('RequestId')
        self.data = []
        if map.get('Data') is not None:
            for k in map.get('Data'):
                temp_model = GetQualityEntityResponseData()
                self.data.append(temp_model.from_map(k))
        else:
            self.data = None
        return self


class GetQualityEntityResponseData(TeaModel):
    def __init__(self, id=None, project_name=None, table_name=None, env_type=None, match_expression=None,
                 entity_level=None, on_duty=None, modify_user=None, create_time=None, modify_time=None, sql=None, task=None,
                 followers=None, has_relative_node=None, relative_node=None):
        self.id = id                    # type: int
        self.project_name = project_name  # type: str
        self.table_name = table_name    # type: str
        self.env_type = env_type        # type: str
        self.match_expression = match_expression  # type: str
        self.entity_level = entity_level  # type: int
        self.on_duty = on_duty          # type: str
        self.modify_user = modify_user  # type: str
        self.create_time = create_time  # type: int
        self.modify_time = modify_time  # type: int
        self.sql = sql                  # type: int
        self.task = task                # type: int
        self.followers = followers      # type: str
        self.has_relative_node = has_relative_node  # type: bool
        self.relative_node = relative_node  # type: str

    def validate(self):
        self.validate_required(self.id, 'id')
        self.validate_required(self.project_name, 'project_name')
        self.validate_required(self.table_name, 'table_name')
        self.validate_required(self.env_type, 'env_type')
        self.validate_required(self.match_expression, 'match_expression')
        self.validate_required(self.entity_level, 'entity_level')
        self.validate_required(self.on_duty, 'on_duty')
        self.validate_required(self.modify_user, 'modify_user')
        self.validate_required(self.create_time, 'create_time')
        self.validate_required(self.modify_time, 'modify_time')
        self.validate_required(self.sql, 'sql')
        self.validate_required(self.task, 'task')
        self.validate_required(self.followers, 'followers')
        self.validate_required(self.has_relative_node, 'has_relative_node')
        self.validate_required(self.relative_node, 'relative_node')

    def to_map(self):
        result = {}
        result['Id'] = self.id
        result['ProjectName'] = self.project_name
        result['TableName'] = self.table_name
        result['EnvType'] = self.env_type
        result['MatchExpression'] = self.match_expression
        result['EntityLevel'] = self.entity_level
        result['OnDuty'] = self.on_duty
        result['ModifyUser'] = self.modify_user
        result['CreateTime'] = self.create_time
        result['ModifyTime'] = self.modify_time
        result['Sql'] = self.sql
        result['Task'] = self.task
        result['Followers'] = self.followers
        result['HasRelativeNode'] = self.has_relative_node
        result['RelativeNode'] = self.relative_node
        return result

    def from_map(self, map={}):
        self.id = map.get('Id')
        self.project_name = map.get('ProjectName')
        self.table_name = map.get('TableName')
        self.env_type = map.get('EnvType')
        self.match_expression = map.get('MatchExpression')
        self.entity_level = map.get('EntityLevel')
        self.on_duty = map.get('OnDuty')
        self.modify_user = map.get('ModifyUser')
        self.create_time = map.get('CreateTime')
        self.modify_time = map.get('ModifyTime')
        self.sql = map.get('Sql')
        self.task = map.get('Task')
        self.followers = map.get('Followers')
        self.has_relative_node = map.get('HasRelativeNode')
        self.relative_node = map.get('RelativeNode')
        return self


class GetQualityFollowerRequest(TeaModel):
    def __init__(self, project_name=None, entity_id=None):
        self.project_name = project_name  # type: str
        self.entity_id = entity_id      # type: int

    def validate(self):
        self.validate_required(self.project_name, 'project_name')
        self.validate_required(self.entity_id, 'entity_id')

    def to_map(self):
        result = {}
        result['ProjectName'] = self.project_name
        result['EntityId'] = self.entity_id
        return result

    def from_map(self, map={}):
        self.project_name = map.get('ProjectName')
        self.entity_id = map.get('EntityId')
        return self


class GetQualityFollowerResponse(TeaModel):
    def __init__(self, error_code=None, success=None, error_message=None, http_status_code=None, request_id=None,
                 data=None):
        self.error_code = error_code    # type: str
        self.success = success          # type: bool
        self.error_message = error_message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.request_id = request_id    # type: str
        self.data = data                # type: List[GetQualityFollowerResponseData]

    def validate(self):
        self.validate_required(self.error_code, 'error_code')
        self.validate_required(self.success, 'success')
        self.validate_required(self.error_message, 'error_message')
        self.validate_required(self.http_status_code, 'http_status_code')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['ErrorCode'] = self.error_code
        result['Success'] = self.success
        result['ErrorMessage'] = self.error_message
        result['HttpStatusCode'] = self.http_status_code
        result['RequestId'] = self.request_id
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.error_code = map.get('ErrorCode')
        self.success = map.get('Success')
        self.error_message = map.get('ErrorMessage')
        self.http_status_code = map.get('HttpStatusCode')
        self.request_id = map.get('RequestId')
        self.data = []
        if map.get('Data') is not None:
            for k in map.get('Data'):
                temp_model = GetQualityFollowerResponseData()
                self.data.append(temp_model.from_map(k))
        else:
            self.data = None
        return self


class GetQualityFollowerResponseData(TeaModel):
    def __init__(self, project_name=None, table_name=None, id=None, entity_id=None, follower=None, alarm_mode=None):
        self.project_name = project_name  # type: str
        self.table_name = table_name    # type: str
        self.id = id                    # type: int
        self.entity_id = entity_id      # type: str
        self.follower = follower        # type: str
        self.alarm_mode = alarm_mode    # type: int

    def validate(self):
        self.validate_required(self.project_name, 'project_name')
        self.validate_required(self.table_name, 'table_name')
        self.validate_required(self.id, 'id')
        self.validate_required(self.entity_id, 'entity_id')
        self.validate_required(self.follower, 'follower')
        self.validate_required(self.alarm_mode, 'alarm_mode')

    def to_map(self):
        result = {}
        result['ProjectName'] = self.project_name
        result['TableName'] = self.table_name
        result['Id'] = self.id
        result['EntityId'] = self.entity_id
        result['Follower'] = self.follower
        result['AlarmMode'] = self.alarm_mode
        return result

    def from_map(self, map={}):
        self.project_name = map.get('ProjectName')
        self.table_name = map.get('TableName')
        self.id = map.get('Id')
        self.entity_id = map.get('EntityId')
        self.follower = map.get('Follower')
        self.alarm_mode = map.get('AlarmMode')
        return self


class DeleteQualityFollowerRequest(TeaModel):
    def __init__(self, project_name=None, follower_id=None):
        self.project_name = project_name  # type: str
        self.follower_id = follower_id  # type: int

    def validate(self):
        self.validate_required(self.project_name, 'project_name')
        self.validate_required(self.follower_id, 'follower_id')

    def to_map(self):
        result = {}
        result['ProjectName'] = self.project_name
        result['FollowerId'] = self.follower_id
        return result

    def from_map(self, map={}):
        self.project_name = map.get('ProjectName')
        self.follower_id = map.get('FollowerId')
        return self


class DeleteQualityFollowerResponse(TeaModel):
    def __init__(self, error_code=None, data=None, success=None, error_message=None, http_status_code=None,
                 request_id=None):
        self.error_code = error_code    # type: str
        self.data = data                # type: bool
        self.success = success          # type: bool
        self.error_message = error_message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.error_code, 'error_code')
        self.validate_required(self.data, 'data')
        self.validate_required(self.success, 'success')
        self.validate_required(self.error_message, 'error_message')
        self.validate_required(self.http_status_code, 'http_status_code')
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['ErrorCode'] = self.error_code
        result['Data'] = self.data
        result['Success'] = self.success
        result['ErrorMessage'] = self.error_message
        result['HttpStatusCode'] = self.http_status_code
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.error_code = map.get('ErrorCode')
        self.data = map.get('Data')
        self.success = map.get('Success')
        self.error_message = map.get('ErrorMessage')
        self.http_status_code = map.get('HttpStatusCode')
        self.request_id = map.get('RequestId')
        return self


class CreateQualityEntityRequest(TeaModel):
    def __init__(self, project_name=None, table_name=None, env_type=None, match_expression=None, entity_level=None):
        self.project_name = project_name  # type: str
        self.table_name = table_name    # type: str
        self.env_type = env_type        # type: str
        self.match_expression = match_expression  # type: str
        self.entity_level = entity_level  # type: int

    def validate(self):
        self.validate_required(self.project_name, 'project_name')
        self.validate_required(self.table_name, 'table_name')
        self.validate_required(self.env_type, 'env_type')
        self.validate_required(self.match_expression, 'match_expression')
        self.validate_required(self.entity_level, 'entity_level')

    def to_map(self):
        result = {}
        result['ProjectName'] = self.project_name
        result['TableName'] = self.table_name
        result['EnvType'] = self.env_type
        result['MatchExpression'] = self.match_expression
        result['EntityLevel'] = self.entity_level
        return result

    def from_map(self, map={}):
        self.project_name = map.get('ProjectName')
        self.table_name = map.get('TableName')
        self.env_type = map.get('EnvType')
        self.match_expression = map.get('MatchExpression')
        self.entity_level = map.get('EntityLevel')
        return self


class CreateQualityEntityResponse(TeaModel):
    def __init__(self, success=None, data=None, error_code=None, error_message=None, http_status_code=None,
                 request_id=None):
        self.success = success          # type: bool
        self.data = data                # type: int
        self.error_code = error_code    # type: str
        self.error_message = error_message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.success, 'success')
        self.validate_required(self.data, 'data')
        self.validate_required(self.error_code, 'error_code')
        self.validate_required(self.error_message, 'error_message')
        self.validate_required(self.http_status_code, 'http_status_code')
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['Success'] = self.success
        result['Data'] = self.data
        result['ErrorCode'] = self.error_code
        result['ErrorMessage'] = self.error_message
        result['HttpStatusCode'] = self.http_status_code
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.success = map.get('Success')
        self.data = map.get('Data')
        self.error_code = map.get('ErrorCode')
        self.error_message = map.get('ErrorMessage')
        self.http_status_code = map.get('HttpStatusCode')
        self.request_id = map.get('RequestId')
        return self


class CreateQualityRuleRequest(TeaModel):
    def __init__(self, block_type=None, entity_id=None, comment=None, checker=None, expect_value=None, trend=None,
                 method_name=None, operator=None, project_name=None, property=None, property_type=None, rule_type=None,
                 where_condition=None, critical_threshold=None, warning_threshold=None, template_id=None, rule_name=None,
                 predict_type=None):
        self.block_type = block_type    # type: int
        self.entity_id = entity_id      # type: int
        self.comment = comment          # type: str
        self.checker = checker          # type: int
        self.expect_value = expect_value  # type: str
        self.trend = trend              # type: str
        self.method_name = method_name  # type: str
        self.operator = operator        # type: str
        self.project_name = project_name  # type: str
        self.property = property        # type: str
        self.property_type = property_type  # type: str
        self.rule_type = rule_type      # type: int
        self.where_condition = where_condition  # type: str
        self.critical_threshold = critical_threshold  # type: str
        self.warning_threshold = warning_threshold  # type: str
        self.template_id = template_id  # type: int
        self.rule_name = rule_name      # type: str
        self.predict_type = predict_type  # type: int

    def validate(self):
        self.validate_required(self.block_type, 'block_type')
        self.validate_required(self.entity_id, 'entity_id')
        self.validate_required(self.project_name, 'project_name')
        self.validate_required(self.rule_type, 'rule_type')
        self.validate_required(self.rule_name, 'rule_name')
        self.validate_required(self.predict_type, 'predict_type')

    def to_map(self):
        result = {}
        result['BlockType'] = self.block_type
        result['EntityId'] = self.entity_id
        result['Comment'] = self.comment
        result['Checker'] = self.checker
        result['ExpectValue'] = self.expect_value
        result['Trend'] = self.trend
        result['MethodName'] = self.method_name
        result['Operator'] = self.operator
        result['ProjectName'] = self.project_name
        result['Property'] = self.property
        result['PropertyType'] = self.property_type
        result['RuleType'] = self.rule_type
        result['WhereCondition'] = self.where_condition
        result['CriticalThreshold'] = self.critical_threshold
        result['WarningThreshold'] = self.warning_threshold
        result['TemplateId'] = self.template_id
        result['RuleName'] = self.rule_name
        result['PredictType'] = self.predict_type
        return result

    def from_map(self, map={}):
        self.block_type = map.get('BlockType')
        self.entity_id = map.get('EntityId')
        self.comment = map.get('Comment')
        self.checker = map.get('Checker')
        self.expect_value = map.get('ExpectValue')
        self.trend = map.get('Trend')
        self.method_name = map.get('MethodName')
        self.operator = map.get('Operator')
        self.project_name = map.get('ProjectName')
        self.property = map.get('Property')
        self.property_type = map.get('PropertyType')
        self.rule_type = map.get('RuleType')
        self.where_condition = map.get('WhereCondition')
        self.critical_threshold = map.get('CriticalThreshold')
        self.warning_threshold = map.get('WarningThreshold')
        self.template_id = map.get('TemplateId')
        self.rule_name = map.get('RuleName')
        self.predict_type = map.get('PredictType')
        return self


class CreateQualityRuleResponse(TeaModel):
    def __init__(self, error_code=None, data=None, success=None, error_message=None, http_status_code=None,
                 request_id=None):
        self.error_code = error_code    # type: str
        self.data = data                # type: str
        self.success = success          # type: bool
        self.error_message = error_message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.error_code, 'error_code')
        self.validate_required(self.data, 'data')
        self.validate_required(self.success, 'success')
        self.validate_required(self.error_message, 'error_message')
        self.validate_required(self.http_status_code, 'http_status_code')
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['ErrorCode'] = self.error_code
        result['Data'] = self.data
        result['Success'] = self.success
        result['ErrorMessage'] = self.error_message
        result['HttpStatusCode'] = self.http_status_code
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.error_code = map.get('ErrorCode')
        self.data = map.get('Data')
        self.success = map.get('Success')
        self.error_message = map.get('ErrorMessage')
        self.http_status_code = map.get('HttpStatusCode')
        self.request_id = map.get('RequestId')
        return self


class UpdateQualityFollowerRequest(TeaModel):
    def __init__(self, project_name=None, follower_id=None, follower=None, alarm_mode=None):
        self.project_name = project_name  # type: str
        self.follower_id = follower_id  # type: int
        self.follower = follower        # type: str
        self.alarm_mode = alarm_mode    # type: int

    def validate(self):
        self.validate_required(self.project_name, 'project_name')
        self.validate_required(self.follower_id, 'follower_id')
        self.validate_required(self.follower, 'follower')
        self.validate_required(self.alarm_mode, 'alarm_mode')

    def to_map(self):
        result = {}
        result['ProjectName'] = self.project_name
        result['FollowerId'] = self.follower_id
        result['Follower'] = self.follower
        result['AlarmMode'] = self.alarm_mode
        return result

    def from_map(self, map={}):
        self.project_name = map.get('ProjectName')
        self.follower_id = map.get('FollowerId')
        self.follower = map.get('Follower')
        self.alarm_mode = map.get('AlarmMode')
        return self


class UpdateQualityFollowerResponse(TeaModel):
    def __init__(self, error_code=None, data=None, success=None, error_message=None, http_status_code=None,
                 request_id=None):
        self.error_code = error_code    # type: str
        self.data = data                # type: bool
        self.success = success          # type: bool
        self.error_message = error_message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.error_code, 'error_code')
        self.validate_required(self.data, 'data')
        self.validate_required(self.success, 'success')
        self.validate_required(self.error_message, 'error_message')
        self.validate_required(self.http_status_code, 'http_status_code')
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['ErrorCode'] = self.error_code
        result['Data'] = self.data
        result['Success'] = self.success
        result['ErrorMessage'] = self.error_message
        result['HttpStatusCode'] = self.http_status_code
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.error_code = map.get('ErrorCode')
        self.data = map.get('Data')
        self.success = map.get('Success')
        self.error_message = map.get('ErrorMessage')
        self.http_status_code = map.get('HttpStatusCode')
        self.request_id = map.get('RequestId')
        return self


class CreateQualityRelativeNodeRequest(TeaModel):
    def __init__(self, env_type=None, match_expression=None, node_id=None, project_id=None,
                 target_node_project_name=None, project_name=None, table_name=None, target_node_project_id=None):
        self.env_type = env_type        # type: str
        self.match_expression = match_expression  # type: str
        self.node_id = node_id          # type: int
        self.project_id = project_id    # type: int
        self.target_node_project_name = target_node_project_name  # type: str
        self.project_name = project_name  # type: str
        self.table_name = table_name    # type: str
        self.target_node_project_id = target_node_project_id  # type: int

    def validate(self):
        self.validate_required(self.env_type, 'env_type')
        self.validate_required(self.match_expression, 'match_expression')
        self.validate_required(self.node_id, 'node_id')
        self.validate_required(self.project_id, 'project_id')
        self.validate_required(self.target_node_project_name, 'target_node_project_name')
        self.validate_required(self.project_name, 'project_name')
        self.validate_required(self.table_name, 'table_name')
        self.validate_required(self.target_node_project_id, 'target_node_project_id')

    def to_map(self):
        result = {}
        result['EnvType'] = self.env_type
        result['MatchExpression'] = self.match_expression
        result['NodeId'] = self.node_id
        result['ProjectId'] = self.project_id
        result['TargetNodeProjectName'] = self.target_node_project_name
        result['ProjectName'] = self.project_name
        result['TableName'] = self.table_name
        result['TargetNodeProjectId'] = self.target_node_project_id
        return result

    def from_map(self, map={}):
        self.env_type = map.get('EnvType')
        self.match_expression = map.get('MatchExpression')
        self.node_id = map.get('NodeId')
        self.project_id = map.get('ProjectId')
        self.target_node_project_name = map.get('TargetNodeProjectName')
        self.project_name = map.get('ProjectName')
        self.table_name = map.get('TableName')
        self.target_node_project_id = map.get('TargetNodeProjectId')
        return self


class CreateQualityRelativeNodeResponse(TeaModel):
    def __init__(self, success=None, error_code=None, error_message=None, http_status_code=None, data=None,
                 request_id=None):
        self.success = success          # type: bool
        self.error_code = error_code    # type: str
        self.error_message = error_message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.data = data                # type: bool
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.success, 'success')
        self.validate_required(self.error_code, 'error_code')
        self.validate_required(self.error_message, 'error_message')
        self.validate_required(self.http_status_code, 'http_status_code')
        self.validate_required(self.data, 'data')
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['Success'] = self.success
        result['ErrorCode'] = self.error_code
        result['ErrorMessage'] = self.error_message
        result['HttpStatusCode'] = self.http_status_code
        result['Data'] = self.data
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.success = map.get('Success')
        self.error_code = map.get('ErrorCode')
        self.error_message = map.get('ErrorMessage')
        self.http_status_code = map.get('HttpStatusCode')
        self.data = map.get('Data')
        self.request_id = map.get('RequestId')
        return self


class DeleteQualityRelativeNodeRequest(TeaModel):
    def __init__(self, env_type=None, match_expression=None, node_id=None, project_id=None,
                 target_node_project_name=None, project_name=None, table_name=None, target_node_project_id=None):
        self.env_type = env_type        # type: str
        self.match_expression = match_expression  # type: str
        self.node_id = node_id          # type: int
        self.project_id = project_id    # type: int
        self.target_node_project_name = target_node_project_name  # type: str
        self.project_name = project_name  # type: str
        self.table_name = table_name    # type: str
        self.target_node_project_id = target_node_project_id  # type: int

    def validate(self):
        self.validate_required(self.env_type, 'env_type')
        self.validate_required(self.match_expression, 'match_expression')
        self.validate_required(self.node_id, 'node_id')
        self.validate_required(self.project_id, 'project_id')
        self.validate_required(self.target_node_project_name, 'target_node_project_name')
        self.validate_required(self.project_name, 'project_name')
        self.validate_required(self.table_name, 'table_name')
        self.validate_required(self.target_node_project_id, 'target_node_project_id')

    def to_map(self):
        result = {}
        result['EnvType'] = self.env_type
        result['MatchExpression'] = self.match_expression
        result['NodeId'] = self.node_id
        result['ProjectId'] = self.project_id
        result['TargetNodeProjectName'] = self.target_node_project_name
        result['ProjectName'] = self.project_name
        result['TableName'] = self.table_name
        result['TargetNodeProjectId'] = self.target_node_project_id
        return result

    def from_map(self, map={}):
        self.env_type = map.get('EnvType')
        self.match_expression = map.get('MatchExpression')
        self.node_id = map.get('NodeId')
        self.project_id = map.get('ProjectId')
        self.target_node_project_name = map.get('TargetNodeProjectName')
        self.project_name = map.get('ProjectName')
        self.table_name = map.get('TableName')
        self.target_node_project_id = map.get('TargetNodeProjectId')
        return self


class DeleteQualityRelativeNodeResponse(TeaModel):
    def __init__(self, success=None, error_code=None, error_message=None, http_status_code=None, data=None,
                 request_id=None):
        self.success = success          # type: bool
        self.error_code = error_code    # type: str
        self.error_message = error_message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.data = data                # type: bool
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.success, 'success')
        self.validate_required(self.error_code, 'error_code')
        self.validate_required(self.error_message, 'error_message')
        self.validate_required(self.http_status_code, 'http_status_code')
        self.validate_required(self.data, 'data')
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['Success'] = self.success
        result['ErrorCode'] = self.error_code
        result['ErrorMessage'] = self.error_message
        result['HttpStatusCode'] = self.http_status_code
        result['Data'] = self.data
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.success = map.get('Success')
        self.error_code = map.get('ErrorCode')
        self.error_message = map.get('ErrorMessage')
        self.http_status_code = map.get('HttpStatusCode')
        self.data = map.get('Data')
        self.request_id = map.get('RequestId')
        return self
