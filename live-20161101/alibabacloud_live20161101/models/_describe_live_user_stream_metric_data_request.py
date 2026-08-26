# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeLiveUserStreamMetricDataRequest(DaraModel):
    def __init__(
        self,
        app_name: str = None,
        domain_name: str = None,
        end_time: str = None,
        page_number: int = None,
        page_size: int = None,
        protocol: str = None,
        start_time: str = None,
        stream_name: str = None,
    ):
        # The application name. Specify the application name to query stream-level data for the corresponding application. If `StreamName` is specified, `AppName` must also be specified.
        self.app_name = app_name
        # The streaming domain to query.
        # 
        # 
        # > Only a single domain name is supported. An error is returned if multiple domain names are specified. If the domain name is empty, aggregate data for all streaming domains under the user is queried. If `AppName` and `StreamName` are not specified, stream-level data for all streams under the domain is returned.
        self.domain_name = domain_name
        # The end of the time range to query. The end time must be later than the start time and the difference cannot exceed 1 day. Specify the time in the ISO 8601 standard in the `YYYY-MM-DDThh:mm:ssZ` format. The time must be in UTC.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The page number.
        # 
        # This parameter is required.
        self.page_number = page_number
        # The number of entries per page. Maximum value: 5000.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The stream protocol name. Specify the protocol name to query data for the corresponding protocol. Supported protocols: `flv`, `hls`, `rtmp`, `rts`, `p2p`. You can query data for multiple protocols by separating them with commas (,). Data for multiple protocols is not aggregated and is output at the stream level.
        # > The **rts** option queries Real-Time Streaming (RTS) streams using the ARTC protocol.
        # > - When using rts, you may need to additionally count the xxx_AliRTS-opus transcoding stream. This is because when playing an RTS stream on the web, a transcoding stream with the _AliRTS-opus suffix appended to the stream name is automatically generated, producing transcoding stream data. For more information, see [RTS sub-second latency automatic transcoding](https://help.aliyun.com/document_detail/2948703.html).
        self.protocol = protocol
        # The beginning of the time range to query. Specify the time in the ISO 8601 standard in the `YYYY-MM-DDThh:mm:ssZ` format. The time must be in UTC.
        # 
        # This parameter is required.
        self.start_time = start_time
        # The stream name. If `StreamName` is specified, stream-level data for the specified `StreamName` under the specified `AppName` is returned. If `StreamName` is specified, `AppName` must also be specified.
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

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.protocol is not None:
            result['Protocol'] = self.protocol

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

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('StreamName') is not None:
            self.stream_name = m.get('StreamName')

        return self

