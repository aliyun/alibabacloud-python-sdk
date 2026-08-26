# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeLiveStreamPushMetricDetailDataRequest(DaraModel):
    def __init__(
        self,
        app_name: str = None,
        domain_name: str = None,
        end_time: str = None,
        next_page_token: str = None,
        owner_id: int = None,
        region_id: str = None,
        start_time: str = None,
        stream_name: str = None,
    ):
        # The name of the application to which the live stream belongs. Specify the application name to query data at the stream granularity for the corresponding application.
        self.app_name = app_name
        # - The accelerated domain name to query. Only a single domain name can be queried. An error is returned if you specify multiple domain names.
        # - If you do not specify AppName or StreamName, data at the stream granularity for all streams under the specified accelerated domain name is returned without aggregation.
        # - If DomainName is specified and both AppName and StreamName are set to all, aggregate data at the stream granularity for all streams under the specified accelerated domain name is returned.
        # 
        # This parameter is required.
        self.domain_name = domain_name
        # The end of the time range to query. Specify the time in the ISO 8601 standard in the UTC time zone. The end time must be later than the start time, and the difference cannot exceed 1 day.
        # 
        # Format: YYYY-MM-DDThh:mm:ssZ.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The paging query token. Each query returns a maximum of 5,000 rows of data. If the data to be queried exceeds 5,000 rows, the response includes the start index for the next query.
        # 
        # Pass this token in the request to continue querying data from the row after the last row returned in the previous query.
        self.next_page_token = next_page_token
        self.owner_id = owner_id
        # The region ID.
        self.region_id = region_id
        # The beginning of the time range to query. Specify the time in the ISO 8601 standard in the UTC time zone.
        # 
        # Format: YYYY-MM-DDThh:mm:ssZ.
        # 
        # This parameter is required.
        self.start_time = start_time
        # The name of the live stream. If you specify StreamName, data at the stream granularity is returned for the specified StreamName under the specified AppName. You must specify AppName when you specify StreamName.
        self.stream_name = stream_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.next_page_token is not None:
            result['NextPageToken'] = self.next_page_token

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.stream_name is not None:
            result['StreamName'] = self.stream_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('NextPageToken') is not None:
            self.next_page_token = m.get('NextPageToken')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('StreamName') is not None:
            self.stream_name = m.get('StreamName')

        return self

