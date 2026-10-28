# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListCheckItemWarningMachineRequest(DaraModel):
    def __init__(
        self,
        check_id: int = None,
        container_field_name: str = None,
        container_field_value: str = None,
        current_page: int = None,
        group_id: int = None,
        lang: str = None,
        page_size: int = None,
        remark: str = None,
        resource_directory_account_id: int = None,
        risk_type: str = None,
        source: str = None,
        status: int = None,
        uuid_list: List[str] = None,
    ):
        # The ID of the check item.
        # 
        # This parameter is required.
        self.check_id = check_id
        # The name of the container security query parameter.
        self.container_field_name = container_field_name
        # The value of the container security query parameter.
        self.container_field_value = container_field_value
        # The page number of the page to return. Pages start from page **1**. Default value: **1**.
        self.current_page = current_page
        # The ID of the asset group to query.
        # > You can call the [DescribeAllGroups](https://help.aliyun.com/document_detail/130972.html) operation to obtain the value of this parameter.
        self.group_id = group_id
        # The language of the request and response. Default value: **zh**. Valid values:
        # 
        # - **zh**: Chinese
        # - **en**: English
        self.lang = lang
        # The maximum number of entries to display on each page during paging in a paged query. Default value: 20. If you leave the PageSize parameter empty, 20 entries are returned by default.
        # > Do not leave this parameter empty.
        self.page_size = page_size
        # The fuzzy match keyword for servers.
        self.remark = remark
        # The ID of the member accounts in the resource folder (Alibaba Cloud account).
        # > You can invoke the [DescribeMonitorAccounts](~~DescribeMonitorAccounts~~) operation to obtain this parameter.
        self.resource_directory_account_id = resource_directory_account_id
        # The category to which the check item belongs.
        self.risk_type = risk_type
        # The data source. If you leave this parameter empty, the baseline check results for servers are queried by default. Valid values:
        # - **default**: server
        # - **agentless**: agentless
        self.source = source
        # The status of the check item. Default value: null. Valid values:
        # 
        # - **1**: failed
        # - **2**: verifying
        # - **3**: passed
        # - **6**: ignored
        # - **7**: fixing
        # - **8**: fixed
        self.status = status
        # The list of server UUIDs.
        self.uuid_list = uuid_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.check_id is not None:
            result['CheckId'] = self.check_id

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

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.resource_directory_account_id is not None:
            result['ResourceDirectoryAccountId'] = self.resource_directory_account_id

        if self.risk_type is not None:
            result['RiskType'] = self.risk_type

        if self.source is not None:
            result['Source'] = self.source

        if self.status is not None:
            result['Status'] = self.status

        if self.uuid_list is not None:
            result['UuidList'] = self.uuid_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckId') is not None:
            self.check_id = m.get('CheckId')

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

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('ResourceDirectoryAccountId') is not None:
            self.resource_directory_account_id = m.get('ResourceDirectoryAccountId')

        if m.get('RiskType') is not None:
            self.risk_type = m.get('RiskType')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UuidList') is not None:
            self.uuid_list = m.get('UuidList')

        return self

