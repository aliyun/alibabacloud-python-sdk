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
        # The strength type of the monitoring rule. Valid values:
        # 
        # *   0: The monitoring rule is a weak rule.
        # *   1: The monitoring rule is a strong rule.
        # 
        # This parameter is required.
        self.block_type = block_type
        # The checker ID.
        self.checker = checker
        # The description of the rule.
        self.comment = comment
        # The threshold for a critical alert. The threshold indicates the deviation of the monitoring result from the expected value. You can customize this threshold based on your business requirements. If a strong rule is used and a critical alert is triggered, nodes are blocked.
        self.critical_threshold = critical_threshold
        # The ID of the partition filter expression.
        # 
        # This parameter is required.
        self.entity_id = entity_id
        # The expected value.
        self.expect_value = expect_value
        # The method used to collect sample data. If you want to use a custom SQL statement as a sampling method, set this parameter to user_defined.
        self.method_name = method_name
        # The comparison operator, such as >, >=, =, ≠, <, or <=.
        # 
        # > If you set the Checker parameter to 9, you must configure the Operator parameter.
        self.operator = operator
        # Specifies whether the monitoring rule is a dynamic threshold rule. Valid values: 0 and 2. The value 0 indicates that the monitoring rule is not a dynamic threshold rule. The value 2 indicates that the monitoring rule is a dynamic threshold rule.
        # 
        # This parameter is required.
        self.predict_type = predict_type
        # The DataWorks workspace ID. You can log on to the [DataWorks console](https://workbench.data.aliyun.com/console) and go to the Workspace page to query the ID.
        self.project_id = project_id
        # The name of the compute engine or data source.
        # 
        # This parameter is required.
        self.project_name = project_name
        # The fields that you want to monitor. If you want to monitor all fields in a table and check the table rows, set this parameter to table_count. If you want to monitor all fields in a table and check the table size, set this parameter to table_size.
        self.property = property
        # The data type of the fields that you want to monitor. If you want to monitor all fields in a table, set this parameter to table. If you want to monitor only a specific field, set this parameter to bigint.
        self.property_type = property_type
        # The name of the monitoring rule.
        # 
        # This parameter is required.
        self.rule_name = rule_name
        # Rule type:
        # 
        # *   0: System template rule
        # *   1: Custom SQL rule
        # *   4: Custom template rule
        # 
        # This parameter is required.
        self.rule_type = rule_type
        # The variable settings inserted before the custom rule. Format: x=a,y=b.
        self.task_setting = task_setting
        # The template ID.
        self.template_id = template_id
        # The trend of the monitoring result. Valid values:
        # 
        # *   up: increasing
        # *   down: decreasing
        # *   abs: absolute value
        self.trend = trend
        # The threshold for a warning alert. The threshold indicates the deviation of the monitoring result from the expected value. You can customize this threshold based on your business requirements.
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

