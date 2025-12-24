# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeRecordingsRequest(DaraModel):
    def __init__(
        self,
        desktop_id: str = None,
        end_time: str = None,
        max_results: int = None,
        need_signed_url: bool = None,
        next_token: str = None,
        policy_group_id: str = None,
        region_id: str = None,
        signed_url_expire_minutes: int = None,
        standard_end_time: str = None,
        standard_start_time: str = None,
        start_time: str = None,
    ):
        # The cloud computer ID. If this parameter is not specified, the screen recording files on all cloud computers in the designated region will be queried.
        self.desktop_id = desktop_id
        # The end time of the query. Specify the time in the `YYYYMMDDhhmmss` format. The time must be in UTC+8.
        self.end_time = end_time
        # The maximum number of entries per page.
        # 
        # Maximum value: 100.
        # 
        # Default value: 10.
        self.max_results = max_results
        # Specifies whether to return a URL.
        # 
        # Valid values:
        # 
        # *   true
        # *   false (default)
        self.need_signed_url = need_signed_url
        # The pagination token that is used in the request to retrieve a new page of results. You do not need to specify this parameter for the first request. You must specify the token that is obtained from the previous query as the value of `NextToken`.
        self.next_token = next_token
        # The policy ID.
        self.policy_group_id = policy_group_id
        # The region ID. You can call the [DescribeRegions](~~DescribeRegions~~) operation to query the list of regions where Elastic Desktop Service (EDS) Enterprise is available.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The validity period of the returned URL. Unit: minutes.
        self.signed_url_expire_minutes = signed_url_expire_minutes
        # The end time of the query. Specify the time in the ISO 8601 standard in the `yyyy-mm-ddthh:mm:ssz` format. The time must be in UTC+0.
        self.standard_end_time = standard_end_time
        # The start time of the query. Specify the time in the ISO 8601 standard in the `yyyy-mm-ddthh:mm:ssz` format. The time must be in UTC+0.
        self.standard_start_time = standard_start_time
        # The start time of the query. Specify the time in the `YYYYMMDDhhmmss` format. The time must be in UTC+8.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.need_signed_url is not None:
            result['NeedSignedUrl'] = self.need_signed_url

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.policy_group_id is not None:
            result['PolicyGroupId'] = self.policy_group_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.signed_url_expire_minutes is not None:
            result['SignedUrlExpireMinutes'] = self.signed_url_expire_minutes

        if self.standard_end_time is not None:
            result['StandardEndTime'] = self.standard_end_time

        if self.standard_start_time is not None:
            result['StandardStartTime'] = self.standard_start_time

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NeedSignedUrl') is not None:
            self.need_signed_url = m.get('NeedSignedUrl')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('PolicyGroupId') is not None:
            self.policy_group_id = m.get('PolicyGroupId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SignedUrlExpireMinutes') is not None:
            self.signed_url_expire_minutes = m.get('SignedUrlExpireMinutes')

        if m.get('StandardEndTime') is not None:
            self.standard_end_time = m.get('StandardEndTime')

        if m.get('StandardStartTime') is not None:
            self.standard_start_time = m.get('StandardStartTime')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

