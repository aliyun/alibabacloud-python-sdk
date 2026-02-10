# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeCheckWarningMachinesRequest(DaraModel):
    def __init__(
        self,
        check_id: int = None,
        current_page: int = None,
        filter_uuid: str = None,
        instance_id: str = None,
        lang: str = None,
        page_size: int = None,
        remark: str = None,
        resource_directory_account_id: int = None,
        risk_id: int = None,
        status: int = None,
    ):
        # The ID of the check item.
        # 
        # > You can call the [DescribeCheckWarningSummary](~~DescribeCheckWarningSummary~~) operation to query the IDs of check items.
        self.check_id = check_id
        # The number of the page to return. Default value: **1**.
        self.current_page = current_page
        # The instance ID of the asset that you don\\"t want to query.
        self.filter_uuid = filter_uuid
        # The instance ID of the asset.
        self.instance_id = instance_id
        # The language of the content within the request and response. Default value: **zh**. Valid values:
        # 
        # *   **zh**: Chinese
        # *   **en**: English
        self.lang = lang
        # The number of entries to return on each page.
        self.page_size = page_size
        # The information about the server that you want to query. The value can be the name or the public IP address of the server.
        self.remark = remark
        # The Alibaba Cloud account ID of the member in the resource directory.
        # 
        # >  You can call the [DescribeMonitorAccounts](~~DescribeMonitorAccounts~~) operation to obtain the IDs.
        self.resource_directory_account_id = resource_directory_account_id
        # The ID of the baseline.
        # 
        # > You can call the [DescribeCheckWarningSummary](~~DescribeCheckWarningSummary~~) operation to query the IDs of baselines.
        self.risk_id = risk_id
        # The risk status of the check item. Valid values:
        # 
        # *   **1**: failed
        # *   **3**: passed
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.check_id is not None:
            result['CheckId'] = self.check_id

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.filter_uuid is not None:
            result['FilterUuid'] = self.filter_uuid

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.resource_directory_account_id is not None:
            result['ResourceDirectoryAccountId'] = self.resource_directory_account_id

        if self.risk_id is not None:
            result['RiskId'] = self.risk_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckId') is not None:
            self.check_id = m.get('CheckId')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('FilterUuid') is not None:
            self.filter_uuid = m.get('FilterUuid')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('ResourceDirectoryAccountId') is not None:
            self.resource_directory_account_id = m.get('ResourceDirectoryAccountId')

        if m.get('RiskId') is not None:
            self.risk_id = m.get('RiskId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

