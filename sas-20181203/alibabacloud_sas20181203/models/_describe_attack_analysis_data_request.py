# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeAttackAnalysisDataRequest(DaraModel):
    def __init__(
        self,
        base_64: str = None,
        current_page: int = None,
        data: str = None,
        end_time: int = None,
        lang: str = None,
        page_size: int = None,
        start_time: int = None,
        type: str = None,
    ):
        # Specifies whether to encode the value of the **client_url** field in the query results by using the Base64 algorithm. Valid values:
        # 
        # *   **true**: yes
        # *   **false**: no
        self.base_64 = base_64
        # The number of the page to return. Pages start from page **1**.
        # 
        # >  If the Type parameter is set to **DETAILS**, you must specify the CurrentPage parameter.
        self.current_page = current_page
        # The condition that is used to filter attack events.
        # 
        # >  The following list describes the valid values of crack_type:
        # 
        # *   3: brute-force attack on MySQL
        # 
        # *   4: FTP brute-force attack
        # 
        # *   5: SSH brute-force attack
        # 
        # *   6: RDP brute-force attack
        # 
        # *   9: brute-force attack on Microsoft SQL Server
        # 
        # *   101: intercepted attack on Java Struts 2
        # 
        # *   102: intercepted attack on Redis
        # 
        # *   103: communication with AntSword Webshell
        # 
        # *   104: communication with China Chopper Webshell
        # 
        # *   133: communication with XISE Webshell
        # 
        # *   sqli: SQL injection
        # 
        # *   codei: code execution
        # 
        # *   xss: cross-site scripting (XSS)
        # 
        # *   lfi: local file inclusion
        # 
        # *   rfi: remote file inclusion
        # 
        # *   webshell: trojan script
        # 
        # *   upload: vulnerability upload
        # 
        # *   path: directory traversal
        # 
        # *   bypass: unauthorized access
        # 
        # *   csrf: cross-site request forgery (CSRF)
        # 
        # *   crlf: carriage return line feed (CRLF)
        # 
        # *   other: others
        self.data = data
        # The timestamp when the attack stops. Unit: seconds.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The language of the content within the request and response. Default value: **zh**. Valid values:
        # 
        # *   **zh**: Chinese
        # *   **en**: English
        self.lang = lang
        # The number of entries to return on each page.
        # 
        # >  If the Type parameter is set to **DETAILS**, you must specify the PageSize parameter.
        self.page_size = page_size
        # The timestamp at which the attack starts. By default, the statistics of the previous seven days are queried. Unit: seconds.
        # 
        # >  The start time that you specify must be within the previous 40 days.
        # 
        # This parameter is required.
        self.start_time = start_time
        # The details of attack analysis. Valid values:
        # 
        # *   **TOTAL**: number of attacks
        # *   **TREND**: attack trend
        # *   **PIE_CHART**: distribution of attacks by type
        # *   **SOURCE_TOP**: top 5 attack sources
        # *   **CLIENT_TOP**: top 5 attacked assets
        # *   **DETAILS**: attack details
        # 
        # >  If the Type parameter is set to **DETAILS**, you must specify the CurrentPage and PageSize parameters.
        # 
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.base_64 is not None:
            result['Base64'] = self.base_64

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.data is not None:
            result['Data'] = self.data

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Base64') is not None:
            self.base_64 = m.get('Base64')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('Data') is not None:
            self.data = m.get('Data')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

