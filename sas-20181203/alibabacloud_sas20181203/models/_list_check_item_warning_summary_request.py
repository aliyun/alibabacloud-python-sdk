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
        # The fuzzy match for the check item name.
        self.check_item_fuzzy = check_item_fuzzy
        # The risk level. Default value: null, which indicates that all levels are queried. Valid values:
        # - **high**: High.
        # - **medium**: Medium.
        # - **low**: Low.
        self.check_level = check_level
        # The check item category name.
        self.check_type = check_type
        # The risk status. Default value: null, which indicates that all statuses are queried. Valid values:
        # - **1**: Failed.
        # - **3**: Passed.
        # - **6**: Whitelisted.
        # - **8**: Fixed.
        self.check_warning_status = check_warning_status
        # The list of risk statuses. If both this parameter and CheckWarningStatus are specified, only CheckWarningStatus takes effect.
        self.check_warning_status_list = check_warning_status_list
        # The container security query parameter name.
        self.container_field_name = container_field_name
        # The container security query parameter value.
        self.container_field_value = container_field_value
        # The page number of the page to return. Default value: **1**, which indicates that query results are displayed starting from page 1.
        self.current_page = current_page
        # The ID of the asset group to query.
        # > You can call the [DescribeAllGroups](~~DescribeAllGroups~~) operation to obtain this parameter.
        self.group_id = group_id
        # The language of the content within the request and response. Default value: **zh**. Valid values:
        # - **zh**: Chinese.
        # - **en**: English.
        self.lang = lang
        # The maximum number of entries per page when paging. Default value: 20. If the PageSize parameter is left empty, 20 entries are returned per page.
        # > Do not leave PageSize empty.
        self.page_size = page_size
        # The ID of the member accounts in the resource directory (Alibaba Cloud account).
        # > You can call the [DescribeMonitorAccounts](~~DescribeMonitorAccounts~~) operation to obtain this parameter.
        self.resource_directory_account_id = resource_directory_account_id
        # The baseline category name.
        self.risk_type = risk_type
        # The data source. Default value: **default**. Valid values:
        # - **agentless**: agentless detection.
        # - **default**: host baseline.
        self.source = source
        # The start time for filtering alerts. This parameter takes effect only when you query historical processed alerts. Specify a UNIX timestamp in milliseconds.
        self.start_time = start_time
        # The list of server UUIDs to query.
        # > You can call the [DescribeCloudCenterInstances](https://help.aliyun.com/document_detail/141932.html) operation to obtain the UUID of a server.
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

