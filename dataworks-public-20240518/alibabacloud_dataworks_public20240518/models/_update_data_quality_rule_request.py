# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class UpdateDataQualityRuleRequest(DaraModel):
    def __init__(
        self,
        checking_config: main_models.UpdateDataQualityRuleRequestCheckingConfig = None,
        description: str = None,
        enabled: bool = None,
        error_handlers: List[main_models.UpdateDataQualityRuleRequestErrorHandlers] = None,
        id: int = None,
        name: str = None,
        project_id: int = None,
        sampling_config: main_models.UpdateDataQualityRuleRequestSamplingConfig = None,
        severity: str = None,
        template_code: str = None,
    ):
        # The sample check settings.
        self.checking_config = checking_config
        # The description of the rule. It can be up to 500 characters in length.
        self.description = description
        # Specifies whether the rule is enabled.
        self.enabled = enabled
        # The list of error handlers for quality rule check issues.
        self.error_handlers = error_handlers
        # The ID of the rule.
        # 
        # This parameter is required.
        self.id = id
        # The name of the rule. The name can contain digits, letters, Chinese characters, and half-width or full-width punctuation marks. It can be up to 255 characters in length.
        self.name = name
        # The ID of the DataWorks workspace. You can log on to the [DataWorks console](https://workbench.data.aliyun.com/console) and go to the Workspace Configuration page to obtain the workspace ID.
        # 
        # This parameter is required.
        self.project_id = project_id
        # The settings required for sample collection.
        self.sampling_config = sampling_config
        # The severity level of the rule for the business, which corresponds to the strong or weak rule on the page. Valid values:
        # - Normal
        # - High
        self.severity = severity
        # The unique identifier of the rule template referenced by the rule.
        self.template_code = template_code

    def validate(self):
        if self.checking_config:
            self.checking_config.validate()
        if self.error_handlers:
            for v1 in self.error_handlers:
                 if v1:
                    v1.validate()
        if self.sampling_config:
            self.sampling_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.checking_config is not None:
            result['CheckingConfig'] = self.checking_config.to_map()

        if self.description is not None:
            result['Description'] = self.description

        if self.enabled is not None:
            result['Enabled'] = self.enabled

        result['ErrorHandlers'] = []
        if self.error_handlers is not None:
            for k1 in self.error_handlers:
                result['ErrorHandlers'].append(k1.to_map() if k1 else None)

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.sampling_config is not None:
            result['SamplingConfig'] = self.sampling_config.to_map()

        if self.severity is not None:
            result['Severity'] = self.severity

        if self.template_code is not None:
            result['TemplateCode'] = self.template_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckingConfig') is not None:
            temp_model = main_models.UpdateDataQualityRuleRequestCheckingConfig()
            self.checking_config = temp_model.from_map(m.get('CheckingConfig'))

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')

        self.error_handlers = []
        if m.get('ErrorHandlers') is not None:
            for k1 in m.get('ErrorHandlers'):
                temp_model = main_models.UpdateDataQualityRuleRequestErrorHandlers()
                self.error_handlers.append(temp_model.from_map(k1))

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('SamplingConfig') is not None:
            temp_model = main_models.UpdateDataQualityRuleRequestSamplingConfig()
            self.sampling_config = temp_model.from_map(m.get('SamplingConfig'))

        if m.get('Severity') is not None:
            self.severity = m.get('Severity')

        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')

        return self

class UpdateDataQualityRuleRequestSamplingConfig(DaraModel):
    def __init__(
        self,
        metric: str = None,
        metric_parameters: str = None,
        sampling_filter: str = None,
        setting_config: str = None,
    ):
        # The name of the sampling metric. This parameter is optional when a template is used. Valid values:
        # - Count: number of rows in the table
        # - Min: minimum value of the field
        # - Max: maximum value of the field
        # - Avg: average value of the field
        # - DistinctCount: number of unique values in the field
        # - DistinctPercent: ratio of the number of unique values in the field to the number of data rows
        # - DuplicatedCount: number of duplicate values in the field
        # - DuplicatedPercent: ratio of the number of duplicate values in the field to the number of data rows
        # - TableSize: size of the table
        # - NullValueCount: number of rows where the field is null
        # - NullValuePercent: ratio of rows where the field is null
        # - GroupCount: number of data rows corresponding to each value after aggregation by field value
        # - CountNotIn: number of rows that do not match the enumerated values
        # - CountDistinctNotIn: number of unique values that do not match the enumerated values
        # - UserDefinedSql: sample collection by using custom SQL statements
        self.metric = metric
        # The parameters required for sample collection.
        self.metric_parameters = metric_parameters
        # The condition used to filter out unneeded data during sampling. It can be up to 16,777,215 characters in length.
        self.sampling_filter = sampling_filter
        # The runtime parameter setting statements that are inserted and executed before the sampling statements are executed. It can be up to 1,000 characters in length. Only MaxCompute is supported.
        self.setting_config = setting_config

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.metric is not None:
            result['Metric'] = self.metric

        if self.metric_parameters is not None:
            result['MetricParameters'] = self.metric_parameters

        if self.sampling_filter is not None:
            result['SamplingFilter'] = self.sampling_filter

        if self.setting_config is not None:
            result['SettingConfig'] = self.setting_config

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Metric') is not None:
            self.metric = m.get('Metric')

        if m.get('MetricParameters') is not None:
            self.metric_parameters = m.get('MetricParameters')

        if m.get('SamplingFilter') is not None:
            self.sampling_filter = m.get('SamplingFilter')

        if m.get('SettingConfig') is not None:
            self.setting_config = m.get('SettingConfig')

        return self

class UpdateDataQualityRuleRequestErrorHandlers(DaraModel):
    def __init__(
        self,
        error_data_filter: str = None,
        type: str = None,
    ):
        # If the rule is a custom SQL rule, you must specify an SQL statement to filter the error data.
        self.error_data_filter = error_data_filter
        # The type of the error handler. Valid values:
        # - SaveErrorData
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_data_filter is not None:
            result['ErrorDataFilter'] = self.error_data_filter

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorDataFilter') is not None:
            self.error_data_filter = m.get('ErrorDataFilter')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class UpdateDataQualityRuleRequestCheckingConfig(DaraModel):
    def __init__(
        self,
        referenced_samples_filter: str = None,
        thresholds: main_models.UpdateDataQualityRuleRequestCheckingConfigThresholds = None,
        type: str = None,
    ):
        # For some types of thresholds, reference samples must be queried, and the values of the reference samples are aggregated to obtain the threshold for comparison. This parameter uses an expression to specify the query method for the reference samples.
        self.referenced_samples_filter = referenced_samples_filter
        # The threshold settings.
        self.thresholds = thresholds
        # The threshold calculation method. This parameter is optional when a template is used. Valid values:
        # - Fixed
        # - Fluctation
        # - FluctationDiscreate
        # - Auto
        # - Average
        # - Variance
        self.type = type

    def validate(self):
        if self.thresholds:
            self.thresholds.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.referenced_samples_filter is not None:
            result['ReferencedSamplesFilter'] = self.referenced_samples_filter

        if self.thresholds is not None:
            result['Thresholds'] = self.thresholds.to_map()

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ReferencedSamplesFilter') is not None:
            self.referenced_samples_filter = m.get('ReferencedSamplesFilter')

        if m.get('Thresholds') is not None:
            temp_model = main_models.UpdateDataQualityRuleRequestCheckingConfigThresholds()
            self.thresholds = temp_model.from_map(m.get('Thresholds'))

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class UpdateDataQualityRuleRequestCheckingConfigThresholds(DaraModel):
    def __init__(
        self,
        critical: main_models.UpdateDataQualityRuleRequestCheckingConfigThresholdsCritical = None,
        expected: main_models.UpdateDataQualityRuleRequestCheckingConfigThresholdsExpected = None,
        warned: main_models.UpdateDataQualityRuleRequestCheckingConfigThresholdsWarned = None,
    ):
        # The threshold settings for critical warnings.
        self.critical = critical
        # The expected threshold settings.
        self.expected = expected
        # The threshold settings for common warnings.
        self.warned = warned

    def validate(self):
        if self.critical:
            self.critical.validate()
        if self.expected:
            self.expected.validate()
        if self.warned:
            self.warned.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.critical is not None:
            result['Critical'] = self.critical.to_map()

        if self.expected is not None:
            result['Expected'] = self.expected.to_map()

        if self.warned is not None:
            result['Warned'] = self.warned.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Critical') is not None:
            temp_model = main_models.UpdateDataQualityRuleRequestCheckingConfigThresholdsCritical()
            self.critical = temp_model.from_map(m.get('Critical'))

        if m.get('Expected') is not None:
            temp_model = main_models.UpdateDataQualityRuleRequestCheckingConfigThresholdsExpected()
            self.expected = temp_model.from_map(m.get('Expected'))

        if m.get('Warned') is not None:
            temp_model = main_models.UpdateDataQualityRuleRequestCheckingConfigThresholdsWarned()
            self.warned = temp_model.from_map(m.get('Warned'))

        return self

class UpdateDataQualityRuleRequestCheckingConfigThresholdsWarned(DaraModel):
    def __init__(
        self,
        expression: str = None,
        operator: str = None,
        value: str = None,
    ):
        # The threshold expression. For fluctuation rules, you must use an expression to specify the fluctuation threshold. Examples:
        # - Fluctuation increase greater than 0.01: $checkValue > 0.01 
        # - Fluctuation decrease greater than 0.01: $checkValue < -0.01 
        # - Absolute value of the fluctuation rate: abs($checkValue) > 0.01
        # For fixed value rules, you can also use an expression to configure the threshold. If both are configured, the expression takes precedence over the Operator and Value parameters.
        self.expression = expression
        # The comparison operator. Valid values:
        # - \\>
        # - \\>=
        # - \\<
        # - \\<=
        # - !=
        # - =
        self.operator = operator
        # The threshold value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.expression is not None:
            result['Expression'] = self.expression

        if self.operator is not None:
            result['Operator'] = self.operator

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Expression') is not None:
            self.expression = m.get('Expression')

        if m.get('Operator') is not None:
            self.operator = m.get('Operator')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class UpdateDataQualityRuleRequestCheckingConfigThresholdsExpected(DaraModel):
    def __init__(
        self,
        expression: str = None,
        operator: str = None,
        value: str = None,
    ):
        # The threshold expression. For fluctuation rules, you must use an expression to specify the fluctuation threshold. Examples:
        # - Fluctuation increase greater than 0.01: $checkValue > 0.01 
        # - Fluctuation decrease greater than 0.01: $checkValue < -0.01 
        # - Absolute value of the fluctuation rate: abs($checkValue) > 0.01
        # For fixed value rules, you can also use an expression to configure the threshold. If both are configured, the expression takes precedence over the Operator and Value parameters.
        self.expression = expression
        # The comparison operator. Valid values:
        # - \\>
        # - \\>=
        # - <
        # - <=
        # - !=
        # - =
        self.operator = operator
        # The threshold value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.expression is not None:
            result['Expression'] = self.expression

        if self.operator is not None:
            result['Operator'] = self.operator

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Expression') is not None:
            self.expression = m.get('Expression')

        if m.get('Operator') is not None:
            self.operator = m.get('Operator')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class UpdateDataQualityRuleRequestCheckingConfigThresholdsCritical(DaraModel):
    def __init__(
        self,
        expression: str = None,
        operator: str = None,
        value: str = None,
    ):
        # The threshold expression. For fluctuation rules, you must use an expression to specify the fluctuation threshold. Examples:
        # - Fluctuation increase greater than 0.01: $checkValue > 0.01 
        # - Fluctuation decrease greater than 0.01: $checkValue < -0.01 
        # - Absolute value of the fluctuation rate: abs($checkValue) > 0.01
        # For fixed value rules, you can also use an expression to configure the threshold. If both are configured, the expression takes precedence over the Operator and Value parameters.
        self.expression = expression
        # The comparison operator. Valid values:
        # - \\>
        # - \\>=
        # - \\<
        # - \\<=
        # - !=
        # - =
        self.operator = operator
        # The threshold value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.expression is not None:
            result['Expression'] = self.expression

        if self.operator is not None:
            result['Operator'] = self.operator

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Expression') is not None:
            self.expression = m.get('Expression')

        if m.get('Operator') is not None:
            self.operator = m.get('Operator')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

