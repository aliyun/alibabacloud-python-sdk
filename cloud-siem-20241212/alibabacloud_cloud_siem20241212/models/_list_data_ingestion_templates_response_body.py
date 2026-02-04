# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloud_siem20241212 import models as main_models
from darabonba.model import DaraModel

class ListDataIngestionTemplatesResponseBody(DaraModel):
    def __init__(
        self,
        data_ingestion_templates: List[main_models.ListDataIngestionTemplatesResponseBodyDataIngestionTemplates] = None,
        page_number: str = None,
        page_size: str = None,
        request_id: str = None,
    ):
        self.data_ingestion_templates = data_ingestion_templates
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id

    def validate(self):
        if self.data_ingestion_templates:
            for v1 in self.data_ingestion_templates:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DataIngestionTemplates'] = []
        if self.data_ingestion_templates is not None:
            for k1 in self.data_ingestion_templates:
                result['DataIngestionTemplates'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_ingestion_templates = []
        if m.get('DataIngestionTemplates') is not None:
            for k1 in m.get('DataIngestionTemplates'):
                temp_model = main_models.ListDataIngestionTemplatesResponseBodyDataIngestionTemplates()
                self.data_ingestion_templates.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListDataIngestionTemplatesResponseBodyDataIngestionTemplates(DaraModel):
    def __init__(
        self,
        capacity_count: str = None,
        create_time: int = None,
        data_ingestion_mode: str = None,
        data_ingestion_status: str = None,
        data_ingestion_template_id: str = None,
        data_ingestion_template_name: str = None,
        data_ingestion_template_status: str = None,
        data_source_template_id: str = None,
        normalization_rule_id: str = None,
        normalization_rule_name: str = None,
        update_time: int = None,
    ):
        self.capacity_count = capacity_count
        self.create_time = create_time
        self.data_ingestion_mode = data_ingestion_mode
        self.data_ingestion_status = data_ingestion_status
        self.data_ingestion_template_id = data_ingestion_template_id
        self.data_ingestion_template_name = data_ingestion_template_name
        self.data_ingestion_template_status = data_ingestion_template_status
        self.data_source_template_id = data_source_template_id
        self.normalization_rule_id = normalization_rule_id
        self.normalization_rule_name = normalization_rule_name
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.capacity_count is not None:
            result['CapacityCount'] = self.capacity_count

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.data_ingestion_mode is not None:
            result['DataIngestionMode'] = self.data_ingestion_mode

        if self.data_ingestion_status is not None:
            result['DataIngestionStatus'] = self.data_ingestion_status

        if self.data_ingestion_template_id is not None:
            result['DataIngestionTemplateId'] = self.data_ingestion_template_id

        if self.data_ingestion_template_name is not None:
            result['DataIngestionTemplateName'] = self.data_ingestion_template_name

        if self.data_ingestion_template_status is not None:
            result['DataIngestionTemplateStatus'] = self.data_ingestion_template_status

        if self.data_source_template_id is not None:
            result['DataSourceTemplateId'] = self.data_source_template_id

        if self.normalization_rule_id is not None:
            result['NormalizationRuleId'] = self.normalization_rule_id

        if self.normalization_rule_name is not None:
            result['NormalizationRuleName'] = self.normalization_rule_name

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CapacityCount') is not None:
            self.capacity_count = m.get('CapacityCount')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DataIngestionMode') is not None:
            self.data_ingestion_mode = m.get('DataIngestionMode')

        if m.get('DataIngestionStatus') is not None:
            self.data_ingestion_status = m.get('DataIngestionStatus')

        if m.get('DataIngestionTemplateId') is not None:
            self.data_ingestion_template_id = m.get('DataIngestionTemplateId')

        if m.get('DataIngestionTemplateName') is not None:
            self.data_ingestion_template_name = m.get('DataIngestionTemplateName')

        if m.get('DataIngestionTemplateStatus') is not None:
            self.data_ingestion_template_status = m.get('DataIngestionTemplateStatus')

        if m.get('DataSourceTemplateId') is not None:
            self.data_source_template_id = m.get('DataSourceTemplateId')

        if m.get('NormalizationRuleId') is not None:
            self.normalization_rule_id = m.get('NormalizationRuleId')

        if m.get('NormalizationRuleName') is not None:
            self.normalization_rule_name = m.get('NormalizationRuleName')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

