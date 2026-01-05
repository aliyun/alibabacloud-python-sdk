# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class GetDataQualityRuleResponseBody(DaraModel):
    def __init__(
        self,
        data_quality_rule: main_models.GetDataQualityRuleResponseBodyDataQualityRule = None,
        request_id: str = None,
    ):
        # The information about the rule.
        self.data_quality_rule = data_quality_rule
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data_quality_rule:
            self.data_quality_rule.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_quality_rule is not None:
            result['DataQualityRule'] = self.data_quality_rule.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataQualityRule') is not None:
            temp_model = main_models.GetDataQualityRuleResponseBodyDataQualityRule()
            self.data_quality_rule = temp_model.from_map(m.get('DataQualityRule'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetDataQualityRuleResponseBodyDataQualityRule(DaraModel):
    def __init__(
        self,
        checking_config: main_models.GetDataQualityRuleResponseBodyDataQualityRuleCheckingConfig = None,
        description: str = None,
        enabled: bool = None,
        error_handlers: List[main_models.GetDataQualityRuleResponseBodyDataQualityRuleErrorHandlers] = None,
        id: int = None,
        name: str = None,
        project_id: int = None,
        sampling_config: main_models.GetDataQualityRuleResponseBodyDataQualityRuleSamplingConfig = None,
        severity: str = None,
        target: main_models.GetDataQualityRuleResponseBodyDataQualityRuleTarget = None,
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
        # The sampling settings.
        self.sampling_config = sampling_config
        # Rule for the business level (corresponding to the strong and weak rules on the page), optional enumeration value:
        # - Normal
        # - High
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
            temp_model = main_models.GetDataQualityRuleResponseBodyDataQualityRuleCheckingConfig()
            self.checking_config = temp_model.from_map(m.get('CheckingConfig'))

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')

        self.error_handlers = []
        if m.get('ErrorHandlers') is not None:
            for k1 in m.get('ErrorHandlers'):
                temp_model = main_models.GetDataQualityRuleResponseBodyDataQualityRuleErrorHandlers()
                self.error_handlers.append(temp_model.from_map(k1))

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('SamplingConfig') is not None:
            temp_model = main_models.GetDataQualityRuleResponseBodyDataQualityRuleSamplingConfig()
            self.sampling_config = temp_model.from_map(m.get('SamplingConfig'))

        if m.get('Severity') is not None:
            self.severity = m.get('Severity')

        if m.get('Target') is not None:
            temp_model = main_models.GetDataQualityRuleResponseBodyDataQualityRuleTarget()
            self.target = temp_model.from_map(m.get('Target'))

        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')

        return self

class GetDataQualityRuleResponseBodyDataQualityRuleTarget(DaraModel):
    def __init__(
        self,
        database_type: str = None,
        partition_spec: str = None,
        table_guid: str = None,
        type: str = None,
    ):
        # The dataset of the table type. The database type to which the table belongs.
        # - maxcompute
        # - emr
        # - cdh
        # - hologres
        # - analyticdb_for_postgresql
        # - analyticdb_for_mysql
        # - starrocks
        self.database_type = database_type
        # The configuration of the partitioned table.
        self.partition_spec = partition_spec
        # The ID of the table that is limited by the rule in Data Map.
        self.table_guid = table_guid
        # Monitoring object type
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

        if self.partition_spec is not None:
            result['PartitionSpec'] = self.partition_spec

        if self.table_guid is not None:
            result['TableGuid'] = self.table_guid

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatabaseType') is not None:
            self.database_type = m.get('DatabaseType')

        if m.get('PartitionSpec') is not None:
            self.partition_spec = m.get('PartitionSpec')

        if m.get('TableGuid') is not None:
            self.table_guid = m.get('TableGuid')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class GetDataQualityRuleResponseBodyDataQualityRuleSamplingConfig(DaraModel):
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
        # *   DistinctPercent: the proportion of the number of unique values of the field after deduplication to the number of rows in the table.
        # *   DuplicatedCount: the number of duplicated values of the field.
        # *   DuplicatedPercent: the proportion of the number of duplicated values of the field to the number of rows in the table.
        # *   TableSize: the table size.
        # *   NullValueCount: the number of rows in which the field value is null.
        # *   NullValuePercent: the proportion of the number of rows in which the field value is null to the number of rows in the table.
        # *   GroupCount: the field value and the number of rows for each field value.
        # *   CountNotIn: the number of rows in which the field values are different from the referenced values that you specified in the rule.
        # *   CountDistinctNotIn: the number of unique values that are different from the referenced values that you specified in the rule after deduplication.
        # *   UserDefinedSql: indicates that data is sampled by executing custom SQL statements.
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

class GetDataQualityRuleResponseBodyDataQualityRuleErrorHandlers(DaraModel):
    def __init__(
        self,
        error_data_filter: str = None,
        type: str = None,
    ):
        # The SQL statement that is used to filter failed tasks. If you define the rule by using custom SQL statements, you must specify an SQL statement to filter failed tasks.
        self.error_data_filter = error_data_filter
        # Processor type:
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

class GetDataQualityRuleResponseBodyDataQualityRuleCheckingConfig(DaraModel):
    def __init__(
        self,
        referenced_samples_filter: str = None,
        thresholds: main_models.GetDataQualityRuleResponseBodyDataQualityRuleCheckingConfigThresholds = None,
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
            temp_model = main_models.GetDataQualityRuleResponseBodyDataQualityRuleCheckingConfigThresholds()
            self.thresholds = temp_model.from_map(m.get('Thresholds'))

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class GetDataQualityRuleResponseBodyDataQualityRuleCheckingConfigThresholds(DaraModel):
    def __init__(
        self,
        critical: main_models.GetDataQualityRuleResponseBodyDataQualityRuleCheckingConfigThresholdsCritical = None,
        expected: main_models.GetDataQualityRuleResponseBodyDataQualityRuleCheckingConfigThresholdsExpected = None,
        warned: main_models.GetDataQualityRuleResponseBodyDataQualityRuleCheckingConfigThresholdsWarned = None,
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
            temp_model = main_models.GetDataQualityRuleResponseBodyDataQualityRuleCheckingConfigThresholdsCritical()
            self.critical = temp_model.from_map(m.get('Critical'))

        if m.get('Expected') is not None:
            temp_model = main_models.GetDataQualityRuleResponseBodyDataQualityRuleCheckingConfigThresholdsExpected()
            self.expected = temp_model.from_map(m.get('Expected'))

        if m.get('Warned') is not None:
            temp_model = main_models.GetDataQualityRuleResponseBodyDataQualityRuleCheckingConfigThresholdsWarned()
            self.warned = temp_model.from_map(m.get('Warned'))

        return self

class GetDataQualityRuleResponseBodyDataQualityRuleCheckingConfigThresholdsWarned(DaraModel):
    def __init__(
        self,
        expression: str = None,
        operator: str = None,
        value: str = None,
    ):
        # The threshold expression.
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

class GetDataQualityRuleResponseBodyDataQualityRuleCheckingConfigThresholdsExpected(DaraModel):
    def __init__(
        self,
        expression: str = None,
        operator: str = None,
        value: str = None,
    ):
        # The threshold expression.
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

class GetDataQualityRuleResponseBodyDataQualityRuleCheckingConfigThresholdsCritical(DaraModel):
    def __init__(
        self,
        expression: str = None,
        operator: str = None,
        value: str = None,
    ):
        # The threshold expression.
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

