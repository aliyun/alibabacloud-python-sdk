# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeCheckWarningsRequest(DaraModel):
    def __init__(
        self,
        check_id: int = None,
        check_type: str = None,
        container_name: str = None,
        current_page: int = None,
        lang: str = None,
        page_size: int = None,
        resource_directory_account_id: int = None,
        risk_id: int = None,
        risk_status: int = None,
        source_ip: str = None,
        uuid: str = None,
    ):
        # The ID of the check item.
        self.check_id = check_id
        # The type of the check item. Valid values:
        # 
        # *   **hc.check.type.identity_auth**: identity authentication
        # *   **hc.check.type.access_control**: access control
        # *   **hc.check.type.network_service**: network and service
        # *   **hc.check.type.service_conf**: service configuration
        # *   **hc.check.type.file_rights**: file permission
        # *   **hc.check.type.security_audit**: security audit
        # *   **hc.check.type.attack_defense**: intrusion prevention
        # *   **hc.check.type.others**: others
        self.check_type = check_type
        # The name of the container.
        self.container_name = container_name
        # The number of the page to return. Default value: **1**.
        self.current_page = current_page
        # The language of the content within the request and response. Default value: **zh**. Valid values:
        # 
        # *   **zh**: Chinese
        # *   **en**: English
        self.lang = lang
        # The number of entries to return on each page. Default value: **20**.
        self.page_size = page_size
        # The Alibaba Cloud account ID of the member in the resource directory.
        # 
        # >  To obtain the Alibaba Cloud account ID, call the [DescribeMonitorAccounts](~~DescribeMonitorAccounts~~) operation.
        self.resource_directory_account_id = resource_directory_account_id
        # The ID of the risk item. This parameter is required.
        # 
        # >  To query the information about the risk items and check items of a server, you must specify the IDs of the risk items. You can call the [DescribeCheckWarningSummary](~~DescribeCheckWarningSummary~~) operation to query the IDs of risk items.
        self.risk_id = risk_id
        # The status of the check item. Valid values:
        # 
        # *   **1**: failed
        # *   **2**: verifying
        # *   **3**: passed
        # *   **5**: expired
        # *   **6**: ignored
        self.risk_status = risk_status
        # The source IP address of the request.
        self.source_ip = source_ip
        # The UUID of the server on which the baseline check is performed.
        # 
        # > To query specified risk items and the check items of a specified server, you must provide the ID of the server on which the baseline check is performed. You can call the [DescribeWarningMachines](~~DescribeWarningMachines~~) operation to query the IDs of servers.
        # 
        # This parameter is required.
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.check_id is not None:
            result['CheckId'] = self.check_id

        if self.check_type is not None:
            result['CheckType'] = self.check_type

        if self.container_name is not None:
            result['ContainerName'] = self.container_name

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.resource_directory_account_id is not None:
            result['ResourceDirectoryAccountId'] = self.resource_directory_account_id

        if self.risk_id is not None:
            result['RiskId'] = self.risk_id

        if self.risk_status is not None:
            result['RiskStatus'] = self.risk_status

        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckId') is not None:
            self.check_id = m.get('CheckId')

        if m.get('CheckType') is not None:
            self.check_type = m.get('CheckType')

        if m.get('ContainerName') is not None:
            self.container_name = m.get('ContainerName')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ResourceDirectoryAccountId') is not None:
            self.resource_directory_account_id = m.get('ResourceDirectoryAccountId')

        if m.get('RiskId') is not None:
            self.risk_id = m.get('RiskId')

        if m.get('RiskStatus') is not None:
            self.risk_status = m.get('RiskStatus')

        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        return self

