# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloud_siem20241212 import models as main_models
from darabonba.model import DaraModel

class ListDataSourceTemplatesResponseBody(DaraModel):
    def __init__(
        self,
        data_source_templates: List[main_models.ListDataSourceTemplatesResponseBodyDataSourceTemplates] = None,
        page_number: str = None,
        page_size: str = None,
        request_id: str = None,
    ):
        self.data_source_templates = data_source_templates
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id

    def validate(self):
        if self.data_source_templates:
            for v1 in self.data_source_templates:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DataSourceTemplates'] = []
        if self.data_source_templates is not None:
            for k1 in self.data_source_templates:
                result['DataSourceTemplates'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_source_templates = []
        if m.get('DataSourceTemplates') is not None:
            for k1 in m.get('DataSourceTemplates'):
                temp_model = main_models.ListDataSourceTemplatesResponseBodyDataSourceTemplates()
                self.data_source_templates.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListDataSourceTemplatesResponseBodyDataSourceTemplates(DaraModel):
    def __init__(
        self,
        auto_scan_new: str = None,
        create_time: int = None,
        data_source_from: str = None,
        data_source_recognize_enabled: bool = None,
        data_source_recognizer: str = None,
        data_source_template_id: str = None,
        data_source_template_name: str = None,
        log_project_pattern: str = None,
        log_region_ids: List[str] = None,
        log_store_pattern: str = None,
        log_user_ids: List[str] = None,
        update_time: int = None,
    ):
        self.auto_scan_new = auto_scan_new
        self.create_time = create_time
        self.data_source_from = data_source_from
        self.data_source_recognize_enabled = data_source_recognize_enabled
        self.data_source_recognizer = data_source_recognizer
        self.data_source_template_id = data_source_template_id
        self.data_source_template_name = data_source_template_name
        self.log_project_pattern = log_project_pattern
        self.log_region_ids = log_region_ids
        self.log_store_pattern = log_store_pattern
        self.log_user_ids = log_user_ids
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_scan_new is not None:
            result['AutoScanNew'] = self.auto_scan_new

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.data_source_from is not None:
            result['DataSourceFrom'] = self.data_source_from

        if self.data_source_recognize_enabled is not None:
            result['DataSourceRecognizeEnabled'] = self.data_source_recognize_enabled

        if self.data_source_recognizer is not None:
            result['DataSourceRecognizer'] = self.data_source_recognizer

        if self.data_source_template_id is not None:
            result['DataSourceTemplateId'] = self.data_source_template_id

        if self.data_source_template_name is not None:
            result['DataSourceTemplateName'] = self.data_source_template_name

        if self.log_project_pattern is not None:
            result['LogProjectPattern'] = self.log_project_pattern

        if self.log_region_ids is not None:
            result['LogRegionIds'] = self.log_region_ids

        if self.log_store_pattern is not None:
            result['LogStorePattern'] = self.log_store_pattern

        if self.log_user_ids is not None:
            result['LogUserIds'] = self.log_user_ids

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoScanNew') is not None:
            self.auto_scan_new = m.get('AutoScanNew')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DataSourceFrom') is not None:
            self.data_source_from = m.get('DataSourceFrom')

        if m.get('DataSourceRecognizeEnabled') is not None:
            self.data_source_recognize_enabled = m.get('DataSourceRecognizeEnabled')

        if m.get('DataSourceRecognizer') is not None:
            self.data_source_recognizer = m.get('DataSourceRecognizer')

        if m.get('DataSourceTemplateId') is not None:
            self.data_source_template_id = m.get('DataSourceTemplateId')

        if m.get('DataSourceTemplateName') is not None:
            self.data_source_template_name = m.get('DataSourceTemplateName')

        if m.get('LogProjectPattern') is not None:
            self.log_project_pattern = m.get('LogProjectPattern')

        if m.get('LogRegionIds') is not None:
            self.log_region_ids = m.get('LogRegionIds')

        if m.get('LogStorePattern') is not None:
            self.log_store_pattern = m.get('LogStorePattern')

        if m.get('LogUserIds') is not None:
            self.log_user_ids = m.get('LogUserIds')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

