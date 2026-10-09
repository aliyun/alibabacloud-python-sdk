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
        # The search criteria for assets. This parameter is in JSON format. Pay attention to case sensitivity when entering parameter values.
        # > You can search for assets by instance ID, instance name, VPC ID, region, public IP address, and other criteria. Call [DescribeCriteria](~~DescribeCriteria~~) to query the supported search criteria.
        self.criteria = criteria
        # The page number from which to start displaying query results. Default value: **1**. This means results are displayed starting from page 1.
        self.current_page = current_page
        # The asset vendor. Separate multiple vendors with commas (,). Valid values:
        # 
        # - **0**: Alibaba Cloud asset
        # - **1**: off-cloud asset
        # - **2**: IDC asset
        # - **3**, **4**, **5**, **7**, **14**, **16**: assets from other cloud vendors
        # - **8**: lightweight asset
        # - **9**: SAE
        # - **10**: PAI
        self.flags = flags
        # The importance level of the asset. Valid values:
        # - **2**: important asset
        # - **1**: general asset
        # - **0**: test asset
        self.importance = importance
        # The language of the request and response messages. Default value: **zh**. Valid values:
        # 
        # - **zh**: Chinese
        # - **en**: English
        self.lang = lang
        # The logical relationship between multiple search criteria. Default value: **OR**. Valid values:
        # 
        # - **OR**: The multiple search criteria have an OR relationship.
        # - **AND**: The multiple search criteria have an AND relationship.
        self.logical_exp = logical_exp
        # The type of assets to query. Valid values:
        # 
        # - **ecs**: server
        # - **cloud_product**: cloud product
        # - **eci**: Elastic Container Instance
        # - **rund**: RunD container instance
        # - **runc**: RunC container instance
        self.machine_types = machine_types
        # The NextToken value returned when using the NextToken method. Leave this parameter empty for the first request.
        self.next_token = next_token
        # Specifies whether to apply internationalization to the default group **Ungrouped**. Default value: **false**. Valid values:
        # 
        # - **true**: Internationalization is not applied. When the GroupTrace parameter returns the Security Center default group **Ungrouped**, it is still displayed as **Ungrouped**.
        # - **false**: Internationalization is applied. When the GroupTrace parameter returns the Security Center default group **Ungrouped**, it is displayed as **default**.
        self.no_group_trace = no_group_trace
        # The number of assets to display per page in a paged query. Settings take effect per page. Default value: **20**. This means 20 assets are displayed per page.
        self.page_size = page_size
        # The ID of the region where the instance to query resides.
        self.region_id = region_id
        # The primary account ID of the resource directory member accounts.
        # > Call [DescribeMonitorAccounts](~~DescribeMonitorAccounts~~) to obtain this parameter.
        self.resource_directory_account_id = resource_directory_account_id
        # Specifies whether to use the NextToken method to retrieve the asset list. If this parameter is set to true, TotalCount is no longer returned. Valid values:
        # 
        # - **true**: Use the NextToken method.
        # - **false**: Do not use the NextToken method.
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

