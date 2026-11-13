# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class ListDataQualityResultsResponseBody(DaraModel):
    def __init__(
        self,
        paging_info: main_models.ListDataQualityResultsResponseBodyPagingInfo = None,
        request_id: str = None,
    ):
        # The paginated data quality check results.
        self.paging_info = paging_info
        # The API request ID.
        self.request_id = request_id

    def validate(self):
        if self.paging_info:
            self.paging_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.paging_info is not None:
            result['PagingInfo'] = self.paging_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PagingInfo') is not None:
            temp_model = main_models.ListDataQualityResultsResponseBodyPagingInfo()
            self.paging_info = temp_model.from_map(m.get('PagingInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListDataQualityResultsResponseBodyPagingInfo(DaraModel):
    def __init__(
        self,
        data_quality_results: List[main_models.ListDataQualityResultsResponseBodyPagingInfoDataQualityResults] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The list of data quality check results.
        self.data_quality_results = data_quality_results
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The total number of entries.
        self.total_count = total_count

    def validate(self):
        if self.data_quality_results:
            for v1 in self.data_quality_results:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DataQualityResults'] = []
        if self.data_quality_results is not None:
            for k1 in self.data_quality_results:
                result['DataQualityResults'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_quality_results = []
        if m.get('DataQualityResults') is not None:
            for k1 in m.get('DataQualityResults'):
                temp_model = main_models.ListDataQualityResultsResponseBodyPagingInfoDataQualityResults()
                self.data_quality_results.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListDataQualityResultsResponseBodyPagingInfoDataQualityResults(DaraModel):
    def __init__(
        self,
        create_time: int = None,
        details: List[main_models.ListDataQualityResultsResponseBodyPagingInfoDataQualityResultsDetails] = None,
        id: int = None,
        rule: main_models.ListDataQualityResultsResponseBodyPagingInfoDataQualityResultsRule = None,
        sample: str = None,
        status: str = None,
        task_instance_id: int = None,
    ):
        # The time when the check result was generated.
        self.create_time = create_time
        # The details of this check.
        self.details = details
        # The check result ID.
        self.id = id
        # The snapshot of the rule configuration at the start of the check.
        self.rule = rule
        # The sample value used for this check.
        self.sample = sample
        # The status of the check result. Valid values:
        # - Running
        # - Error
        # - Passed
        # - Warned
        # - Critical
        self.status = status
        # The ID of the data quality evaluation task instance.
        self.task_instance_id = task_instance_id

    def validate(self):
        if self.details:
            for v1 in self.details:
                 if v1:
                    v1.validate()
        if self.rule:
            self.rule.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        result['Details'] = []
        if self.details is not None:
            for k1 in self.details:
                result['Details'].append(k1.to_map() if k1 else None)

        if self.id is not None:
            result['Id'] = self.id

        if self.rule is not None:
            result['Rule'] = self.rule.to_map()

        if self.sample is not None:
            result['Sample'] = self.sample

        if self.status is not None:
            result['Status'] = self.status

        if self.task_instance_id is not None:
            result['TaskInstanceId'] = self.task_instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        self.details = []
        if m.get('Details') is not None:
            for k1 in m.get('Details'):
                temp_model = main_models.ListDataQualityResultsResponseBodyPagingInfoDataQualityResultsDetails()
                self.details.append(temp_model.from_map(k1))

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Rule') is not None:
            temp_model = main_models.ListDataQualityResultsResponseBodyPagingInfoDataQualityResultsRule()
            self.rule = temp_model.from_map(m.get('Rule'))

        if m.get('Sample') is not None:
            self.sample = m.get('Sample')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TaskInstanceId') is not None:
            self.task_instance_id = m.get('TaskInstanceId')

        return self

class ListDataQualityResultsResponseBodyPagingInfoDataQualityResultsRule(DaraModel):
    def __init__(
        self,
        checking_config: main_models.ListDataQualityResultsResponseBodyPagingInfoDataQualityResultsRuleCheckingConfig = None,
        description: str = None,
        enabled: bool = None,
        error_handlers: List[main_models.ListDataQualityResultsResponseBodyPagingInfoDataQualityResultsRuleErrorHandlers] = None,
        id: int = None,
        name: str = None,
        project_id: int = None,
        sampling_config: main_models.ListDataQualityResultsResponseBodyPagingInfoDataQualityResultsRuleSamplingConfig = None,
        severity: str = None,
        target: main_models.ListDataQualityResultsResponseBodyPagingInfoDataQualityResultsRuleTarget = None,
        template_code: str = None,
    ):
        # The sample check settings.
        self.checking_config = checking_config
        # The description of the rule. It can be up to 500 characters in length.
        self.description = description
        # Specifies whether the rule is enabled.
        self.enabled = enabled
        # The error handlers for data quality rule checks.
        self.error_handlers = error_handlers
        # The rule ID.
        self.id = id
        # The rule name. The name can contain digits, letters, Chinese characters, and half-width or full-width punctuation marks. It can be up to 255 characters in length.
        self.name = name
        # The DataWorks workspace ID.
        self.project_id = project_id
        # The settings required for sample collection.
        self.sampling_config = sampling_config
        # The severity level of the rule for the business, which corresponds to strong and weak rules on the page. Valid values:
        # - High
        # - Normal
        self.severity = severity
        # The object monitored by the rule.
        self.target = target
        # The code of the rule template referenced when the rule was created.
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
        if self.target:
            self.target.validate()

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

        if self.target is not None:
            result['Target'] = self.target.to_map()

        if self.template_code is not None:
            result['TemplateCode'] = self.template_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckingConfig') is not None:
            temp_model = main_models.ListDataQualityResultsResponseBodyPagingInfoDataQualityResultsRuleCheckingConfig()
            self.checking_config = temp_model.from_map(m.get('CheckingConfig'))

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')

        self.error_handlers = []
        if m.get('ErrorHandlers') is not None:
            for k1 in m.get('ErrorHandlers'):
                temp_model = main_models.ListDataQualityResultsResponseBodyPagingInfoDataQualityResultsRuleErrorHandlers()
                self.error_handlers.append(temp_model.from_map(k1))

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('SamplingConfig') is not None:
            temp_model = main_models.ListDataQualityResultsResponseBodyPagingInfoDataQualityResultsRuleSamplingConfig()
            self.sampling_config = temp_model.from_map(m.get('SamplingConfig'))

        if m.get('Severity') is not None:
            self.severity = m.get('Severity')

        if m.get('Target') is not None:
            temp_model = main_models.ListDataQualityResultsResponseBodyPagingInfoDataQualityResultsRuleTarget()
            self.target = temp_model.from_map(m.get('Target'))

        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')

        return self

class ListDataQualityResultsResponseBodyPagingInfoDataQualityResultsRuleTarget(DaraModel):
    def __init__(
        self,
        database_type: str = None,
        table_guid: str = None,
        type: str = None,
    ):
        # The database type of the table dataset. Valid values:
        # - maxcompute
        # - emr
        # - cdh
        # - hologres
        # - analyticdb_for_postgresql
        # - analyticdb_for_mysql
        # - starrocks
        self.database_type = database_type
        # The unique ID of the table in DataWorks Data Map.
        self.table_guid = table_guid
        # The type of the monitored object. Valid values:
        # - Table
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.database_type is not None:
            result['DatabaseType'] = self.database_type

        if self.table_guid is not None:
            result['TableGuid'] = self.table_guid

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatabaseType') is not None:
            self.database_type = m.get('DatabaseType')

        if m.get('TableGuid') is not None:
            self.table_guid = m.get('TableGuid')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class ListDataQualityResultsResponseBodyPagingInfoDataQualityResultsRuleSamplingConfig(DaraModel):
    def __init__(
        self,
        metric: str = None,
        metric_parameters: str = None,
        sampling_filter: str = None,
        setting_config: str = None,
    ):
        # The name of the sampling metric. Valid values:
        # - Count: The number of rows in the table.
        # - Min: The minimum value of the field.
        # - Max: The maximum value of the field.
        # - Avg: The average value of the field.
        # - DistinctCount: The number of unique values in the field.
        # - DistinctPercent: The ratio of unique values to the total number of rows in the field.
        # - DuplicatedCount: The number of duplicate values in the field.
        # - DuplicatedPercent: The ratio of duplicate values to the total number of rows in the field.
        # - TableSize: The table size.
        # - NullValueCount: The number of rows with null values in the field.
        # - NullValuePercent: The ratio of null values in the field.
        # - GroupCount: The number of rows corresponding to each value after aggregation by field value.
        # - CountNotIn: The number of rows that do not match the enumerated values.
        # - CountDistinctNotIn: The number of unique values that do not match the enumerated values.
        # - UserDefinedSql: Sample collection through custom SQL.
        self.metric = metric
        # The parameters required for sample collection.
        self.metric_parameters = metric_parameters
        # The conditions used to filter out unneeded data during sampling. It can be up to 16,777,215 characters in length.
        self.sampling_filter = sampling_filter
        # The runtime parameter setting statements inserted before the sampling statement is executed. It can be up to 1,000 characters in length. Only MaxCompute is supported.
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

class ListDataQualityResultsResponseBodyPagingInfoDataQualityResultsRuleErrorHandlers(DaraModel):
    def __init__(
        self,
        error_data_filter: str = None,
        type: str = None,
    ):
        # The SQL statement specified by the user to filter error data for custom SQL rules.
        self.error_data_filter = error_data_filter
        # The handler type. Valid values:
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

class ListDataQualityResultsResponseBodyPagingInfoDataQualityResultsRuleCheckingConfig(DaraModel):
    def __init__(
        self,
        referenced_samples_filter: str = None,
        thresholds: main_models.ListDataQualityResultsResponseBodyPagingInfoDataQualityResultsRuleCheckingConfigThresholds = None,
        type: str = None,
    ):
        # The expression used to query reference samples for certain types of thresholds. The values of the reference samples are aggregated to obtain the threshold for comparison.
        self.referenced_samples_filter = referenced_samples_filter
        # The threshold settings.
        self.thresholds = thresholds
        # The threshold calculation method. Valid values:
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
            temp_model = main_models.ListDataQualityResultsResponseBodyPagingInfoDataQualityResultsRuleCheckingConfigThresholds()
            self.thresholds = temp_model.from_map(m.get('Thresholds'))

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class ListDataQualityResultsResponseBodyPagingInfoDataQualityResultsRuleCheckingConfigThresholds(DaraModel):
    def __init__(
        self,
        critical: main_models.ListDataQualityResultsResponseBodyPagingInfoDataQualityResultsRuleCheckingConfigThresholdsCritical = None,
        expected: main_models.ListDataQualityResultsResponseBodyPagingInfoDataQualityResultsRuleCheckingConfigThresholdsExpected = None,
        warned: main_models.ListDataQualityResultsResponseBodyPagingInfoDataQualityResultsRuleCheckingConfigThresholdsWarned = None,
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
            temp_model = main_models.ListDataQualityResultsResponseBodyPagingInfoDataQualityResultsRuleCheckingConfigThresholdsCritical()
            self.critical = temp_model.from_map(m.get('Critical'))

        if m.get('Expected') is not None:
            temp_model = main_models.ListDataQualityResultsResponseBodyPagingInfoDataQualityResultsRuleCheckingConfigThresholdsExpected()
            self.expected = temp_model.from_map(m.get('Expected'))

        if m.get('Warned') is not None:
            temp_model = main_models.ListDataQualityResultsResponseBodyPagingInfoDataQualityResultsRuleCheckingConfigThresholdsWarned()
            self.warned = temp_model.from_map(m.get('Warned'))

        return self

class ListDataQualityResultsResponseBodyPagingInfoDataQualityResultsRuleCheckingConfigThresholdsWarned(DaraModel):
    def __init__(
        self,
        expression: str = None,
        operator: str = None,
        value: str = None,
    ):
        # The threshold expression.
        # 
        # For fluctuation rules, you must use an expression to represent the fluctuation threshold. Examples:
        # 
        # - Fluctuation increase greater than 0.01: $checkValue > 0.01 
        # - Fluctuation decrease greater than 0.01: $checkValue < -0.01 
        # - Absolute value of fluctuation rate: abs($checkValue) > 0.01
        # 
        # For fixed value rules, you can also use an expression to configure the threshold. If both are configured, the expression takes precedence over Operator and Value.
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

class ListDataQualityResultsResponseBodyPagingInfoDataQualityResultsRuleCheckingConfigThresholdsExpected(DaraModel):
    def __init__(
        self,
        expression: str = None,
        operator: str = None,
        value: str = None,
    ):
        # The threshold expression.
        # 
        # For fluctuation rules, you must use an expression to represent the fluctuation threshold. Examples:
        # 
        # - Fluctuation increase greater than 0.01: $checkValue > 0.01 
        # - Fluctuation decrease greater than 0.01: $checkValue < -0.01 
        # - Absolute value of fluctuation rate: abs($checkValue) > 0.01
        # 
        # For fixed value rules, you can also use an expression to configure the threshold. If both are configured, the expression takes precedence over Operator and Value.
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

class ListDataQualityResultsResponseBodyPagingInfoDataQualityResultsRuleCheckingConfigThresholdsCritical(DaraModel):
    def __init__(
        self,
        expression: str = None,
        operator: str = None,
        value: str = None,
    ):
        # The threshold expression.
        # 
        # For fluctuation rules, you must use an expression to represent the fluctuation threshold. Examples:
        # 
        # - Fluctuation increase greater than 0.01: $checkValue > 0.01 
        # - Fluctuation decrease greater than 0.01: $checkValue < -0.01 
        # - Absolute value of fluctuation rate: abs($checkValue) > 0.01
        # 
        # For fixed value rules, you can also use an expression to configure the threshold. If both are configured, the expression takes precedence over Operator and Value.
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

class ListDataQualityResultsResponseBodyPagingInfoDataQualityResultsDetails(DaraModel):
    def __init__(
        self,
        checked_value: str = None,
        referenced_value: str = None,
        status: str = None,
    ):
        # The final value used for comparison with the threshold.
        self.checked_value = checked_value
        # The referenced sample value used as the baseline for calculating the checked value.
        self.referenced_value = referenced_value
        # The final comparison result status. Valid values:
        # - Error
        # - Passed
        # - Warned
        # - Critical
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.checked_value is not None:
            result['CheckedValue'] = self.checked_value

        if self.referenced_value is not None:
            result['ReferencedValue'] = self.referenced_value

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckedValue') is not None:
            self.checked_value = m.get('CheckedValue')

        if m.get('ReferencedValue') is not None:
            self.referenced_value = m.get('ReferencedValue')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

