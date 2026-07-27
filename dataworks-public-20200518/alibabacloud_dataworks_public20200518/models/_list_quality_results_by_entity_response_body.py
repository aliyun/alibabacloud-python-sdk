# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20200518 import models as main_models
from darabonba.model import DaraModel

class ListQualityResultsByEntityResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.ListQualityResultsByEntityResponseBodyData = None,
        error_code: str = None,
        error_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The data object that contains the quality check results.
        self.data = data
        # The error code.
        self.error_code = error_code
        # The error message.
        self.error_message = error_message
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.ListQualityResultsByEntityResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListQualityResultsByEntityResponseBodyData(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        rule_checks: List[main_models.ListQualityResultsByEntityResponseBodyDataRuleChecks] = None,
        total_count: int = None,
    ):
        # The page number.
        self.page_number = page_number
        # The number of entries per page. Default value: 10. Maximum value: 100.
        self.page_size = page_size
        # The monitoring rule check results.
        self.rule_checks = rule_checks
        # The total number of entries.
        self.total_count = total_count

    def validate(self):
        if self.rule_checks:
            for v1 in self.rule_checks:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        result['RuleChecks'] = []
        if self.rule_checks is not None:
            for k1 in self.rule_checks:
                result['RuleChecks'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        self.rule_checks = []
        if m.get('RuleChecks') is not None:
            for k1 in m.get('RuleChecks'):
                temp_model = main_models.ListQualityResultsByEntityResponseBodyDataRuleChecks()
                self.rule_checks.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListQualityResultsByEntityResponseBodyDataRuleChecks(DaraModel):
    def __init__(
        self,
        actual_expression: str = None,
        begin_time: int = None,
        biz_date: int = None,
        block_type: int = None,
        check_result: int = None,
        check_result_status: int = None,
        checker_id: int = None,
        checker_name: str = None,
        checker_type: int = None,
        comment: str = None,
        critical_threshold: float = None,
        date_type: str = None,
        discrete_check: bool = None,
        end_time: int = None,
        entity_id: int = None,
        expect_value: float = None,
        external_id: str = None,
        external_type: str = None,
        fixed_check: bool = None,
        id: int = None,
        is_prediction: bool = None,
        lower_value: float = None,
        match_expression: str = None,
        method_name: str = None,
        op: str = None,
        project_name: str = None,
        property: str = None,
        reference_value: List[main_models.ListQualityResultsByEntityResponseBodyDataRuleChecksReferenceValue] = None,
        result_string: str = None,
        rule_id: int = None,
        rule_name: str = None,
        sample_value: List[main_models.ListQualityResultsByEntityResponseBodyDataRuleChecksSampleValue] = None,
        table_name: str = None,
        task_id: str = None,
        template_id: int = None,
        template_name: str = None,
        time_cost: str = None,
        trend: str = None,
        upper_value: float = None,
        warning_threshold: float = None,
        where_condition: str = None,
    ):
        # The expression that specifies the data partition that was checked.
        self.actual_expression = actual_expression
        # The start time of the check. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.begin_time = begin_time
        # The business date. If the monitored data is offline, the business date is typically the day before the check is performed.
        self.biz_date = biz_date
        # The strength of the monitoring rule. Valid values:
        # 
        # - 1: Strong Rule. If a Strong Rule check generates a critical alert, the associated Scheduling Task is blocked.
        # 
        # - 0: Weak Rule.
        self.block_type = block_type
        # The check result. This parameter usually has the same value as `CheckResultStatus`. Valid values:
        # 
        # - 0: Normal
        # 
        # - 1: Warning
        # 
        # - 2: Critical
        self.check_result = check_result
        # The status of the check result. This parameter corresponds to the status displayed in the UI. Valid values:
        # 
        # - 0: Normal
        # 
        # - 1: Warning
        # 
        # - 2: Critical
        self.check_result_status = check_result_status
        # The ID of the checker.
        self.checker_id = checker_id
        # The name of the checker.
        self.checker_name = checker_name
        # The type of the checker. Valid values:
        # 
        # - 0: Fixed Value
        # 
        # - 1: Fluctuation
        # 
        # - 2: Dynamic Threshold
        self.checker_type = checker_type
        # The description of the monitoring rule.
        self.comment = comment
        # The acceptable deviation from the expected value that triggers a critical alert. This threshold is customizable. If a critical alert is triggered for a Strong Rule, the associated Scheduling Task is blocked.
        self.critical_threshold = critical_threshold
        # The scheduling cycle. A common value is YMD, which represents year, month, and day.
        self.date_type = date_type
        # Specifies whether the check is a discrete check. Valid values:
        # 
        # - true: The check is a discrete check.
        # 
        # - false: The check is not a discrete check.
        self.discrete_check = discrete_check
        # The end time of the check. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.end_time = end_time
        # The ID of the partition filter expression.
        self.entity_id = entity_id
        # The expected value.
        self.expect_value = expect_value
        # The Node ID of the Scheduling Task.
        self.external_id = external_id
        # The type of the scheduling system. Currently, only CWF is supported.
        self.external_type = external_type
        # Specifies whether the check is based on a fixed value. Valid values:
        # 
        # - true: The check is based on a fixed value.
        # 
        # - false: The check is not based on a fixed value.
        self.fixed_check = fixed_check
        # The unique ID of the check result.
        self.id = id
        # Specifies whether the result is a predicted value. Valid values:
        # 
        # - true: The result is a predicted value.
        # 
        # - false: The result is not a predicted value.
        self.is_prediction = is_prediction
        # The predicted lower limit. This value is automatically generated after you set a threshold.
        self.lower_value = lower_value
        # The partition filter expression.
        self.match_expression = match_expression
        # The method for collecting sample data. Valid values include `avg`, `count`, `sum`, `min`, `max`, `count_distinct`, `user_defined`, `table_count`, `table_size`, `table_dt_load_count`, `table_dt_refuseload_count`, `null_value`, `null_value/table_count`, `(table_count-count_distinct)/table_count`, and `table_count-count_distinct`.
        self.method_name = method_name
        # The comparison operator.
        self.op = op
        # The name of the monitored compute engine or Data Source.
        self.project_name = project_name
        # The name of the monitored column in the Data Source table.
        self.property = property
        # The historical sample values.
        self.reference_value = reference_value
        # The check result, returned as a string.
        self.result_string = result_string
        # The monitoring rule ID.
        self.rule_id = rule_id
        # The name of the monitoring rule.
        self.rule_name = rule_name
        # The current sample values.
        self.sample_value = sample_value
        # The name of the table that is monitored.
        self.table_name = table_name
        # The ID of the check task.
        self.task_id = task_id
        # The ID of the rule template.
        self.template_id = template_id
        # The name of the rule template.
        self.template_name = template_name
        # The time taken to run the check, in seconds.
        self.time_cost = time_cost
        # The trend of the check result.
        self.trend = trend
        # The predicted upper limit. This value is automatically generated after you set a threshold.
        self.upper_value = upper_value
        # The warning threshold. This value indicates the acceptable deviation from the expected value. You can customize this threshold based on your business requirements.
        self.warning_threshold = warning_threshold
        # The filter condition of the monitoring rule.
        self.where_condition = where_condition

    def validate(self):
        if self.reference_value:
            for v1 in self.reference_value:
                 if v1:
                    v1.validate()
        if self.sample_value:
            for v1 in self.sample_value:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.actual_expression is not None:
            result['ActualExpression'] = self.actual_expression

        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time

        if self.biz_date is not None:
            result['BizDate'] = self.biz_date

        if self.block_type is not None:
            result['BlockType'] = self.block_type

        if self.check_result is not None:
            result['CheckResult'] = self.check_result

        if self.check_result_status is not None:
            result['CheckResultStatus'] = self.check_result_status

        if self.checker_id is not None:
            result['CheckerId'] = self.checker_id

        if self.checker_name is not None:
            result['CheckerName'] = self.checker_name

        if self.checker_type is not None:
            result['CheckerType'] = self.checker_type

        if self.comment is not None:
            result['Comment'] = self.comment

        if self.critical_threshold is not None:
            result['CriticalThreshold'] = self.critical_threshold

        if self.date_type is not None:
            result['DateType'] = self.date_type

        if self.discrete_check is not None:
            result['DiscreteCheck'] = self.discrete_check

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.entity_id is not None:
            result['EntityId'] = self.entity_id

        if self.expect_value is not None:
            result['ExpectValue'] = self.expect_value

        if self.external_id is not None:
            result['ExternalId'] = self.external_id

        if self.external_type is not None:
            result['ExternalType'] = self.external_type

        if self.fixed_check is not None:
            result['FixedCheck'] = self.fixed_check

        if self.id is not None:
            result['Id'] = self.id

        if self.is_prediction is not None:
            result['IsPrediction'] = self.is_prediction

        if self.lower_value is not None:
            result['LowerValue'] = self.lower_value

        if self.match_expression is not None:
            result['MatchExpression'] = self.match_expression

        if self.method_name is not None:
            result['MethodName'] = self.method_name

        if self.op is not None:
            result['Op'] = self.op

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        if self.property is not None:
            result['Property'] = self.property

        result['ReferenceValue'] = []
        if self.reference_value is not None:
            for k1 in self.reference_value:
                result['ReferenceValue'].append(k1.to_map() if k1 else None)

        if self.result_string is not None:
            result['ResultString'] = self.result_string

        if self.rule_id is not None:
            result['RuleId'] = self.rule_id

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        result['SampleValue'] = []
        if self.sample_value is not None:
            for k1 in self.sample_value:
                result['SampleValue'].append(k1.to_map() if k1 else None)

        if self.table_name is not None:
            result['TableName'] = self.table_name

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        if self.template_name is not None:
            result['TemplateName'] = self.template_name

        if self.time_cost is not None:
            result['TimeCost'] = self.time_cost

        if self.trend is not None:
            result['Trend'] = self.trend

        if self.upper_value is not None:
            result['UpperValue'] = self.upper_value

        if self.warning_threshold is not None:
            result['WarningThreshold'] = self.warning_threshold

        if self.where_condition is not None:
            result['WhereCondition'] = self.where_condition

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActualExpression') is not None:
            self.actual_expression = m.get('ActualExpression')

        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')

        if m.get('BizDate') is not None:
            self.biz_date = m.get('BizDate')

        if m.get('BlockType') is not None:
            self.block_type = m.get('BlockType')

        if m.get('CheckResult') is not None:
            self.check_result = m.get('CheckResult')

        if m.get('CheckResultStatus') is not None:
            self.check_result_status = m.get('CheckResultStatus')

        if m.get('CheckerId') is not None:
            self.checker_id = m.get('CheckerId')

        if m.get('CheckerName') is not None:
            self.checker_name = m.get('CheckerName')

        if m.get('CheckerType') is not None:
            self.checker_type = m.get('CheckerType')

        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('CriticalThreshold') is not None:
            self.critical_threshold = m.get('CriticalThreshold')

        if m.get('DateType') is not None:
            self.date_type = m.get('DateType')

        if m.get('DiscreteCheck') is not None:
            self.discrete_check = m.get('DiscreteCheck')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')

        if m.get('ExpectValue') is not None:
            self.expect_value = m.get('ExpectValue')

        if m.get('ExternalId') is not None:
            self.external_id = m.get('ExternalId')

        if m.get('ExternalType') is not None:
            self.external_type = m.get('ExternalType')

        if m.get('FixedCheck') is not None:
            self.fixed_check = m.get('FixedCheck')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('IsPrediction') is not None:
            self.is_prediction = m.get('IsPrediction')

        if m.get('LowerValue') is not None:
            self.lower_value = m.get('LowerValue')

        if m.get('MatchExpression') is not None:
            self.match_expression = m.get('MatchExpression')

        if m.get('MethodName') is not None:
            self.method_name = m.get('MethodName')

        if m.get('Op') is not None:
            self.op = m.get('Op')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('Property') is not None:
            self.property = m.get('Property')

        self.reference_value = []
        if m.get('ReferenceValue') is not None:
            for k1 in m.get('ReferenceValue'):
                temp_model = main_models.ListQualityResultsByEntityResponseBodyDataRuleChecksReferenceValue()
                self.reference_value.append(temp_model.from_map(k1))

        if m.get('ResultString') is not None:
            self.result_string = m.get('ResultString')

        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        self.sample_value = []
        if m.get('SampleValue') is not None:
            for k1 in m.get('SampleValue'):
                temp_model = main_models.ListQualityResultsByEntityResponseBodyDataRuleChecksSampleValue()
                self.sample_value.append(temp_model.from_map(k1))

        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')

        if m.get('TimeCost') is not None:
            self.time_cost = m.get('TimeCost')

        if m.get('Trend') is not None:
            self.trend = m.get('Trend')

        if m.get('UpperValue') is not None:
            self.upper_value = m.get('UpperValue')

        if m.get('WarningThreshold') is not None:
            self.warning_threshold = m.get('WarningThreshold')

        if m.get('WhereCondition') is not None:
            self.where_condition = m.get('WhereCondition')

        return self

class ListQualityResultsByEntityResponseBodyDataRuleChecksSampleValue(DaraModel):
    def __init__(
        self,
        biz_date: str = None,
        discrete_property: str = None,
        value: float = None,
    ):
        # The business date. If the monitored data is offline, the business date is typically the day before the check is performed.
        self.biz_date = biz_date
        # The value of the sample field when a `group by` clause is used. For example, if you group by the gender field, the values for `DiscreteProperty` can be male, female, or null.
        self.discrete_property = discrete_property
        # The current sample value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_date is not None:
            result['BizDate'] = self.biz_date

        if self.discrete_property is not None:
            result['DiscreteProperty'] = self.discrete_property

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizDate') is not None:
            self.biz_date = m.get('BizDate')

        if m.get('DiscreteProperty') is not None:
            self.discrete_property = m.get('DiscreteProperty')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class ListQualityResultsByEntityResponseBodyDataRuleChecksReferenceValue(DaraModel):
    def __init__(
        self,
        biz_date: str = None,
        discrete_property: str = None,
        single_check_result: int = None,
        threshold: float = None,
        value: float = None,
    ):
        # The business date. If the monitored data is offline, the business date is typically the day before the check is performed.
        self.biz_date = biz_date
        # The value of the sample field when a `group by` clause is used. For example, if you group by the gender field, the values for `DiscreteProperty` can be male, female, or null.
        self.discrete_property = discrete_property
        # The result of a single check.
        self.single_check_result = single_check_result
        # The threshold that was applied to this historical data point.
        self.threshold = threshold
        # The historical check value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_date is not None:
            result['BizDate'] = self.biz_date

        if self.discrete_property is not None:
            result['DiscreteProperty'] = self.discrete_property

        if self.single_check_result is not None:
            result['SingleCheckResult'] = self.single_check_result

        if self.threshold is not None:
            result['Threshold'] = self.threshold

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizDate') is not None:
            self.biz_date = m.get('BizDate')

        if m.get('DiscreteProperty') is not None:
            self.discrete_property = m.get('DiscreteProperty')

        if m.get('SingleCheckResult') is not None:
            self.single_check_result = m.get('SingleCheckResult')

        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

