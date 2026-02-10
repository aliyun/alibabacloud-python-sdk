# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeAttackAnalysisDataResponseBody(DaraModel):
    def __init__(
        self,
        data: str = None,
        page: int = None,
        page_size: int = None,
        request_id: str = None,
        total: int = None,
    ):
        # The attack events. Valid values:
        # 
        # *   **client_url**: the URL of the attack request.
        # 
        # *   **internetIp**: the IP address of the asset.
        # 
        # *   **instanceName**: the name of the asset.
        # 
        # *   **table_src**: the data source.
        # 
        # *   **uuid**: the UUID of the asset.
        # 
        # *   **crack_method**: the method of the attack request.
        # 
        # *   **crack_hour**: the attack time.
        # 
        # *   **crack_src_ip**: the IP address from which the attack is launched.
        # 
        # *   **instanceId**: the ID of the asset.
        # 
        # *   **dst_port**: the attacked port.
        # 
        # *   **client_ip**: the attacked IP address.
        # 
        # *   **location**: the region from which the attack is launched.
        # 
        # *   **aliuid**: the ID of the Alibaba Cloud account.
        # 
        # *   **crack_cnt**: the number of times that the attack is launched.
        # 
        # *   **crack_type**: the type of the attack. Valid values:
        # 
        #     *   **113**: improper authorization.
        #     *   **112**: redirection attack.
        #     *   **upload**: vulnerability upload.
        #     *   **other**: others.
        #     *   **webshell**: trojan script.
        #     *   **201**: suspicious connection.
        #     *   **9**: brute-force attack on Microsoft SQL Server.
        #     *   **5**: SSH brute-force attack.
        #     *   **6**: RDP brute-force attack.
        #     *   **lfi**: local file inclusion.
        #     *   **7**: code execution.
        #     *   **sqli**: SQL injection.
        #     *   **209**: web attack.
        #     *   **31**: buffer overflow.
        #     *   **3**: brute-force attack on MySQL.
        #     *   **30**: clickjacking.
        #     *   **4**: FTP brute-force attack.
        #     *   **bypass**: unauthorized access.
        #     *   **33**: format string.
        #     *   **deeplearning**: others.
        #     *   **32**: integer overflow.
        #     *   **203**: brute-force attack.
        #     *   **34**: race condition.
        #     *   **rfi**: remote file inclusion.
        #     *   **0**: SQL injection attack.
        #     *   **212**: mining behavior.
        #     *   **213**: reverse shell.
        #     *   **211**: worm.
        #     *   **61**: session timeout.
        #     *   **20**: directory traversal.
        #     *   **xss**: XSS attack.
        #     *   **22**: unauthorized access.
        #     *   **21**: scan attack.
        #     *   **24**: file modification.
        #     *   **26**: file deletion.
        #     *   **25**: file reading.
        #     *   **28**: CRLF injection.
        #     *   **27**: logic error.
        #     *   **29**: template injection.
        #     *   **csrf**: CSRF.
        #     *   **path**: directory traversal.
        #     *   **crlf**: CRLF.
        #     *   **102**: CSRF.
        #     *   **103**: server-side request forgery (SSRF).
        #     *   **101**: XSS.
        #     *   **11**: file inclusion.
        #     *   **10**: file upload.
        #     *   **12**: vulnerability upload.
        #     *   **15**: unauthorized access.
        #     *   **14**: information leakage.
        #     *   **17**: XML entity injection.
        #     *   **16**: insecure configuration.
        #     *   **19**: Lightweight Directory Access Protocol (LDAP) injection.
        #     *   **18**: XPath injection.
        #     *   **codei**: code execution.
        #     *   **ai_webshell**: intelligent defense against webshell upload.
        #     *   **alinet_webrce**: adaptive web attack defense.
        #     *   **210**: JSP webshell upload.
        #     *   **161**: webshell upload.
        self.data = data
        # The page number of the returned page.
        self.page = page
        # The number of entries returned per page. Default value: 10.
        self.page_size = page_size
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # The total number of attack events returned.
        self.total = total

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data

        if self.page is not None:
            result['Page'] = self.page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')

        if m.get('Page') is not None:
            self.page = m.get('Page')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

