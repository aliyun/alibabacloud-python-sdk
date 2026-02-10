# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeEmgVulItemRequest(DaraModel):
    def __init__(
        self,
        check_type: int = None,
        current_page: int = None,
        lang: str = None,
        page_size: int = None,
        resource_directory_account_id: int = None,
        risk_status: str = None,
        scan_type: str = None,
        vul_name: str = None,
    ):
        # The check method. Valid values:
        # *   **0**: proof of concept (POC) verification
        # *   **1**: version comparison
        self.check_type = check_type
        # The number of the page to return. Default value: **1**.
        self.current_page = current_page
        # The language of the content within the request and response. Default value: **zh**. Valid values:
        # 
        # *   **zh**: Chinese
        # *   **en**: English
        self.lang = lang
        # The number of entries to return on each page. Default value: **10**.
        self.page_size = page_size
        # The Alibaba Cloud account ID of the member in the resource directory.
        # 
        # >  You can call the [DescribeMonitorAccounts](~~DescribeMonitorAccounts~~) operation to obtain the IDs.
        self.resource_directory_account_id = resource_directory_account_id
        # Specifies whether the vulnerability poses risks.\\
        # If you do not specify this parameter, all vulnerabilities are queried regardless of whether the vulnerabilities pose risks. Valid values:
        # 
        # *   **y**: yes
        # *   **n**: no
        self.risk_status = risk_status
        # The method that is used to detect the vulnerability.\\
        # If you do not specify this parameter, all vulnerabilities are queried regardless of which method is used. Valid values:
        # 
        # *   **python**: The Version method is used. Security Center checks the software versions of your server to check whether disclosed vulnerabilities exist on your server.
        # *   **scan**: The Network Scan method is used. Security Center analyzes the access traffic to your server over the Internet to check whether vulnerabilities exist on your server.
        self.scan_type = scan_type
        # The name of the urgent vulnerability.
        self.vul_name = vul_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.check_type is not None:
            result['CheckType'] = self.check_type

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.resource_directory_account_id is not None:
            result['ResourceDirectoryAccountId'] = self.resource_directory_account_id

        if self.risk_status is not None:
            result['RiskStatus'] = self.risk_status

        if self.scan_type is not None:
            result['ScanType'] = self.scan_type

        if self.vul_name is not None:
            result['VulName'] = self.vul_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckType') is not None:
            self.check_type = m.get('CheckType')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ResourceDirectoryAccountId') is not None:
            self.resource_directory_account_id = m.get('ResourceDirectoryAccountId')

        if m.get('RiskStatus') is not None:
            self.risk_status = m.get('RiskStatus')

        if m.get('ScanType') is not None:
            self.scan_type = m.get('ScanType')

        if m.get('VulName') is not None:
            self.vul_name = m.get('VulName')

        return self

