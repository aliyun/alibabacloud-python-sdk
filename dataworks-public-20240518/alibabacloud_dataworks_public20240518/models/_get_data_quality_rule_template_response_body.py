# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class GetDataQualityRuleTemplateResponseBody(DaraModel):
    def __init__(
        self,
        data_quality_rule_template: main_models.GetDataQualityRuleTemplateResponseBodyDataQualityRuleTemplate = None,
        request_id: str = None,
    ):
        # The details of the rule template.
        self.data_quality_rule_template = data_quality_rule_template
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data_quality_rule_template:
            self.data_quality_rule_template.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_quality_rule_template is not None:
            result['DataQualityRuleTemplate'] = self.data_quality_rule_template.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataQualityRuleTemplate') is not None:
            temp_model = main_models.GetDataQualityRuleTemplateResponseBodyDataQualityRuleTemplate()
            self.data_quality_rule_template = temp_model.from_map(m.get('DataQualityRuleTemplate'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetDataQualityRuleTemplateResponseBodyDataQualityRuleTemplate(DaraModel):
    def __init__(
        self,
        checking_config: main_models.GetDataQualityRuleTemplateResponseBodyDataQualityRuleTemplateCheckingConfig = None,
        code: str = None,
        directory_path: str = None,
        name: str = None,
        project_id: int = None,
        sampling_config: main_models.GetDataQualityRuleTemplateResponseBodyDataQualityRuleTemplateSamplingConfig = None,
        visible_scope: str = None,
    ):
        # The sample verification settings.
        self.checking_config = checking_config
        # The code of the rule template.
        self.code = code
        # The category directory in which the custom template is stored. Levels are separated by forward slashes (/). Each level name can be a maximum of 1,024 characters in length and cannot contain whitespace characters or forward slashes (/).
        self.directory_path = directory_path
        # The name of the rule template. The name can be a combination of digits, letters, Chinese characters, and half-width or full-width punctuation marks. The name can be a maximum of 512 characters in length.
        self.name = name
        # The ID of the DataWorks workspace.
        self.project_id = project_id
        # The settings required for sample collection.
        self.sampling_config = sampling_config
        # The scope in which the template is available:
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

        if self.visible_scope is not None:
            result['VisibleScope'] = self.visible_scope

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckingConfig') is not None:
            temp_model = main_models.GetDataQualityRuleTemplateResponseBodyDataQualityRuleTemplateCheckingConfig()
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
            temp_model = main_models.GetDataQualityRuleTemplateResponseBodyDataQualityRuleTemplateSamplingConfig()
            self.sampling_config = temp_model.from_map(m.get('SamplingConfig'))

        if m.get('VisibleScope') is not None:
            self.visible_scope = m.get('VisibleScope')

        return self

class GetDataQualityRuleTemplateResponseBodyDataQualityRuleTemplateSamplingConfig(DaraModel):
    def __init__(
        self,
        metric: str = None,
        metric_parameters: str = None,
        setting_config: str = None,
    ):
        # The name of the metric to be sampled:
        # - Count: the number of rows in the table.
        # - Min: the minimum value of the field.
        # - Max: the maximum value of the field.
        # - Avg: the average value of the field.
        # - DistinctCount: the number of distinct values of the field.
        # - DistinctPercent: the ratio of the number of distinct values of the field to the number of data rows.
        # - DuplicatedCount: the number of duplicate values of the field.
        # - DuplicatedPercent: the ratio of the number of duplicate values of the field to the number of data rows.
        # - TableSize: the size of the table.
        # - NullValueCount: the number of rows in which the field is null.
        # - NullValuePercent: the percentage of rows in which the field is null.
        # - GroupCount: the number of data rows corresponding to each value after aggregation by field value.
        # - CountNotIn: the number of rows whose enumerated values do not match.
        # - CountDistinctNotIn: the number of distinct values whose enumerated values do not match.
        # - UserDefinedSql: collects samples by using a custom SQL statement.
        self.metric = metric
        # The parameters required for sample collection.
        self.metric_parameters = metric_parameters
        # The runtime parameter setting statements that are inserted and executed before the specific sampling statement is executed. The setting can be a maximum of 1,000 characters in length. Only MaxCompute is supported.
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

class GetDataQualityRuleTemplateResponseBodyDataQualityRuleTemplateCheckingConfig(DaraModel):
    def __init__(
        self,
        referenced_samples_filter: str = None,
        type: str = None,
    ):
        # Some types of thresholds require you to query reference samples and aggregate the values of the reference samples to obtain the threshold for comparison. An expression is used to indicate the query method of reference samples.
        self.referenced_samples_filter = referenced_samples_filter
        # The threshold calculation method:
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

