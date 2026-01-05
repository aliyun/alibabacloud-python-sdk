# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class UpdateDataQualityRuleTemplateRequest(DaraModel):
    def __init__(
        self,
        checking_config: main_models.UpdateDataQualityRuleTemplateRequestCheckingConfig = None,
        code: str = None,
        directory_path: str = None,
        name: str = None,
        project_id: int = None,
        sampling_config: main_models.UpdateDataQualityRuleTemplateRequestSamplingConfig = None,
    ):
        # The check settings for sample data.
        self.checking_config = checking_config
        # The code for the template.
        # 
        # This parameter is required.
        self.code = code
        # The directory in which the template is stored. Slashes (/) are used to separate directory levels. The name of each directory level can be up to 1,024 characters in length. It cannot contain whitespace characters or slashes (/).
        self.directory_path = directory_path
        # The name of the template. The name can be up to 512 characters in length and can contain digits, letters, and punctuation marks.
        self.name = name
        # This parameter is required.
        self.project_id = project_id
        # The sampling settings.
        self.sampling_config = sampling_config

    def validate(self):
        if self.checking_config:
            self.checking_config.validate()
        if self.sampling_config:
            self.sampling_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.checking_config is not None:
            result['CheckingConfig'] = self.checking_config.to_map()

        if self.code is not None:
            result['Code'] = self.code

        if self.directory_path is not None:
            result['DirectoryPath'] = self.directory_path

        if self.name is not None:
            result['Name'] = self.name

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.sampling_config is not None:
            result['SamplingConfig'] = self.sampling_config.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckingConfig') is not None:
            temp_model = main_models.UpdateDataQualityRuleTemplateRequestCheckingConfig()
            self.checking_config = temp_model.from_map(m.get('CheckingConfig'))

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('DirectoryPath') is not None:
            self.directory_path = m.get('DirectoryPath')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('SamplingConfig') is not None:
            temp_model = main_models.UpdateDataQualityRuleTemplateRequestSamplingConfig()
            self.sampling_config = temp_model.from_map(m.get('SamplingConfig'))

        return self

class UpdateDataQualityRuleTemplateRequestSamplingConfig(DaraModel):
    def __init__(
        self,
        metric: str = None,
        metric_parameters: str = None,
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

        if self.setting_config is not None:
            result['SettingConfig'] = self.setting_config

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Metric') is not None:
            self.metric = m.get('Metric')

        if m.get('MetricParameters') is not None:
            self.metric_parameters = m.get('MetricParameters')

        if m.get('SettingConfig') is not None:
            self.setting_config = m.get('SettingConfig')

        return self

class UpdateDataQualityRuleTemplateRequestCheckingConfig(DaraModel):
    def __init__(
        self,
        referenced_samples_filter: str = None,
        type: str = None,
    ):
        # The method that is used to query the referenced samples. To obtain some types of thresholds, you need to query reference samples and perform aggregate operations on the reference values. In this example, an expression is used to specify the query method of referenced samples.
        self.referenced_samples_filter = referenced_samples_filter
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
        if self.referenced_samples_filter is not None:
            result['ReferencedSamplesFilter'] = self.referenced_samples_filter

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ReferencedSamplesFilter') is not None:
            self.referenced_samples_filter = m.get('ReferencedSamplesFilter')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

