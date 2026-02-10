# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribeEmgVulItemResponseBody(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        grouped_vul_items: List[main_models.DescribeEmgVulItemResponseBodyGroupedVulItems] = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The page number of the returned page. Pages start from page **1**. Default value: **1**.
        self.current_page = current_page
        # An array that consists of the urgent vulnerabilities returned.
        self.grouped_vul_items = grouped_vul_items
        # The number of entries returned per page. Default value: **10**.
        self.page_size = page_size
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # The total number of the urgent vulnerabilities returned.
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
                temp_model = main_models.DescribeEmgVulItemResponseBodyGroupedVulItems()
                self.grouped_vul_items.append(temp_model.from_map(k1))

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeEmgVulItemResponseBodyGroupedVulItems(DaraModel):
    def __init__(
        self,
        alias_name: str = None,
        check_type: int = None,
        description: str = None,
        gmt_last_check: int = None,
        gmt_publish: int = None,
        name: str = None,
        pending_count: int = None,
        progress: int = None,
        rasp_defend: int = None,
        status: int = None,
        type: str = None,
    ):
        # The name of the urgent vulnerability.
        self.alias_name = alias_name
        # The check method.
        self.check_type = check_type
        # The introduction to the vulnerability.
        self.description = description
        # The timestamp when the urgent vulnerability was last detected. Unit: milliseconds.
        self.gmt_last_check = gmt_last_check
        # The timestamp when the urgent vulnerability was last disclosed. Unit: milliseconds.
        self.gmt_publish = gmt_publish
        # The name of the detection rule.
        self.name = name
        # The number of unhandled urgent vulnerabilities.
        self.pending_count = pending_count
        # The progress of the urgent vulnerability detection task. Valid values: 0 to 100.
        # 
        # >  This parameter is returned only when an urgent vulnerability is being detected.
        self.progress = progress
        # Indicates whether the application protection feature is supported. Valid values:
        # *   **0**: no
        # *   **1**: yes
        # >  If this parameter is not returned, the application protection is not supported.
        self.rasp_defend = rasp_defend
        # The detection status of the urgent vulnerability. Valid values:
        # 
        # *   **10**: The urgent vulnerability is not detected.
        # *   **20**: The urgent vulnerability is being detected.
        # *   **30**: The urgent vulnerability detection is complete.
        self.status = status
        # The method that is used to detect the urgent vulnerability. Valid values:
        # 
        # *   **python**: The Version method is used. Security Center checks the software versions of your server to check whether disclosed vulnerabilities exist on your server.
        # *   **scan**: The Network Scan method is used. Security Center analyzes the access traffic to your server over the Internet to check whether vulnerabilities exist on your server.
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

        if self.check_type is not None:
            result['CheckType'] = self.check_type

        if self.description is not None:
            result['Description'] = self.description

        if self.gmt_last_check is not None:
            result['GmtLastCheck'] = self.gmt_last_check

        if self.gmt_publish is not None:
            result['GmtPublish'] = self.gmt_publish

        if self.name is not None:
            result['Name'] = self.name

        if self.pending_count is not None:
            result['PendingCount'] = self.pending_count

        if self.progress is not None:
            result['Progress'] = self.progress

        if self.rasp_defend is not None:
            result['RaspDefend'] = self.rasp_defend

        if self.status is not None:
            result['Status'] = self.status

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliasName') is not None:
            self.alias_name = m.get('AliasName')

        if m.get('CheckType') is not None:
            self.check_type = m.get('CheckType')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('GmtLastCheck') is not None:
            self.gmt_last_check = m.get('GmtLastCheck')

        if m.get('GmtPublish') is not None:
            self.gmt_publish = m.get('GmtPublish')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PendingCount') is not None:
            self.pending_count = m.get('PendingCount')

        if m.get('Progress') is not None:
            self.progress = m.get('Progress')

        if m.get('RaspDefend') is not None:
            self.rasp_defend = m.get('RaspDefend')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

