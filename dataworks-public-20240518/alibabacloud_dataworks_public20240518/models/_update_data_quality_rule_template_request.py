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
        # The settings for sample validation.
        self.checking_config = checking_config
        # The code of the rule template.
        # 
        # This parameter is required.
        self.code = code
        # The category directory in which the custom template is stored. Levels are separated by forward slashes (/). The name of each level can be up to 1024 characters in length and cannot contain whitespace characters or forward slashes (/).
        self.directory_path = directory_path
        # The name of the rule template. The name can contain digits, letters, Chinese characters, and half-width and full-width punctuation marks. The name can be up to 512 characters in length.
        self.name = name
        # The ID of the DataWorks workspace. You can log on to the [DataWorks console](https://workbench.data.aliyun.com/console) and go to the Workspace Management page to obtain the ID.
        # 
        # This parameter specifies the DataWorks workspace used for this API call.
        # 
        # This parameter is required.
        self.project_id = project_id
        # The settings required for sample collection.
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
        # The name of the metric to be sampled. Valid values:
        # - Count: the number of table rows.
        # - Min: the minimum value of a field.
        # - Max: the maximum value of a field.
        # - Avg: the average value of a field.
        # - DistinctCount: the number of distinct values of a field.
        # - DistinctPercent: the ratio of the number of distinct values of a field to the number of data rows.
        # - DuplicatedCount: the number of duplicate values of a field.
        # - DuplicatedPercent: the ratio of the number of duplicate values of a field to the number of data rows.
        # - TableSize: the size of the table.
        # - NullValueCount: the number of rows in which the field is null.
        # - NullValuePercent: the percentage of rows in which the field is null.
        # - GroupCount: the number of data rows corresponding to each value after the field values are aggregated.
        # - CountNotIn: the number of rows whose values do not match the enumerated values.
        # - CountDistinctNotIn: the number of distinct values that do not match the enumerated values.
        # - UserDefinedSql: sample collection by using custom SQL.
        self.metric = metric
        # The parameters required for sample collection.
        self.metric_parameters = metric_parameters
        # The runtime parameter setting statements that are inserted and executed before the sampling statements are executed. The statements can be up to 1,000 characters in length. Only MaxCompute is supported.
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
        # For some types of thresholds, you must query reference samples and then aggregate the values of the reference samples to obtain the threshold used for comparison. An expression is used here to indicate the query method of reference samples.
        self.referenced_samples_filter = referenced_samples_filter
        # The type of the monitored object. Valid values:
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

