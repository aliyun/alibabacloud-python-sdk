# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListCheckItemWarningSummaryRequest(DaraModel):
    def __init__(
        self,
        check_item_fuzzy: str = None,
        check_level: str = None,
        check_type: str = None,
        check_warning_status: int = None,
        check_warning_status_list: List[int] = None,
        container_field_name: str = None,
        container_field_value: str = None,
        current_page: int = None,
        group_id: int = None,
        lang: str = None,
        page_size: int = None,
        resource_directory_account_id: int = None,
        risk_type: str = None,
        source: str = None,
        start_time: int = None,
        uuid_list: List[str] = None,
    ):
        # The name of the check item. Fuzzy match is supported.
        self.check_item_fuzzy = check_item_fuzzy
        # The risk level. Default value: null, which indicates that check items at all risk levels are queried.Valid values:
        # *   **high**
        # *   **medium**
        # *   **low**
        self.check_level = check_level
        # The type of the check item.
        self.check_type = check_type
        # The risk status. Default value is null, meaning check items in all states are queried. Valid values:
        # 
        # *   **1**: failed
        # *   **3**: passed
        # *   **6**: whitelisted
        # *   **8**: fixed
        self.check_warning_status = check_warning_status
        # The list of risk levels. If the CheckWarningStatus parameter is specified, only it takes effect.
        self.check_warning_status_list = check_warning_status_list
        # The name of the field that is used to query containers.
        self.container_field_name = container_field_name
        # The value of the field that is used to query containers.
        self.container_field_value = container_field_value
        # The number of the page to return. Default value: **1**.
        self.current_page = current_page
        # The ID of the asset group.
        # 
        # > You can call the [DescribeAllGroups](~~DescribeAllGroups~~) operation to query the IDs of asset groups.
        self.group_id = group_id
        # The language of the content within the request and response. Default value: **zh**. Valid values:
        # 
        # *   **zh**: Chinese
        # *   **en**: English
        self.lang = lang
        # The number of entries to return on each page. Default value: 20. If you leave this parameter empty, 20 entries are returned on each page.
        # 
        # > We recommend that you do not leave this parameter empty.
        self.page_size = page_size
        # The Alibaba Cloud account ID of the member in the resource directory.
        # 
        # >  You can call the [DescribeMonitorAccounts](~~DescribeMonitorAccounts~~) operation to obtain the IDs.
        self.resource_directory_account_id = resource_directory_account_id
        # The type of the baseline.
        self.risk_type = risk_type
        # The data source. Default value: **default**. Valid value:
        # 
        # *   **agentless**: The check items of baselines for agentless detection.
        # *   **default**: The check items of baselines for hosts.
        self.source = source
        # Start of time range for filtering alerts, effective only for querying historically handled alerts.
        self.start_time = start_time
        # The UUIDs of the servers.
        # 
        # >  You can call the [DescribeCloudCenterInstances](https://help.aliyun.com/document_detail/141932.html) operation to query the UUIDs of the servers.
        self.uuid_list = uuid_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.check_item_fuzzy is not None:
            result['CheckItemFuzzy'] = self.check_item_fuzzy

        if self.check_level is not None:
            result['CheckLevel'] = self.check_level

        if self.check_type is not None:
            result['CheckType'] = self.check_type

        if self.check_warning_status is not None:
            result['CheckWarningStatus'] = self.check_warning_status

        if self.check_warning_status_list is not None:
            result['CheckWarningStatusList'] = self.check_warning_status_list

        if self.container_field_name is not None:
            result['ContainerFieldName'] = self.container_field_name

        if self.container_field_value is not None:
            result['ContainerFieldValue'] = self.container_field_value

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.resource_directory_account_id is not None:
            result['ResourceDirectoryAccountId'] = self.resource_directory_account_id

        if self.risk_type is not None:
            result['RiskType'] = self.risk_type

        if self.source is not None:
            result['Source'] = self.source

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.uuid_list is not None:
            result['UuidList'] = self.uuid_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckItemFuzzy') is not None:
            self.check_item_fuzzy = m.get('CheckItemFuzzy')

        if m.get('CheckLevel') is not None:
            self.check_level = m.get('CheckLevel')

        if m.get('CheckType') is not None:
            self.check_type = m.get('CheckType')

        if m.get('CheckWarningStatus') is not None:
            self.check_warning_status = m.get('CheckWarningStatus')

        if m.get('CheckWarningStatusList') is not None:
            self.check_warning_status_list = m.get('CheckWarningStatusList')

        if m.get('ContainerFieldName') is not None:
            self.container_field_name = m.get('ContainerFieldName')

        if m.get('ContainerFieldValue') is not None:
            self.container_field_value = m.get('ContainerFieldValue')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ResourceDirectoryAccountId') is not None:
            self.resource_directory_account_id = m.get('ResourceDirectoryAccountId')

        if m.get('RiskType') is not None:
            self.risk_type = m.get('RiskType')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('UuidList') is not None:
            self.uuid_list = m.get('UuidList')

        return self

