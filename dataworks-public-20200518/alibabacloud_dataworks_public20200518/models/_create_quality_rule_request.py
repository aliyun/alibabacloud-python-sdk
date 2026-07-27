# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateQualityRuleRequest(DaraModel):
    def __init__(
        self,
        block_type: int = None,
        checker: int = None,
        comment: str = None,
        critical_threshold: str = None,
        entity_id: int = None,
        expect_value: str = None,
        method_name: str = None,
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
        # The strength of the rule. Valid values:
        # 
        # - 0: weak rule
        # 
        # - 1: strong rule
        # 
        # This parameter is required.
        self.block_type = block_type
        # The ID of the checker. Valid values:
        # 
        # - 2: 7-day average fluctuation
        # 
        # - 3: 30-day average fluctuation
        # 
        # - 4: day-over-day comparison
        # 
        # - 5: week-over-week comparison
        # 
        # - 6: month-over-month comparison
        # 
        # - 7: 7-day variance fluctuation
        # 
        # - 8: 30-day variance fluctuation
        # 
        # - 9: comparison with a fixed value
        # 
        # - 10: fluctuation detection over 1, 7, and 30 days
        # 
        # - 11: comparison with the previous cycle
        self.checker = checker
        # The comments of the rule.
        self.comment = comment
        # The critical threshold. It indicates the deviation of the check result from the expected value. You can customize this threshold based on your business requirements. If a strong rule is used and a critical alert is triggered, the scheduling task is blocked.
        self.critical_threshold = critical_threshold
        # The ID of the partition filter expression.
        # 
        # This parameter is required.
        self.entity_id = entity_id
        # The expected value.
        self.expect_value = expect_value
        # The check method. If you use a custom SQL statement, set this parameter to `user_defined`.
        self.method_name = method_name
        # The comparison operator. Examples: `>`, `>=`, `=`, `<>`, `<`, and `<=`.
        # 
        # > If you set the Checker parameter to 9, you must specify the Operator parameter.
        self.operator = operator
        # Specifies whether to use a dynamic threshold. Valid values:
        # 
        # This parameter is required.
        self.predict_type = predict_type
        # The DataWorks workspace ID. You can log on to the [DataWorks console](https://workbench.data.aliyun.com/console) and go to the Workspace Management page to obtain the workspace ID.
        self.project_id = project_id
        # The name of the compute engine or data source.
        # 
        # This parameter is required.
        self.project_name = project_name
        # The field that is monitored by the rule. To perform a table-level check, set this parameter to `table_count` for the number of rows or `table_size` for the table size.
        self.property = property
        # The data type of the field. For a table-level check, set this parameter to `table`. For a field-level check, set this parameter to a specific data type, such as `bigint`.
        self.property_type = property_type
        # The name of the rule.
        # 
        # This parameter is required.
        self.rule_name = rule_name
        # The type of the rule. Valid values:
        # 
        # - 0: system template
        # 
        # - 1: custom SQL
        # 
        # - 2: custom template
        # 
        # This parameter is required.
        self.rule_type = rule_type
        # The variable settings that are inserted before the custom rule. Format: x=a,y=b.
        self.task_setting = task_setting
        # The ID of the template.
        self.template_id = template_id
        # The trend of the check result. Valid values:
        # 
        # - `up`: upward trend
        # 
        # - `down`: downward trend
        # 
        # - `abs`: absolute value
        self.trend = trend
        # The warning threshold. It indicates the deviation of the check result from the expected value. You can customize this threshold based on your business requirements.
        self.warning_threshold = warning_threshold
        # The filter condition or custom SQL statement.
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

        if self.method_name is not None:
            result['MethodName'] = self.method_name

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

        if m.get('MethodName') is not None:
            self.method_name = m.get('MethodName')

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

