# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeCloudCenterInstancesRequest(DaraModel):
    def __init__(
        self,
        criteria: str = None,
        current_page: int = None,
        flags: str = None,
        importance: int = None,
        lang: str = None,
        logical_exp: str = None,
        machine_types: str = None,
        next_token: str = None,
        no_group_trace: bool = None,
        page_size: int = None,
        region_id: str = None,
        resource_directory_account_id: int = None,
        use_next_token: bool = None,
    ):
        # The search conditions for assets. This parameter is in JSON format. Pay attention to the case sensitivity when you specify this parameter.
        # > You can search for assets by conditions such as instance ID, instance name, VPC ID, region, and public IP address. You can call the [DescribeCriteria](~~DescribeCriteria~~) operation to query the supported search conditions.
        self.criteria = criteria
        # The page number of the page to return. Default value: **1**.
        self.current_page = current_page
        # The asset provider. Separate multiple asset providers with commas (,). Valid values:
        # 
        # - **0**: Alibaba Cloud asset
        # - **1**: non-Alibaba Cloud asset
        # - **2**: IDC asset
        # - **3**, **4**, **5**, **7**, **14**, and **16**: asset on other cloud platforms
        # - **8**: lightweight asset
        # - **9**: SAE
        # - **10**: PAI
        self.flags = flags
        # The importance of the asset. Valid values:
        # - **2**: important asset
        # - **1**: general asset
        # - **0**: test asset
        self.importance = importance
        # The language of the request and response. Default value: **zh**. Valid values:
        # 
        # - **zh**: Chinese
        # - **en**: English
        self.lang = lang
        # The logical relationship between multiple search conditions. Default value: **OR**. Valid values:
        # 
        # - **OR**: The logical relationship between multiple search conditions is **OR**.
        # - **AND**: The logical relationship between multiple search conditions is **AND**.
        self.logical_exp = logical_exp
        # The type of the asset to query. Valid values:
        # 
        # - **ecs**: server
        # - **cloud_product**: cloud service
        # - **eci**: elastic container instance
        # - **rund**: RunD container instance
        # - **runc**: RunC container instance
        self.machine_types = machine_types
        # The NextToken value returned when the NextToken method is used. Leave this parameter empty for the first query.
        self.next_token = next_token
        # Specifies whether to internationalize the default group **Ungrouped**. Default value: **false**. Valid values:
        # 
        # - **true**: does not internationalize the default group. If the value of the GroupTrace response parameter is the default group **Ungrouped** in Security Center, **Ungrouped** is still displayed as **Ungrouped**.
        # - **false**: internationalizes the default group. If the value of the GroupTrace response parameter is the default group **Ungrouped** in Security Center, **Ungrouped** is displayed as **default**.
        self.no_group_trace = no_group_trace
        # The number of Asset entries to display on each page when you configure paging for a paged query through Settings. Default value: **20**, which indicates that 20 pieces of Asset information are displayed on each page.
        self.page_size = page_size
        # The ID of the region where the instance resides.
        self.region_id = region_id
        # The ID of the Alibaba Cloud account to which the member accounts in the resource folder belong.
        # > You can invoke the [DescribeMonitorAccounts](~~DescribeMonitorAccounts~~) operation to obtain this parameter.
        self.resource_directory_account_id = resource_directory_account_id
        # Specifies whether to use the NextToken method to pull asset list data. If you use this parameter, TotalCount is not returned. Valid values:
        # 
        # - **true**: uses the NextToken method.
        # - **false**: does not use the NextToken method.
        self.use_next_token = use_next_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.criteria is not None:
            result['Criteria'] = self.criteria

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.flags is not None:
            result['Flags'] = self.flags

        if self.importance is not None:
            result['Importance'] = self.importance

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.logical_exp is not None:
            result['LogicalExp'] = self.logical_exp

        if self.machine_types is not None:
            result['MachineTypes'] = self.machine_types

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.no_group_trace is not None:
            result['NoGroupTrace'] = self.no_group_trace

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_directory_account_id is not None:
            result['ResourceDirectoryAccountId'] = self.resource_directory_account_id

        if self.use_next_token is not None:
            result['UseNextToken'] = self.use_next_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Criteria') is not None:
            self.criteria = m.get('Criteria')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('Flags') is not None:
            self.flags = m.get('Flags')

        if m.get('Importance') is not None:
            self.importance = m.get('Importance')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('LogicalExp') is not None:
            self.logical_exp = m.get('LogicalExp')

        if m.get('MachineTypes') is not None:
            self.machine_types = m.get('MachineTypes')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('NoGroupTrace') is not None:
            self.no_group_trace = m.get('NoGroupTrace')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceDirectoryAccountId') is not None:
            self.resource_directory_account_id = m.get('ResourceDirectoryAccountId')

        if m.get('UseNextToken') is not None:
            self.use_next_token = m.get('UseNextToken')

        return self

