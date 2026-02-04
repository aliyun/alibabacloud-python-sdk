# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateDataSourceTemplateShrinkRequest(DaraModel):
    def __init__(
        self,
        auto_scan_new: str = None,
        data_source_recognize_enabled: bool = None,
        data_source_template_id: str = None,
        data_source_template_name: str = None,
        lang: str = None,
        log_project_pattern: str = None,
        log_region_ids: str = None,
        log_store_pattern: str = None,
        log_user_ids_shrink: str = None,
        region_id: str = None,
        role_for: int = None,
    ):
        self.auto_scan_new = auto_scan_new
        self.data_source_recognize_enabled = data_source_recognize_enabled
        self.data_source_template_id = data_source_template_id
        self.data_source_template_name = data_source_template_name
        self.lang = lang
        self.log_project_pattern = log_project_pattern
        self.log_region_ids = log_region_ids
        self.log_store_pattern = log_store_pattern
        self.log_user_ids_shrink = log_user_ids_shrink
        self.region_id = region_id
        self.role_for = role_for

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_scan_new is not None:
            result['AutoScanNew'] = self.auto_scan_new

        if self.data_source_recognize_enabled is not None:
            result['DataSourceRecognizeEnabled'] = self.data_source_recognize_enabled

        if self.data_source_template_id is not None:
            result['DataSourceTemplateId'] = self.data_source_template_id

        if self.data_source_template_name is not None:
            result['DataSourceTemplateName'] = self.data_source_template_name

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.log_project_pattern is not None:
            result['LogProjectPattern'] = self.log_project_pattern

        if self.log_region_ids is not None:
            result['LogRegionIds'] = self.log_region_ids

        if self.log_store_pattern is not None:
            result['LogStorePattern'] = self.log_store_pattern

        if self.log_user_ids_shrink is not None:
            result['LogUserIds'] = self.log_user_ids_shrink

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.role_for is not None:
            result['RoleFor'] = self.role_for

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoScanNew') is not None:
            self.auto_scan_new = m.get('AutoScanNew')

        if m.get('DataSourceRecognizeEnabled') is not None:
            self.data_source_recognize_enabled = m.get('DataSourceRecognizeEnabled')

        if m.get('DataSourceTemplateId') is not None:
            self.data_source_template_id = m.get('DataSourceTemplateId')

        if m.get('DataSourceTemplateName') is not None:
            self.data_source_template_name = m.get('DataSourceTemplateName')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('LogProjectPattern') is not None:
            self.log_project_pattern = m.get('LogProjectPattern')

        if m.get('LogRegionIds') is not None:
            self.log_region_ids = m.get('LogRegionIds')

        if m.get('LogStorePattern') is not None:
            self.log_store_pattern = m.get('LogStorePattern')

        if m.get('LogUserIds') is not None:
            self.log_user_ids_shrink = m.get('LogUserIds')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')

        return self

