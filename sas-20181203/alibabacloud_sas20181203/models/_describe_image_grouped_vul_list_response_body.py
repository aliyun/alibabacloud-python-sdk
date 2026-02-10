# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribeImageGroupedVulListResponseBody(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        grouped_vul_items: List[main_models.DescribeImageGroupedVulListResponseBodyGroupedVulItems] = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The page number of the returned page.
        self.current_page = current_page
        # An array that consists of the image vulnerabilities.
        self.grouped_vul_items = grouped_vul_items
        # The number of entries returned per page. Default value: **20**.
        self.page_size = page_size
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # The total number of image system vulnerabilities.
        self.total_count = total_count

    def validate(self):
        if self.grouped_vul_items:
            for v1 in self.grouped_vul_items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        result['GroupedVulItems'] = []
        if self.grouped_vul_items is not None:
            for k1 in self.grouped_vul_items:
                result['GroupedVulItems'].append(k1.to_map() if k1 else None)

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        self.grouped_vul_items = []
        if m.get('GroupedVulItems') is not None:
            for k1 in m.get('GroupedVulItems'):
                temp_model = main_models.DescribeImageGroupedVulListResponseBodyGroupedVulItems()
                self.grouped_vul_items.append(temp_model.from_map(k1))

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeImageGroupedVulListResponseBodyGroupedVulItems(DaraModel):
    def __init__(
        self,
        alias_name: str = None,
        asap_count: int = None,
        can_fix: str = None,
        gmt_last: int = None,
        last_scan_time: int = None,
        later_count: int = None,
        name: str = None,
        nntf_count: int = None,
        rule_tag: str = None,
        status: int = None,
        tags: str = None,
        type: str = None,
    ):
        # The alias of the vulnerability.
        self.alias_name = alias_name
        # The number of vulnerabilities that have the high priority.
        self.asap_count = asap_count
        # Indicates whether the vulnerability can be fixed in the Security Center console. Valid values:
        # 
        # *   **yes**
        # *   **no**
        self.can_fix = can_fix
        # The timestamp when the first scan was performed. Unit: milliseconds.
        self.gmt_last = gmt_last
        # The timestamp when the last scan was performed. Unit: milliseconds.
        self.last_scan_time = last_scan_time
        # The number of vulnerabilities that have the medium priority.
        self.later_count = later_count
        # The name of the vulnerability.
        self.name = name
        # The number of vulnerabilities that have the low priority.
        self.nntf_count = nntf_count
        # The tag of this vulnerability. Valid values:
        # 
        # *   **AI**: AI-related components.
        self.rule_tag = rule_tag
        # The status of the vulnerability. Valid values:
        # 
        # *   **0**: unhandled
        # *   **1**: handled
        # *   **2**: verifying
        # *   **3**: added to the whitelist
        self.status = status
        # The tag of the vulnerability. Valid values:
        # 
        # *   Restart required
        # *   Remote exploitation
        # *   Exploit exists
        # *   Exploitable
        # *   Privilege escalation
        # *   Code execution
        self.tags = tags
        # The type of the vulnerability. Valid values:
        # 
        # *   **cve**: image system vulnerability
        # *   **sca**: image application vulnerability
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alias_name is not None:
            result['AliasName'] = self.alias_name

        if self.asap_count is not None:
            result['AsapCount'] = self.asap_count

        if self.can_fix is not None:
            result['CanFix'] = self.can_fix

        if self.gmt_last is not None:
            result['GmtLast'] = self.gmt_last

        if self.last_scan_time is not None:
            result['LastScanTime'] = self.last_scan_time

        if self.later_count is not None:
            result['LaterCount'] = self.later_count

        if self.name is not None:
            result['Name'] = self.name

        if self.nntf_count is not None:
            result['NntfCount'] = self.nntf_count

        if self.rule_tag is not None:
            result['RuleTag'] = self.rule_tag

        if self.status is not None:
            result['Status'] = self.status

        if self.tags is not None:
            result['Tags'] = self.tags

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliasName') is not None:
            self.alias_name = m.get('AliasName')

        if m.get('AsapCount') is not None:
            self.asap_count = m.get('AsapCount')

        if m.get('CanFix') is not None:
            self.can_fix = m.get('CanFix')

        if m.get('GmtLast') is not None:
            self.gmt_last = m.get('GmtLast')

        if m.get('LastScanTime') is not None:
            self.last_scan_time = m.get('LastScanTime')

        if m.get('LaterCount') is not None:
            self.later_count = m.get('LaterCount')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NntfCount') is not None:
            self.nntf_count = m.get('NntfCount')

        if m.get('RuleTag') is not None:
            self.rule_tag = m.get('RuleTag')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

