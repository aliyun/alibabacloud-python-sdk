# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class UpdateDataSourceTemplateRequest(DaraModel):
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
        log_user_ids: List[str] = None,
        region_id: str = None,
        role_for: int = None,
    ):
        # Specifies whether to automatically discover new users.
        # 
        # - enabled: Enabled.
        # 
        # - disabled: Disabled.
        self.auto_scan_new = auto_scan_new
        # Specifies whether to automatically discover new data sources.
        self.data_source_recognize_enabled = data_source_recognize_enabled
        # The ID of the data source template.
        self.data_source_template_id = data_source_template_id
        # The name of the data source template.
        self.data_source_template_name = data_source_template_name
        # The language of the response message. Valid values:
        # 
        # - **zh** (default): Chinese.
        # 
        # - **en**: English.
        self.lang = lang
        # The matching rule for the names of Simple Log Service projects.
        self.log_project_pattern = log_project_pattern
        # The list of IDs of log storage regions.
        self.log_region_ids = log_region_ids
        # The matching rule for the names of Simple Log Service Logstores.
        self.log_store_pattern = log_store_pattern
        # The list of user IDs for batch data access.
        self.log_user_ids = log_user_ids
        # The region where the Management Hub of threat analysis is located. Select a region based on the region where your assets are located. Valid values:
        # 
        # - cn-hangzhou: Assets are in the Chinese mainland.
        # 
        # - ap-southeast-1: Assets are outside the Chinese mainland.
        self.region_id = region_id
        # The user ID of the member. This parameter lets an administrator switch to the perspective of the member.
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

        if self.log_user_ids is not None:
            result['LogUserIds'] = self.log_user_ids

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
            self.log_user_ids = m.get('LogUserIds')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')

        return self

