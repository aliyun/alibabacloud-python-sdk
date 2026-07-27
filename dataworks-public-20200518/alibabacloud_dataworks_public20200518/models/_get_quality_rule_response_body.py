# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dataworks_public20200518 import models as main_models
from darabonba.model import DaraModel

class GetQualityRuleResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetQualityRuleResponseBodyData = None,
        error_code: str = None,
        error_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The quality rule details.
        self.data = data
        # The error code.
        self.error_code = error_code
        # The error message.
        self.error_message = error_message
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The request ID.
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
            temp_model = main_models.GetQualityRuleResponseBodyData()
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

class GetQualityRuleResponseBodyData(DaraModel):
    def __init__(
        self,
        block_type: int = None,
        checker: int = None,
        checker_name: str = None,
        comment: str = None,
        critical_threshold: str = None,
        entity_id: int = None,
        expect_value: str = None,
        fix_check: bool = None,
        id: int = None,
        method_id: int = None,
        method_name: str = None,
        on_duty: str = None,
        on_duty_account_name: str = None,
        open_switch: bool = None,
        operator: str = None,
        predict_type: int = None,
        property: str = None,
        rule_name: str = None,
        rule_type: int = None,
        task_setting: str = None,
        template_id: int = None,
        template_name: str = None,
        trend: str = None,
        warning_threshold: str = None,
        where_condition: str = None,
    ):
        # The severity of the quality rule. Valid values:
        # 
        # - `1`: Strong Rule. If a Strong Rule triggers a critical Alert, the associated Scheduling Task is blocked.
        # 
        # - `0`: Weak Rule.
        self.block_type = block_type
        # The checker ID, which is derived from a primary key and used for front-end identification.
        self.checker = checker
        # The name of the checker.
        self.checker_name = checker_name
        # The comment for the rule.
        self.comment = comment
        # The threshold for a critical Alert, which defines the maximum acceptable deviation from the Expected Value. If this threshold is met for a Strong Rule, the associated Scheduling Task is blocked.
        self.critical_threshold = critical_threshold
        # The ID of the partition expression.
        self.entity_id = entity_id
        # The expected value.
        self.expect_value = expect_value
        # Indicates whether to validate against a fixed value.
        self.fix_check = fix_check
        # The ID of the rule.
        self.id = id
        # The ID of the method used to collect sample data.
        self.method_id = method_id
        # The name of the method used to collect sample data. Valid values include `avg`, `count`, `sum`, `min`, `max`, `count_distinct`, `user_defined`, `table_count`, `table_size`, `table_dt_load_count`, `table_dt_refuseload_count`, `null_value`, `null_value/table_count`, `(table_count-count_distinct)/table_count`, and `table_count-count_distinct`.
        self.method_name = method_name
        # The ID of the Alibaba Cloud account that configured the rule.
        self.on_duty = on_duty
        # The name of the Alibaba Cloud account that configured the rule.
        self.on_duty_account_name = on_duty_account_name
        # Indicates whether the rule is enabled.
        self.open_switch = open_switch
        # The comparison operator.
        self.operator = operator
        # Indicates whether the threshold is dynamic. Valid values:
        # 
        # - `0`: The threshold is static.
        # 
        # - `1`: The threshold is dynamic.
        self.predict_type = predict_type
        # The column in the data source table to which the rule applies.
        self.property = property
        # The name of the rule.
        self.rule_name = rule_name
        # The type of the quality rule. Valid values:
        # 
        # - `0`: A rule based on a system template.
        # 
        # - `1`: A rule based on a custom SQL statement.
        # 
        # - `4`: A rule based on a custom template.
        self.rule_type = rule_type
        # The variable settings inserted before a custom rule. The format is x=a,y=b.
        self.task_setting = task_setting
        # The ID of the template used.
        self.template_id = template_id
        # The name of the template used.
        self.template_name = template_name
        # The trend of the validation result.
        self.trend = trend
        # The threshold for a warning Alert. This value specifies the acceptable deviation from the Expected Value and can be customized.
        self.warning_threshold = warning_threshold
        # The filter condition or custom SQL statement used for validation.
        self.where_condition = where_condition

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.block_type is not None:
            result['BlockType'] = self.block_type

        if self.checker is not None:
            result['Checker'] = self.checker

        if self.checker_name is not None:
            result['CheckerName'] = self.checker_name

        if self.comment is not None:
            result['Comment'] = self.comment

        if self.critical_threshold is not None:
            result['CriticalThreshold'] = self.critical_threshold

        if self.entity_id is not None:
            result['EntityId'] = self.entity_id

        if self.expect_value is not None:
            result['ExpectValue'] = self.expect_value

        if self.fix_check is not None:
            result['FixCheck'] = self.fix_check

        if self.id is not None:
            result['Id'] = self.id

        if self.method_id is not None:
            result['MethodId'] = self.method_id

        if self.method_name is not None:
            result['MethodName'] = self.method_name

        if self.on_duty is not None:
            result['OnDuty'] = self.on_duty

        if self.on_duty_account_name is not None:
            result['OnDutyAccountName'] = self.on_duty_account_name

        if self.open_switch is not None:
            result['OpenSwitch'] = self.open_switch

        if self.operator is not None:
            result['Operator'] = self.operator

        if self.predict_type is not None:
            result['PredictType'] = self.predict_type

        if self.property is not None:
            result['Property'] = self.property

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        if self.rule_type is not None:
            result['RuleType'] = self.rule_type

        if self.task_setting is not None:
            result['TaskSetting'] = self.task_setting

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        if self.template_name is not None:
            result['TemplateName'] = self.template_name

        if self.trend is not None:
            result['Trend'] = self.trend

        if self.warning_threshold is not None:
            result['WarningThreshold'] = self.warning_threshold

        if self.where_condition is not None:
            result['WhereCondition'] = self.where_condition

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BlockType') is not None:
            self.block_type = m.get('BlockType')

        if m.get('Checker') is not None:
            self.checker = m.get('Checker')

        if m.get('CheckerName') is not None:
            self.checker_name = m.get('CheckerName')

        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('CriticalThreshold') is not None:
            self.critical_threshold = m.get('CriticalThreshold')

        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')

        if m.get('ExpectValue') is not None:
            self.expect_value = m.get('ExpectValue')

        if m.get('FixCheck') is not None:
            self.fix_check = m.get('FixCheck')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('MethodId') is not None:
            self.method_id = m.get('MethodId')

        if m.get('MethodName') is not None:
            self.method_name = m.get('MethodName')

        if m.get('OnDuty') is not None:
            self.on_duty = m.get('OnDuty')

        if m.get('OnDutyAccountName') is not None:
            self.on_duty_account_name = m.get('OnDutyAccountName')

        if m.get('OpenSwitch') is not None:
            self.open_switch = m.get('OpenSwitch')

        if m.get('Operator') is not None:
            self.operator = m.get('Operator')

        if m.get('PredictType') is not None:
            self.predict_type = m.get('PredictType')

        if m.get('Property') is not None:
            self.property = m.get('Property')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')

        if m.get('TaskSetting') is not None:
            self.task_setting = m.get('TaskSetting')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')

        if m.get('Trend') is not None:
            self.trend = m.get('Trend')

        if m.get('WarningThreshold') is not None:
            self.warning_threshold = m.get('WarningThreshold')

        if m.get('WhereCondition') is not None:
            self.where_condition = m.get('WhereCondition')

        return self

