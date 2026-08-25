# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class ListDataQualityRuleTemplatesResponseBody(DaraModel):
    def __init__(
        self,
        paging_info: main_models.ListDataQualityRuleTemplatesResponseBodyPagingInfo = None,
        request_id: str = None,
    ):
        # The paging result of the data quality rule template paged query.
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
            temp_model = main_models.ListDataQualityRuleTemplatesResponseBodyPagingInfo()
            self.paging_info = temp_model.from_map(m.get('PagingInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListDataQualityRuleTemplatesResponseBodyPagingInfo(DaraModel):
    def __init__(
        self,
        data_quality_rule_templates: List[main_models.ListDataQualityRuleTemplatesResponseBodyPagingInfoDataQualityRuleTemplates] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The list of rule templates.
        self.data_quality_rule_templates = data_quality_rule_templates
        # The page number.
        self.page_number = page_number
        # The page size.
        self.page_size = page_size
        # The total number of entries.
        self.total_count = total_count

    def validate(self):
        if self.data_quality_rule_templates:
            for v1 in self.data_quality_rule_templates:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DataQualityRuleTemplates'] = []
        if self.data_quality_rule_templates is not None:
            for k1 in self.data_quality_rule_templates:
                result['DataQualityRuleTemplates'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_quality_rule_templates = []
        if m.get('DataQualityRuleTemplates') is not None:
            for k1 in m.get('DataQualityRuleTemplates'):
                temp_model = main_models.ListDataQualityRuleTemplatesResponseBodyPagingInfoDataQualityRuleTemplates()
                self.data_quality_rule_templates.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListDataQualityRuleTemplatesResponseBodyPagingInfoDataQualityRuleTemplates(DaraModel):
    def __init__(
        self,
        checking_config: main_models.ListDataQualityRuleTemplatesResponseBodyPagingInfoDataQualityRuleTemplatesCheckingConfig = None,
        code: str = None,
        directory_path: str = None,
        name: str = None,
        project_id: int = None,
        sampling_config: main_models.ListDataQualityRuleTemplatesResponseBodyPagingInfoDataQualityRuleTemplatesSamplingConfig = None,
        visible_scope: str = None,
    ):
        # The sample verification settings.
        self.checking_config = checking_config
        # The code of the rule template.
        self.code = code
        # The category directory where the custom template is stored. Levels are separated by forward slashes. Each level name can be up to 1024 characters in length and cannot contain whitespace characters or forward slashes.
        self.directory_path = directory_path
        # The name of the rule template. The name can contain digits, letters, Chinese characters, and half-width or full-width punctuation marks. The name can be up to 512 characters in length.
        self.name = name
        # The DataWorks workspace ID.
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
            temp_model = main_models.ListDataQualityRuleTemplatesResponseBodyPagingInfoDataQualityRuleTemplatesCheckingConfig()
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
            temp_model = main_models.ListDataQualityRuleTemplatesResponseBodyPagingInfoDataQualityRuleTemplatesSamplingConfig()
            self.sampling_config = temp_model.from_map(m.get('SamplingConfig'))

        if m.get('VisibleScope') is not None:
            self.visible_scope = m.get('VisibleScope')

        return self

class ListDataQualityRuleTemplatesResponseBodyPagingInfoDataQualityRuleTemplatesSamplingConfig(DaraModel):
    def __init__(
        self,
        metric: str = None,
        metric_parameters: str = None,
        setting_config: str = None,
    ):
        # The metric name for sampling. Valid values:
        # 
        # - Count: table row count.
        # - Min: minimum value of the field.
        # - Max: maximum value of the field.
        # - Avg: average value of the field.
        # - DistinctCount: number of unique values in the field.
        # - DistinctPercent: ratio of unique values to total rows.
        # - DuplicatedCount: number of duplicate values in the field.
        # - DuplicatedPercent: ratio of duplicate values to total rows.
        # - TableSize: table size.
        # - NullValueCount: number of rows where the field is null.
        # - NullValuePercent: ratio of rows where the field is null.
        # - GroupCount: row count for each value after aggregation by field value.
        # - CountNotIn: number of rows with non-matching enumeration values.
        # - CountDistinctNotIn: number of unique values with non-matching enumeration values.
        # - UserDefinedSql: sample collection through custom SQL.
        self.metric = metric
        # The parameters required for sample collection.
        self.metric_parameters = metric_parameters
        # The runtime parameter setting statements that are executed before the sampling statement. The value can be up to 1000 characters in length. Currently, only MaxCompute is supported.
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

class ListDataQualityRuleTemplatesResponseBodyPagingInfoDataQualityRuleTemplatesCheckingConfig(DaraModel):
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

