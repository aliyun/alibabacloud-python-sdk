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
        # The application name. Specify this parameter to query stream-level data for a specific application.
        # 
        # > If you specify StreamName, you must also specify AppName.
        self.app_name = app_name
        # - The accelerated domain name to query. Only a single domain name can be queried at a time. An error is returned if multiple domain names are specified.
        # - If AppName and StreamName are not specified, stream-level data for all streams under the domain name is returned.
        # - If the domain name is left empty, aggregate data for all accelerated domain names under the account is returned.
        # - If DomainName is specified and both AppName and StreamName are set to all, aggregate data for the specified accelerated domain name is returned.
        # - When you specify DomainName, make sure the domain name is a live streaming domain and the user calling this operation has the required permissions on the domain name.
        self.domain_name = domain_name
        # The end of the time range to query. The end time must be later than the start time, and the difference cannot exceed 1 day. Specify the time in the ISO 8601 standard in the YYYY-MM-DDThh:mm:ssZ format. The time must be in UTC.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The paged query token. A maximum of 5,000 rows of data can be returned per query. If the data to query exceeds 5,000 rows, the response includes the starting index for the next paging request. Pass this token in the request to continue querying data from where the previous query ended.
        self.next_page_token = next_page_token
        self.owner_id = owner_id
        # The stream protocol. Valid values: **flv**, **hls**, **rtmp**, **rts**, and **p2p**.
        # 
        # You can query data for multiple protocols by separating them with commas (,). Data for multiple protocols is not aggregated and is output at the stream level.
        # 
        # > The **rts** option queries Real-Time Streaming (RTS) streams that use the ARTC protocol.
        # > - When using rts, you may need to additionally collect statistics for the xxx_AliRTS-opus transcoding stream. This is because when playing an RTS stream on the web, a transcoding stream with the _AliRTS-opus suffix appended to the stream name is automatically generated. For more information, see [RTS sub-second latency automatic transcoding](https://help.aliyun.com/document_detail/2948703.html).
        self.protocol = protocol
        # The region ID.
        self.region_id = region_id
        # The start of the time range to query. Specify the time in the ISO 8601 standard in the YYYY-MM-DDThh:mm:ssZ format. The time must be in UTC.
        # 
        # This parameter is required.
        self.start_time = start_time
        # The stream name. Specify this parameter together with AppName to return stream-level data.
        # 
        # > If you specify StreamName, you must also specify AppName.
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

