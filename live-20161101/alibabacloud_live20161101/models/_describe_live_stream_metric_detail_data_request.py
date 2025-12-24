# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeLiveStreamMetricDetailDataRequest(DaraModel):
    def __init__(
        self,
        app_name: str = None,
        domain_name: str = None,
        end_time: str = None,
        next_page_token: str = None,
        owner_id: int = None,
        protocol: str = None,
        region_id: str = None,
        start_time: str = None,
        stream_name: str = None,
    ):
        # The name of the application for which you want to query the monitoring data of streams.
        # 
        # >  If you specify the StreamName parameter, you must also specify the AppName parameter.
        self.app_name = app_name
        # *   The accelerated domain name. You can specify only one domain name. If you specify multiple domain names, an error occurs.
        # *   If you do not specify the AppName and StreamName parameters, monitoring data of all streams for the domain name is returned.
        # *   If you leave this parameter empty, monitoring data of streams under all domain names is returned.
        # *   If you specify the DomainName parameter and set both the AppName and StreamName parameters to all, monitoring data of all streams in all applications under the specified domain name is returned.
        # *   When you specify the DomainName parameter, make sure that the domain name is a domain name used for live streaming and that you have the permissions on the domain name.
        self.domain_name = domain_name
        # The end of the time range to query. The end time must be later than the start time, and the maximum time range that can be specified is one day. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The token used to query data by page. Up to 5,000 rows of data can be returned per query. If the number of rows exceeds 5,000, a token that determines the start point of the next query is provided in the response. If you specify this parameter, data continues to be obtained from the end of the previous query.
        self.next_page_token = next_page_token
        self.owner_id = owner_id
        # The streaming protocol. Valid values: **flv**, **hls**, **rtmp**, **rts**, and **p2p**.
        # 
        # You can specify multiple protocols. Separate multiple protocols with commas (,). However, data over multiple protocols is not aggregated and is returned based on the stream.
        self.protocol = protocol
        self.region_id = region_id
        # The beginning of the time range to query. Specify the time in the ISO 8601 standard in the YYYY-MM-DDThh:mm:ssZ format. The time must be in UTC.
        # 
        # This parameter is required.
        self.start_time = start_time
        # The name of the stream. The stream must belong to the application that is specified by the AppName parameter.
        # 
        # >  If you specify the StreamName parameter, you must also specify the AppName parameter.
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

        if self.protocol is not None:
            result['Protocol'] = self.protocol

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

        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('StreamName') is not None:
            self.stream_name = m.get('StreamName')

        return self

