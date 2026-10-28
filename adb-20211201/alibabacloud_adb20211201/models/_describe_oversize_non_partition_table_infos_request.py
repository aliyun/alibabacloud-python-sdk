# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeOversizeNonPartitionTableInfosRequest(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        end_time: str = None,
        lang: str = None,
        order: str = None,
        owner_account: str = None,
        owner_id: int = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        start_time: str = None,
    ):
        # The cluster ID.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # The end time of the query. The time is in UTC and follows the <i>yyyy-MM-ddTHH:mm:ssZ</i> format.
        # > The end time must be later than the start time. The interval between the start time and the end time must be less than 7 days.
        self.end_time = end_time
        # The language of the title for the downloaded file and specific error messages. Valid values:
        # - **zh**: Simplified Chinese. This is the default value.
        # - **en**: English.
        # - **ja**: Japanese.
        # - **zh-tw**: Traditional Chinese.
        self.lang = lang
        # The sorting rule for a specified field. The value is a JSON array. You must specify the fields to be sorted and the sorting order in sequence. Example:
        # 
        # ```
        # [
        # 
        #     {
        # 
        #         "Field":"Name",
        # 
        #         "Type":"Asc"
        # 
        #     }
        # 
        # ]
        # ```
        # 
        # Field: the name of the field to be sorted. Only the Name field is supported.
        # Type: the sorting order. Valid values: Desc for descending order, and Asc for ascending order.
        # 
        # The values are not case-sensitive.
        self.order = order
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The page number. The value must be a positive integer. Default value: **1**.
        self.page_number = page_number
        # The number of entries per page. Valid values:
        # 
        # - 30
        # - 50
        # - 100
        # 
        # Default value: 30.
        self.page_size = page_size
        # The region ID.
        # > You can call the [DescribeRegions](https://help.aliyun.com/document_detail/143074.html) operation to query the region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The start time of the query. The time is in UTC and follows the yyyy-MM-ddTHH:mmZ format.
        # > SQL audit logs can be queried only when SQL audit is enabled. You can query SQL audit logs generated within the last 30 days. If SQL audit is disabled and then re-enabled, you can query only the SQL audit logs generated after it is re-enabled.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.order is not None:
            result['Order'] = self.order

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('Order') is not None:
            self.order = m.get('Order')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

