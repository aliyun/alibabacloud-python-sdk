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
        # The pagination information.
        self.paging_info = paging_info
        # The request ID.
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
        # The rules.
        self.data_quality_rules = data_quality_rules
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The total number of entries returned.
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
        # The check settings for sample data.
        self.checking_config = checking_config
        # The description of the rule. The description can be up to 500 characters in length.
        self.description = description
        # Indicates whether the rule is enabled.
        self.enabled = enabled
        # The operations that you can perform after the rule-based check fails.
        self.error_handlers = error_handlers
        # The rule ID.
        self.id = id
        # The rule name.
        self.name = name
        # The DataWorks workspace ID.
        self.project_id = project_id
        # The settings for sampling.
        self.sampling_config = sampling_config
        # The strength of the rule. Valid values:
        # 
        # *   Normal
        # *   High
        self.severity = severity
        # The monitored object of the rule.
        self.target = target
        # The ID of the template used by the rule.
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
        # The type of the database to which the table belongs. Valid values:
        # 
        # *   maxcompute
        # *   emr
        # *   cdh
        # *   hologres
        # *   analyticdb_for_postgresql
        # *   analyticdb_for_mysql
        # *   starrocks
        self.database_type = database_type
        # The ID of the table that is limited by the rule in Data Map.
        self.table_guid = table_guid
        # The type of the monitored object. Valid values:
        # 
        # *   Table
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
        # The metrics used for sampling. Valid values:
        # 
        # *   Count: the number of rows in the table.
        # *   Min: the minimum value of the field.
        # *   Max: the maximum value of the field.
        # *   Avg: the average value of the field.
        # *   DistinctCount: the number of unique values of the field after deduplication.
        # *   DistinctPercent: the percentage of the number of unique values of the field after deduplication to the number of rows in the table.
        # *   DuplicatedCount: the number of duplicated values in the field.
        # *   DuplicatedPercent: the percentage of the number of duplicated values of the field to the number of rows in the table.
        # *   TableSize: the table size.
        # *   NullValueCount: the number of rows in which the field is set to null.
        # *   NullValuePercent: the percentage of the number of rows in which the field is set to null to the number of rows in the table.
        # *   GroupCount: the field value and the number of rows for each field value.
        # *   CountNotIn: the number of rows in which the field values are different from the referenced values that you specified in the rule.
        # *   CountDistinctNotIn: the number of unique values that are different from the referenced values that you specified in the rule after deduplication.
        # *   UserDefinedSql: indicates that the data is sampled by executing custom SQL statements.
        self.metric = metric
        # The parameters required for sampling.
        self.metric_parameters = metric_parameters
        # The statements that are used to filter unnecessary data during sampling. The statements can be up to 16,777,215 characters in length.
        self.sampling_filter = sampling_filter
        # The statements that are used to configure the parameters required for sampling before you execute the sampling statements. The statements can be up to 1,000 characters in length. Only the MaxCompute database is supported.
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
        # The SQL statement that is used to filter failed tasks. If the rule is defined by custom SQL statements, you must specify an SQL statement to filter failed tasks.
        self.error_data_filter = error_data_filter
        # The type of the operation. Valid values:
        # 
        # *   SaveErrorData
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
        # The method that is used to query the referenced samples. To obtain some types of thresholds, you need to query reference values. In this example, an expression is used to indicate the query method of referenced samples.
        self.referenced_samples_filter = referenced_samples_filter
        # The threshold settings.
        self.thresholds = thresholds
        # The threshold calculation method. Valid values:
        # 
        # *   Fixed
        # *   Fluctation
        # *   FluctationDiscreate
        # *   Auto
        # *   Average
        # *   Variance
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
        # The threshold settings for critical alerts.
        self.critical = critical
        # The expected threshold setting.
        self.expected = expected
        # The threshold settings for normal alerts.
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
        # The threshold expression.
        # 
        # If the template specified by the TemplateCode parameter is about fluctuation, you must use an expression to represent the threshold for fluctuation. Examples:
        # 
        # *   $checkValue > 0.01
        # *   $checkValue < -0.01
        # *   abs($checkValue) > 0.01
        # 
        # If the template specified by the TemplateCode parameter is about fixed value, you can also use an expression to represent the threshold. If you configure the Expression, Operator, and Value parameters for the threshold at the same time, the Expression parameter takes precedence over the Operator and Value parameters.
        self.expression = expression
        # The comparison operator. Valid values:
        # 
        # *   \\>
        # *   \\>=
        # *   <
        # *   <=
        # *   !=
        # *   \\=
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

class ListDataQualityRulesResponseBodyPagingInfoDataQualityRulesCheckingConfigThresholdsExpected(DaraModel):
    def __init__(
        self,
        expression: str = None,
        operator: str = None,
        value: str = None,
    ):
        # The threshold expression.
        # 
        # If the template specified by the TemplateCode parameter is about fluctuation, you must use an expression to represent the threshold for fluctuation. Examples:
        # 
        # *   $checkValue > 0.01
        # *   $checkValue < -0.01
        # *   abs($checkValue) > 0.01
        # 
        # If the template specified by the TemplateCode parameter is about fixed value, you can also use an expression to represent the threshold. If you configure the Expression, Operator, and Value parameters for the threshold at the same time, the Expression parameter takes precedence over the Operator and Value parameters.
        self.expression = expression
        # The comparison operator. Valid values:
        # 
        # *   \\>
        # *   \\>=
        # *   <
        # *   <=
        # *   !=
        # *   \\=
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

class ListDataQualityRulesResponseBodyPagingInfoDataQualityRulesCheckingConfigThresholdsCritical(DaraModel):
    def __init__(
        self,
        expression: str = None,
        operator: str = None,
        value: str = None,
    ):
        # The threshold expression.
        # 
        # If the template specified by the TemplateCode parameter is about fluctuation, you must use an expression to represent the threshold for fluctuation. Examples:
        # 
        # *   $checkValue > 0.01
        # *   $checkValue < -0.01
        # *   abs($checkValue) > 0.01
        # 
        # If the template specified by the TemplateCode parameter is about fixed value, you can also use an expression to represent the threshold. If you configure the Expression, Operator, and Value parameters for the threshold at the same time, the Expression parameter takes precedence over the Operator and Value parameters.
        self.expression = expression
        # The comparison operator. Valid values:
        # 
        # *   \\>
        # *   \\>=
        # *   <
        # *   <=
        # *   !=
        # *   \\=
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

