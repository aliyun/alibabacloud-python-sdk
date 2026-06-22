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
        # The check type. Valid values:
        # 
        # - **0**: POC verification
        # - **1**: version comparison.
        self.check_type = check_type
        # The page number of the first page to return. Default value: **1**, which indicates that query results are displayed starting from page 1.
        self.current_page = current_page
        # The language type for the request and response messages. Default value: **zh**. Valid values:
        # - **zh**: Chinese
        # - **en**: English.
        self.lang = lang
        # The number of entries per page in a paged query. Default value: **10**, which indicates that 10 emergency vulnerability entries are displayed per page. Maximum value: 50.
        self.page_size = page_size
        # The ID of the member accounts in the resource directory (Alibaba Cloud account).
        # > Invoke the [DescribeMonitorAccounts](~~DescribeMonitorAccounts~~) operation to obtain this parameter.
        self.resource_directory_account_id = resource_directory_account_id
        # The risk status of the vulnerabilities to query. If this parameter is not specified, vulnerabilities of all risk statuses are returned, including those with risks and those without risks. Valid values:
        # - **y**: at risk
        # - **n**: not at risk.
        self.risk_status = risk_status
        # The detection method of the vulnerabilities to query. If this parameter is not specified, vulnerabilities detected by all methods are returned by default, including version detection and network scanning. Valid values:
        # - **python**: version detection (server software version detection). Detects whether your server has disclosed software vulnerabilities.
        # - **scan**: network scanning (network traffic detection). Detects whether your public assets (Internet-accessible servers) have vulnerabilities.
        self.scan_type = scan_type
        # The name of the emergency vulnerability to query.
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

