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
        # The templates.
        self.data_quality_rule_templates = data_quality_rule_templates
        # Page number
        self.page_number = page_number
        # Page size
        self.page_size = page_size
        # Total number of entries
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
        # Sample verification settings
        self.checking_config = checking_config
        # Rule template Code
        self.code = code
        # The directory in which the template is stored. Slashes (/) are used to separate directory levels. The name of each directory level can be up to 1,024 characters in length. It cannot contain whitespace characters or slashes (/).
        self.directory_path = directory_path
        # The name of the template. The name can be up to 512 characters in length and can contain digits, letters, and punctuation marks.
        self.name = name
        # DataWorks workspace ID
        self.project_id = project_id
        # Settings required for sample collection
        self.sampling_config = sampling_config
        # Available range of templates:
        # - Tenant: all tenants are available
        # - Project: only available in the current Project
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
        # The name of the sampled metric.
        # - Count: number of table rows
        # - Min: minimum value of the field
        # - Max: The maximum value of the field.
        # - Avg: field mean
        # - DistinctCount: number of unique field values
        # - DistinctPercent: the ratio of the number of unique field values to the number of data rows.
        # - DuplicatedCount: number of duplicate field values
        # - DuplicatedPercent: the ratio of the number of duplicate field values to the number of data rows.
        # - TableSize: table size
        # - NullValueCount: number of rows with empty fields
        # - NullValuePercent: the proportion of fields that are empty.
        # - GroupCount: aggregate each value by field value and the corresponding number of data rows
        # - CountNotIn: the enumerated value does not match the number of rows.
        # - CountDistinctNotIn: the number of unique values that the enumerated values do not match.
        # - UserDefinedSql: use custom SQL to collect samples
        self.metric = metric
        # Parameters required for sample collection
        self.metric_parameters = metric_parameters
        # Before executing the sample statement, insert some runtime parameter setting statements, which can be up to 1000 characters in length. Currently, only MaxCompute are supported.
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
        # Some types of thresholds need to query some reference samples, and then summarize the values of the reference samples to obtain the threshold for comparison. Here, an expression is used to represent the query method of the reference samples.
        self.referenced_samples_filter = referenced_samples_filter
        # Threshold Calculation method
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

