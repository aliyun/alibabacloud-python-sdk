# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class ListDataQualityRulesResponseBody(DaraModel):
    def __init__(
        self,
        paging_info: main_models.ListDataQualityRulesResponseBodyPagingInfo = None,
        request_id: str = None,
    ):
        # Paginated query result of the rule list.
        self.paging_info = paging_info
        # Request ID.
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
            temp_model = main_models.ListDataQualityRulesResponseBodyPagingInfo()
            self.paging_info = temp_model.from_map(m.get('PagingInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListDataQualityRulesResponseBodyPagingInfo(DaraModel):
    def __init__(
        self,
        data_quality_rules: List[main_models.ListDataQualityRulesResponseBodyPagingInfoDataQualityRules] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # Specific rule list.
        self.data_quality_rules = data_quality_rules
        # Page number.
        self.page_number = page_number
        # Page size.
        self.page_size = page_size
        # Total number of entries.
        self.total_count = total_count

    def validate(self):
        if self.data_quality_rules:
            for v1 in self.data_quality_rules:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DataQualityRules'] = []
        if self.data_quality_rules is not None:
            for k1 in self.data_quality_rules:
                result['DataQualityRules'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_quality_rules = []
        if m.get('DataQualityRules') is not None:
            for k1 in m.get('DataQualityRules'):
                temp_model = main_models.ListDataQualityRulesResponseBodyPagingInfoDataQualityRules()
                self.data_quality_rules.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListDataQualityRulesResponseBodyPagingInfoDataQualityRules(DaraModel):
    def __init__(
        self,
        checking_config: main_models.ListDataQualityRulesResponseBodyPagingInfoDataQualityRulesCheckingConfig = None,
        description: str = None,
        enabled: bool = None,
        error_handlers: List[main_models.ListDataQualityRulesResponseBodyPagingInfoDataQualityRulesErrorHandlers] = None,
        id: int = None,
        name: str = None,
        project_id: int = None,
        sampling_config: main_models.ListDataQualityRulesResponseBodyPagingInfoDataQualityRulesSamplingConfig = None,
        severity: str = None,
        target: main_models.ListDataQualityRulesResponseBodyPagingInfoDataQualityRulesTarget = None,
        template_code: str = None,
    ):
        # Sample validation settings.
        self.checking_config = checking_config
        # Rule description. Maximum length: 500 characters.
        self.description = description
        # Whether the data quality rule is enabled.
        self.enabled = enabled
        # List of issue handlers for data quality rule validation.
        self.error_handlers = error_handlers
        # Rule ID.
        self.id = id
        # Rule name.
        self.name = name
        # DataWorks workspace ID.
        self.project_id = project_id
        # Settings required for sample collection.
        self.sampling_config = sampling_config
        # Severity level of the rule for the business (corresponding to strong/weak rules on the page). Valid enumerated values:
        # - Normal
        # - High
        self.severity = severity
        # Object monitored by the rule.
        self.target = target
        # Unique identifier of the rule template referenced by the rule.
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
            temp_model = main_models.ListDataQualityRulesResponseBodyPagingInfoDataQualityRulesCheckingConfig()
            self.checking_config = temp_model.from_map(m.get('CheckingConfig'))

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')

        self.error_handlers = []
        if m.get('ErrorHandlers') is not None:
            for k1 in m.get('ErrorHandlers'):
                temp_model = main_models.ListDataQualityRulesResponseBodyPagingInfoDataQualityRulesErrorHandlers()
                self.error_handlers.append(temp_model.from_map(k1))

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('SamplingConfig') is not None:
            temp_model = main_models.ListDataQualityRulesResponseBodyPagingInfoDataQualityRulesSamplingConfig()
            self.sampling_config = temp_model.from_map(m.get('SamplingConfig'))

        if m.get('Severity') is not None:
            self.severity = m.get('Severity')

        if m.get('Target') is not None:
            temp_model = main_models.ListDataQualityRulesResponseBodyPagingInfoDataQualityRulesTarget()
            self.target = temp_model.from_map(m.get('Target'))

        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')

        return self

class ListDataQualityRulesResponseBodyPagingInfoDataQualityRulesTarget(DaraModel):
    def __init__(
        self,
        database_type: str = None,
        table_guid: str = None,
        type: str = None,
    ):
        # For table-type datasets, the database type to which the table belongs.
        # - maxcompute
        # - emr
        # - cdh
        # - hologres
        # - analyticdb_for_postgresql
        # - analyticdb_for_mysql
        # - starrocks
        self.database_type = database_type
        # Unique ID of the table to which the rule applies in Data Map.
        self.table_guid = table_guid
        # Type of the monitored object.
        # 
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

class ListDataQualityRulesResponseBodyPagingInfoDataQualityRulesSamplingConfig(DaraModel):
    def __init__(
        self,
        metric: str = None,
        metric_parameters: str = None,
        sampling_filter: str = None,
        setting_config: str = None,
    ):
        # Sampling metric name.
        # - Count: number of table rows.
        # - Min: minimum value of the field.
        # - Max: maximum value of the field.
        # - Avg: average value of the field.
        # - DistinctCount: number of distinct values of the field.
        # - DistinctPercent: ratio of the number of distinct values of the field to the number of data rows.
        # - DuplicatedCount: number of duplicate values of the field.
        # - DuplicatedPercent: ratio of the number of duplicate values of the field to the number of data rows.
        # - TableSize: table size.
        # - NullValueCount: number of rows where the field value is null.
        # - NullValuePercent: percentage of rows where the field value is null.
        # - GroupCount: each value and its corresponding number of data rows after aggregation by field value.
        # - CountNotIn: number of rows whose enumerated values do not match.
        # - CountDistinctNotIn: number of distinct values whose enumerated values do not match.
        # - UserDefinedSql: sample collection via custom SQL.
        self.metric = metric
        # Parameters required during sample collection.
        self.metric_parameters = metric_parameters
        # Condition for the secondary filtering of data that is not of concern during sampling. Maximum length: 16,777,215 characters.
        self.sampling_filter = sampling_filter
        # Runtime parameter setting statements inserted and executed before the sampling statement is actually executed. Maximum length: 1,000 characters. Currently only MaxCompute is supported.
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

class ListDataQualityRulesResponseBodyPagingInfoDataQualityRulesErrorHandlers(DaraModel):
    def __init__(
        self,
        error_data_filter: str = None,
        type: str = None,
    ):
        # For custom SQL rules, the user needs to specify SQL to filter problem data.
        self.error_data_filter = error_data_filter
        # Handler type:
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

class ListDataQualityRulesResponseBodyPagingInfoDataQualityRulesCheckingConfig(DaraModel):
    def __init__(
        self,
        referenced_samples_filter: str = None,
        thresholds: main_models.ListDataQualityRulesResponseBodyPagingInfoDataQualityRulesCheckingConfigThresholds = None,
        type: str = None,
    ):
        # Some types of thresholds require querying some reference samples, then aggregating the values of the reference samples to obtain the threshold for comparison. An expression is used here to represent the query method for the reference samples.
        self.referenced_samples_filter = referenced_samples_filter
        # Threshold settings.
        self.thresholds = thresholds
        # Threshold calculation method.
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
            temp_model = main_models.ListDataQualityRulesResponseBodyPagingInfoDataQualityRulesCheckingConfigThresholds()
            self.thresholds = temp_model.from_map(m.get('Thresholds'))

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class ListDataQualityRulesResponseBodyPagingInfoDataQualityRulesCheckingConfigThresholds(DaraModel):
    def __init__(
        self,
        critical: main_models.ListDataQualityRulesResponseBodyPagingInfoDataQualityRulesCheckingConfigThresholdsCritical = None,
        expected: main_models.ListDataQualityRulesResponseBodyPagingInfoDataQualityRulesCheckingConfigThresholdsExpected = None,
        warned: main_models.ListDataQualityRulesResponseBodyPagingInfoDataQualityRulesCheckingConfigThresholdsWarned = None,
    ):
        # Threshold settings for critical warnings.
        self.critical = critical
        # Expected threshold settings.
        self.expected = expected
        # Threshold settings for normal warnings.
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
            temp_model = main_models.ListDataQualityRulesResponseBodyPagingInfoDataQualityRulesCheckingConfigThresholdsCritical()
            self.critical = temp_model.from_map(m.get('Critical'))

        if m.get('Expected') is not None:
            temp_model = main_models.ListDataQualityRulesResponseBodyPagingInfoDataQualityRulesCheckingConfigThresholdsExpected()
            self.expected = temp_model.from_map(m.get('Expected'))

        if m.get('Warned') is not None:
            temp_model = main_models.ListDataQualityRulesResponseBodyPagingInfoDataQualityRulesCheckingConfigThresholdsWarned()
            self.warned = temp_model.from_map(m.get('Warned'))

        return self

class ListDataQualityRulesResponseBodyPagingInfoDataQualityRulesCheckingConfigThresholdsWarned(DaraModel):
    def __init__(
        self,
        expression: str = None,
        operator: str = None,
        value: str = None,
    ):
        # Threshold expression.
        # 
        # Fluctuation rate type rules must use the expression method to indicate the fluctuation threshold. Examples:
        # 
        # - Fluctuation increase greater than 0.01: $checkValue > 0.01 
        # - Fluctuation decrease greater than 0.01: $checkValue < -0.01 
        # - Absolute value of the fluctuation rate: abs($checkValue) > 0.01
        # 
        # Fixed value type rules can also configure thresholds using expressions. If both are configured, the expression takes precedence over Operator and Value.
        self.expression = expression
        # Comparison operator.
        # - \\>
        # - \\>=
        # - <
        # - <=
        # - !=
        # - =
        self.operator = operator
        # Threshold value.
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

class ListDataQualityRulesResponseBodyPagingInfoDataQualityRulesCheckingConfigThresholdsExpected(DaraModel):
    def __init__(
        self,
        expression: str = None,
        operator: str = None,
        value: str = None,
    ):
        # Threshold expression.
        # 
        # Fluctuation rate type rules must use the expression method to indicate the fluctuation threshold. Examples:
        # 
        # - Fluctuation increase greater than 0.01: $checkValue > 0.01 
        # - Fluctuation decrease greater than 0.01: $checkValue < -0.01 
        # - Absolute value of the fluctuation rate: abs($checkValue) > 0.01
        # 
        # Fixed value type rules can also configure thresholds using expressions. If both are configured, the expression takes precedence over Operator and Value.
        self.expression = expression
        # Comparison operator.
        # - \\>
        # - \\>=
        # - <
        # - <=
        # - !=
        # - =
        self.operator = operator
        # Threshold value.
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

class ListDataQualityRulesResponseBodyPagingInfoDataQualityRulesCheckingConfigThresholdsCritical(DaraModel):
    def __init__(
        self,
        expression: str = None,
        operator: str = None,
        value: str = None,
    ):
        # Threshold expression.
        # 
        # Fluctuation rate type rules must use the expression method to indicate the fluctuation threshold. Examples:
        # 
        # - Fluctuation increase greater than 0.01: $checkValue > 0.01 
        # - Fluctuation decrease greater than 0.01: $checkValue < -0.01 
        # - Absolute value of the fluctuation rate: abs($checkValue) > 0.01
        # 
        # Fixed value type rules can also configure thresholds using expressions. If both are configured, the expression takes precedence over Operator and Value.
        self.expression = expression
        # Comparison operator.
        # - \\>
        # - \\>=
        # - <
        # - <=
        # - !=
        # - =
        self.operator = operator
        # Threshold value.
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

