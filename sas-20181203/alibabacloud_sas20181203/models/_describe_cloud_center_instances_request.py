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
        # The search conditions. The value of this parameter is in the JSON format and is case-sensitive.
        # 
        # >  You can search for an asset by using the search conditions, such as the instance ID, instance name, VPC ID, region, or public IP address. You can call the [DescribeCriteria](https://help.aliyun.com/document_detail/149773.html) operation to query the supported search conditions.
        self.criteria = criteria
        # The number of the page to return. Default value: **1**.
        self.current_page = current_page
        # Asset vendor. Multiple asset vendors should be separated by a comma (,). Values:
        # - **0**: an asset provided by Alibaba Cloud
        # - **1**: an asset outside Alibaba Cloud
        # - **2**: an asset in a data center
        # - **3**, **4**, **5**, **7**, **14**, **16**: an asset from a third-party cloud service provider
        # - **8**: a lightweight asset
        # - **9**: a Serverless App Engine (SAE) instance
        # - **10**: an instance in Platform for AI (PAI)
        self.flags = flags
        # The importance of the asset. Valid values:
        # 
        # *   **2**: an important asset
        # *   **1**: a common asset
        # *   **0**: a test asset
        self.importance = importance
        # The language of the content within the request and response. Default value: **zh**. Valid values:
        # 
        # *   **zh**: Chinese
        # *   **en**: English
        self.lang = lang
        # The logical relationship among multiple search conditions. Valid values:
        # 
        # *   **OR**: The logical relationship among search conditions is **OR**.
        # *   **AND**: The logical relationship among search conditions is **AND**.
        self.logical_exp = logical_exp
        # The type of asset to be queried. Values:
        # - **ecs**: Server 
        # - **cloud_product**: Cloud Product 
        # - **eci**: Elastic Container Instance 
        # - **rund**: RunD Container Instance 
        # - **runc**: RunC Container Instance
        self.machine_types = machine_types
        # The value of NextToken that is returned when the NextToken method is used. You do not need to specify this parameter for the first request.
        self.next_token = next_token
        # Specifies whether to internationalize the name of the default group. Valid values:
        # 
        # *   **true**: The system returns the Chinese name of the default group for the GroupTrace response parameter.
        # *   **false**: The system returns default for the GroupTrace response parameter.
        self.no_group_trace = no_group_trace
        # The number of entries to return on each page. Default value: **20**.
        self.page_size = page_size
        # The ID of the region in which the asset resides.
        self.region_id = region_id
        # The Alibaba Cloud account ID of the member in the resource directory.
        # 
        # >  You can call the [DescribeMonitorAccounts](~~DescribeMonitorAccounts~~) operation to obtain the IDs.
        self.resource_directory_account_id = resource_directory_account_id
        # Specifies whether to use the NextToken method to retrieve a new page of results. If you set UseNextToken to true, the value of TotalCount is not returned. Valid values:
        # 
        # - **true**: The NextToken method is used.
        # - **false**: The NextToken method is not used.
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

