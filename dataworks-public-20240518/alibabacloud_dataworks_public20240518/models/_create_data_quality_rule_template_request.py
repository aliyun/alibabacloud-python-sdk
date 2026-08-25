# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class CreateDataQualityRuleTemplateRequest(DaraModel):
    def __init__(
        self,
        checking_config: main_models.CreateDataQualityRuleTemplateRequestCheckingConfig = None,
        directory_path: str = None,
        name: str = None,
        project_id: int = None,
        sampling_config: main_models.CreateDataQualityRuleTemplateRequestSamplingConfig = None,
        visible_scope: str = None,
    ):
        # The sample verification settings.
        self.checking_config = checking_config
        # The directory path where the custom template is stored. Levels are separated by forward slashes (/). Each level name can be up to 1024 characters in length and cannot contain whitespace characters or forward slashes.
        self.directory_path = directory_path
        # The name of the rule template. The name can contain digits, letters, Chinese characters, and half-width or full-width punctuation marks. The name can be up to 512 characters in length.
        # 
        # This parameter is required.
        self.name = name
        # The DataWorks workspace ID.
        # 
        # This parameter is required.
        self.project_id = project_id
        # The settings required for sample collection.
        self.sampling_config = sampling_config
        # The visibility scope of the template. Valid values:
        # 
        # - Tenant: available to the entire tenant.
        # - Project: available only in the current project.
        self.visible_scope = visible_scope

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

        if self.directory_path is not None:
            result['DirectoryPath'] = self.directory_path

        if self.name is not None:
            result['Name'] = self.name

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.sampling_config is not None:
            result['SamplingConfig'] = self.sampling_config.to_map()

        if self.visible_scope is not None:
            result['VisibleScope'] = self.visible_scope

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckingConfig') is not None:
            temp_model = main_models.CreateDataQualityRuleTemplateRequestCheckingConfig()
            self.checking_config = temp_model.from_map(m.get('CheckingConfig'))

        if m.get('DirectoryPath') is not None:
            self.directory_path = m.get('DirectoryPath')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('SamplingConfig') is not None:
            temp_model = main_models.CreateDataQualityRuleTemplateRequestSamplingConfig()
            self.sampling_config = temp_model.from_map(m.get('SamplingConfig'))

        if m.get('VisibleScope') is not None:
            self.visible_scope = m.get('VisibleScope')

        return self

class CreateDataQualityRuleTemplateRequestSamplingConfig(DaraModel):
    def __init__(
        self,
        metric: str = None,
        metric_parameters: str = None,
        setting_config: str = None,
    ):
        # The name of the sampling metric. Valid values:
        # 
        # - Count: the number of table rows.
        # - Min: the minimum value of a field.
        # - Max: the maximum value of a field.
        # - Avg: the average value of a field.
        # - DistinctCount: the number of distinct values in a field.
        # - DistinctPercent: the ratio of distinct values to the total number of rows.
        # - DuplicatedCount: the number of duplicate values in a field.
        # - DuplicatedPercent: the ratio of duplicate values to the total number of rows.
        # - TableSize: the table size.
        # - NullValueCount: the number of rows where the field value is null.
        # - NullValuePercent: the ratio of rows where the field value is null.
        # - GroupCount: the count of rows for each value after aggregation by field value.
        # - CountNotIn: the number of rows that do not match the enumerated values.
        # - CountDistinctNotIn: the number of distinct values that do not match the enumerated values.
        # - UserDefinedSql: sample collection through a custom SQL statement.
        self.metric = metric
        # The parameters required for sample collection.
        self.metric_parameters = metric_parameters
        # The runtime parameter setting statements to execute before the sampling statement. The value can be up to 1000 characters in length. Currently, only MaxCompute is supported.
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

class CreateDataQualityRuleTemplateRequestCheckingConfig(DaraModel):
    def __init__(
        self,
        referenced_samples_filter: str = None,
        type: str = None,
    ):
        # An expression that specifies how to query reference samples. Some threshold types require querying reference samples and then aggregating their values to derive the threshold for comparison.
        self.referenced_samples_filter = referenced_samples_filter
        # The threshold calculation method. Valid values:
        # 
        # - Fixed
        # - Fluctation
        # - FluctationDiscreate
        # - Auto
        # - Average
        # - Variance
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

