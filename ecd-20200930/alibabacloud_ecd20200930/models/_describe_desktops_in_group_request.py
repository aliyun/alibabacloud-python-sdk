# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDesktopsInGroupRequest(DaraModel):
    def __init__(
        self,
        custom_end_time_period: int = None,
        custom_start_time_period: int = None,
        desktop_group_id: str = None,
        ignore_deleted: bool = None,
        max_results: int = None,
        next_token: str = None,
        pay_type: str = None,
        region_id: str = None,
    ):
        self.custom_end_time_period = custom_end_time_period
        self.custom_start_time_period = custom_start_time_period
        # The ID of the cloud computer share.
        # 
        # This parameter is required.
        self.desktop_group_id = desktop_group_id
        # Specifies whether to ignore deletion flags.
        # 
        # Default value: true. Valid values:
        # 
        # *   true: ignores deletion flags. The cloud computers that were deleted are returned.
        # *   false: does not ignore deletion flags. The cloud computers that were deleted are not returned.
        self.ignore_deleted = ignore_deleted
        # The maximum number of entries per page.
        # 
        # *   Default value: 10.
        # *   Maximum value: 100.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results. You do not need to specify this parameter for the first request. You must specify the token that is obtained from the previous query as the value of NextToken.
        self.next_token = next_token
        # The billing method of the cloud computer share.
        self.pay_type = pay_type
        # The region ID. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/196646.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.custom_end_time_period is not None:
            result['CustomEndTimePeriod'] = self.custom_end_time_period

        if self.custom_start_time_period is not None:
            result['CustomStartTimePeriod'] = self.custom_start_time_period

        if self.desktop_group_id is not None:
            result['DesktopGroupId'] = self.desktop_group_id

        if self.ignore_deleted is not None:
            result['IgnoreDeleted'] = self.ignore_deleted

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.pay_type is not None:
            result['PayType'] = self.pay_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomEndTimePeriod') is not None:
            self.custom_end_time_period = m.get('CustomEndTimePeriod')

        if m.get('CustomStartTimePeriod') is not None:
            self.custom_start_time_period = m.get('CustomStartTimePeriod')

        if m.get('DesktopGroupId') is not None:
            self.desktop_group_id = m.get('DesktopGroupId')

        if m.get('IgnoreDeleted') is not None:
            self.ignore_deleted = m.get('IgnoreDeleted')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

