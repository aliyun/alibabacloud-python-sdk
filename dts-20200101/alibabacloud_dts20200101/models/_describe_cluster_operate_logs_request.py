# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeClusterOperateLogsRequest(DaraModel):
    def __init__(
        self,
        account_id: str = None,
        client_token: str = None,
        dedicated_cluster_id: str = None,
        dts_job_id: str = None,
        end_time: int = None,
        owner_id: str = None,
        page_number: int = None,
        page_size: int = None,
        resource_group_id: str = None,
        start_time: int = None,
    ):
        # The ID of the Alibaba Cloud account.
        self.account_id = account_id
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. **The token can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # The ID of the DTS dedicated cluster on which a DTS task runs.
        # 
        # This parameter is required.
        self.dedicated_cluster_id = dedicated_cluster_id
        # The ID of the data migration or synchronization task.
        self.dts_job_id = dts_job_id
        # The end of the time range to query. The value must be in the UNIX timestamp format. Unit: milliseconds.
        self.end_time = end_time
        self.owner_id = owner_id
        # The number of the page to return. Specify the parameter to a positive integer that does not exceed the maximum value of the INTEGER data type. Default value: **1**.
        self.page_number = page_number
        # The number of entries to return on each page. Default value: **20**.
        self.page_size = page_size
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # The beginning of the time range to query. The value must be in the UNIX timestamp format. Unit: milliseconds. If you do not specify this parameter, the data within the last seven days is returned by default.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_id is not None:
            result['AccountId'] = self.account_id

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.dedicated_cluster_id is not None:
            result['DedicatedClusterId'] = self.dedicated_cluster_id

        if self.dts_job_id is not None:
            result['DtsJobId'] = self.dts_job_id

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.owner_id is not None:
            result['OwnerID'] = self.owner_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DedicatedClusterId') is not None:
            self.dedicated_cluster_id = m.get('DedicatedClusterId')

        if m.get('DtsJobId') is not None:
            self.dts_job_id = m.get('DtsJobId')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('OwnerID') is not None:
            self.owner_id = m.get('OwnerID')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

