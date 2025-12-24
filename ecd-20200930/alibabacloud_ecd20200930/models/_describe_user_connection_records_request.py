# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeUserConnectionRecordsRequest(DaraModel):
    def __init__(
        self,
        connect_duration_from: int = None,
        connect_duration_to: int = None,
        connect_end_time_from: int = None,
        connect_end_time_to: int = None,
        connect_start_time_from: int = None,
        connect_start_time_to: int = None,
        desktop_group_id: str = None,
        desktop_id: str = None,
        end_user_id: str = None,
        end_user_type: str = None,
        max_results: int = None,
        next_token: str = None,
        region_id: str = None,
    ):
        # The duration when the cloud desktop is connected, which is the minimum value for condition filtering.
        self.connect_duration_from = connect_duration_from
        # The duration when the cloud desktop is connected, which is the maximum value for condition filtering.
        self.connect_duration_to = connect_duration_to
        # The time when the cloud desktop stops to be connected, which is the minimum value for condition filtering. The value is a UNIX timestamp. Unit: milliseconds.
        self.connect_end_time_from = connect_end_time_from
        # The time when the cloud desktop stops to be connected, which is the maximum value for condition filtering. The value is a UNIX timestamp. Unit: milliseconds.
        self.connect_end_time_to = connect_end_time_to
        # The time when the cloud desktop starts to be connected, which is the minimum value for condition filtering. The value is a UNIX timestamp. Unit: milliseconds.
        self.connect_start_time_from = connect_start_time_from
        # The time when the cloud desktop starts to be connected, which is the maximum value for condition filtering. The value is a UNIX timestamp. Unit: milliseconds.
        self.connect_start_time_to = connect_start_time_to
        # The ID of the cloud computer pool.
        # 
        # This parameter is required.
        self.desktop_group_id = desktop_group_id
        # The ID of the cloud computer.
        self.desktop_id = desktop_id
        # The ID of the authorized user.
        # 
        # This parameter is required.
        self.end_user_id = end_user_id
        # The type of the user account.
        # 
        # Valid values:
        # 
        # *   SIMPLE: convenience account
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   AD_CONNECTOR: enterprise AD account
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.end_user_type = end_user_type
        # The number of entries to return on each page. Maximum value: 100. Default value: 10.
        self.max_results = max_results
        # The token that determines the start point of the next query. If this parameter is empty, all results are returned.
        self.next_token = next_token
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
        if self.connect_duration_from is not None:
            result['ConnectDurationFrom'] = self.connect_duration_from

        if self.connect_duration_to is not None:
            result['ConnectDurationTo'] = self.connect_duration_to

        if self.connect_end_time_from is not None:
            result['ConnectEndTimeFrom'] = self.connect_end_time_from

        if self.connect_end_time_to is not None:
            result['ConnectEndTimeTo'] = self.connect_end_time_to

        if self.connect_start_time_from is not None:
            result['ConnectStartTimeFrom'] = self.connect_start_time_from

        if self.connect_start_time_to is not None:
            result['ConnectStartTimeTo'] = self.connect_start_time_to

        if self.desktop_group_id is not None:
            result['DesktopGroupId'] = self.desktop_group_id

        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id

        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id

        if self.end_user_type is not None:
            result['EndUserType'] = self.end_user_type

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectDurationFrom') is not None:
            self.connect_duration_from = m.get('ConnectDurationFrom')

        if m.get('ConnectDurationTo') is not None:
            self.connect_duration_to = m.get('ConnectDurationTo')

        if m.get('ConnectEndTimeFrom') is not None:
            self.connect_end_time_from = m.get('ConnectEndTimeFrom')

        if m.get('ConnectEndTimeTo') is not None:
            self.connect_end_time_to = m.get('ConnectEndTimeTo')

        if m.get('ConnectStartTimeFrom') is not None:
            self.connect_start_time_from = m.get('ConnectStartTimeFrom')

        if m.get('ConnectStartTimeTo') is not None:
            self.connect_start_time_to = m.get('ConnectStartTimeTo')

        if m.get('DesktopGroupId') is not None:
            self.desktop_group_id = m.get('DesktopGroupId')

        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')

        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')

        if m.get('EndUserType') is not None:
            self.end_user_type = m.get('EndUserType')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

