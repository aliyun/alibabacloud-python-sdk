# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeOssObjectsRequest(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        file_category_code: int = None,
        instance_id: str = None,
        lang: str = None,
        last_scan_time_end: int = None,
        last_scan_time_start: int = None,
        marker: int = None,
        name: str = None,
        page_size: int = None,
        risk_level_id: int = None,
        rule_id: int = None,
        service_region_id: str = None,
        template_id: int = None,
    ):
        # The page number of the page to return.
        self.current_page = current_page
        # The code of the file type.
        self.file_category_code = file_category_code
        # The ID of the instance to which the OSS object belongs.
        # 
        # > You can call the **DescribeInstances** operation to query the instance ID.
        self.instance_id = instance_id
        # The language of the content within the request and response. Valid values:
        # 
        # *   **zh**: Chinese
        # *   **en**: English
        self.lang = lang
        # The end time of the last scan. The value is a UNIX timestamp. Unit: milliseconds.
        self.last_scan_time_end = last_scan_time_end
        # The start time of the last scan. The value is a UNIX timestamp. Unit: milliseconds.
        self.last_scan_time_start = last_scan_time_start
        # When you query data by page, use the `Marker` parameter to query the data that follows the `Marker` value.
        self.marker = marker
        # The search keyword. Fuzzy match is supported.
        self.name = name
        # The number of entries to return on each page.
        self.page_size = page_size
        # The sensitivity level of the OSS object. Valid values:
        # 
        # *   **1**: N/A, which indicates that no sensitive data is detected.
        # *   **2**: S1, which indicates the low sensitivity level.
        # *   **3**: S2, which indicates the medium sensitivity level.
        # *   **4**: S3, which indicates the high sensitivity level.
        # *   **5**: S4, which indicates the highest sensitivity level.
        self.risk_level_id = risk_level_id
        # The ID of the sensitive data detection rule that the OSS object hits.
        # 
        # > You can call the **DescribeRules** operation to query the ID of the sensitive data detection rule.
        self.rule_id = rule_id
        # The region in which the data asset resides.
        self.service_region_id = service_region_id
        # The ID of the industry-specific rule template.
        self.template_id = template_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.file_category_code is not None:
            result['FileCategoryCode'] = self.file_category_code

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.last_scan_time_end is not None:
            result['LastScanTimeEnd'] = self.last_scan_time_end

        if self.last_scan_time_start is not None:
            result['LastScanTimeStart'] = self.last_scan_time_start

        if self.marker is not None:
            result['Marker'] = self.marker

        if self.name is not None:
            result['Name'] = self.name

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.risk_level_id is not None:
            result['RiskLevelId'] = self.risk_level_id

        if self.rule_id is not None:
            result['RuleId'] = self.rule_id

        if self.service_region_id is not None:
            result['ServiceRegionId'] = self.service_region_id

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('FileCategoryCode') is not None:
            self.file_category_code = m.get('FileCategoryCode')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('LastScanTimeEnd') is not None:
            self.last_scan_time_end = m.get('LastScanTimeEnd')

        if m.get('LastScanTimeStart') is not None:
            self.last_scan_time_start = m.get('LastScanTimeStart')

        if m.get('Marker') is not None:
            self.marker = m.get('Marker')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RiskLevelId') is not None:
            self.risk_level_id = m.get('RiskLevelId')

        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')

        if m.get('ServiceRegionId') is not None:
            self.service_region_id = m.get('ServiceRegionId')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        return self

