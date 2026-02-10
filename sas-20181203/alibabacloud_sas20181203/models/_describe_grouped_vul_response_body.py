# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribeGroupedVulResponseBody(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        grouped_vul_items: List[main_models.DescribeGroupedVulResponseBodyGroupedVulItems] = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The page number.
        self.current_page = current_page
        # The information about the vulnerability.
        self.grouped_vul_items = grouped_vul_items
        # The number of entries per page. Default value: 10.
        self.page_size = page_size
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # The total number of entries returned.
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
                temp_model = main_models.DescribeGroupedVulResponseBodyGroupedVulItems()
                self.grouped_vul_items.append(temp_model.from_map(k1))

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeGroupedVulResponseBodyGroupedVulItems(DaraModel):
    def __init__(
        self,
        alias_name: str = None,
        asap_count: int = None,
        gmt_first: int = None,
        gmt_last: int = None,
        handled_count: int = None,
        language_type: str = None,
        later_count: int = None,
        name: str = None,
        nntf_count: int = None,
        rasp_defend: int = None,
        related: str = None,
        tags: str = None,
        total_fix_count: int = None,
        type: str = None,
    ):
        # The alias of the vulnerability.
        self.alias_name = alias_name
        # The number of vulnerabilities that have the **high** priority.
        self.asap_count = asap_count
        # The timestamp when the vulnerability was first detected. Unit: milliseconds.
        self.gmt_first = gmt_first
        # The timestamp when the vulnerability was last detected. Unit: milliseconds.
        self.gmt_last = gmt_last
        # The number of handled vulnerabilities.
        self.handled_count = handled_count
        # The language type associated with the vulnerability. Valid values:
        # 
        # *   **java**
        # *   **php**
        # 
        # >  This parameter is valid only for a vulnerability of the sca type.
        self.language_type = language_type
        # The number of vulnerabilities that have the **medium** priority.
        self.later_count = later_count
        # The name of the vulnerability.
        self.name = name
        # The number of vulnerabilities that have the **low** priority.
        self.nntf_count = nntf_count
        # Indicates whether the application protection feature is supported. Valid values:
        # 
        # *   **0**: not supported
        # *   **1**: supported
        # 
        # >  If this parameter is not returned, the application protection feature is not supported.
        self.rasp_defend = rasp_defend
        # The IDs of the common vulnerabilities and exposures (CVEs) that are related to the vulnerability.
        self.related = related
        # The tag of the vulnerability. Valid values:
        # 
        # *   **Restart required**
        # *   **Remote utilization**
        # *   **EXP exists**
        # *   **Available**
        # *   **Elevation of Privilege**
        # *   **Code Execution**
        self.tags = tags
        # The total number of fixed vulnerabilities.
        self.total_fix_count = total_fix_count
        # The type of the vulnerability. Valid values:
        # 
        # *   **cve**: Linux software vulnerability
        # *   **sys**: Windows system vulnerability
        # *   **cms**: Web-CMS vulnerability
        # *   **app**: application vulnerability
        # *   **emg**: urgent vulnerability
        # *   **sca**: vulnerability that is detected by software component analysis
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

        if self.gmt_first is not None:
            result['GmtFirst'] = self.gmt_first

        if self.gmt_last is not None:
            result['GmtLast'] = self.gmt_last

        if self.handled_count is not None:
            result['HandledCount'] = self.handled_count

        if self.language_type is not None:
            result['LanguageType'] = self.language_type

        if self.later_count is not None:
            result['LaterCount'] = self.later_count

        if self.name is not None:
            result['Name'] = self.name

        if self.nntf_count is not None:
            result['NntfCount'] = self.nntf_count

        if self.rasp_defend is not None:
            result['RaspDefend'] = self.rasp_defend

        if self.related is not None:
            result['Related'] = self.related

        if self.tags is not None:
            result['Tags'] = self.tags

        if self.total_fix_count is not None:
            result['TotalFixCount'] = self.total_fix_count

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliasName') is not None:
            self.alias_name = m.get('AliasName')

        if m.get('AsapCount') is not None:
            self.asap_count = m.get('AsapCount')

        if m.get('GmtFirst') is not None:
            self.gmt_first = m.get('GmtFirst')

        if m.get('GmtLast') is not None:
            self.gmt_last = m.get('GmtLast')

        if m.get('HandledCount') is not None:
            self.handled_count = m.get('HandledCount')

        if m.get('LanguageType') is not None:
            self.language_type = m.get('LanguageType')

        if m.get('LaterCount') is not None:
            self.later_count = m.get('LaterCount')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NntfCount') is not None:
            self.nntf_count = m.get('NntfCount')

        if m.get('RaspDefend') is not None:
            self.rasp_defend = m.get('RaspDefend')

        if m.get('Related') is not None:
            self.related = m.get('Related')

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        if m.get('TotalFixCount') is not None:
            self.total_fix_count = m.get('TotalFixCount')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

