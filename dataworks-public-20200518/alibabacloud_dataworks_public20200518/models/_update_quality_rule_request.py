# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateQualityRuleRequest(DaraModel):
    def __init__(
        self,
        block_type: int = None,
        checker: int = None,
        comment: str = None,
        critical_threshold: str = None,
        entity_id: int = None,
        expect_value: str = None,
        id: int = None,
        method_name: str = None,
        open_switch: bool = None,
        operator: str = None,
        predict_type: int = None,
        project_id: int = None,
        project_name: str = None,
        property: str = None,
        property_type: str = None,
        rule_name: str = None,
        rule_type: int = None,
        task_setting: str = None,
        template_id: int = None,
        trend: str = None,
        warning_threshold: str = None,
        where_condition: str = None,
    ):
        # The strength of the monitoring rule. The strength of a monitoring rule indicates the importance of the rule. Valid values:
        # 
        # *   1: indicates that the monitoring rule is a strong rule.
        # *   0: indicates that the monitoring rule is a weak rule. You can specify whether a monitoring rule is a strong rule based on your business requirements. If a monitoring rule is a strong rule and the critical threshold is exceeded, a critical alert is reported and nodes that are associated with the rule are blocked from running.
        self.block_type = block_type
        # The checker ID. Valid values: 2: indicates that the current value is compared with the average value of the previous 7 days. 3: indicates that the current value is compared with the average value of the previous 30 days. 4: indicates that the current value is compared with the value 1 day earlier. 5: indicates that the current value is compared with the value 7 days earlier. 6: indicates that the current value is compared with the value 30 days earlier. 7: indicates the variance between the current value and the value 7 days earlier. 8: indicates the variance between the current value and the value 30 days earlier. 9: indicates that the current value is compared with a fixed value. 10: indicates that the current value is compared with the value 1, 7, or 30 days earlier. 11: indicates that the current value is compared with the value of the previous cycle. You can call the [ListQualityRules](https://help.aliyun.com/document_detail/173995.html) operation to query the ID.
        self.checker = checker
        # The description of the monitoring rule.
        self.comment = comment
        # The threshold for a critical alert. The threshold indicates the deviation of the monitoring result from the expected value. You can specify a custom value for the threshold based on your business requirements. If a monitoring rule is a strong rule and the critical threshold is exceeded, a critical alert is reported and tasks that are associated with the rule are blocked from running.
        self.critical_threshold = critical_threshold
        # The ID of the partition filter expression. You can call the [ListQualityRules](https://help.aliyun.com/document_detail/173995.html) operation to obtain the ID of the partition filter expression.
        self.entity_id = entity_id
        # The expected value of the monitoring rule.
        self.expect_value = expect_value
        # The monitoring rule ID. You can call the [ListQualityRules](https://help.aliyun.com/document_detail/173995.html) operation to query the ID of the monitoring rule.
        # 
        # This parameter is required.
        self.id = id
        # The method that is used to collect sample data, such as avg, count, sum, min, max, count_distinct, user_defined, table_count, table_size, table_dt_load_count, table_dt_refuseload_count, null_value, null_value/table_count, (table_count-count_distinct)/table_count, or table_count-count_distinct.
        # 
        # This parameter is required.
        self.method_name = method_name
        # Specifies whether to enable the monitoring rule in the production environment. Valid values:
        # 
        # *   true: The monitoring rule is triggered when the associated auto triggered node that generates the output data starts to run.
        # *   false: The monitoring rule is not triggered when the associated auto triggered node that generates the output data starts to run.
        self.open_switch = open_switch
        # The comparison operator, such as >, >=, =, ≠, <, or <=.
        # 
        # >  If you set the Checker parameter to 9, you must configure the Operator parameter.
        self.operator = operator
        # Specifies whether the threshold is a dynamic threshold. Valid values:
        # 
        # *   0: The threshold is not a dynamic threshold.
        # *   2: The threshold is a dynamic threshold.
        self.predict_type = predict_type
        # The DataWorks workspace ID.
        self.project_id = project_id
        # The name of the compute engine or data source. You can log on to the [DataWorks console](https://workbench.data.aliyun.com/console) and go to the Workspace page to obtain the name of the compute engine or data source.
        # 
        # This parameter is required.
        self.project_name = project_name
        # The name of the field.
        # 
        # This parameter is required.
        self.property = property
        # The data type of the field.
        self.property_type = property_type
        # The name of the monitoring rule.
        self.rule_name = rule_name
        # Rule type:
        # 
        # *   0: System template rule
        # *   1: Custom SQL rule
        # *   4: Custom template rule
        self.rule_type = rule_type
        # The variable settings inserted before the custom rule. Format: x=a,y=b.
        self.task_setting = task_setting
        # The ID of the monitoring template. You can call the [ListQualityRules](https://help.aliyun.com/document_detail/173995.html) operation to obtain the ID of the monitoring template.
        self.template_id = template_id
        # The trend of the monitoring result. Valid values:
        # 
        # *   up: increasing
        # *   down: decreasing
        # *   abs: absolute value
        self.trend = trend
        # The threshold for a warning alert. The threshold specifies the deviation of the monitoring result from the expected value. You can specify a custom value for the threshold based on your business requirements.
        self.warning_threshold = warning_threshold
        # The filter condition or custom SQL statement that is used for monitoring.
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

        if self.comment is not None:
            result['Comment'] = self.comment

        if self.critical_threshold is not None:
            result['CriticalThreshold'] = self.critical_threshold

        if self.entity_id is not None:
            result['EntityId'] = self.entity_id

        if self.expect_value is not None:
            result['ExpectValue'] = self.expect_value

        if self.id is not None:
            result['Id'] = self.id

        if self.method_name is not None:
            result['MethodName'] = self.method_name

        if self.open_switch is not None:
            result['OpenSwitch'] = self.open_switch

        if self.operator is not None:
            result['Operator'] = self.operator

        if self.predict_type is not None:
            result['PredictType'] = self.predict_type

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        if self.property is not None:
            result['Property'] = self.property

        if self.property_type is not None:
            result['PropertyType'] = self.property_type

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        if self.rule_type is not None:
            result['RuleType'] = self.rule_type

        if self.task_setting is not None:
            result['TaskSetting'] = self.task_setting

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

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

        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('CriticalThreshold') is not None:
            self.critical_threshold = m.get('CriticalThreshold')

        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')

        if m.get('ExpectValue') is not None:
            self.expect_value = m.get('ExpectValue')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('MethodName') is not None:
            self.method_name = m.get('MethodName')

        if m.get('OpenSwitch') is not None:
            self.open_switch = m.get('OpenSwitch')

        if m.get('Operator') is not None:
            self.operator = m.get('Operator')

        if m.get('PredictType') is not None:
            self.predict_type = m.get('PredictType')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('Property') is not None:
            self.property = m.get('Property')

        if m.get('PropertyType') is not None:
            self.property_type = m.get('PropertyType')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')

        if m.get('TaskSetting') is not None:
            self.task_setting = m.get('TaskSetting')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        if m.get('Trend') is not None:
            self.trend = m.get('Trend')

        if m.get('WarningThreshold') is not None:
            self.warning_threshold = m.get('WarningThreshold')

        if m.get('WhereCondition') is not None:
            self.where_condition = m.get('WhereCondition')

        return self

