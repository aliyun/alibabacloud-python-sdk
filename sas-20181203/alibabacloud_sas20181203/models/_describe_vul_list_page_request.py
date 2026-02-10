# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeVulListPageRequest(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        cve_id: str = None,
        page_size: int = None,
        rasp_defend: int = None,
        vul_name_like: str = None,
        vul_type: str = None,
    ):
        # The number of the page to return.
        self.current_page = current_page
        # The Common Vulnerabilities and Exposures (CVE) ID of the vulnerability.
        self.cve_id = cve_id
        # The number of entries to return on each page.
        self.page_size = page_size
        # Indicates whether the application protection feature is supported. Valid values:
        # 
        # - **0**: no.
        # 
        # - **1**: yes.
        self.rasp_defend = rasp_defend
        # The name of the vulnerability.
        self.vul_name_like = vul_name_like
        # The type of the vulnerabilities. Valid values:
        # 
        # *   **cve**: Linux software vulnerability.
        # *   **sys**: Windows system vulnerability.
        # *   **app**: Application vulnerability that is detected by using web scanner.
        self.vul_type = vul_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.cve_id is not None:
            result['CveId'] = self.cve_id

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.rasp_defend is not None:
            result['RaspDefend'] = self.rasp_defend

        if self.vul_name_like is not None:
            result['VulNameLike'] = self.vul_name_like

        if self.vul_type is not None:
            result['VulType'] = self.vul_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('CveId') is not None:
            self.cve_id = m.get('CveId')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RaspDefend') is not None:
            self.rasp_defend = m.get('RaspDefend')

        if m.get('VulNameLike') is not None:
            self.vul_name_like = m.get('VulNameLike')

        if m.get('VulType') is not None:
            self.vul_type = m.get('VulType')

        return self

